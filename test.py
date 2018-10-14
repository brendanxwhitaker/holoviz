import json
import pyemblib

embedding_file = 'top_10000_emb.txt' 

text_embedding = pyemblib.read(embedding_file, mode=pyemblib.Mode.Text)
print(text_embedding)
print(json.dumps(text_embedding))
