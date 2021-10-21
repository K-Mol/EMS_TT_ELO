import json
from playerclass import player

Will = player("Will")

#create object
laptop1 = Laptop()
laptop1.name = 'Dell Alienware'
laptop1.processor = 'Intel Core i7'

#convert to JSON string
jsonStr = json.dumps(laptop1.__dict__)

#print json string
print(jsonStr)
