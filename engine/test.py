import requests
import json
from pprint import pprint
import StringIO

class DataConnection():

    def __init__(self):
        self.uri = ""

    def retrieve(self, lat, lon, dis):
        baseURI = 'http://opendata.brussels.be/api/records/1.0/search/'
        geofilter = '%r,%r,%d' % (lat, lon, dis)
        payload = {'dataset': 'villo-stations-availability-in-real-time',
                   'facet': ['bonus', 'status','contract_name'],
                   'geofilter.distance': geofilter}

        r = requests.get(baseURI, params=payload)

        try:
            decoded = json.loads(r.text)
            print json.dumps(decoded, sort_keys=True, indent=4)

            #this is not good because the data-structure might change. better to implement a loop
            #also does not take into account multistation
            availableBikes =  decoded['records'][0]['fields']['available_bikes']
            station = decoded['records'][0]['fields']['address']
            print "There are %s bikes available at %s" % (availableBikes, station)
        except (ValueError, KeyError, TypeError):
            print "JSON format error"




myTest = DataConnection()
myTest.retrieve(50.8758, 4.3843, 200)

