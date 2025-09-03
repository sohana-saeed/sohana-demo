# message = ""

# while message.lower()!= "bye":
#     message =input("You: ")
#     if message.lower()!= "bye":
#         print("chatbot: I hear you said", message)

# print("chatbot: Byee dear apna khayal rkhna..")

# distance = 0

# while distance<11:
#     print("Distance:", distance, "km")
#     distance+=1
# print("Trip end")

# rows = ["A", "B", "C"]

# for row in rows:
#     for seat in range(1,4):
#         print(row + str(seat) )

# total = 0
# num = int(input("Enter your number: "))
# while num!=0:
#     total+=num
#     num = int(input("Enter your number: "))

# print("total sum is:", total)
# correct_password = "sohana"
# password = ""
# while password!= correct_password:
#     password = input("Enter your password: ")
#     if password!= correct_password:
#         print("Invalid password, Try again")

# print("unlocked successfully")


# factorial = int(input("Enter your number: "))
# i = factorial
# fact = 1

# while i > 0:
#     fact=fact *i
#     i-=1

# print("The factorial is:",fact)

# num = int(input("Enter your number: "))
# limit = int(input("Enter limit number: "))

# i = 0
# while i<(limit+1):
#     mul = i*num
#     i+=1

# print("The multiplication is:", mul)

# total_even = 0
# num = int(input("Enter number (-1 to stop): "))

# while num != -1:
#     if num % 2 == 0:
#         total_even += num
#     num = int(input("Enter number (-1 to stop): "))

# print("Sum of even numbers =", total_even)

Total_sum = 0
num = int(input("Enter your number (-1 to stop): "))
while num!= -1:
    if num%2==0:
        Total_sum+=num
    
    num = int(input("Enter your number (-1 to stop): "))

print("the sum of even number:", Total_sum)

