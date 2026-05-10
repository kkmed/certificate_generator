while True:

    print("\n===== CERTIFICATE GENERATOR =====")

    print("1. Generate Certificates")
    print("2. Send Emails")
    print("3. Generate + Send")
    print("4. Exit")

    choice = input("\nEnter your choice: ")


    # OPTION 1
    if choice == "1":

        print("\nGenerating certificates...\n")

        exec(open("batch_generator.py").read())


    # OPTION 2
    elif choice == "2":

        print("\nEmail system runs automatically during generation.\n")


    # OPTION 3
    elif choice == "3":

        print("\nGenerating certificates and sending emails...\n")

        exec(open("batch_generator.py").read())


    # OPTION 4
    elif choice == "4":

        print("\nExiting program...\n")

        break


    # INVALID OPTION
    else:

        print("\nInvalid choice. Please try again.\n")