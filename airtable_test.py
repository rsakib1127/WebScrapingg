import airtable

at = airtable.Airtable('appUlbwmILTwOjboF','Table 1','keyjE3YdXPSqVt1yw')
table_name = 'Table 1'
at.insert({'Email': 'John'})