
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == None:
        raise ValueError('No list entered')
    
    elif len(int_list) <= 0:
        return None
    
    else:
        max_val = int_list[0] 
        for i in int_list:
            if i > max_val:
                max_val = i
    return max_val

def reverse_rec(int_list):   # must use recursion
    if int_list == None:
        raise ValueError('No list entered')
    
    else:
        if len(int_list) == 0:
            return []
        return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
    if int_list == None:                                                        
        raise ValueError('No list entered')
    
    if len(int_list) == 0:
        return None
 
    if high >= low:
        midpoint = low + (high-low) // 2

        if int_list[midpoint] == target:
            return (midpoint)
    
        elif int_list[midpoint] < target:
                return bin_search(target, midpoint+1, high, int_list)

        else:
                return bin_search(target, low, midpoint-1, int_list)
    
    else:
        return None

    
