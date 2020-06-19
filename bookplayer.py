#!/usr/bin/python
import os
import json
import sys
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor
from callback import Callback
from ansibleoptions import ansibleoptions
def playthebook():
  variable_manager = VariableManager()
  loader = DataLoader()
  inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list=['192.168.56.103'])
  playbook_path = 'play.yml'

  if not os.path.exists(playbook_path):
    print('[INFO] No playbook')
    sys.exit()
  Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check', 'show_custom_stats', 'display_args_to_stdout'])
  options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='nadeem', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method='sudo', become_user='root', verbosity=None, check=False, show_custom_stats=False, display_args_to_stdout=True)
  options=ansibleoptions().get_options()
  passwords = {}
  results_callback = Callback()
  pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=passwords)
  pbex._tqm._stdout_callback = results_callback
  results = pbex.run()
  return results, pbex
