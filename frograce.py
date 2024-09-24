## #############################################################################
## DRIVER:
## NAVIGATOR:
## #############################################################################

# The final position will never change, so use a constant
FINAL_POSITION = 10

# Each from has a different jump length. These can be constants too.
STEADY_STU_JUMP = 1
LEGS_JOHNSON_JUMP = 2
CRAZY_BILL_JUMP = 3

# Get the starting position for the race from the user.
start_position = int(input("Enter a starting position: "))

## BEGIN STEADY STU
# Make a variable to keep track of the current frog's position.
current_position = start_position

# We will start with Steady Stu.
# The "end" parameter tells print to not print a newline - just use a space.
print("Steady Stu:", end=" ")

# Loop until the frog reaches or passes the final position.
while current_position <= FINAL_POSITION:

    # Print the current position of the frog
    print(current_position, end=" ")

    # Update the position for the frog (make it jump)
    current_position = current_position + STEADY_STU_JUMP

# This prints a newline (line break) so that the next print output will be on a new line.
print()
## END STEADY STU

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Do not edit above this line
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# 1: Do the same as above for Legs Johnson. You can copy and paste the lines between the BEGIN and END comments and modify them.

# 2: Do the same as above for Crazy Bill. You can copy and paste the lines between the BEGIN and END comments and modify them.
