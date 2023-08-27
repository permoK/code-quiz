# ------------ @Permo ----------------

#this function finds the numbers divisibe by 5 in a given list
def divisible_by_5(my_list=[10,2,55,3]):
    #find the length of the string
    length = len(my_list)

    # loop through the elements of the list
    for i in range(length):
        #check the items which are divisible by 5
        if my_list[i]%5 == 0:
            #print the number
            print(i)

#call the function
divisible_by_5()

