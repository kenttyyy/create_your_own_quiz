# Use a while loop for infinite input, unless the user chooses to exit
while True:
    print("What do you want to do?")
    print("Type 1 - Add A Question")
    print("Type 2 - Exit")

    choice = int(input("Enter your choice 1 or 2: "))

# Ask user for a question
    if choice == 1:
        question = input("Enter a question ")
# Ask for 4 possible answer (a,b,c,d) and the correct answer.
        choice_one = input("Enter Choice A ")
        choice_two = input("Enter Choice B ")
        choice_three = input("Enter Choice C ")
        choice_four = input("Enter Choice D ")
        correct_answer = input("Enter the correct answer ")

# Write the collected data to a text file.



# Ask another question until the user chose to exit.

    elif choice == 2:
        print("Exiting the Quiz Creator.")
        break
    else:
        print("Invalid input. Please enter 1 or 2.")