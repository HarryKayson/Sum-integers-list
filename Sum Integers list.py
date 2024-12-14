# Program to create a list of integers and compute their sum

def main():
    print("Enter integers separated by spaces:")
    try:
        # Take user input and split into a list of integers
        user_input = input()
        integer_list = list(map(int, user_input.split()))

        # Compute the sum of the integers
        total_sum = sum(integer_list)

        # Output the result
        print(f"The sum of the integers is: {total_sum}")
    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
