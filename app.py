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
credit_score = input('What is you "Credit Score"? ')
print()
credit_score = int(credit_score)
price = 1000000
if credit_score in range(670, 850):
    down_payment = 0.1
    down_payment *= price
    print(f'You have Good Credit, so your down payment is only ${down_payment:.2f}')
elif credit_score in range(300, 669):
    down_payment = 0.2
    down_payment *= price
    print(f'You have Bad Credit, so you have to put down ${down_payment:.2f}')
else:
    print('Error! "Invalid Credit Score" \nPlease, type in your Credit Score between 300 - 850')
