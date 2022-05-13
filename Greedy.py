import math
n = int (input("Enter a number: " ))

#minimum number of boxes that the machine will generate
box = [0] * int((math.log(n)/math.log(2))+1)

real_box = [0] * int((math.log(n)/math.log(2))+1)

#array contain values 1 2 4 8 .. 
for i in range (0, len(box)):
    box[i] = pow(2, i)
    
for j in reversed(range(0, len(box))):
    if n >= box[j]:
        real_box[j] = 1
        n -= box[j]
    elif n == 0:
        break
    else: 
        real_box[j] = 0
    print(real_box)
