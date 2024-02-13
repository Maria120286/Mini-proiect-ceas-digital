from datetime import datetime
import time
import pytz

num_map = {
    '0': [' __ ', '|  |', '|__|'],
    '1': ['   ', '   |', '   |'],
    '2': [' __', ' __|', '|__ '],
    '3': ['__ ', ' __|', ' __|'],
    '4': ['   ', '|__|', '   |'],
    '5': ['__ ', '|__ ', ' __|'],
    '6': ['__ ', '|__ ', '|__|'],
    '7': ['__ ', '   |', '   |'],
    '8': ['__  ', '|__|', '|__|'],
    '9': ['__ ',  '|__|', ' __|']
}
separator = ['   ', '   ', '   ']


def display_time():
    while True:
        now = datetime.now(pytz.timezone('Europe/Bucharest'))
        h, m, s = now.hour, now.minute, now.second
        time_str = f"{h:02d}o{m:02d}o{s:02d}"

        for i in range(3):
            line = ""
            for digit in time_str:
                if digit == 'o':
                    line += separator[i]
                else:
                    line += num_map[digit][i]
            print(line)

        time.sleep(1)
        print("\033c", end="")
display_time()
