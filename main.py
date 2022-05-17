                                            # Grading Calculator

"""EDIT THE GREATER OR EQUAL SIGN TO LESS THAN OR EQUAL TO MOSTLY BECAUSE THE GRADE WILL BE THE WRONG LETTER"""

'''Plan is to create a small data base of our class so i can search and grade mine or others work including teachers
Start time 1:00pm 10/5/22 finished part of it at 7:00, Finished most of the project but now im moving on to the Bingo
game.started working at 9:00am stopped working at 11:53am'''
# TEACHERS
Teacher_1 = "Nidhi Gowdra", "N.G", "Nidhi"
#Teacher_2 = "Roman Mitch", "R.M", "Roman"
#Teacher_3 = "Jay Panchal", "J.P", "Jay"
#Teacher_4 = "Shahbaz Pervez", "S.P", "Shahbaz"
#Teacher_5 = "Sarmad Soomro", "S.S",  "Sarmad"
# STUDENTS
#Student_0 = "Student Timothy Leatau" or "T.L" or "Timothy"
#Student_1 = "Student Sherzod Nosirov" or "S.N" or "Sherzod"
#Student_2 = "Student Charlie Colin" or "C.C" or "Charlie"
#Student_3 = "Student Fungai Mathe Mabvurira" or "F.M" or "Fungai"

# My Variables
score = 'Please enter your score:'
other = 'invalid'
typez = 'entered name'

while True:
    # While True will loop my code until the user decides to type "q" or "Q"
    # Line below will display 1st when the programme is run
    Search = input("Search for Teacher or Student, initials or first name:")
    if Search == "Q" or Search == "q":
        break
    # My attempt at trying to have a small search function,I hoped for the user to type in their name to acquire their
    # name and also see a grade next to their name, but it's proven to get the best of me as of this moment
    if Search == "Nidhi Gowdra" or "N.G" or "Nidhi":
        print("Welcome Nidhi Gowdra.")
        score = int(input('Please enter your score:'))  # This line will appear when user has correct name

        if 90 <= score <= 100:  # Grater than or equal to 90pts or less than or equal to 100pts
            print("Great job you've achieved a grade of")
            print('"A"')
            print('Please continue')
            print('If you would like to quit type "Q" or "q"')
        elif 75 <= score <= 89:  # Grater than or equal to 75pts or less than or equal to 89pts
            print("Great job you've achieved a grade of")
            print('"B"')
            print('Please continue')
            print('If you would like to quit type "Q" or "q"')
        elif 60 <= score <= 74:  # Grater than or equal to 60pts or less than or equal to 74pts
            print("Great job you've achieved a grade of")
            print('"C"')
            print('Please continue')
            print('If you would like to quit type "Q" or "q"')
        elif 45 <= score <= 59:  # Grater than or equal to 45pts or less than or equal to 59pts
            print("Great job you've achieved a grade of")
            print('"D"')
            print('Please continue')
            print('If you would like to quit type "Q" or "q"')
        elif 30 <= score >= 44:  # Grater than or equal to 30pts or less than or equal to 44pts
            print("Great job you've achieved a grade of")
            print('"E"')
            print('Please continue')
            print('If you would like to quit type "Q" or "q"')
        elif 0 <= score <= 10:  # Grater than or equal to 0pts or less than or equal to 10pts
            print("Great job you've achieved a grade of")
            print('"F"')
            print('Please continue')
            print('If you would like to quit type "Q" or "q"')
    else:  # Else statement was incase the user typed in the wrong name or number in the search area
        print('Failed, Please try again')
    if Search == "Q" or Search == "q":
        break

# My little test area
'''for Teacher_0 in array:
    print('One second.')
    if successful:
        print("Welcome Muhammad Azam.")
else:
    print("Please enter a valid name")

if array:'''

#  Is it possible to have a small login
#  How to only search for specific words like in an array
