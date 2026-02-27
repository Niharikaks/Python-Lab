from flask import Flask

app = Flask(__name__)

@app.route('/check/<int:number>')
def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

if __name__ == '__main__':
    app.run(debug=True)
    



