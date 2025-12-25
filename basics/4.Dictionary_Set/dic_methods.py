info={
    "name":"vaibhav sonawane",
    "Language":{"python":30,
                "C":90,
                "C++":20
                },
    "Collage":"JSPM University",
    "Age":21
} 
print(info.keys()) #return keys
print(info.values()) #return values
print(info.items()) #return all(keys,value) pairs as tuples
print(info.get("name")) #return keys according to value
print(info.update({"city":"Pune"})) #insert the specified item to thew dictionary
print(info)