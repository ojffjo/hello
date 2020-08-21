# Python Tutorial with "Mosh Hamedani"

# course = "Python for Beginners"
# print(course[0:5])
# print(len(course))  # to count number of character include space
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.find("Beginners"))  # Return the index of "B"
# print('Python' in course)  # Return Boolean values, True or False
# print(course.replace("Beginners", "Absolute Beginners"))
#
# a = "This is the island of istanbul"
# # 3 is the maximum replacement that can be done in the string
# print(a.replace("is", "was", 3))  # Output --> Thwas was the wasland of istanbul


# If clause
# Score range 300-850, Bad credit is below 670
# credit_score = input('What is you "Credit Score"? ')
# print()
# credit_score = int(credit_score)
# price = 1000000
# if credit_score in range(670, 850):
#     down_payment = 0.1
#     down_payment *= price
#     print(f'You have Good Credit, so your down payment is only ${down_payment:.2f}')
# elif credit_score in range(300, 669):
#     down_payment = 0.2
#     down_payment *= price
#     print(f'You have Bad Credit, so you have to put down ${down_payment:.2f}')
# else:
#     print('Error! "Invalid Credit Score" \nPlease, type in your Credit Score between 300 - 850')


# # ** Weight Converter **
# weight = input('Weight: ')
# # to check if input is number
# while True:
#     try:
#         weight = int(weight)
#         break
#     except ValueError:
#         try:
#             weight = float(weight)
#             break
#         except ValueError:
#             # print('Your input is not a number. Please enter a valid Number!')
#             break
#
# if isinstance(weight, int) or isinstance(weight, float):
#     weight = float(weight)
#     print(weight)
#     unit = input('(L)bs or (K)g: ')
#     unit = unit.lower()
#     if unit == 'l':
#         converted_weight = weight * 0.45
#         print(f'You are {converted_weight:.1f} Kg.')
#     elif unit == 'k':
#         converted_weight = weight / 0.45
#         print(f'You are {converted_weight:.1f} Lbs.')
#     else:
#         print('Please enter only "L" or "K"!')
# else:
#     print('Your input is not a number. Please enter a valid Number!')

# for loop
# for item in 'Python':
#     print(item)
# print()
#
# for item in ['Jiab', 'Peter', 'Prateep']:
#     print(item)
# print()
#
# for item in range(10):
#     print(item)
#
# print()
# for item in range(5, 10):
#     print(item)

# # Calculate total price
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += (price)
# print(f'Total: {total}')
# print()
#
#
# # Nested loop
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')
#
# print()


# # Use for loop print "F" letter
# numbers = [2, 2, 2, 2, 8]
# for x_count in numbers:
#     count = ''
#     for i in range(x_count):
#         count += 'X'
#     print(count)
#
# print()

# # List
# names = ['Jiab', 'Peter', 'Prateep', 'Kul', 'Nattcha', 'ปิติ']
# print(names[1])
# print(names[-1])

# # finding the largest number in the list
# numbers = [3, 6, 8, 37, 5, 27]
# max_number = numbers[0]  # assume first number in the list is the largest number
#
# for number in numbers:
#     if number > max_number:
#         max_number = number
# print(max_number)


# # 2D List
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix[0][1] = 20
# print(matrix[0][1])
# print(matrix)

# Program to remove duplicate number in list
numbers = [2, 4, 6, 8, 2, 4, 6, 10]
unique = []  # Create new list if the number is not already in, add it to the list
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

