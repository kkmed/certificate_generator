def manual_input():
    data = []
    n = int(input("Enter number of records: "))

    for i in range(n):
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")

        record = {
            "name": name,
            "age": age,
            "email": email
        }
        data.append(record)

    return data
