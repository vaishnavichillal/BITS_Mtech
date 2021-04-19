"""Armstrong number"""
import math

def Armstrong(number,order):
    total=0
    temp=number
    while (temp!=0):
        
        total = total+pow((temp%10),order)
        temp = temp//10
    
    return (total==number)



