 import os

# Function to display the main menu
def display_menu():
    print("\nBus Reservation System")
    print("1. View available seats")
    print("2. Book a seat")
    print("3. Cancel booking")
    print("4. View passenger list")
    print("5. Exit")

# Function to load bus data from file
def load_bus_data():
    if os.path.exists("bus_data.txt"):
        with open("bus_data.txt", "r") as file:
            return [line.strip().split(",") for line in file.readlines()]
    else:
        return []

# Function to save bus data to file
def save_bus_data(bus_data):
    with open("bus_data.txt", "w") as file:
        for bus_seat in bus_data:
            file.write(",".join(bus_seat) + "\n")

# Function to view available seats
def view_available_seats(bus_data):
    print("\nAvailable Seats:")
    for bus_seat in bus_data:
        if not bus_seat[2]:
            print(f"Bus Number: {bus_seat[0]}, Seat Number: {bus_seat[1]}")

# Function to book a seat
def book_seat(bus_data):
    bus_number = input("Enter bus number: ")
    seat_number = input("Enter seat number: ")
    passenger_name = input("Enter passenger name: ")

    for bus_seat in bus_data:
        if bus_seat[0] == bus_number and bus_seat[1] == seat_number:
            if not bus_seat[2]:
                bus_seat[2] = passenger_name
                print("Seat booked successfully!")
                return
            else:
                print("Seat already booked!")
                return

    print("Invalid bus number or seat number!")

# Function to cancel booking
def cancel_booking(bus_data):
    seat_number = input("Enter seat number to cancel booking: ")

    for bus_seat in bus_data:
        if bus_seat[1] == seat_number:
            if bus_seat[2]:
                bus_seat[2] = ""
                print("Booking canceled successfully!")
                return

    print("Invalid seat number or seat not booked!")

# Function to view passenger list
def view_passenger_list(bus_data):
    print("\nPassenger List:")
    for bus_seat in bus_data:
        if bus_seat[2]:
            print(f"Bus Number: {bus_seat[0]}, Seat Number: {bus_seat[1]}, Passenger Name: {bus_seat[2]}")

def main():
    bus_data = load_bus_data()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_seats(bus_data)
        elif choice == "2":
            book_seat(bus_data)
        elif choice == "3":
            cancel_booking(bus_data)
        elif choice == "4":
            view_passenger_list(bus_data)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

    save_bus_data(bus_data)

if _name_ == "_main_":
    main()
#The bus reservation system project is successfully completed
