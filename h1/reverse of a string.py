from flask import Flask

app = Flask(__name__)

@app.route('/reverse/<string:text>')
def reverse_string(text):
    reversed_text = text[::-1]
    return f"Reversed: {reversed_text}"

if __name__ == '__main__':
    app.run(debug=True)
