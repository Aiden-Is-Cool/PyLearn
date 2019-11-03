import argparse
parser = argparse.ArgumentParser()

parser.add_argument("x", help="The X value.", type=int)
parser.add_argument("y",  help="The Y value.", type=int)
parser.add_argument("-v", "--verbosity", action="store_true", help="Verbose output")

args=parser.parse_args()
x= args.x
y=args.y
answer = x+y
print(answer)
print(args.x)
print(args.y)

if args.verbose:
    print("Adding {} plus {} equals {}".format(args.x, args.y, answer))

# print('Number of Arguments:' + str(len(sys.argv)) + '.')
# print('Argument List:' + str(sys.argv))


# str_Hello = "Hello World, I love you"