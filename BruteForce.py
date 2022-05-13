import math
n = int (input("Enter a number: " ))

#minimum number of boxes that the machine will generate
box = [0] * int((math.log(n)/math.log(2))+1)

#give the first box the number of pennies to start the iterations
box[0] = n
print(box)

#iterate on each box and replace a pair of pennies with a single penny
for i in range (0, len(box)):
    #the stopping condition 
    while(box[i] !=0 and box[i] != 1):
            box[i] -=2
            box[i+1] +=1
            print(box)
