from tkinter import *

class Userinterface:

    def __init__(self):
        """Initialises the graphical user interface in a grid.
        """

        self.__mainwindow = Tk()

        self.__label_weight = Label(self.__mainwindow, text="Weight")
        self.__weight_value = Entry(self.__mainwindow)

        self.__label_height = Label(self.__mainwindow, text="Height")
        self.__height_value = Entry()

        self.__calculate_button = Button(self.__mainwindow, text="Calculate BMI",
                                         command=self.calculate_BMI,
                                         bg="green",
                                         fg="black")

        self.__result_text = Label(self.__mainwindow,
                                   textvariable="")

        self.__explanation_text = Label(self.__mainwindow, text="")

        self.__stop_button = Button(self.__mainwindow, text="Stop",
                                    command=self.stop)

        self.__label_weight.grid(row=0, column=0)
        self.__label_height.grid(row=1, column=0)
        self.__weight_value.grid(row=0, column=1)
        self.__height_value.grid(row=1, column=1)
        self.__calculate_button.grid(row=2, column=1)
        self.__stop_button.grid(row=4, column=0)
        self.__result_text.grid(row=3, column=1)
        self.__explanation_text.grid(row=4, column=1)

    def calculate_BMI(self):
        """
        This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        try:
            if float(self.__weight_value.get()) < 0\
                    or float(self.__height_value.get()) < 0:

                self.__explanation_text.configure(
                    text="Error: height and weight must be positive.")

                self.reset_fields()
                return

        except ValueError:
            self.__explanation_text.configure(
                text="Error: height and weight must be numbers.")

            self.reset_fields()
            return

        weight = float(self.__weight_value.get())
        height = float(self.__height_value.get()) / 100
        result = weight / (height**2)
        self.__result_text.configure(text=f"{result:.2f}")

        if 18.5 <= result <= 25:
            self.__explanation_text.configure(text="Your weight is normal.")
        elif result < 18.5:
            self.__explanation_text.configure(text="You are underweight.")
        else:
            self.__explanation_text.configure(text="You are overweight.")

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__weight_value.delete(0, "end")
        self.__height_value.delete(0, "end")
        self.__result_text.configure(text="")

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
