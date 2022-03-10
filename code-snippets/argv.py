"""argv.py"""
import sys

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

args = sys.argv[1:]
print(args)

# all(True, True, True) -> True
# all(False, True, True) -> False
if all(arg.isdigit() for arg in args):
    print(f"input was all digits, sum:{sum(int(arg) for arg in args)}")

if all(arg.isascii() for arg in args):
    print(f"input was all characters: { ','.join(args) }")

options = [arg for arg in sys.argv[1:] if '--' in arg]
ints = [int(arg) for arg in sys.argv[1:] if arg.isdigit()]

if '--add' in options:
    print(f"The sum is {sum(ints)}")
elif '--mult' in options:
    TOTAL = 1
    for int_ in ints:
        TOTAL *= int_

    print(f"The product is {TOTAL}")
