# ============================================================
# Question 1 — Print Hello World with your name
# Date: [12-May-2026]
# ============================================================

# STEP 1 — UNDERSTAND
# What does it do:  
#   -Takes Input text from the User(Name) 
#   -Print Hello World with their Along Name
# 
# Input: - Aakash Chauhan or Aakash 
# Output: 
#      Hi!! Aakash Chauhan 
#      Hello World is your First Program
#
# Rules:
#   -Takes the User name in the String in the Variable

# Edge cases: 
#   If there is just he blank Spaces

# STEP 2 — EXAMPLES
# Example 1: Aakash → Hi!! Aakash
#                     Hello World is your First Program
#                       
# Example 2: Aakash Chauhan The Great → Hi!! Aakash
#                     Hello World is your First Program
# Example 3: "  " → Hi!! Unknown Friend
#                   Hello World is your First Program

# STEP 3 — PIECES
# Piece 1: Takes input from the User as String
# Piece 2: Need to use the stripe function to remove spaces
# Piece 3: Required If condition to Indentify wheather it is blank space Enter by the user
# Piece 4: print the String 
#          Hi!! {User Name}
#          Hello World is your First program  

# ============================================================
# SOLUTION
# ============================================================

user_name = input("Enter Your Name:- ")

name = user_name.strip()

if len(name) == 0:
    print("Hi!! Unknown User\nHello World is your first Program")
else:
    print(f"Hi!! {name}\nHello World is your first Program")