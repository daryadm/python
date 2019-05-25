import cherrypy
from elasticsearch import Elasticsearch as els
import json


class Root(object):

    def __init__(self):
        url = "http://fcsearchdev04.nycnt1a.fdncenter.org:9200"
        self.es = els(url, http_auth=('elastic', '[givein in class]'), timeout=30)

    @cherrypy.expose
    def index(self, search):
        q = {
            "_source": ["gm_keywords", "grant_recipient_keywords"],
            "query": {
                "more_like_this": {
                    "fields": ["gm_keywords"],
                    "like": search,
                    "min_term_freq": 1,
                    "max_query_terms": 12
                }
            }
        }
        r = self.es.search(index="fdo_grants", body=q, explain=False)
        return json.dumps(r)


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8099})
    cherrypy.quickstart(Root(), '/')