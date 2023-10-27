#Number 1
print("This is Number 1.")
def chop(input_list):
    if len(input_list) >= 2:
        del input_list[0]
        del input_list[-1]
    return None

def middle(input_list):
    if len(input_list) >= 2:
        return input_list[1:-1]

user_input = input("\nEnter the list with space (1 2 3 4): ").split()
input_list = [int(item) for item in user_input]

print("\nmy list before call chop function =>", input_list.copy())
chop(input_list)
print("my list after call chop function =>", input_list)

input_list = [int(item) for item in user_input]

print("\nmy list before call middle function =>", input_list)
new_list = middle(input_list)
print("my list after call middle function =>", input_list)
print("new list after call middle function =>", new_list)

print("\nEnd of program.")
