# Define functions for basic arithmetic operations

def add(x, y):
  """
  This function adds two numbers and returns the sum.
  """
  return x + y

def subtract(x, y):
  """
  This function subtracts the second number from the first and returns the difference.
  """
  return x - y

def multiply(x, y):
  """
  This function multiplies two numbers and returns the product.
  """
  return x * y

def divide(x, y):
  """
  This function divides the first number by the second.
  It checks for division by zero and returns an error message and None if it occurs.
  """
  if y == 0:
    print("Error: Division by zero is not allowed.")
    return None
  return x / y

def exponentiate(x, y):
  """
  This function raises the first number to the power of the second and returns the result.
  """
  return x ** y

# Function to get user input with error handling

def get_user_input():
  """
  This function prompts the user for two numbers and validates the input.
  It uses a loop to keep asking for input until valid numbers are entered.
  """
  while True:
    try:
      num1 = float(input("Enter the first number: "))
      print(num1)  # Print confirmation for user
      num2 = float(input("Enter the second number: "))
      print(num2)  # Print confirmation for user
      return num1, num2
    except ValueError:
      print("Invalid input. Please enter numbers only.")

# Function to display the menu options

def display_menu():
  """
  This function displays the menu with available options for the calculator.
  """
  print("\n*** Simple Calculator with Advanced Features ***")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exponentiate")
  print("6. Quit")

# Main function to run the calculator program

def main():
  """
  This function is the entry point of the program.
  It runs in a loop, displaying the menu, getting user input, performing calculations based on the choice,
  and handling errors.
  """
  while True:
    display_menu()
    choice = input("Enter your choice (1-6): \n")
    print(choice)  # Print user's choice for confirmation

    if choice in ('1', '2', '3', '4', '5'):
      num1, num2 = get_user_input()
      if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
      elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
      # ... similar logic for other choices

    elif choice == '6':
      print("Exiting calculator...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 6.")

# Execute the main function only when the script is run directly
if __name__ == "__main__":
  main()
