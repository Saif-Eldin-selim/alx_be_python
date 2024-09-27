# Get task description from user
task = input("Enter your task: ")

# Get task priority from user
priority = input("Priority (high/medium/low): ").lower()

# Check if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder_message = ""

# Process task based on priority
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder_message += " that should be addressed soon."
    case "low":
        reminder_message = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder_message += " but it can wait until later."
        else:
            reminder_message += ". Consider completing it when you have free time."

# Print the reminder message
print(reminder_message)
