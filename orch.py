import subprocess
#def playthebook(playbook
#subprocess.check_output(['export','ANSIBLE_STDOUT_CALLBACK=json'])
oo=subprocess.Popen(['ansible-playbook', 'play.yml'])
print(oo.stdout)
