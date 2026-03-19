"""
Project Title: Data Analyzer and Transformer
Author: Student Project
Description:
A menu-driven Python program to analyze and transform
1D and 2D list data using built-in functions, UDFs,
args, kwargs, recursion, lambda, global variables,
sorting, and multiple return values.
"""

# =========================
# GLOBAL VARIABLE
# =========================
dataset_summary = {}

# =========================
# BUILT-IN FUNCTIONS
# =========================
def basic_statistics(data):
    """Returns length, sum, min, max, and average using built-in functions"""
    length = len(data)
    total = sum(data)
    minimum = min(data)
    maximum = max(data)
    average = total / length if length != 0 else 0
    return length, total, minimum, maximum, average


# =========================
# USER DEFINED FUNCTIONS
# =========================
def find_duplicates(data):
    """Finds duplicate values in the dataset"""
    duplicates = set([x for x in data if data.count(x) > 1])
    return list(duplicates)


def unique_values(data):
    """Returns unique values from the dataset"""
    return list(set(data))


# =========================
# *ARGS FUNCTION
# =========================
def display_values(*args):
    """Displays multiple values using *args"""
    print("Values received:")
    for value in args:
        print(value)


# =========================
# **KWARGS FUNCTION
# =========================
def dataset_info(**kwargs):
    """Displays dataset summary using **kwargs"""
    print("\nDataset Summary:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")


# =========================
# RECURSION
# =========================
def factorial(n):
    """Calculates factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# =========================
# LAMBDA + FILTER
# =========================
def filter_data(data, threshold):
    """Filters values greater than threshold using lambda"""
    return list(filter(lambda x: x > threshold, data))


# =========================
# SORTING FUNCTIONS
# =========================
def sort_1d_list(data, order="asc"):
    """Sorts 1D list using sort()"""
    if order == "asc":
        data.sort()
    else:
        data.sort(reverse=True)
    return data


def sort_2d_list(data):
    """Sorts 2D list using sorted()"""
    return sorted(data)


# =========================
# DISPLAY 2D LIST
# =========================
def display_2d_list(data):
    """Displays 2D list in grid format"""
    print("\n2D List:")
    for row in data:
        for value in row:
            print(value, end="\t")
        print()


# =========================
# MAIN MENU
# =========================
def main_menu():
    """Displays main menu"""
    print("""
==============================
DATA ANALYZER & TRANSFORMER
==============================
1. Use Sample 1D Data
2. Enter Custom 1D Data
3. Built-in Statistics
4. Find Duplicates
5. Show Unique Values
6. Sort Data
7. Filter Data (Lambda)
8. Factorial (Recursion)
9. Display Dataset Summary
10. Work with 2D List
0. Exit
""")


# =========================
# MAIN PROGRAM
# =========================
def main():
    global dataset_summary

    data = []
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            data = [10, 20, 30, 20, 40, 10]
            print("Sample Data Loaded:", data)

        elif choice == "2":
            data = list(map(int, input("Enter numbers separated by space: ").split()))
            print("Custom Data Loaded:", data)

        elif choice == "3":
            if not data:
                print("No data available!")
                continue

            length, total, minimum, maximum, average = basic_statistics(data)
            dataset_summary = {
                "Length": length,
                "Sum": total,
                "Minimum": minimum,
                "Maximum": maximum,
                "Average": average
            }

            print("Statistics:")
            print(dataset_summary)

        elif choice == "4":
            print("Duplicates:", find_duplicates(data))

        elif choice == "5":
            print("Unique Values:", unique_values(data))

        elif choice == "6":
            order = input("Enter order (asc/desc): ")
            print("Sorted Data:", sort_1d_list(data, order))

        elif choice == "7":
            threshold = int(input("Enter threshold value: "))
            print("Filtered Data:", filter_data(data, threshold))

        elif choice == "8":
            num = int(input("Enter number for factorial: "))
            print("Factorial:", factorial(num))

        elif choice == "9":
            dataset_info(**dataset_summary)

        elif choice == "10":
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            matrix = []
            print("Enter values row-wise:")
            for _ in range(rows):
                matrix.append(list(map(int, input().split())))
            display_2d_list(matrix)
            print("Sorted 2D List:", sort_2d_list(matrix))

        elif choice == "0":
            print("Thank you! Program Exited.")
            break

        else:
            print("Invalid choice! Try again.")


# =========================
# PROGRAM START
# =========================
main()
