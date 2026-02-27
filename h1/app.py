from flask import Flask
app=Flask(__name__)
@app.route('/home')
def home():
    return"hello world"

@app.route('/social')
def social():
    return'''
    <html>
    <head>
    <title>  hii there i am Niharika </title>
    <style>
    p {
        font-family:"times New roman",serif;
    color:blue;}
    h1{text-align :center;}   
    </style>
    </head>
    <body style ="background-color:DarkGoldenrod;">
    <p><h1>hello follow me if u find my page attractive</h1></p>
    
    <h2>links</h2>
    <ol>
    <li><a href = "https://www.facebook.com"target="_blank">facebook</a></li>
    <li><a href = "https://www.twitter.com"target="_blank">twitter</a></li>
    <li><a href = "https://www.instagram.com"target="_blank">instagram</a></li>
    <li><a href = "https://www.youtube.com"target="_blank">youtube</a></li>
    <li><a href= "https://www.pinterest.com"target="_blank">pinterest</a></li>
    <img src ="https://www.shutterstock.com/shutterstock/photos/2198245029/display_1500/stock-photo-autumn-nature-landscape-lake-bridge-in-fall-forest-path-way-in-gold-woods-romantic-view-image-2198245029.jpg" alt="social media" width="700" height ="500">
    </ol>
    </body>
    </html>
    '''
if __name__=='__main__':
    app.run(debug=True) 