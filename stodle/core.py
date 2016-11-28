"""
stodle

small package to keep windows running
"""

from win32api import GetTickCount, GetLastInputInfo
from ctypes import windll


def stop_idle(seconds=1, debug=False, debug_statement='user inactive'):
    """
    Detects idle and creates a mouse event to keep windows running

    :param seconds: numeric -  time in seconds before making an event
    :param debug: bool - if true prints the print statement
    :param print_statement: statement to print when user is idle
    """

    last_input = (GetTickCount() - GetLastInputInfo()) / 1000
    if last_input >= seconds:
        if debug:
            print(debug_statement)
        windll.user32.mouse_event(1, 1, 1, 0, 0)

if __name__ == '__main__':
    while True:
        stop_idle(debug=True)