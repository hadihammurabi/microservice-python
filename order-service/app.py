from flask import Flask, jsonify

app = Flask('order-service')

@app.route('/')
def index():
  return jsonify({
    'message': 'order',
  })

app.run(port=8003)
