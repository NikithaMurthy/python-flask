from flask import * 
  
app = Flask(__name__) 
 
@app.route('/login',methods = ['POST'])  
def home():  
    return render_template('customer.html')
  
if __name__ =='__main__':  
    app.run(debug = True) 