import json

class Converter:
    data = []
    location = ""


    def __init__(self, data):
        self.data = data

    def add_intent(self, data):
        self.data.append(data)

    def get_intent(self):
        return self.data

    def set_intent(self, data):
        self.data = data


    def extractLocation(self):

        self.location = self.data['Location']
        print("location %s" % self.location)

    def myPrint(self):
        print(self.data)
