#stores values in form
#key = value
info={
    "name":"vaibhav sonawane",
    "Language":["python","C","C++"],
    "Collage":"JSPM University",
    "Age":21
}
#we can use all type of data types in dictionary
#dictionary are unordered and are mutable  
print(info)
#nested Dictionary
info={
    "name":"vaibhav sonawane",
    "Language":{"python":30,
                "C":90,
                "C++":20
                },
    "Collage":"JSPM University",
    "Age":21
}
print(info["Language"])