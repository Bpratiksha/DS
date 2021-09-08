#Selection sort in Python

def sort(data):
    try:
        for i in range(len(data)):
            temp=i
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            for j in range(i+1,len(data)):
                if data[j]<data[temp]:
                    temp=j
             
            # put min at the correct position
            data[temp],data[i]=data[i],data[temp]   

    except:
        print("enter valid input")

data=[34,7,98,2,6,1]
sort(data)
print(f"selection sort:=> {data}")
