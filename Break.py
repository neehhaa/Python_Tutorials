n=2
while(1):
    i=1;
    while i<=10:
        print("%d X %d = %d"%(n,i,n*i))
        i=i+1
    choice=int(input("DO YOU WANT TO CONTINUE?? PRESS 0 TO STOP!!! "))
    if choice == 0:
        break
    n=n+1