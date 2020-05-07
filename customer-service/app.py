from flask import Flask, jsonify

app = Flask('customer-service')

@app.route('/')
def index():
  return jsonify({
    'message': 'customer',
  })

if __name == "__main__":
  app.run(port=8002)
