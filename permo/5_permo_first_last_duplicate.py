# ------------ @Permo ----------------

#function that checks whether the last and the first integers are equal
def duplicate(list):
    #find the length of the list
    length = len(list)

    #give a condition 
    if list[0] == list[length-1]:
        return True
    else:
        #if the above condition is not met then return false
        return False
    
#call the function 
print(duplicate([10,2,2,3,4,1]))