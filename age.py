# Age Calculator Program

# User Details
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Friend Details
friend_name = input("Enter your friend's name: ")
friend_age = int(input("Enter your friend's age: "))

# Average Age
average_age = (age + friend_age) / 2

# Age Difference
age_difference = abs(age - friend_age)

# Display Results
print("\n------ Result ------")
print("Your Name:", name)
print("Your Age:", age)
print("Friend's Name:", friend_name)
print("Friend's Age:", friend_age)
print("Average Age:", average_age)
print("Age Difference:", age_difference)

# Compare Ages
if age > friend_age:
    print(name, "is older than", friend_name, "by", age_difference, "years.")
elif friend_age > age:
    print(friend_name, "is older than", name, "by", age_difference, "years.")
else:
    print("Both are the same age!")

#Enter your name: Harsh
#Enter your age: 22
#Enter your friend's name: Rahul
#Enter your friend's age: 20

#------ Result ------
#Your Name: Harsh
#Your Age: 22
#Friend's Name: Rahul
#Friend's Age: 20
#Average Age: 21.0
#Age Difference: 2
#Harsh is older than Rahul by 2 years.    