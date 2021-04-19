"""Count the frequency of elements in a given array"""

def CountFrequency(arr):
    list_number=arr
    frequency={}
    for number in list_number:
        if number in frequency:
            frequency[number]+=1
        else:
            frequency[number]=1

    return frequency


