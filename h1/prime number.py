from flask import Flask

app = Flask(__name__)

@app.route('/prime/<int:number>')
def check_prime(number):
    if number < 2:
        return f"{number} is not a prime number"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number"
    return f"{number} is a prime number"

if __name__ == '__main__':
    app.run(debug=True)


