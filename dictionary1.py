dict1={"key1":10,"key2":20,"key3":30,"key4:":40,"key5":50}
print(dict1)
#method 1
#list=list(dict1.values()))
#print(list)
#method 2
#for i in dict1:
#    print(dict1[i])
#method 3 without using library functions
list1=[dict1[i] for i in dict1]
print(list1)
