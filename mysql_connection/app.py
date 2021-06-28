import random
from flask import Flask, render_template, redirect, request, url_for

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1ga12cs060'
app.config['MYSQL_DATABASE_DB'] = 'flaskdemo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def registerr():
    name=request.form["name"],
    classs=request.form["classs"],
    division=request.form["division"],
    total_sum=random.randint(0, 500)
    division_num=random.randint(0, 50)
    cursor = mysql.get_db().cursor()
    cursor.execute('insert into users values(%s, %s, %s, %s, %s);',
                   (name,classs,division,total_sum,division_num))
    mysql.get_db().commit()

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
