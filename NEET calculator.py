B=90
C=45
P=45
a=float(input("Biology (Questions Attempted)="))
b=float(input("Physics (Questions Attempted)="))
c=float(input("Chemistry (Questions Attempted)="))
d=a*4
e=(B-a)
f=b*4
g=(C-b)
h=c*4
i=(P-c)
print("Biology Marks=",d-e)
print("Physics Marks=",f-g)
print("Chemistry Marks=",h-i)
X=(d-e)
Y=(f-g)
Z=(h-i)
Total=X+Y+Z
print("Total Marks=",Total)
