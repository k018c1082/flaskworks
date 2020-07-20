from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/Kamata/')
def Kamata():
    return render_template('Kamata.html',message = 'Kamataを追加しました')

@app.route('/user/Tokyo/')
def Tokyo():
    return render_template('Tokyo.html',message = 'Tokyoを追加しました')

@app.route('/user/<cityname>/')
def city(cityname):
    return render_template('index03.html', message=cityname)

if __name__=='__main__':
    app.debug = True
    app.run()