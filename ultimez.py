n=int(input("enter number of individuals : "))


large=n//8
medium=(n%8)//6
regular=(n%6)//4
small=(n%4)//1

print("large : ",large)
print("medium : ",medium)
print("regular : ",regular)
print("small : ",small)