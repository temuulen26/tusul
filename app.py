from flask import Flask , render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/medee')
def medee():
    return render_template('shine_medee.html')
@app.route('/medlegee_huvaaltsay')
def medleg():
    return render_template('medleg.html')
@app.route('/setgegdel')
def setgegdel():
    return render_template('setgegdel.html')
@app.route('/bid')
def bid():
    return render_template('bid.html')

if __name__ == '__main__': 
    app.run(debug=True)


