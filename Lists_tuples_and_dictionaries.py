myFruits = ["apple", "banana", "cherry"]
print(myFruits)
print(type(myFruits))
print(myFruits[0])
print(myFruits[1])
print(myFruits[2])
myFruits[2] = "orange"
print(myFruits)
tuple1 = ("apple", "banana", "pineapple")
print(tuple1)
print(type(tuple1))
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
Dict = {
  "Akua" : "apple",
  "Sanvi" : "banana",
  "Paulo" : "pineapple"
}
print(Dict)
print(type(Dict))
print(Dict["Akua"])
print(Dict["Paulo"])
print(Dict["Sanvi"])

mixed=(45,234554,1.675,True,'My dog is on my bed',"45")

for objects in mixed:
    print("{} is one of the data type{}".format(objects,type(objects)))