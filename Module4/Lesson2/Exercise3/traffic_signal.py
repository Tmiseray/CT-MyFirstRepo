class TrafficSignal:
    def __init__(self):
        self.current_signal = 'red'

    def change_signal(self):
        if self.current_signal == 'red':
            self.current_signal = 'green'
        elif self.current_signal == 'green':
            self.current_signal = 'yellow'
        else:
            self.current_signal = 'red'

    def display_signal(self):
        print(f"Current Signal: {self.current_signal}")