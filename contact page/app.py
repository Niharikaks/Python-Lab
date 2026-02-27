
from  flask import Flask, render_template,request
app=Flask(__name__)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/submit',methods =['POST'])
def submit():
  name=request.form['username']
  msg=request.form['message']
  return f"<h2> Thanks,{name}!</h2><p>your message:{msg}</p>"

@app.route('/submit',methods =['GET'])
def submit():
 name=request.args.get('username')
 msg=request.args.get('message')
 return f"<h2> Thanks,{name}!</h2><p>your message:{msg}</p>" 

if __name__== '__main__':
    app.run(debug=True)
