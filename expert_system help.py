# ============================================================
# QUESTION:
# Implement Expert System for Help Desk Management.
# ============================================================


# ============================================================
# EXPLANATION:
#
# Expert System simulates decision-making of a human expert.
#
# This program:
#
# - Stores problems
# - Matches user input
# - Provides solution
#
# It uses:
# - Dictionary
# - Condition checking
# - Loop
# ============================================================


# ============================================================
# EXPLANATION WITH EXAMPLE:
#
# User Input:
# Printer not working
#
# Output:
# Check printer connection.
#
# User Input:
# exit
#
# Output:
# Goodbye
# ============================================================


# ======================
# EXPERT SYSTEM PROGRAM
# ======================
# Expert System - Help Desk Management

problem_dict = {

    "Printer not working":
    "Check printer power, cable connection, and restart the printer.",

    "Can't log in":
    "Check username and password. Reset password if needed.",

    "Software not installing":
    "Check system requirements and available storage space.",

    "Internet connection not working":
    "Restart modem/router and check network cables.",

    "Email not sending":
    "Check email settings and internet connection.",

    "Computer running slow":
    "Close unnecessary programs and scan for viruses.",

    "Keyboard not working":
    "Reconnect keyboard or check keyboard drivers.",

    "Mouse not working":
    "Reconnect mouse and check battery if wireless.",

    "Blue screen error":
    "Restart computer and check for hardware/software issues.",

    "System overheating":
    "Clean cooling fan and ensure proper ventilation."

}


def handle_request(user_input):

    if user_input.lower() == "exit":

        return "Thank you for using Help Desk Expert System."

    elif user_input in problem_dict:

        return problem_dict[user_input]

    else:

        return "Problem not found in database. Please contact technical support."


print("===================================")
print("   HELP DESK EXPERT SYSTEM")
print("===================================")

while True:

    print("\nAvailable Problems:")

    for problem in problem_dict:
        print("-", problem)

    user_input = input(
        "\nEnter problem (type exit to quit): ")

    response = handle_request(user_input)

    print("\nSolution:", response)

    if user_input.lower() == "exit":

        break