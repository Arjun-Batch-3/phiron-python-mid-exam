class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self.show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)

        # Allocate seats with rows and cols using nested loops
        show_seats = []
        for i in range(self._rows):
            row = []
            for x in range(self._cols):
                row.append('free')
            show_seats.append(row)

        self._seats[show_id] = show_seats

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            print(f"Error: Invalid show ID {show_id}")
            return

        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print(f"Error: Invalid seat ({row}, {col}) for show {show_id}")
                continue

            if self._seats[show_id][row][col] == 'free':
                self._seats[show_id][row][col] = 'booked'
                print(f"Seat ({row}, {col}) booked for show {show_id}")
            else:
                print(f"Error: Seat ({row}, {col}) is already booked for show {show_id}")

    def view_show_list(self):
        print("Shows Today:")
        for show in self.show_list:
            show_id, movie_name, show_datetime = show
            print(f"Movie: {movie_name} (ID: {show_id}) - Time: {show_datetime}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
           # print(f"Error: Invalid show ID {show_id}")
            return

        print(f"Available Seats for Show {show_id} (array index Format):")
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[show_id][row][col] == 'free':
                    print(f"({row}, {col})", end=' ')
                    print()
        print()  # Move to the next line

    def display_seats_2d_matrix(self, show_id):
        if show_id not in self._seats:
            print(f"Error: Wrong ID {show_id}")
            return

        print("Seating Arrangement (2D Matrix Format):")
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[show_id][row][col] == 'free':
                    print("O", end=' ')
                else:
                    print("X", end=' ')
            print()  # Move to the next line

class StarCinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

# Example Usage
hall1 = Hall(rows=10, cols=10, hall_no=1)
hall1.entry_show(show_id="111", movie_name="Animal", time="25/10/2023 11:00 AM")
hall1.entry_show(show_id="333", movie_name="Dubung", time="25/10/2023 2:00 PM")

StarCinema.entry_hall(hall1)

while True:
    print("\n1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. Exit")
    option = input("ENTER OPTION: ")

    if option == '1':
        hall1.view_show_list()

    elif option == '2':
        show_id = input("Enter Show ID: ")
        hall1.display_seats_2d_matrix(show_id)
        hall1.view_available_seats(show_id)

    elif option == '3':
        show_id = input("Enter Show ID: ")

        show_ids = [show[0] for show in hall1.show_list]
        if show_id in show_ids:
            num_tickets = int(input("Number of Tickets?: "))
            seat_list = []
            for _ in range(num_tickets):
                row = int(input("Enter Seat Row: "))
                col = int(input("Enter Seat Col: "))
                seat_list.append((row, col))

            hall1.book_seats(show_id, seat_list)
        else:
            print(f"Error: Invalid show ID {show_id}")

    elif option == '4':
        break

    else:
        print("Invalid option. Please choose again.")
