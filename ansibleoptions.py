from collections import namedtuple
class ansibleoptions(object):
  def __init__(self):
    self.Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check', 'show_custom_stats', 'display_args_to_stdout'])
    self.options = self.Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=100, remote_user='nadeem', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method='sudo', become_user='root', verbosity=None, check=False, show_custom_stats=False, display_args_to_stdout=True)

  def _set_arg(self):
    pass

  def get_options(self):
    return self.options
