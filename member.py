{
}
name1 = (input("Member 1, Please insert your full name: "))
name2 = (input("Member 2, Please insert your full name: "))
name3 = (input("Member 3, Please insert your full name: "))
name4 = (input("Member 4, Please insert your full name: "))
name5 = (input("Member 5, Please insert your full name: "))

nickname1 = (input("Member 1, Please insert your nickname: "))
nickname2 = (input("Member 2, Please insert your nickname: "))
nickname3 = (input("Member 3, Please insert your nickname: "))
nickname4 = (input("Member 4, Please insert your nickname: "))
nickname5 = (input("Member 5, Please insert your nickname: "))

age1 = int(input("Member 1, please insert your age: "))
age2 = int(input("Member 2, please insert your age: "))
age3 = int(input("Member 3, please insert your age: "))
age4 = int(input("Member 4, please insert your age: "))
age5 = int(input("Member 5, please insert your age: "))
average_age = ((age1+age2+age3+age4+age5)/5)

height1 = int(input("Member 1, please insert your height in centimeter: "))
height2 = int(input("Member 2, please insert your height in centimeter: "))
height3 = int(input("Member 3, please insert your height in centimeter: "))
height4 = int(input("Member 4, please insert your height in centimeter: "))
height5 = int(input("Member 5, please insert your height in centimeter: "))
average_height = ((height1+height2+height3+height4+height5)/5)

print("The full name of the first member is", name1 + ".", end = " ") 
print("The nickname of the first member is", nickname1 + ".", end = " ") 
print("The age of the first member is", age1, end = " ") 
print("years old.", end = " ") 
print("the height of the first member is", height1, end = " ") 
print("cm.")


print("The full name of the second member is", name2 + ".", end = " ") 
print("The nickname of the second member is", nickname2 + ".", end = " ") 
print("The age of the second member is", age2, end = " ") 
print("years old.", end = " ") 
print("The height of the second member is", height2, end = " ") 
print("cm.")

print("The full name of the third member is", name3 + ".", end = " ") 
print("The nickname of the third member is", nickname3 + ".", end = " ") 
print("The age of the third member is", age3, end = " ") 
print("years old.", end = " ") 
print("The height of the third member is", height3, end = " ") 
print("cm.")

print("The full name of the fourth member is", name4 + ".", end = " ") 
print("The nickname of the fourth member is", nickname4 + ".", end = " ") 
print("The age of the fourth member is", age4, end = " ") 
print("years old.", end = " ") 
print("The height of the fourth member is", height4, end = " ") 
print("cm.")

print("The full name of the fifth member is", name5 + ".", end = " ") 
print("The nickname of the fifth member is", nickname5 + ".", end = " ") 
print("The age of the fifth member is", age5, end = " ") 
print("years old.", end = " ") 
print("The height of the fifth member is", height5, end = " ") 
print("cm.")
print("Our average member's age is", average_age, end = " ") 
print("years old")
print("Our average member's height is", average_height, end = " ") 
print("cm")
