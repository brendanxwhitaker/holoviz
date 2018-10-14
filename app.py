from flask import Flask
import json
import pyemblib

app = Flask(__name__)

embedding_file = '' # TODO - insert file path 

@app.route("/")
def loadEmbeddings():
  embeddings = pyemblib.read(embedding_file, mode=pyemblib.Mode.Text)
  
