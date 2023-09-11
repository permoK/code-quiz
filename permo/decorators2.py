#recap of decorators

#the f in the decorator function replaces any function as used when calling the decorator

def trigger(f): #3
    def permission(): #4
        print("waits for the function")

        #this calls the function with the decorator
        f() #5

        print("actually calls the function")
#this returns the function held by the decorator
    return permission #4


#add the decorator 
@trigger  #2
def hello(): #define a function  #5
    print("hello world")


#call the hello function and see whether the decorator does the work
hello()  #1
