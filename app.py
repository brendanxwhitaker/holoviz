from flask import Flask, render_template
import json
import pyemblib

app = Flask(__name__)

embedding_file = 'test.txt' # change file here 

@app.route('/')
@app.route('/index')
def loadEmbeddings():
  embeddings = pyemblib.read(embedding_file, mode=pyemblib.Mode.Text)
  encoded = {}
  for k in embeddings:
    encoded[str(k)] = embeddings[k].tolist()
  return render_template('index.html', data=encoded)


