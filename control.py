"""
Using control flow to perform decisions based on certain conditions
"""
number = 1  # test with 10, 18 e.t.c.

if number == -1:
    print(f"{number} is Negative number")
elif number == 3:
    print(f"{number} is equal to 3")
elif number > 3:
    print(f"{number} is greater than 3")
else:
    print(f"{number}")


"""
Using Ternary if statements.
Use this for cases where only one if and else exist
"""
text = "Hi ya, dear" if number == 1 else f"{number} is not equal to 1"
print(text)
