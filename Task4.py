import math
n = int (input("Enter a number: " ))

box = [0] * int((math.log(n)/math.log(2))+1)

box[0] = n
print(box)
for i in range (0, len(box)):
    while(box[i] !=0 and box[i] > 0 and box[i] != 1):
        if (n % 2 == 0):
            box[i] -=2
            box[i+1] +=1
            print(box)
            n-=2

        else:
            box[i] -=2
            box[i+1] +=1
            print(box)
            n-=2