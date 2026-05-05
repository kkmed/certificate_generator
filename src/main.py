from reader import read_csv_file
from validator import validate_data
from formatter import format_data

def manual_input():
    data = []
    n = int(input("Enter number of records: "))

    for i in range(n):
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")

        data.append({
            "name": name,
            "age": age,
            "email": email
        })

    return data


def main():
    choice = input("1. Read CSV\n2. Manual Input\nEnter choice: ")

    if choice == "1":
        path = input("Enter CSV file path: ")
        data = read_csv_file(path)
    else:
        data = manual_input()

    validated = validate_data(data)
    formatted = format_data(validated)

    print("\nFinal Processed Data:")
    for item in formatted:
        print(item)


if __name__ == "__main__":
    main()
