#It is a collection of unorderes items 
#Each element in the set must be unique 
#NOTE:We can't store set and dic in the set
#set are mutable but elements in set are immutable

info={1,2,4,4,4,"hello","hello","vaibhav"}
print(info)
print(type(info))#Output:{1,2,4,'hello','vaibhav'}


#the repeted values are ignored in the set 
print(len(info))#total number of items in output

#Empty set
collection=set()
print(type(collection))