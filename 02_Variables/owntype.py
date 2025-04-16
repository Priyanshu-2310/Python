



def pritype(data):
    if data is None:
        return "None"
    
    elif(hasattr(data, 'lower') and hasattr(data, 'strip')):
        return "String"
    
    elif(isinstance(data, list)):
        return "List"
    
    elif(isinstance(data, dict)):
        return "dis"
    
    elif(isinstance(data, int)):
        return "Interger"
    
    elif(isinstance(data, float)):
        return "float"
    
    elif(isinstance(data, set)):
        return "set"
    
    else: 
        return "Unknown"
    



print(pritype("divyanshi"))