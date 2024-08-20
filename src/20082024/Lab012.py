score = int(input("Enter the score of the student:\n"))

# if score >= 90:
#     print("The grade is ", 'A')
# elif score >= 80:
#     print("The grade is ", 'B')
# elif score >= 70:
#     print("The grade is ", 'C')
# elif score >= 60:
#     print("The grade is ", 'D')
# else:
#     print("The grade is ", 'FAIL')

if 90 <= score <=100:
    print("The grade is ", 'A')
elif 80 <= score <=89:
    print("The grade is ", 'B')
elif 70 <= score <=79:
    print("The grade is ", 'C')
elif 60 <= score <=69:
    print("The grade is ", 'D')
elif 0 <= score <=59:
    print("The grade is ", 'FAIL')
else:
    print("You are a super man")