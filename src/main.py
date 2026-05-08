from reader import read_manual_input, read_json_file
from validator import validate_data
from formatter import format_data
from certificate_generator import generate_certificate


style = {
    "certificate_title": {
        "font_family": "serif",
        "font_size": 65,
        "color": (80, 80, 80)
    },

    "recipient_name": {
        "font_family": "serif",
        "font_size": 95,
        "color": (150, 110, 40)
    }
}


layout = {
    "recipient_name": {"y": 350},
    "certificate_title": {"y": 180}
}


def main():

    print("1. Manual Input")
    print("2. Read JSON File")

    choice = input("Enter choice: ")

    if choice == "1":
        data = read_manual_input()

    elif choice == "2":
        path = input("Enter JSON file path: ")
        data = read_json_file(path)

    else:
        print("Invalid choice")
        return

    # validate
    if not validate_data(data):
        print("Validation failed")
        return

    # format
    formatted_data = format_data(data)

    # generate certificate
    generate_certificate(
        formatted_data,
        "classic",
        "output/certificate.png",
        style,
        layout
    )


if __name__ == "__main__":
    main()
