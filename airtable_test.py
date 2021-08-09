import airtable
import json
f = open('airtable.json',)
data = json.load(f)
print(data['APIkey'])
at = airtable.Airtable(data['BaseID'],data['Table'],data['APIkey'])
tableA1 = at.get_all()
print(tableA1)
# at.insert({'Email': 'John'})