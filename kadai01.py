from flask import Flask

app = Flask(__name__)

@app.route('/')

def page():
    return 'トップページ'
    
if __name__=='__main__':
    app.debug = True
    app.run()