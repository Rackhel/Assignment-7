#Number 3
print("This is Number 3.\n")
with open('mbox.txt', 'r') as file:
    count = 0
    senders = []
    for line in file:
        if line.startswith("From") and not line.startswith("From:"):
            words = line.split()
            sender = words[1]
            senders.append(sender)
            count += 1

for sender in senders:
    print(sender)

print(f"\nTotal {count} were printed.")
print("\nEnd of program.")