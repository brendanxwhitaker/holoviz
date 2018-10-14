from flask import Flask, render_template
from sklearn.manifold import MDS
import numpy as np
import json
import pyemblib

app = Flask(__name__)

embedding_file = 'test.txt' # change file here 

@app.route('/')
@app.route('/index')
def loadEmbeddings():
  embeddings = pyemblib.read(embedding_file, mode=pyemblib.Mode.Text)
  keys = list(embeddings.keys())
  values = np.array(list(embeddings.values()))
  mds = MDS(n_components=3)
  values_transformed = mds.fit_transform(values)

  transformed = {}
  for i in range(len(keys)):
    transformed[keys[i]] = values_transformed[i].tolist()
  return render_template('index.html', data=transformed)


