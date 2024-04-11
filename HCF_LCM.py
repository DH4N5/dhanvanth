n1=int(input("Enter your number: "))
n2=int(input("Enter your number: "))
x=0
for i in range(1,n1+n2):
    if n1%i==0 and n2%i==0:
        x=i
print("HCF=",x)
print("LCM=",(n1*n2)/x)

