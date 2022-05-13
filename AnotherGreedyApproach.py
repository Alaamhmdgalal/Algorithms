import math
n = int (input("Enter a number: " ))

#minimum number of boxes that the machine will generate
box = [0] * int((math.log(n)/math.log(2))+1)

box[0] = n

for i in range(0, len(box)-1):
    box[i+1] = int(box[i]/2)
    if box[i] % 2 == 0:
        box[i] = 0
    else:
        box[i] = 1
    print(box)
