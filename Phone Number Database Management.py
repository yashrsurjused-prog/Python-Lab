import sys

def manage_phone_database():
    database = {}
    
    # Read first line for the number of operations
    line = sys.stdin.readline()
    if not line:
        return
        
    try:
        n = int(line.strip())
    except ValueError:
        return
    
    # Process each operation one by one
    for _ in range(n):
        line = sys.stdin.readline()
        if not line:
            break
            
        parts = line.strip().split()
        if not parts:
            continue
            
        command = parts[0]
        
        if command == "ADD":
            # format: ADD <name> <phone_number>
            name = parts[1]
            phone = parts[2]
            database[name] = phone
            
        elif command == "REMOVE":
            # format: REMOVE <name>
            name = parts[1]
    manage_phone_database()
