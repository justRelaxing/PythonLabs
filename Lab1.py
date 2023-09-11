import random

def first_task():
    while True:

        chinese_animals = (
            "Monkey", "Rooster", "Dog", "Pig", "Rat", "Bull", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat")

        year = input("\n\tInput Year To Convert It to Chinese Calendar Year (Input 0 to Exit): ")

        if year == '0':
            break

        try:

            year = int(year)

            if year < 0:
                print("\tChinese Year Was Supposed to Be a Positive Number!")

            else:
                print("\n\tYour Year in Chinese Calendar is", chinese_animals[year % 12])

        except ValueError:
            print("\n\tIncorrect Input! Try to Input Another Year!")


def second_task():
    def count_even_words(string):

        words = string.split()
        count = 0

        for word in words:

            word_length = 0

            for i in word:
                if not i.isalnum():
                    word_length += 1

            if word_length % 2 == 0:
                count += 1

        return count

    def calculate_frequency(string):

        frequency = {}

        for letter in string:

            if letter.isalpha():

                letter = letter.lower()

                if letter in frequency:
                    frequency[letter] += 1

                else:
                    frequency[letter] = 1

        return frequency

    user_string = input("\n\tInput Your String to Calculate Task: ")

    print("\n\tNumber of Words with Even Length:", count_even_words(user_string))

    print("\n\tFrequencies of Occurrences of Each Letter:")

    for letter, count in calculate_frequency(user_string).items():
        print("\t", letter, ": ", count)


def third_task():
    def random_list(count, min_value, max_value):
        return [random.randint(min_value, max_value) for i in range(count)]

    numbers = random_list(10, -5, 5)

    count = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1

    print("\n\tYour List of Numbers:", numbers)

    print("\n\tNumber Pairs of Equival Elements:", count)


def fourth_task():
    def find_keys(dictionary):
        sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)

        return sorted_keys[:3]

    user_dict = {'a': 111, 'b': 122, 'c': 566, 'd': 405, 'e': 21, 'f': 266}

    three_keys = find_keys(user_dict)

    print("\n\tThree Highest Keys:", three_keys)


def fifth_task():
    def display_description(products):
        for product, details in products.items():
            print(f"\t{product} - {details[0]}")

    def display_price(products):
        for product, details in products.items():
            print(f"\t{product} - {details[1]}")

    def display_quantity(products):
        for product, details in products.items():
            print(f"\t{product} - {details[2]}")

    def display_all_info(products):
        for product, details in products.items():
            print(f"\t{product} - {details[0]}, Price: {details[1]}, Quantity: {details[2]}")

    def make_purchase(products):

        total_price = 0

        while True:

            product = input("\n\tInput Product Name (Input 'N' to Exit): ")

            if product == 'n':
                break

            if product in products:

                quantity = int(input("\n\tEnter Quantity: "))

                if quantity <= products[product][2]:

                    products[product][2] -= quantity

                    total_price += products[product][1] * quantity

                else:
                    print("\n\tToo Much Quantity!")

            else:
                print("\n\tProduct Not Found!")

        print("\n\tTotal Price:", total_price)

        print("\n\tRemaining quantities:")

        display_quantity(products)

    products = {
        "Apple": ["Juicy and Sweet Fruit", 50, 10],
        "Banana": ["Creamy and Sweet Fruit", 30, 15],
        "Orange": ["Juicy Citrus Fruit", 10, 20],
        "Strawberry": ["Small and Juicy Red Berry", 20, 5],
        "Blueberry": ["Small and Juicy Blue Berry", 15, 25]
    }

    while True:
        print("\n\t1. Display Description"
              "\n\t2. Display Price"
              "\n\t3. Display Quantity"
              "\n\t4. Display All Information"
              "\n\t5. Make a Purchase")

        choice = input("\n\tInput Your Choice (Input 'N' to Exit): ")

        if choice == '1':
            display_description(products)

        elif choice == '2':
            display_price(products)

        elif choice == '3':
            display_quantity(products)

        elif choice == '4':
            display_all_info(products)

        elif choice == '5':
            make_purchase(products)

        else:
            print("\n\tGoodbye!")
            break


def sixth_task():
    def find_smallest_even(tuple):

        smallest_even = None

        for element in tuple:
            if element % 2 == 0:
                if smallest_even is None or element < smallest_even:
                    smallest_even = element

        if smallest_even is not None:
            return smallest_even

        else:
            return tuple[0]

    def random_tuple(count, min_value, max_value):
        return tuple(random.randint(min_value, max_value) for i in range(count))

    numbers = random_tuple(10, -50, 50)

    print("\n\tYour Tuple of Numbers:", numbers)

    print("\n\tSmallest Even Number in Tuple:", find_smallest_even(numbers))


def menu():
    print("\n\tHello, Dear User!")

    while True:

        print("\n\tMenu:"
              "\n\t1. First Task"
              "\n\t2. Second Task"
              "\n\t3. Third Task"
              "\n\t4. Fourth Task"
              "\n\t5. Fifth Task"
              "\n\t6. Sixth Task"
              "\n\tAnother. Exit")

        choice = input("\n\tInput Number of Task from Menu to Test: ")

        if choice == "1":
            first_task()

        elif choice == "2":
            second_task()

        elif choice == "3":
            third_task()

        elif choice == "4":
            fourth_task()

        elif choice == "5":
            fifth_task()

        elif choice == "6":
            sixth_task()

        else:
            print("\n\tGoodbye, Dear User!")
            break


if __name__ == "__main__":
    menu()
