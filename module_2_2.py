first =int( input('ВВЕДИТЕ 1-ое ЧИСЛО :'))
print(first)
second =int( input('ВВЕДИТЕ 2-ое ЧИСЛО :'))
print(second)
third = int(input('ВВЕДИТЕ 3-ье ЧИСЛО :'))
print(third)
if third == second == first :
    print('3')
elif third == second or second == first or third == first :
    print(2)
else:
    print('0')




