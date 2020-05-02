from flask import Flask, jsonify

app = Flask('order-service')

@app.route('/')
def index():
  return jsonify({
    'message': 'get all orders',
  })

if __name__ == '__main__':
  app.run(port=8003)
