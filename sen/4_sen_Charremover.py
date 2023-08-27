
#@ Sen -----------Exercise -------- 

# Removing characters from a string
i=0
string=input("Input Your String: ")
remove=int(input("How many characters do you want to remove: "))

def char_remover():
    
    leng=len(string)
    # print(leng)
    
    #while leng>remove:
    if leng<=remove:
        print('String Length is too short')
    else:
        # setting remove to be equal to i
        i=remove
        
        # print from the string i. : is used to show to --> 
        print(string[i:i+len(string)])
        #print(string[0:i])
    
    
char_remover()