data=[5,8,4,6,9,2]

def search(data,n):
    
    for i in range(len(data)):        
        if data[i]==n:
            return i+1
    return -1

n=int(input("enter a numb u want to search: "))
output=search(data,n) 
if output==-1:
    print("numb is not present")
else:
    print(f"numb is present at index {output}")




    