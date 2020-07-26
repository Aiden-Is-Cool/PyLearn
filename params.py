# Lesson #2:  This explores using arguments from the command line ("standard in" aka stdin) and doing a little bit of math with them.
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-x", help="The X value.", type=int)
parser.add_argument("-y", help="The Y value.", type=int)
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

args=parser.parse_args()
x = args.x
y = args.y
answer = x*y

print("=============================")
print(answer)

if args.verbose:
    print("Adding {} plus {} equals {}".format(args.x, args.y, answer))