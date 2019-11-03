from flask import Flask, jsonify, request
import mysql.connector

db = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='root',
  database='authors'
)

app = Flask('author-service')

@app.route('/', methods=['GET'])
def index():
  cursor = db.cursor(dictionary=True)
  cursor.execute('SELECT * FROM authors')
  authors = cursor.fetchall()
  return jsonify(authors)

@app.route('/<id>', methods=['GET'])
def show(id):
  cursor = db.cursor(dictionary=True)
  cursor.execute('SELECT * FROM authors WHERE id='+id)
  authors = cursor.fetchall()
  return jsonify(authors[0])

@app.route('/', methods=['POST'])
def create():
  author = request.get_json()
  cursor = db.cursor(dictionary=True)
  query = 'INSERT INTO authors (name, city, state) VALUES ("%s", "%s", "%s")' % (author['name'], author['city'], author['state'])
  cursor.execute(query)
  return jsonify({'message': 'success', 'data': author})

app.run(port=8000)
