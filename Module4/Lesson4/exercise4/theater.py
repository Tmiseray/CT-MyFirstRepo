class Theater:
    def __init__(self, rows, seats_per_row):
        self.seating = [[{'row': row, 'number': seat, 'reserved': False} for seat in range(1, seats_per_row +1)] for row in range(1, rows + 1)]

    def display_seating_chart(self):
        for row in self.seating:
            print(" ".join(['X' if seat['reserved'] else 'O' for seat in row]))

    def reserve_seat(self, row_number, seat_number):
        if self.seating[row_number - 1][seat_number - 1]['reserved']:
            return False
        else:
            self.seating[row_number - 1][seat_number - 1]['reserved'] = True
            return True