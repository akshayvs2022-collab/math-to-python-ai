def generate_ap(start, difference, terms):
    """Generates an Arithmetic Progression sequence."""
    return [start + (i * difference) for i in range(terms)]

# The Function Header: def generate_ap(start, difference, terms):
# def: Tells Python you are defining a new function.
# generate_ap: The name of your function (short for "generate arithmetic progression").
# (start, difference, terms): These are the inputs (parameters) the function needs to do its job:

# The Docstring: """Generates an Arithmetic Progression sequence."""
# This is a docstring (documentation string). It doesn't affect how the code runs, but it explains to anyone reading your code what the function does.

# The Core Logic: return [start + (i * difference) for i in range(terms)]This part uses a list comprehension, 
# which is a compact way to build a list using a loop.
#  Let's translate it into plain English:range(terms): This generates a sequence of numbers starting from 0 up to terms - 1.
# If terms = 4, range(4) gives us: 0, 1, 2, 3.for i in range(terms): A loop that takes each number from that range one by one and stores it in the variable i.
# start + (i * difference): This is the mathematical formula for the $i$-th term of an AP.
# [...]: The square brackets tell Python to put all the calculated values into a list and return (send) that list back to wherever the function was called.

print("--- Arithmetic Progression Solver ---")

# Printing the Title
# print(...): Displays text on the screen in your terminal.
# It prints --- Arithmetic Progression Solver --- just to make the program look professional and tell the user what they are running.



# Asking the user for input
# We use float() or int() to convert the text input into numbers
start = float(input("Enter the starting number (a): "))
difference = float(input("Enter the common difference (d): "))
terms = int(input("Enter the number of terms (n): "))

# Getting the Starting Number
# input("..."): This pauses the program, prints the text "Enter the starting number (a): ", and waits for you to type something on your keyboard and press Enter.
# ⚠️ Important Python Rule: By default, whatever you type into input() is treated as text (a string), even if you type a number like 8000. You cannot do math on text!
# float(...): This wraps around the input and converts that text into a floating-point number (a decimal number) like 8000.0, allowing Python to perform mathematical calculations with it.

# Getting the Common Difference
# It uses float() so the difference can be a whole number, a decimal, or even a negative number.


# Getting the Number of Terms
# This asks how many terms you want to generate (e.g., how many years of salary or how many rungs on the ladder).

# int(...): Notice this uses int() instead of float(). Why? Because the number of terms must be a whole counting number (like 4 or 8). You can't have 4.5 terms in a sequence! int() converts the text input into an integer.

# Generating the sequence
sequence = generate_ap(start, difference, terms)

# Calculating the sum of the AP using the formula: S_n = n/2 * [2a + (n-1)d]
total_sum = (terms / 2) * (2 * start + (terms - 1) * difference)

# Displaying the results
print("\n--- Results ---")
print(f"Your AP Sequence: {sequence}")
print(f"The last term is: {sequence[-1]}")
print(f"The sum of all terms is: {total_sum}")