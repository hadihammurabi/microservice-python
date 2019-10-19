from flask import Flask, jsonify
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

app.run(port=8000)
