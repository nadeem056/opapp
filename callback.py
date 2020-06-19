import json
from ansible.plugins.callback import CallbackBase

class Callback(CallbackBase):
    def __init__(self):
        self.task_result=[]
    def v2_playbook_on_start(self):
        print('{"status": "Initilization"}','\n')
        #self.task.logs.append('{"status": "Initilization"}')
    def v2_playbook_on_play_start(self, play):
        print('{"status": "Started", "play": "%s"}'%(play) )
        #self.task.logs.append('{"status": "Started"}') 
    def v2_runner_on_ok(self, result, **kwargs):
        print('{"status": "OK"}')
        host = result._host
        self.task_result.append(result._result)
        #print(json.dumps({host.name: result._result}, indent=4))
    def v2_runner_on_failed(self, result, ignore_errors=False):
        host = result._host
        self.task_result.append(result._result)
        #print(json.dumps({host.name: result._result}, indent=4))
    def v2_runner_on_unreachable(self, result):
        host = result._host
        self.task_result.append(result._result)
        #print(json.dumps({host.name: result._result}, indent=4))
