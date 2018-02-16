def first_recurring(given_string):
    counts = {}

    for char in given_string:
        if char in given_string:
            
            print(char)
            counts[char] = 1
            print(counts)
    
        
