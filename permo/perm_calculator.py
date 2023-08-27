# ------------ @Permo ----------------

#this function returns their product only if the product is equal to or lower than 1000, else return their sum.

def cal():
    first = input("Enter the first integer: ")
    second = input("Enter the second integer: ")
    #calculate the product
    product = int(first) * int(second)

    #check if the product is greater than 1000
    if product > 1000:
        #if greater make the sum of the integers
        sum =  int(first) + int(second)
        return sum
    else: #if product is less than 1000 return the product instead
        return product
    
#call the function
print(cal())