from flask import Flask
import json
import pyemblib

app = Flask(__name__)

embedding_file = 'top_10000_emb.txt' # change file here 

@app.route("/")
def loadEmbeddings():
  embeddings = pyemblib.read(embedding_file, mode=pyemblib.Mode.Text)
  response = app.response_class(
    response=json.dumps(embeddings),
    status=200,
    mimetype='application/json'
  )  
  return response
