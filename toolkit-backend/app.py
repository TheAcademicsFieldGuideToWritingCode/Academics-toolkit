from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/my-function', methods=['POST'])
def my_function():
    data = request.get_json()
    # Process the data and perform your Python logic here
    result = {"output": "Hello, " + data["input"]}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

# Your Flask routes and code here

if __name__ == '__main__':
    app.run(debug=True)