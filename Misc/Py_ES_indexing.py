import pyodbc
cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=redhookdev;DATABASE=news_matching;uid=python_class_user;pwd=[provided in class]")
import elasticsearch as els
from elasticsearch import helpers

es = els.Elasticsearch("http://fcsearchdev04.nycnt1a.fdncenter.org:9200", http_auth=("elastic", "ocelot243kiwi"))
chunk_size = 1
data = None
counter = 0

with open("fromdavid.json", encoding='utf-8') as f:
    data = f.read()

if data is not None:
    data = json.loads(data)
    docs = data ["fromdavid"]
    docs_to_index = []
    for d in docs:
        counter += 1
        identifier = d["key"]
        docs_to_index.append({"_index": "dao", "_source": d, "_type": "text", "id": identifier})
        if counter % chunk_size == 0:
            try:
                helpers.bulk(es, docs_to_index)
                print("Committed {0} records.".format(counter))
            except Exception as e:
                print(e)
            docs_to_index = []
print("All done!")