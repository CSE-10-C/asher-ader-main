'''
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of  6 to, 10 print Weird
If n is even and greater than 20, print Not Weird
'''


'''
If n is odd, print weird
'''



#this is the variable for the the number that the user imputs
n = int(input("Enter any number "))

#this checks if the number is odd
if n % 2:
#this prints weird if the number is odd and doesn't print if it isn't
    print("weird")





'''
If n is even and in the inclusive range of 2 to 5, print Not Weird
'''


#this is the variable for the the number that the user imputs
n = int(input("Enter any number "))

#this checks if its odd
if n % 2:
#if its odd it print nothing 
    print(" ")
    #if its even and between 1 and 6 then it prints not wierd
elif 1<n<6:
    print ("not wierd")






'''
If n is even and in the inclusive range of  6 to, 10 print Weird
'''


#this is the variable for the the number that the user imputs
n = int(input("Enter any number "))

#this checks if its odd
if n % 2:
#if its odd it print nothing 
    print(" ")
#if its even and between 5 and 11 then it prints not wierd
elif 5<n<11:
    print ("not wierd")




'''
If n is even and greater than 20, print Not Weird
'''


#this is the variable for the the number that the user imputs
n = int(input("Enter any number "))

#this checks if its odd
if n % 2:
#if its odd it print nothing 
    print(" ")
#if its even and and more than 20 then it prints not wierd 
elif n>19:
    print ("not wierd")
