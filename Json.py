# Description: Handles json files
# Author: Jacob Maughan

# Sys Imports
import json
from os import path

class Json():
    def __init__(self, file):
        self.file = file
        if not path.isfile(file):
            with open(self.file, "w") as newFile:
                newFile.write("{}")

    
    # Get the data from json file
    def getJson(self):
        with open(self.file) as tmpFile:
            return json.load(tmpFile)
    
    # Save the data to json file
    def saveJson(self, data):
        with open(self.file, 'w') as tmpFile:
            json.dump(data, tmpFile, indent=4)