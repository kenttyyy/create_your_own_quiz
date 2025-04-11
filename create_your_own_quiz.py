# Changes text color using ANSI color code
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Use a while loop for infinite input, unless the user chooses to exit
while True:
    print(f"{BOLD}{CYAN}What do you want to do?")
    print(f"{YELLOW}Type 1 - Add A Question")
    print(f"{YELLOW}Type 2 - Exit")

    choice = int(input(f"{MAGENTA}Enter your choice 1 or 2: "))

# Ask user for a question
    if choice == 1:
        question = input(f"{BOLD}{GREEN}Enter a question ")
# Ask for 4 possible answer (a,b,c,d) and the correct answer.
        choice_one = input(f"{CYAN}Enter Choice A ")
        choice_two = input(f"{CYAN}Enter Choice B ")
        choice_three = input(f"{CYAN}Enter Choice C ")
        choice_four = input(f"{CYAN}Enter Choice D ")
        correct_answer = input(f"{CYAN}Enter the correct answer ")

# Write the collected data to a text file.
        with open("quiz_questions.txt", "a") as file:
            file.write(f"Question: {question}\n")
            file.write(f"A. {choice_one}\n")
            file.write(f"B. {choice_two}\n")
            file.write(f"C. {choice_three}\n")
            file.write(f"D. {choice_four}\n")
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write("\n")

# Ask another question until the user chose to exit.

    elif choice == 2:
        print(f"{BOLD}{MAGENTA}Exiting the Quiz Creator.")
        break
    else:
        print(f"{RED}Invalid input. Please enter 1 or 2.")