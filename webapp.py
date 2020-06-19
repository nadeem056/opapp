from flask import Flask, render_template, request
import tasks
import sys
from bookplayer import playthebook


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
  if 'submit' in request.args:
    try:
       a=int(request.args.get('num1'))
       b=int(request.args.get('num2'))
       c=tasks.add.delay(a,b).wait()
       return render_template('index.html', result=c)
    except:
      e = sys.exc_info()[0]
      return render_template('index.html', result=e )
  elif 'playbook' in request.args:
    res=tasks.play()
    return render_template('index.html', result=res)
  elif 'pbcel' in request.args:
    res=tasks.play.delay().wait()
    return render_template('index.html', result=res)
  else:
    return render_template('index.html', result=request.args)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081,debug=True)
