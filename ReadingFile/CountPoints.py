
def main():
    filename = input("Enter the name of the score file: ")
    try:
        file = open(filename, mode="r")
    except OSError:
        print("Error")

    dict = {}
    for line in file:
        line_parts = line.split()
        if line_parts[0] in dict:
            dict[line_parts[0]] += int(line_parts[1])
        else:
            dict[line_parts[0]] = int(line_parts[1])

    print("Contestant score:")
    for key in sorted(dict):
        print(key, dict.get(key))


if __name__ == "__main__":
    main()
