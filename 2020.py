class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
val1 = int(input("Enter number one:"))
print(val1)
val2 = int(input("Enter number two:"))
print(val2)

print(bcolors.OKGREEN + "Enter choice(1/2/3/4)" + bcolors.ENDC)
print(bcolors.OKBLUE + "1. Add" + bcolors.ENDC) 
print(bcolors.OKBLUE + "2. Subtract" + bcolors.ENDC)
print(bcolors.OKBLUE + "3. Multiply" + bcolors.ENDC)
print(bcolors.OKBLUE + "4. Division" + bcolors.ENDC)
choice = input(bcolors.OKGREEN + "input here: " + bcolors.ENDC)

if choice == '1':
    print('The sum of your numbers are ' + str(val1 + val2) + '.')
elif choice == '2':
    print('Your numbers when subtracted are ' + str(val1 - val2) + '.')
elif choice == '3':
    print('Your numbers when multiplyed are ' + str (val1 * val2) + '.')
elif choice == '4':
    print('Your numbers when divided are ' + str (val1 / val2) + '.')
else:
    print("Invalid input.")






