def to_alternating_case(string):
    result = ""
    for x in string:
        if x.isupper():
            result += x.lower() 
        
        else: 
            result += x.upper()
    return result

# or you can just use swapcase()
