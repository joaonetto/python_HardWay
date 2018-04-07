import requests
import json
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '10.0.1.6', 'port': 9200}])

# Inclui novo item
#es.index(index='test-index', doc_type='test', id=1, body={'test': 'test'})

#res = requests.get('http://10.0.1.6:9200/test-index')
#res = json.loads(res.content)
#print(json.dumps(res, indent=2))

# Deleta o indice 'test-index'
#es.delete(index='test-index', doc_type='test')
"""
# incluindo um registro
es.index(index='sw', doc_type='people', id=1, body={
	"name": "Luke Skywalker",
	"height": "172",
	"mass": "77",
	"hair_color": "blond",
	"birth_year": "19BBY",
	"gender": "male",
})

r = requests.get('http://10.0.1.6:9200')
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1
print(i)

res = requests.get('http://10.0.1.6:9200/_cat/indices?v')
print(res.content)

r = requests.get('http://10.0.1.6:9200')
i = 18
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1
print(i)
"""
res = requests.get('http://10.0.1.6:9200/_cat/indices?v')
print(res.content)

resultado = es.get(index='sw', doc_type='people', id=10)
print(json.dumps(resultado, indent=2))

resultado = es.search(index="sw", body={"query": {"prefix" : { "name" : "Obi-Wan Kenobi" }}})
print(json.dumps(resultado, indent=2))
