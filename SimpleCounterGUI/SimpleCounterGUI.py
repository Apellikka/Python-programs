
import tkinter as tk
from tkinter import *


class Counter:
    def __init__(self):

        self.__main_window = Tk()

        # Int variable to show in label.
        self.__integer = tk.IntVar()
        self.__integer.set(0)

        self.__current_value_label = Label(self.__main_window,
                                           textvariable=str(self.__integer))
        self.__current_value_label.pack(side = TOP)

        self.__quit_button = Button(self.__main_window, text="Quit",
                                    command=self.quit)
        self.__quit_button.pack(side = RIGHT)

        self.__reset_button = Button(self.__main_window, text="Reset",
                                     command=self.reset)
        self.__reset_button.pack(side = RIGHT)

        self.__increase_button = Button(self.__main_window, text="Increment",
                                        command=self.increment)
        self.__increase_button.pack(side = RIGHT)

        self.__decrease_button = Button(self.__main_window, text="Decrease",
                                        command=self.decrease)
        self.__decrease_button.pack(side = RIGHT)

        self.__main_window = mainloop()

    # TODO: Implement the rest of the needed methods here.

    def quit(self):
        """Shuts down the main window.
        """

        self.__main_window.destroy()

    def reset(self):
        """Resets the value label to 0
        """

        self.__integer.set(0)

    def increment(self):
        """Increments the value label by 1
        """

        self.__integer.set(self.__integer.get() + 1)

    def decrease(self):
        """Decreases the value label by 1
        """

        self.__integer.set(self.__integer.get() - 1)


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
