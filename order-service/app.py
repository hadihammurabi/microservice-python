from flask import Flask, jsonify

app = Flask('order-service')

@app.route('/')
def index():
  return jsonify({
    'message': 'get all orders',
  })

app.run(port=8003)
