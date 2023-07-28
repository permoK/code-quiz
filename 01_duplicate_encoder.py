def duplicate_encode(word):
    length = len(word)
   
    
    
    for i in range(length):
        letter_count =  (word.count(word[i]))
        if letter_count >1:
            return True
        else:
            return "no duplicate"
        
        
        

    
    
    
    
    
word = "din"

print(duplicate_encode(word))