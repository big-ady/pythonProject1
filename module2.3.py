list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i= 0
while i < len(list) :
    if list[i] > 0 :
     print( list[i] )
    elif list[i] < 0:
        break
    i += 1