#this functions returns the count of a substring from a string
def count_substring(str_x="Emma is a good developer. Emma is a writer"):
    #declare a variable to store the number of the substring
    c = str_x.count("Emma")
    #print the results 
    print(f"Emma appeared {c} times")

#call the function
count_substring()