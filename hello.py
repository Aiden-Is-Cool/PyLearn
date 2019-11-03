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
""" 
print(str_Hello)
print(str_Hello[-1])
print(len(str_Hello))

str_Hello= "Goodbye world, I am dying"
print(str_Hello)

letters="n"
if letters=="y":
    for i in str_Hello:
        print(i)
else:
    for i in str_Hello:
        print(str_Hello)  """