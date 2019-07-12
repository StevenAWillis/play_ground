from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/play')
def play():

    print ("////////////////////////////////////")
    return render_template('index.html')

@app.route('/play/<num>') 
def play_num(num):
    
    return render_template('index.html' ,num = int(num))

@app.route('/play/<num>/<color>') 
def play_num_color(num,color):
    
    return render_template('index.html' ,num = int(num),color = color)


app.run(debug=True)
