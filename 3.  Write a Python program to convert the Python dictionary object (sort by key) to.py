""" 3: Write a Python program to convert the Python dictionary object (sort by key) to
JSON data. Print the object members with indent level 4."""

import json
j_str={'6':"C", '4':"C++", '2':"Java", '1':"Python", '3':"Kotlin", '5':"PHP"}
print("original String:")
print(j_str)
#print("\n JSON data:)
#print(json.dumps(j_str, sort_keys=True, indent=4)
print("\n JSON Data")
json_object=json.dumps(j_str, sort_keys=True, indent=4)
print(json_object)
