def fibo(n):

    a,b=0,1
    #if series contain 0 terms thn it will priint 0 only and for 1 it will print 0,1
    if n==0:
        print(a)
    elif n==1:
        print(a,b)

    #if it contain more than 1 term thn it will print next terms according to fibonaci logic
    else:
        print(a,b, end=" ")

        #logic for fibonaci series
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(c,end=" ")

#taking input from user 
n=int(input("enter number of terms present in series: "))
fibo(n)
