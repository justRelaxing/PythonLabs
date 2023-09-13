import random


def first_task():

    def count_elements():

        elements_sum = 0
        n = 1

        try:

            while elements_sum <= 4:

                elements_sum += 1 / n
                n += 1

        except ZeroDivisionError:
            print("\n\tError: Division by Zero Occurred.")

        finally:
            return n

    print("\n\tNumber of Elements Needed to Make the Sum Greater than 4 is:", count_elements())

def second_task():

    def process_data(data):

        try:

            if isinstance(data, list):

                data = list(data)
                sum_after_positive = 0
                found_positive = False
                occured_numbers = set()

                for num in data:
                    if num > 0 and not found_positive:
                        found_positive = True

                    elif found_positive and num not in occured_numbers:
                        sum_after_positive += num
                        occured_numbers.add(num)

                return sum_after_positive

            elif isinstance(data, dict):

                sorted_dict = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

                return sorted_dict

            elif isinstance(data, int):

                if data < 2:
                    return "\n\tNot Prime"

                for i in range(2, int(data ** 0.5) + 1):
                    if data % i == 0:
                        return "\n\tNot Prime"

                return "\n\tPrime"

            elif isinstance(data, str):

                unicode_list = [ord(char) for char in data]

                return unicode_list

            else:
                return "\n\tInvalid Input!"

        except Exception as e:
            return f"\n\tError: {str(e)}"

    # List
    data_list = [-5, -5, -1, -2, 4, 4, 1, 1, 1]

    # Dictionary
    data_dict = {'a': 111, 'b': 122, 'c': 566, 'd': 405, 'e': 21, 'f': 266}

    # Integer
    data_number = 17

    # String
    data_string = "Hello"

    # Float Number
    invalid_data = 123.45

    while True:

        print("\n\tMenu:"
              "\n\t1. List"
              "\n\t2. Dictionary"
              "\n\t3. Integer"
              "\n\t4. String"
              "\n\t5. Another"
              "\n\tAnother. Exit")

        choice = input("\n\tSelect Type You Want to Pass to the Function: ")

        if choice == "1":
            print("\n\tResult of Task with List:", data_list)
            print("\n\t", process_data(data_list))

        elif choice == "2":
            print("\n\tResult of Task with Dictionary:", data_dict)
            print("\n\t", process_data(data_dict))

        elif choice == "3":
            print("\n\tResult of Task with Integer:", data_number)
            print(process_data(data_number))

        elif choice == "4":
            print("\n\tResult of Task with String:", data_string)
            print("\n\t", process_data(data_string))

        elif choice == "5":
            print("\n\tResult of Task with Invalid Data:", invalid_data)
            print(process_data(invalid_data))

        else:
            return

def third_task():

    def generate_random_matrix(rows, cols):

        matrix = []

        for i in range(rows):

            row = []

            for i in range(cols):
                row.append(random.randint(-100, 10))

            matrix.append(row)

        return matrix

    def find_negative_row(matrix):

        try:
            for row in matrix:
                if all(element < 0 for element in row):
                    return row

            raise ValueError("\n\tNo Row with All Negative Elements Found.")

        except ValueError as e:
            print(f"\n\tError: {str(e)}")

    try:

        rows = int(input("\n\tInput Number of Rows: "))

        cols = int(input("\n\tInput Number of Columns: "))

        matrix = generate_random_matrix(rows, cols)

        negative_row = find_negative_row(matrix)

        print("\n\tMatrix:")
        for row in matrix:
            print("\t", row)

        if negative_row:

            sum_of_elements = sum(negative_row)

            print("\n\tFirst Row with All Negative Elements:", negative_row)

            print("\n\tSum of Elements in This Row:", sum_of_elements)

        else:
            print("\n\tNo Row with All Negative Elements Found.")

    except ValueError:
        print("\n\tIncorrect Input! Try Again!")

def menu():

    print("\n\tHello, Dear User!")

    while True:

        print("\n\tMenu:"
              "\n\t1. First Task"
              "\n\t2. Second Task"
              "\n\t3. Third Task"
              "\n\t4. Fourth Task"
              "\n\tAnother. Exit")

        choice = input("\n\tInput Number of Task from Menu to Test: ")

        if choice == "1":
            first_task()

        elif choice == "2":
            second_task()

        elif choice == "3":
            third_task()

        else:
            print("\n\tGoodbye, Dear User!")
            break


if __name__ == "__main__":
    menu()
