import random
import string
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
    cursor = mysql.get_db().cursor()
    cursor.execute('truncate table student')
    mysql.get_db().commit()
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/addStudent',methods=['POST'])
def addStudent():
    division_num=random.randint(30,50)
    for i in range(1,division_num):
        classs=random.randint(1,12)
        total_sum=random.randint(1,500)
        name=''.join((random.choice(string.ascii_lowercase) for x in range(10)))
        division=chr(random.randint(ord('A'), ord('E')))
        cursor = mysql.get_db().cursor()
        cursor.execute('insert into student values(%s, %s, %s, %s, %s);',(name, classs, division, total_sum, division_num))
        mysql.get_db().commit()



    return render_template('register.html')

@app.route('/display')
def display():
    cursor = mysql.get_db().cursor()
    cursor.execute('select * from student order by total_sum desc;')
    student = cursor.fetchall()
    return render_template('display.html', student=student[0:5])

@app.route('/displaypage')
def displaypage():
    cursor = mysql.get_db().cursor()
    cursor.execute('select classs,division,name,max(total_sum) from student group by division;')
    student = cursor.fetchall()
    return render_template('displaypage.html', student=student)
if __name__ == '__main__':
    app.run(debug=True)
