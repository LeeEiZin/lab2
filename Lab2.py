def display_main_menu():
    print("display_main_menu")

def get_user_input():
    print("get_user_input")

def calc_average():
    print("calc_average")

def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

# Calling the functions to verify
display_main_menu()
get_user_input()
calc_average()
find_min_max()
sort_temperature()
calc_median_temperature()

def display_main_menu():
    # Display the menu text
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    # Read user input from console
    user_input = input("Enter your numbers: ")

    # Split the user input based on the comma character to create a list of strings
    str_list = user_input.split(",")

    # Convert list of strings to a list of floats

    float_list = [float(num.strip()) for num in str_list]

    # Return the list of floats
    return float_list

# Testing the functions
display_main_menu()
user_numbers = get_user_input()
print("List of numbers entered:", user_numbers)

def calc_average_temperature(temperature_list):
    # Calculate and return the average of all temperature readings
    if len(temperature_list) == 0:
        return 0.0  # Handle the empty list case
    return sum(temperature_list) / len(temperature_list)

def calc_min_max_temperature(temperature_list):
    # Return a list with the minimum and maximum temperature values
    if len(temperature_list) == 0:
        return [None, None]  # Handle the empty list case
    return [min(temperature_list), max(temperature_list)]

# Testing the functions
temperatures = [23.5, 25.3, 19.8, 30.0, 22.7]
average_temp = calc_average_temperature(temperatures)
min_max_temp = calc_min_max_temperature(temperatures)

print("Average Temperature:", average_temp)
print("Min and Max Temperatures:", min_max_temp)

