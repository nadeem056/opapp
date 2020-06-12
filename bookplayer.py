import json
from time import sleep
from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.plugins.callback import CallbackBase

class ResultCallback(CallbackBase):
    ok_results=''
    fl_results=''
    ur_results=''
    hst=None
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        self.ok_results=result._result
    def v2_runner_on_failed(self, result, ignore_errors=False):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))
    def v2_runner_on_unreachable(self, result):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))

def playthebook(book,host):
  loader = DataLoader()
  context.CLIARGS = ImmutableDict(tags={},
			listtags=False,
			listtasks=False,
			listhosts=False,
			syntax=False,
			connection='ssh',
                    	module_path=None,
			forks=100,
			remote_user='nadeem',
			private_key_file=None,
                    	ssh_common_args=None,
			ssh_extra_args=None,
			sftp_extra_args=None,
			scp_extra_args=None,
			become=True,
                    	become_method='sudo',
			become_user='root',
			verbosity=True,
			check=False,
			start_at_task=None)

  rc = ResultCallback()
  inventory = InventoryManager(loader=loader, sources=('inventory',))
  variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
  pbex = PlaybookExecutor(playbooks=['play.yml'], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
  pbex._tqm._stdout_callback = rc
  results = pbex.run()
  res_dict = pbex._tqm._stdout_callback.ok_results
  return res_dict
