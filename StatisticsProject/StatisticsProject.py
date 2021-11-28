from math import sqrt


def main():
    values = read_user_input()
    print(f"The mean of given data was: {calculate_mean(values):.2f}")
    print(f"The standard deviation of given data was: "
          f"{calculate_std_dev(calculate_variance(values)):.2f}")
    print_histogram(values)


def read_user_input():

    """Reads input from a user and adds them to a list
    :return: the list in which the user inputs are saved
    """

    values = []
    print("Enter the data, one value per line.")
    print("End by entering empty line.")
    flag = True
    value_count = 0

    # Asks for user input and appends them to a list, unless user inputs
    # a blank line
    # The loop ends when flag equals False

    while flag:
        from_user = input()
        if from_user == "" and value_count < 2:
            print("Error: needs two or more values.")
            flag = False
        elif from_user != "":
            values.append(float(from_user))
            value_count += 1
        elif from_user == "":
            flag = False
    return values


def calculate_mean(values):

    """Calculates the mean from the values in a list
    :param values: the list from which the mean is calculated from
    :return: returns the mean
    """

    sum = 0
    for value in values:
        sum += value
    mean = sum / len(values)
    return mean


def calculate_variance(values):

    """Calculates the variance from the values in a list
    :param values: the list from which the variance is calculated from
    :return: returns the variance
    """

    mean = calculate_mean(values)
    sum = 0
    for value in values:
        sum += (value - mean) ** 2
    variance = sum / (len(values) - 1)
    return variance


def calculate_std_dev(variance):

    """Calculates the standard deviation from the variance by squaring it
    :param variance: the variance of the values from the list
    :return: returns the standard deviation based on the variance
    """

    standard_deviation = sqrt(variance)
    return standard_deviation


def print_histogram(values):

    """Prints the histogram and class interval.
    :param values: the list from which everything is calculated from
    """

    mean = calculate_mean(values)
    std_dev = calculate_std_dev(calculate_variance(values))
    if std_dev == 0:
        print("Deviation is zero.")
        return

    for category_number in range(0, 6):
        count = 0
        lower_limit = category_number * 0.5 * std_dev
        upper_limit = (category_number + 1) * 0.5 * std_dev

        # Calculates the category intervals in the loop above and
        # checks which category each value in
        # the list belongs to in the loop below
        # and prints them.

        for value in values:
            observed = abs(value - mean)
            if lower_limit <= observed < upper_limit:
                count += 1
        print(f"Values between std. dev. "
              f"{lower_limit:.2f}-{upper_limit:.2f}:", end=" ")
        print(count * "*")


if __name__ == "__main__":
    main()
