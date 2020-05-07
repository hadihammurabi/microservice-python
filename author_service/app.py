from flask import Flask, jsonify, request

app = Flask('author-service')

@app.route('/', methods=['GET'])
def index():
  return jsonify({
    'message': 'get all authors',
  })

@app.route('/<id>', methods=['GET'])
def show(id):
  return jsonify({
    'message': 'get author by id',
  })

@app.route('/', methods=['POST'])
def create():
  return jsonify({
    'message': 'create author',
  })

if __name__ == '__main__':
  app.run(port=8000)
