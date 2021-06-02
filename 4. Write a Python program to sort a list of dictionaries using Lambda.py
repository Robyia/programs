#4: Write a Python program to sort a list of dictionaries using Lambda.

d1= [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("original list of dictionaries:")
print(d1)
sorted_d1=sorted(d1, key=lambda x:x['color'])
print("\n sorting the list of dictionaries")
print(sorted_d1)
