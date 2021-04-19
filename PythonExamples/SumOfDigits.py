"""Sum of digits"""


def sumOfDigits(number):
    total=0
    while (number!=0):
        total = total+(number%10)
        number = number//10
    
    return total



def sumofDigits2(number):
    
    return sum(list(map(int,number.strip())))


number=int(input("Enter a number"))

print("Sum of {} is {}".format(number,sumOfDigits(number)))






