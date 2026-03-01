def get(file_name, v_name):
    data = {}
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()  
            if "=" in line:
                key, value = line.split("=", 1)
                data[key.strip()] = value.strip()
    return data.get(v_name)
    
    
    
    
    
   
   
print(get(".env","NAME"))