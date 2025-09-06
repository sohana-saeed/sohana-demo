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

# Total_sum = 0
# num = int(input("Enter your number (-1 to stop): "))
# while num!= -1:
#     if num%2==0:
#         Total_sum+=num
    
#     num = int(input("Enter your number (-1 to stop): "))

# # print("the sum of even number:", Total_sum)

# days = [1, 2, 3]
# slots = ["Morning", "Evening"]

# for d in days:
#     for s in slots:
#         print("Day", d, "-", s)

# rows = [1, 2, 3]
# seats = ["A", "B", "C", "D"]

# for r in rows:
#     for s in seats:
#         print(str(r) + s, end=" ")

# for i in range(3):
#     for j in range(3):
#         print("X", end="")
#     print()

# for i in range(5):
#     for j in range(i):
#         print("*", end="")
#     print()
    
# players = ["Ali", "Sana", "Ahmed"]

# for i in range(len(players)):
#     for j in range(i + 1, len(players)):
#         print(players[i], "vs", players[j])

# for i in range(2, 6):
#     print("Table of", i)
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)
#     print()

# for i in range(1,6):
#     for j in range(1, 4):
#         print(j*i, "", end="")
#     print()

# for i in range(6):
#     for j in range(i):
#         print(j+1, end="")
#     print()

# for i in range(4):
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(4):
#     for j in range(4-i):
#         print("*", end="")
#     print()



# for i in range(6):
#     for j in range(i):
#         print(j+1, end="")
#     print()


# for i in range(1, 4):
#     j = 1
#     while j <= i:
#         print(j, end="")
#         j += 1
#     print()

# def greet(name = "bacchi"):
#     print("Hello pyari", name, "!")
#     return greet

# greet("sohana")
# greet()


# def square(num):
#     return num**2

# num = int(input("Enter your number: "))
# print("The square is", square(num))


# def power(base, expo = 2):
#     return base ** expo

# # base = int(input("Enter your base: "))
# # expo = int(input("Enter your expo: "))
# print("The answer is", power(4))

name = ["ali", "sana", "ahmed"]
num = [3,7,9]
res = []
for i in range(len(name)):
    res.append((name[i], num[i]))

print(res)

