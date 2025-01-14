from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_data():
    # Example JSON response
    return jsonify({"message": "This is a JSON response", "status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

