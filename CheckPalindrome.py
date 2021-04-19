"""To check if string is palindrome or not A string is said to be palindrome if the reverse
of the string is the same as string. For example, “malayalam” is a
palindrome, but “music” is not a palindrome."""

def isPalindrome(check):
    reverse_string=check[::-1]
    if check==reverse_string:
        return "String is palindrome"
    else:
        return "not a palindrome"

    
