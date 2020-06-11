#!/usr/bin/python3
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.plugins.callback import CallbackBase
from ansible.vars.manager import VariableManager
from ansible import context
from ansible.module_utils.common.collections import ImmutableDict

class ResultsCollector(CallbackBase):
    def __init__(self, *args, **kwargs):
        super(ResultsCollector, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}
    def v2_runner_on_unreachable(self, result):
        self.host_unreachable[result._host.get_name()] = result
    def v2_runner_on_ok(self, result, *args, **kwargs):
        self.host_ok[result._host.get_name()] = result
    def v2_runner_on_failed(self, result, *args, **kwargs):
        self.host_failed[result._host.get_name()] = result


def playthebook():
    host_list = ['192.168.56.101']
    context.CLIARGS = ImmutableDict(connection='smart', module_path=['/usr/share/ansible'], forks=10, become=None,
                                    become_method=None, become_user=None, check=False, diff=False)
    sources = ','.join(host_list)
    if len(host_list) == 1:
        sources += ','
    print(sources)
    # initialize needed objects
    loader = DataLoader()
    passwords = dict()

    # create inventory and pass to var manager
    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create play with tasks
    play_source = dict(
        name="Ansible Play",
        hosts=host_list,
        gather_facts='no',
        tasks=[dict(action=dict(module='command', args=dict(cmd='/usr/bin/uptime')))]
    )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # actually run it
    tqm = None
    callback = ResultsCollector()
    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            passwords=passwords,
            stdout_callback=callback,
        )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()
        if loader:
            loader.cleanup_all_tmp_files()

    print("UP ***********")
    for host, result in callback.host_ok.items():
        print('{0} >>> {1}'.format(host, result._result['stdout']))

    print("FAILED *******")
    for host, result in callback.host_failed.items():
        print('{0} >>> {1}'.format(host, result._result['msg']))

    print("DOWN *********")
    for host, result in callback.host_unreachable.items():
        print('{0} >>> {1}'.format(host, result._result['msg']))
