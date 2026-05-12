# STEP 1 — UNDERSTAND
# What does it do:
#   Takes two numbers from user, swaps their values
#   without using any third/temp variable
#
# Input:  Two numbers (default a=5, b=10 if left blank)
# Output: Both values printed after swap
#
# Rules:
#   - No third variable for swapping
#   - input() returns string — must convert to number
#   - If both blank use defaults a=5, b=10
#   - If only one blank show specific error
#   - If same value warn user but still swap
#
# Edge cases:
#   - Both blank       → use defaults
#   - One blank        → ask which one is missing
#   - Same values      → warn but swap anyway
#   - Letters entered  → must handle gracefully

# STEP 2 — EXAMPLES
# Example 1: a=2, b=4     → After swap: a=4, b=2
# Example 2: a="", b=""   → Use defaults: a=5, b=10
#                            After swap: a=10, b=5
# Example 3: a=4, b=4     → Warning: same values
#                            After swap: a=4, b=4
# Example 4: a="", b=7    → Error: a is missing

# STEP 3 — PIECES
# Piece 1: Get input for a and b
# Piece 2: Handle blank inputs — both blank or one blank
# Piece 3: Convert string inputs to numbers safely
# Piece 4: Check if values are the same — warn if so
# Piece 5: Swap using tuple unpacking — no third variable
# Piece 6: Print the result

# ============================================================
# SOLUTION
# ============================================================


# Piece 1 — get inputs
a_input = input("Enter value of a (press Enter for default 5) : ").strip()
b_input = input("Enter value of b (press Enter for default 10): ").strip()


# Piece 2 — handle blank inputs
if a_input == "" and b_input == "":
    # Both blank — use defaults
    a = 5
    b = 10
    print("Both blank — using defaults: a=5, b=10")
    
elif a_input == "" and b_input != "":
    # Only a is blank
    print("Error: You left 'a' empty. Please enter a value for a.")
    exit()

elif a_input != "" and b_input == "":
    # Only b is blank
    print("Error: You left 'b' empty. Please enter a value for b.")
    exit()

else:
    # Piece 3 — both provided, convert to numbers
    try:
        a = float(a_input)
        b = float(b_input)
    except ValueError:
        print("Error: Please enter numbers only, not text.")
        exit()

# Piece 4 — warn if same values
if a == b:
    print(f"Note: Both values are the same ({a}). Swap will not change anything.")

# Piece 5 — swap without third variable
print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a

# Piece 6 — print result
print(f"After swap:  a = {a}, b = {b}")