d = {"name" : "jeno", "age" : 24}
print(d)
print(type(d))

data = [("name", "jeno"), ("age", 24), ("gender", "male")]
d1=dict(data)
print(d1)
print(type(d1))
#print(d["nam"])
print(d.get("name"))
print(d.get("city", "jaffna"))
d.update({"city":"jaffna"})
d["Nic"] = "200134500469"
print(d)

print("name" in d)
d.update({"city":"jaffna", "age" : 50})
print(d)
del d["name"]
#d.pop("age")
#d.popitem()
#d.clear()
value = d.values()
print(value)
key = d.keys()
print(key)
print(d)