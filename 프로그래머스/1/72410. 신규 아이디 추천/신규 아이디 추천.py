import re

def solution(new_id):
    # 1
    new_id = new_id.lower()
    
    # 2
    regx = r"[^a-z0-9-_.]"
    new_id = re.sub(regx, "", new_id)
    
    # 3
    regx = r"\.+"
    new_id = re.sub(regx, ".", new_id)
    
    # 4
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    
    # 5
    if new_id == "":
        new_id = "a"
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    
    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id