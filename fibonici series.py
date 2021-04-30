tn = int(input("Enter the Number of terms of the fibonici series :-"))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if tn <= 0:
   print("Please enter a positive integer")
elif tn == 1:
   print("Fibonacci sequence upto",tn,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < tn :
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1