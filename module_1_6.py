my_dict = { "KOLY" : 1967, "ZOY" : 1966, "ADY" : 1961 }
print(my_dict)
print(my_dict["ZOY"])
my_dict["IVAN"] = 1967
print(my_dict)
my_dict.update({"SLAVA" : 1957,
 "RIK" : 1988})
print(my_dict)
x = my_dict.pop("ZOY")
print(x)
print(my_dict)
my_set = {9,8,7,7,9,8,6,"ZOY","BIL","ZOY"}
print(my_set)
my_set.add(False)
my_set.add((4,5,6))
# my_set = {9,8,7,7,9,8,6,"ZOY","BIL","ZOY",False,(4,5,6)}
print(my_set)
my_set.remove(8)
print(my_set)