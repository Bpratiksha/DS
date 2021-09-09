# check given numb is prime or not
def is_prime(n):

    #check wheather numb is grater than 1 or not
    if n > 1:
        for i in range(2, (n//2)+1):

            #it will check the numb is divisible or not......if not then it will be prime
            if n % i == 0:
                return f"{n} is not a prime number"
        else:
            return f"{n} is prime number"

    # this is exception if numb is smaller than 1 ...it will ask to enter valid input
    else:
        return "enter valid input"

#input from user
numb = int(input("enter a number: "))
print(is_prime(numb))

#================================================================================================

#check prime numbers bewteen a perticular range 
def prime(s,l):

    #declearing specific range
    for i in range(s,l+1):

        # check numb is grater than 1 or not
        if i>1:

            #if numb is divisible then break else print number
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i, end=' ')   

#taking lower and heigheer range from user
s=int(input("enter lower number: "))
l=int(input("enter higher number: "))
prime(s,l)