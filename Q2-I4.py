dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4}

keys = dict1.keys()
values = dict1.values()
items = dict1.items()
val1=dict1.get("b")
dict1.update(dict2)
dict1.update([("e", 5)])
pop = dict1.pop("b")

print("value of a is :",val1)
print("Keys:", list(keys))
print("Values:", list(values))
print("Items:", list(items))
print("Final Dict:", dict1)
