from flask import Flask, jsonify

app = Flask('customer-service')

@app.route('/')
def index():
  return jsonify({
    'message': 'get all customers',
  })

app.run(port=8002)
