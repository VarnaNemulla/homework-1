//Question1

test_str=input("Enter the word:")


new_str=test_str[:3]+test_str[5:]
reversed=new_str[::-1]
print(reversed)

//question1.2

num1 = int(input ("Enter First Number: "))

num2 = int (input ("Enter Second Number:"))


print("Enter which operation would you like to perform?")

ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0

if ch == '+':

 result = num1 + num2

elif ch =='-':

 result = num1 - num2

elif ch =='*':


 result = num1 * num2

elif ch == '/':

 result = num1 / num2

else:
 print ("Input character is not recognized!")

 //Question 2

marks = float(input ("Enter student score in class:"))

if marks>100 and marks<0:

 print ("Marks not in range")

elif marks <= 100 and marks >=90:

 print ("Grade: A")

elif marks >= 80 and marks <=89:

 print ("Grade: B")

elif marks >= 70 and marks <= 79:

 print ("Grade: C")

elif marks >=60 and marks <=69:

 print ("Grade: D")

elif marks <60 and marks >=0:

 print("Grade: F")

else:

 print ("Please enter a valid score")


//Question 3

string= input("Enter a sentence:")
string=string.replace("python", "pythons")
print("Modified string:",string)




