#this function adds the ten previous number and next number in a range of 10
def prev_next():
    #create a for loop with a range of 10 numbers
    for i in range(10):
        #declare the variables prev, next and sum
        current = i
        prev = i-1
        # if the previous is less than zero make it a zero 
        if prev < 0:
            prev = 0
        sum = int(current) + int(prev)

        # print the output
        print("Current number {} previous number {} sum: {}".format(current, prev, sum))

#call the function
prev_next()