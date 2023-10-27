#Number 4
print("This is Number 4.\n")
print("Typing 'done' will exit the program.\n")
integer_list = []
while True:
    user_input = input("Please enter an integer: ")
    
    if user_input.lower() == 'done':
        print("\n------- Bye !! -------")
        break
    try:
        numbers = int(user_input)
        integer_list.append(numbers)
        if len(integer_list) > 0:
            average = sum(integer_list) / len(integer_list)
        print(integer_list,f", average = {average}")
    except ValueError:
        print("\n<<<Please enter a valid integer.>>>\n")

print("\nEnd of program.")


