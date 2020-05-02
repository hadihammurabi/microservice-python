from flask import Flask, jsonify

app = Flask('book-service')

@app.route('/', methods=['GET'])
def index():
  return jsonify({
    'message': 'get all books',
  })

app.run(port=8001)
