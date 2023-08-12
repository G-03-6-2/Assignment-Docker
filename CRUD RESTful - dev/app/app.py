from flask import Flask , request , jsonify
import database

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello This is Index!"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)


@app.route('/calculate/<num1>/<num2>', methods=['GET'])
def calculate(num1, num2):
    try:
        num1 = eval(num1)
        num2 = int(num2)

        results = {
                'plus' : num1 + num2,
                'minus' : num1 - num2,
                'multiply': num1 * num2,
                'divide' : num1/num2
            }
    except:
        results = { 'error_msg' : 'inputs must be numbers' }

    return jsonify(results)

# a GET request to /user/ returns a list of registered users on a system
@app.route('/user/' , methods=['GET'])
def get_all_user():
    return jsonify(database.get_all_user())

# a POST request to /user/new creates a user with the using the body data. The response returns the ID.
@app.route('/user/new' , methods=['POST'])
def insert():
    request_data = request.get_json()
    name = request_data['name']
    age = int(request_data['age'])
    results = database.insert_user(name, age)
    return jsonify(results)

# a PUT request to /user/123 updates user 123 with the body data
@app.route('/user/<_id>' , methods=['PUT'])
def update(_id):
    request_data = request.get_json()
    name = request_data['name']
    age = int(request_data['age'])
    database.update_user(_id, name, age)
    results = {'message' : "Update user success"}
    return jsonify(results)

# a GET request to /user/123 returns the details of user 123
@app.route('/user/<_id>' , methods=['GET'])
def find(_id):
    return jsonify(database.get_user(_id))

# a DELETE request to /user/123 deletes user 123
@app.route('/user/<_id>' , methods=['DELETE'])
def delete(_id):
    database.delete_user(_id)
    return jsonify({'message' : "Delete user success"})

if __name__ == '__main__':
    app.run()