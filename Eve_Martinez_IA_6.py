# PROBLEM 1
# ---------------------------------------------------------------

# Create a list of weekdays
Week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Create list of corresponding sales
Sale_list = [50, 75, 150, 125, 100]

# Find maximum sales value
max_sale = max(Sale_list)

# Find the index of the maximum sale in Sale_list
index_max = Sale_list.index(max_sale)

# Use that index to find the matching weekday
max_day = Week_list[index_max]

# Display results using f-strings
print("------ Problem 1 ------")
print(f"The Max sales is ${max_sale}")
print(f"The Max sales day is {max_day}")

# ---------------------------------------------------------------
# PROBLEM 2

# Create an empty list to store the numbers
numbers = []

# Prompt user for input
value = float(input("\nEnter value (or 0 to end): "))

# Use a while loop to collect values until user enters 0
while value != 0:
    numbers.append(value)
    value = float(input("Enter value (or 0 to end): "))

# Display the list entered by the user
print(numbers)

# If list is not empty, calculate and display the range
if len(numbers) > 0:
    num_range = max(numbers) - min(numbers)
    print(f"Range = {num_range}")
else:
    print("No numbers were entered.")
