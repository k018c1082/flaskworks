import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hiniti():
    dt = datetime.datetime.now()    
    return dt.strftime('%m/%d %H:%M')
    
if __name__=='__main__':
    app.debug = True
    app.run()