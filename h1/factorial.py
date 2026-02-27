from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/factorial/<int:n>')
def factorial_calc(n):
    
    result=1
    for i in range(1,n+1):
        result*=i
    return f"the factorial of {n} is {result}"
if __name__ == '__main__':
    app.run(debug=True)