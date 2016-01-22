__author__ = 'zackasan'

import json
import sys
from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

from converter import Converter

engine = IntentDeterminationEngine()

bike_keyword = ["bikes"]

for bk in bike_keyword:
    engine.register_entity(bk, "BikeKeyword")

bike_possibilities = [
    "available",
    "not available"
]

for bp in bike_possibilities:
    engine.register_entity(bp, "BikePossibility")

locations = [ "Brussels", "Paris" ]

for loc in locations:
    engine.register_entity(loc, "Location")


bike_intent = IntentBuilder("BikeIntent")\
    .require("BikeKeyword")\
    .require("BikePossibility")\
    .optionally("Location")\
    .build()


engine.register_intent_parser(bike_intent)

if __name__ == "__main__":
    for intent in engine.determine_intent(' '.join(sys.argv[1:])):
        if intent.get('confidence') > 0:
            print(json.dumps(intent, indent=4))

            myConverter = Converter(intent)
            myConverter.extractLocation()
        else:
            print ("I don't get it man")
