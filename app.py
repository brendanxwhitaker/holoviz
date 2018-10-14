from flask import Flask, render_template
import json
import pyemblib

app = Flask(__name__)

embedding_file = 'top_10000_emb.txt' # change file here 

@app.route('/')
@app.route('/index')
def loadEmbeddings():
  embeddings = pyemblib.read(embedding_file, mode=pyemblib.Mode.Text)
  for k in embeddings:
    embeddings[str(k)] = embeddings[k].tolist()
    del k
  return render_template('index.html', data=json.dumps(embeddings))


