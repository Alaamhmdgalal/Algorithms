def decimalToBinary(n):
    return bin(n).replace("0b","")


if __name__ == '__main__':
    n = int (input("Enter a number: " ))
    print(list(reversed(decimalToBinary(n))))
