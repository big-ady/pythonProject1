immutable_var=(1,2,True,"python")
print(immutable_var)
#immutable_var[1] = 100 # ошибка кортеж является неизменяемым списком
print(immutable_var)
mutable_list =[10,9,8,False]
print(mutable_list)
mutable_list[2] = 3
print(mutable_list)