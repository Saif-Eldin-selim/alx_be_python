task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder variable
reminder = ""

# Match the priority level and format the reminder accordingly
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " it should be done soon."
        else:
            reminder += " You can schedule it for later."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " but consider completing it when you have free time."
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Print the reminder
print(reminder)
