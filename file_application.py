import pandas as pd
import termcolor as tc


def create_csv_file():
    dictionary = {}

    description = "\n\n-a for adding data\n-c for creating\n-h for help\n-q for quitting" \
                  "\n-r for reading\n-s for saving\n"
    print("Welcome! \nHere you can create a csv file.{}".format(description))

    while True:

        statement = input("\nWhat do you want to do?  ")

        if statement == "-q":
            print("Thank you for using the tool. Goodbye.")
            break

        if statement == "-c":
            dictionary = create_dataset(dictionary)
            continue

        if statement == "-d":
            dictionary = delete_last_row(dictionary)
            continue

        if statement == "-a":
            if not dictionary.keys():
                print("\nThere is no table header created. Create a table header to add data!\n")
                continue

            else:
                print("Data input started.\n")

                next_row = True
                while next_row:
                    dictionary = add_data(dictionary)
                    continue_data_input = input("\nIf you want to continue with adding data press \"y\".\n")
                    if continue_data_input != "y":
                        next_row = False
                continue

        if statement == "-h":
            print("\n-a  You can add a row of data to an already created table.")
            print("\n-c  Lets you create a table header.")
            print("\n-h  Shows you a description to a command's function.")
            print("\n-q  Eventually exits the application.")
            print("\n-r  Displays you the content of an arbitrary csv file.")
            print("\n-s  Saves your created table as a csv file.")
            continue

        if statement == "-s":
            while True:
                file_name = input("Please name your file to save it.\n") + ".csv"
                print("{} - y?\n".format(file_name))
                accept = input()
                if accept == "y":
                    dataframe = pd.DataFrame(dictionary)
                    dataframe.to_csv(file_name, index=False)
                    print("File created.")
                    break

                else:
                    continue

            continue

        if statement == "-r":
            while True:
                print("Enter a filename!  ")

                filename = input() + ".csv"

                try:
                    dataframe = pd.read_csv(filename)
                    print(dataframe)
                    break

                except FileNotFoundError:
                    print(tc.colored("There's not such a file. Try again!\n"))
                    continue

        else:
            print(tc.colored("\nThis was no valid statement.{}".format(description)))
            continue


def create_dataset(dictionary):
    columns = input("How many columns shall your file have?  ")

    try:

        for i in range(int(columns)):
            name = input("\nName of column {}:  ".format(i + 1))
            dictionary[name] = []
        print("\nCreated a file with %s columns.\n" % columns)
        print("\nPlease name the columns.\n")

        return dictionary

    except ValueError:
        print(tc.colored("\n Please enter a valid number!\n", "red"))


def add_data(dictionary):

    for table_element in dictionary.keys():
        data_input = input("\n{}:  ".format(table_element))
        dictionary[table_element].append(data_input)

    return dictionary


def delete_last_row(dictionary):

    for table_element in dictionary.keys():
        dictionary[table_element].remove(-1)

    return dictionary


if __name__ == '__main__':
    create_csv_file()

    # deleting a row
    # json