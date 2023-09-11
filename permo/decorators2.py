#recap of decorators

def trigger(f):
    def permission():
        print("waits for the function")

        #this calls the function with the decorator
        f()

        print("actually calls the function")

    return permission


#add the decorator function
@trigger 
def hello(): #define a function 
    print("hello world")


#call the hello function and see whether the decorator does the work

hello()
