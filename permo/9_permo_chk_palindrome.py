#checks if a number is a palindrome
def palindrome(num='121'):
    length = len(num)
    

    for i in range(length):
        left = 0
        right = length-1
        if num[left] == num[right]:
            right -= i
            left += i
            if right == 0:
                return f"Yes the number given palindrome"
        else:
            return f"the number given is not a pallindrome"


#call the function
print(palindrome())