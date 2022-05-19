                                        # Grading Calculator
"""My original goal was to add teachers and students but after touching on the bingo project I had built
 a simple grade calculator"""
# TEACHERS
Teacher_1 = "Nidhi Gowdra", "N.G", "Nidhi"

# My Variables
score = 'Please enter your score:'
other = 'invalid'
typez = 'entered name'

while True:
    # While True will loop my code until the user decides to type "q" or "Q"
    # Line below will display 1st when the programme is run
    print("Welcome to my grading calculator")
    print()
    print()
    Search = input("Please press enter to continue")
    if Search == "Q" or Search == "q":
        break
    # My attempt at trying to have a small search function,I hoped for the user to type in their name to acquire their
    # name and also see a grade next to their name, but it's proven to get the best of me as of this moment
    if Search == "Nidhi Gowdra" or "N.G" or "Nidhi":
        print()
        print("Welcome Nidhi Gowdra or guest user")
        print()
        score = int(input('Please enter your IT Systems exam score :'))  # This line will appear when user has correct name
        score2 = int(input("Please enter your project score :"))
        final_results = (score + score2) * 0.5
        if 80 <= final_results <= 100:  # Grater than or equal to 90pts or less than or equal to 100pts
            print("Great job you've achieved a grade of")
            print()
            print('"A"')
            print('Please continue'"\n")
            print('If you would like to quit type "Q" or "q"'"\n")
        elif 70 <= final_results <= 79:  # Grater than or equal to 75pts or less than or equal to 89pts
            print("Great job you've achieved a grade of")
            print()
            print('"B"')
            print('Please continue'"\n")
            print('If you would like to quit type "Q" or "q"'"\n")
        elif 60 <= final_results <= 69:  # Grater than or equal to 60pts or less than or equal to 74pts
            print("Great job you've achieved a grade of")
            print()
            print('"C"')
            print('Please continue'"\n")
            print('If you would like to quit type "Q" or "q"'"\n")
        elif 50 <= final_results <= 59:  # Grater than or equal to 45pts or less than or equal to 59pts
            print("Great job you've achieved a grade of")
            print()
            print('"D"')
            print('Please continue'"\n")
            print('If you would like to quit type "Q" or "q"'"\n")
        elif 40 <= final_results >= 49:  # Grater than or equal to 30pts or less than or equal to 44pts
            print("Great job you've achieved a grade of")
            print()
            print('"Fail"')
            print('Please continue'"\n")
            print('If you would like to quit type "Q" or "q"'"\n")
    else:  # Else statement was incase the user typed in the wrong name or number in the search area
        print('Failed, Please try again')
    if Search == "Q" or Search == "q":
        break
