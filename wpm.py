
import time
def words(string):
    count = 0
    characters = {
        "space": " ",
        "question_mark": "?",
        "full_stop": "."
    }

    for i in range(len(string)):
       
        if string[i] in characters.values():
            count += 1

    
    return count + 1
    
    
def speed():
    start=time.time()
    string=input("Enter string here:")
    end=time.time()
    minute=(end-start)/60
    speed=words(string)/minute
    
    print(f"Your speed is {speed} words per minute.")
    
    
speed()
    
    
    
    

    
    
    

