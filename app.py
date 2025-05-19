from flask import Flask , render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/tailan')
def tailan():
    return render_template('tailan.html')
@app.route('/medee')
def medee():
    return render_template('medee.html')
@app.route('/setgegdel')
def setgegdel():
    return render_template('setgegdel.html')
@app.route('/bid')
def bid():
    return render_template('bid.html')

users = [{"id": 1, "name": "Temuulen"}, {"id": 2, "name": "Temuunee"}]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.json
    users.append({"id": len(users)+1, "name": data['name']})
    return jsonify({"message": "User added"}), 201
if __name__ == '__main__': 
    app.run(debug=True)


