#Number 2
print("This is Number 2.\n")

with open('romeo.txt', 'r') as file:
    word_list = []  

    for line in file:
        words = line.split()  

        for word in words:
            if word not in word_list:
                word_list.append(word)

    word_list.sort()
    print(word_list)
    print("\nThere are", len(word_list), "words.")
    print("\nEnd of Program.")



