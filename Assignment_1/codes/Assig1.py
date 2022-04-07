k = -2
#To verify the solution, we prove the givens and the results of the solution are, as a whole, consistent with the remainder theorem.
#We know the remainders after division by (x + 1) and (x - 2) are -13 and 14 respectively. 
#We know that the value of k is -2

def polynom(x):
    return x ** 3 + (k * x + 8) * x + k

if polynom(-1) != -13 or polynom(2) != 14:
    print("False.")
else:
    print("True.")
    
    
#Verification of the given "Sum of remainders is 1" is trivial, as 14 - 13 = 1.
