# FUNCTIONS
def flip(state, num) -> int:
    
    lst = []
    lst.extend(state)

    # Flip 1 pancake
    temp = ""
    if num == 1:
        if lst[1] == "w":
            lst[1] = "b"
        else:
            lst[1] = "w"
    
    # Flip 2 pancakes   
    elif num == 2:
        temp = lst[0]
        lst[0] = lst[2]
        lst[2] = temp
        
        temp = lst[1]
        lst[1] = lst[3]
        lst[3] = temp
        
        if lst[1] == "w":
            lst[1] = "b"
        else:
            lst[1] = "w"
            
        if lst[3] == "w":
            lst[3] = "b"
        else:
            lst[3] = "w"  
            
    # Flip 3 pancakes
    elif num == 3:
        temp = lst[0]
        lst[0] = lst[4]
        lst[4] = temp
        
        temp = lst[1]
        lst[1] = lst[5]
        lst[5] = temp
        
        if lst[1] == "w":
            lst[1] = "b"
        else:
            lst[1] = "w"
            
        if lst[3] == "w":
            lst[3] = "b"
        else:
            lst[3] = "w"  
        
        if lst[5] == "w":
            lst[5] = "b"
        else:
            lst[5] = "w"  
        
    # Flip 4 pancakes    
    elif num == 4:
        temp = lst[0]
        lst[0] = lst[6]
        lst[6] = temp
        
        temp = lst[2]
        lst[2] = lst[4]
        lst[4] = temp
        
        temp = lst[1]
        lst[1] = lst[7]
        lst[7] = temp
        
        temp = lst[3]
        lst[3] = lst[5]
        lst[5] = temp
    
        
        if lst[1] == "w":
            lst[1] = "b"
        else:
            lst[1] = "w"
        
        if lst[3] == "w":
            lst[3] = "b"
        else:
            lst[3] = "w"  
    
        if lst[5] == "w":
            lst[5] = "b"
        else:
            lst[5] = "w"

        if lst[7] == "w":
            lst[7] = "b"
        else:
            lst[7] = "w"
    
    ret = "".join(lst) 
    return ret
        
        
        
# CODE  
searched = []  
queue = []
pans = str(input())
searched.append(pans)
test = ""

# Select mode:
print("Select mode:")
inp = str(input())
if inp != "e" and pans[9] == "b":
    print("Normal Mode")
    
    while pans[0:8] != "1w2w3w4w":
        for i in range(1,5):
            test = flip(pans, i)
            if test not in searched:
                queue.append(test)
        searched.append(queue.pop(0))
        pans = queue[0]

            
    
else:
    layer = int(input())
    print(pans, layer)
    print("Experimental Mode")
    while layer <= 4 and pans[0:8] != "1w2w3w4w":
        pans = flip(pans, layer)
        searched.append(pans[0:8])
        print(pans, layer)
        print(searched)
        layer = int(input())





# POST SEARCH
if pans[0:8] == "1w2w3w4w":
    print("\n")
    print("COMPLETE")
    print(len(queue))
    print(len(searched))
else:
    print("END")
    
    
















