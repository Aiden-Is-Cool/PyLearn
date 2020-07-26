# Lesson #3:  This explores using conditionals plus arguments plus using formattting in our output.
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("o", help="Operation (a=Additon, s=Subttracton, m=Multiplication, d=division )", type=str, choices=["a","s","m","d"])
parser.add_argument("x", help="The X value.", type=int)
parser.add_argument("y", help="The Y value.", type=int)
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

args=parser.parse_args()
o = args.o
x = args.x
y = args.y

if o == "a":
    answer = x+y
elif o == "s":
    answer = x-y
elif o == "m":
    answer = x*y
elif o =="d":
    answer = x/y

print("=============================")
print(answer)

if args.verbose:
    print("Adding {} plus {} equals {}".format(args.x, args.y, answer))