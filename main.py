#!/usr/bin/env python3
'''Plan is to create a small data base of our class so i can search and grade mine or others work including teachers
Start time 1:00pm 10/5/22'''
# TEACHERS
Teacher_0 = "Muhammad Azam" or "M.A" or "Muhammad"
Teacher_1 = "Nidhi Gowdra" or "N.G" or "Nidhi"
Teacher_2 = "Roman Mitch" or "R.M" or "Roman"
Teacher_3 = "Jay Panchal" or "J.P" or "Jay"
Teacher_4 = "Shahbaz Pervez" or "S.P" or "Shahbaz"
Teacher_5 = "Sarmad Soomro" or "S.S" or "Sarmad"
# STUDENTS
Student_0 = "Student Timothy Leatau" or "T.L" or "Timothy"
Student_1 = "Student Sherzod Nosirov" or "S.N" or "Sherzod"
Student_2 = "Student Charlie Colin" or "C.C" or "Charlie"
Student_3 = "Student Fungai Mathe Mabvurira" or "F.M" or "Fungai"
# User4 = input("")
# User5 = input("")
# User6 = input("")
# User7 = input("")
# User8 = input("")
# User9 = input("")
# User10 = input("")

Search = input("Search for Teacher or Student:")
score = 'Please enter your score:'

if Teacher_0 == "Muhammad Azam" or "M.A" or "Muhammad":
    print("Welcome Muhammad Azam.")
    score = int(input('Please enter your score:'))
    if 90 <= score <= 100:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('A++')
    if 80 <= score <= 90:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('A+')
    if 70 <= score <= 80:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('A')
    if 60 <= score <= 70:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('B')
    if 50 <= score <= 60:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('C')
    if 40 <= score <= 50:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('D')
    if 30 <= score <= 40:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('E')
    if 20 <= score <= 30:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('F')

    if not Teacher_0 == "Muhammad Azam" or "M.A" or "Muhammad":
        print("Please enter correct name")

elif Teacher_1 == "Nidhi Gowdra" or "N.G" or "Nidhi":
    print("Welcome Nidhi Gowdra")
    score = int(input('Please enter your score:'))
    if 90 <= score <= 100:  # Grater than or equal to 90pts or less than or equal to 100
        print("Great job you've achieved a grade of")
        print('A++')
    if not Teacher_0 == "Muhammad Azam" or "M.A" or "Muhammad":
        print("Please enter correct name")




'''elif Teacher_1 == "Nidhi Gowdra" or "N.G" or "Nidhi":
    if True:
        print("Nidhi Gowdra")

elif Teacher_2 == "Roman Mitch" or "R.M" or "Roman":
    print("Roman Mitch")

elif Teacher_3 == "Jay Panchal" or "J.P" or "Jay":
    print("Jay Panchal")

elif Teacher_4 == "Shahbaz Pervez" or "S.P" or "Shahbaz":
    print("Shahbaz Pervez")

elif Teacher_5 == "Sarmad Soomro" or "S.S" or "Sarmad":
    print("Sarmad Soomro")'''

'''if Search == "Q" or Search == "q":
    break'''

'''Search = input("Search for teacher or student:")
if Search =="Muhammad Azam" or "M.A" or "Muhammad":
    print(Teacher_0)'''
