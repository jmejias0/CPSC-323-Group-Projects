while True:  # Start an infinite loop
    number = int(input("Enter a number from 1 to 10: "))  # Receiving input from the user and storing it in the variable 'number'

    if number == 0:  # Check if the user entered 0
        break  # Exit the loop if the user entered 0

    if 1 <= int(number) <= 10:  # Check if the number is between 1 and 10
        print("Hello")

    else:
        print("Not inside the limits")  # Print a message if the number is not between 1 and 10