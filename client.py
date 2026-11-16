def show_main_menu():
    print("\n========== ESCAPE ZONE ==========")
    print("1. Manage Rooms")
    print("2. Manage Bookings")
    print("3. Reports")
    print("0. Exit")
    print("=================================")


def show_rooms_menu():
    print("\n========== ROOM MANAGEMENT ==========")
    print("1. Show all rooms")
    print("2. Show room details")
    print("3. Add new room")
    print("4. Update room")
    print("5. Activate / Deactivate room")
    print("0. Back to main menu")
    print("=====================================")


def show_bookings_menu():
    print("\n========== BOOKING MANAGEMENT ==========")
    print("1. Show all bookings")
    print("2. Search booking by ID")
    print("3. Show customer bookings")
    print("4. Show bookings by date")
    print("5. Create new booking")
    print("6. Update booking")
    print("7. Cancel booking")
    print("0. Back to main menu")
    print("========================================")


def show_reports_menu():
    print("\n========== REPORTS ==========")
    print("1. Active bookings count")
    print("2. Cancelled bookings count")
    print("3. Total revenue")
    print("4. Total cancellation fees")
    print("5. Most popular room")
    print("6. Bookings per room")
    print("7. Show room occupancy")
    print("0. Back to main menu")
    print("=============================")


def manage_rooms():
    choice = ""

    while choice != "0":
        show_rooms_menu()
        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4", "5"]:
            print("This option will be implemented later.")

        elif choice != "0":
            print("Invalid option. Please try again.")


def manage_bookings():
    choice = ""

    while choice != "0":
        show_bookings_menu()
        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            print("This option will be implemented later.")

        elif choice != "0":
            print("Invalid option. Please try again.")


def manage_reports():
    choice = ""

    while choice != "0":
        show_reports_menu()
        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            print("This option will be implemented later.")

        elif choice != "0":
            print("Invalid option. Please try again.")


def run_menu():
    choice = ""

    while choice != "0":
        show_main_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            manage_rooms()

        elif choice == "2":
            manage_bookings()

        elif choice == "3":
            manage_reports()

        elif choice != "0":
            print("Invalid option. Please try again.")

    print("Goodbye!")