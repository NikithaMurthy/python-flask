from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1ga12cs060'
app.config['MYSQL_DB']='flask'



mysql=MySQL(app)

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        userdetails=request.form
        name=userdetails['name']
        classs=userdetails['class']
        division=userdetails['division']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,class,division) VALUES(%s,%d,%s)",(name,classs,division))
        mysql.connection.commit()
        cur.close()
        return 'Success'

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
