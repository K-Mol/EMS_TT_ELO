import json
from playerclass import player

Will = player("Will")

#convert to JSON string
jsonStr = json.dumps(laptop1.__dict__)

#print json string
print(jsonStr)
