global data
data = []

# Flatten method:
def flatten(data):
    """Converts a 2-D list into a 1-D list."""

    flat_data = []

    for i in data:
        if isinstance(i,list):
            flat_data.extend(i)
        else:
            flat_data.append(i)

    return flat_data

# 2. Display Data Summary:
def summary():
    """Display the total elements, minimum, sum and average of the dataset."""

    flat_data = flatten(data)

    print("\nData Summary:")
    print("- Total elements:",len(flat_data))
    print("- Minimum value:",min(flat_data))
    print("- Maximum value:",max(flat_data))
    print("- Sum of all values:",sum(flat_data))
    print(f"- Average value: {sum(flat_data)/len(flat_data):.2f}")


# 3. Calculate Factorial:
def factorial(num):
    """Calculation the factorial of a number using recursion."""

    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# 5. Sort Data:

def sorting(data):
    """Sorts the dataset in ascending or descending order."""
    
    flat_data = flatten(data)
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice_2 = int(input("\nEnter your choice: "))

    match choice_2:
        case 1:
            sorted_data = sorted(flat_data)
            print("\nSorted data in Ascending Order:\n",end="")
            for value in sorted_data:
                print(value,end=" ")

        case 2:
            sorted_data = sorted(flat_data,reverse=True)
            print("\nSorted data in Descending Order:\n",end="")
            for value in sorted_data:
                print(value,end=" ")

        case _:
            print("\nInvalid choice, Please enter valid choice.")

# 6. Display Dataset Statistics:
def Statistics():
    """Returns the minimum, maximum, sum, and average of the dataset."""
    
    flat_data = flatten(data)
    minimum = min(flat_data)
    maximum = max(flat_data)
    addition = sum(flat_data)
    average = sum(flat_data)/len(flat_data)

    return minimum,maximum,addition,average

print("Welcome to the Data Analyzer and Transformer Program")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("\nPlease enter your choice: "))

    match choice:
        case 1:
            print("1. 1-D Array Manually")
            print("2. 2-D Array Manually")
            print("3. Sample of 1-D  Array")
            print("4. Sample of 2-D  Array")

            choice_1 = int(input("\nPlease enter your choice: "))

            match choice_1:
                case 1:
                    array_1 = input("Enter data for a 1-D array (Separated by spaces):\n").split(" ")
                    for i in array_1:
                        data.append(int(i))
                    print("\nData has been stored successfully!")

                case 2:
                    data = []
                    rows = int(input("Enter the number of rows: "))
                    cols = int(input("Enter the number of columns: "))

                    for i in range(0,rows):
                        temp =[]
                        row = input(f"Enter {cols} elements separated by spaces for {i+1}: \n").split(" ")
                        for j in row:
                            temp.append(int(j))
                        data.append(temp)

                    for row in data:
                        print(row)
                    print("\nData has been stored successfully!")

                case 3:
                    data = []
                    sample_1D = [45, 12, 89, 3, 67, 24, 91]
                    print(sample_1D)
                    data.extend(sample_1D)
                    print("\nData has been stored successfully!")

                case 4:
                    data = []
                    sample_2D = [
                        [45, 12, 89],
                        [3, 67, 24],
                        [91, 56, 78]
                    ]
                    for row in sample_2D:
                        print(row)
                    data.extend(sample_2D)
                    print("\nData has been stored successfully!")

                case _:
                    print("Inavalid choice, enter valid choice.")


        case 2:
            if len(data) == 0:
                print("\nData is not available.")
            else:
                summary()

        case 3:
            num = int(input("\nEnter a number yo calculate its factorial: "))

            result = factorial(num)

            print(f"\nFactorial of {num} is: {result}")

        case 4:
            if len(data) == 0:
                print("\nData is not available.")
            else:
                threshold = int(input("\nEnter a threshold value to filter out data above this value: \n"))

                flat_data = flatten(data)

                filter_data = list(filter(lambda x : x >= threshold,flat_data))
                print("\nFiltered Data (values >= 50):\n",end="")

                for value in filter_data:
                    print(value,end=" ")
                print()

        case 5:
            if len(data) == 0:
                print("Data is not availabel.")
            else:
                sorting(data)
                print()

        case 6:
            if len(data) == 0:
                print("Data is not availabel.")
            else:
                 minimum,maximum,addition,average = Statistics() 

                 print("\nDataset Statistics:")
                 print("- Minimum value:",minimum)
                 print("- Maximum value:",maximum)
                 print("- Sum of all values:",addition)
                 print(f"- Average value: {average:.2f}")                 

        case 7:
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!\n")
            break

        case _:
            print("\nInvalid choice. Please enter valid choice!\n")