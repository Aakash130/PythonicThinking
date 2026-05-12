# ============================================================
# Question 2 — Print your name, age, and favorite hobby on separate lines
# Date: [12-05-2026]
# ============================================================

# STEP 1 — UNDERSTAND
# What does it do: 
#   -Takes Informantion like Name, age and favourate hobby.
#   -Printing the Information on Separate lines
# Input: Aakash, 32 yrs old, Coding and Travelling 
# Output: -Hi Aakash
#         -Your age is 32
#         -You like Coding and Travelling 
# Rules:
#     -Must handle blanck spaces
#     -Must contain new line to print every statement
#     
# Edge cases:
#       -Blank space in user input should be handled
#       -Empty input user should be handled
#       -Missing inputs need to tell the user
#       -String should be in proper case 

# STEP 2 — EXAMPLES
# Example 1: 
#       -user input[Aakash,32 yrs old, Dance] → 
#          Hi Aakash
#          You are 32 yrs old
#          You like Dance
                                   
# Example 2: 
#         -user input[Aakash Chuauhan,only 32, Nothing to do] → 
#          Hi Aakash Chauhan
#          you are only 32
#          You like nothing to do 

# STEP 3 — PIECES
# Piece 1: Take user input in 3 different Variable
# Piece 2: Use Strip and check the Empty input
# Piece 3: Use Match case for instead of If Else

# ============================================================
# SOLUTION
# ============================================================

name = input("Enter your name:- ").strip()
age = input("Enter Your Age:- ").strip()
hobby = input("Enter your hobby:- ").strip()



if all(name and age and hobby):
    print(f"Hi!! {name.title()}\nYou are {age}\nYou like {hobby}")
else:
    print("Some input missing from your End")
    



# user_info = [name,age,hobby]



# for i in user_info:
#     print(i)


