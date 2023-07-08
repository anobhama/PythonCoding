#Python program to swap two elements in a list

a=[1,2,3,4,5]

b=int(input("Enter the 1st index to be swapped: "))
c=int(input("Enter the 2nd index to be swapped: "))

a[b],a[c]=a[c],a[b]

print(a)