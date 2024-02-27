import json

def payload(filename):
    result = f"..\\TestData\\{filename}.json"
    with open(result, 'r') as file:
        data = json.load(file)
        return data