from tkinter import Tk
from controller import TriviaController


def main() -> None:
    """Creates a tkinter window and starts main event loop"""
    window = Tk()
    window.title('Trivia')
    window.geometry('350x300')
    window.resizable(False, False)

    trivia_controller = TriviaController(window)

    window.mainloop()


if __name__ == '__main__':
    main()
