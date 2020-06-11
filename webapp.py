from flask import Flask, render_template, request
from celery import Celery
from datetime import timedelta
import tasks
#from anible import playthebook


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
  if not request.args.get('num1'):
   return render_template('index.html')
  else:
    num1=int(str(request.args.get('num1')))
    num2=int(str(request.args.get('num2')))
    result=tasks.add.delay(num1,num2)
    ans=result.wait()
    #playthebook('play.yml','192.168.56.101')
    return render_template('index.html', result=ans )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081,debug=True)
