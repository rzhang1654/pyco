#!/usr/bin/env python
def iterable(obj): 
    try: 
        iter(obj) 
        return True
          
    except TypeError: 
        return False
  
# Driver Code      
for element in [34, [4, 5], (4, 5),{4,5},
             {"a":4}, "dfsdf", 4.5]: 
                   
    print(element, " is iterable : ", iterable(element)) 
