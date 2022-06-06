import pandas as pd
import termcolor as tc


# main file
def create_csv_file():
    # global dictionary as work list
    dictionary = {}

    description = "\n\n-a for adding data\n-c for creating\n-d for deleting the last row\n-h for help\n-q for quitting" \
                  "\n-r for reading\n-s for saving\n"
    print(tc.colored("\nWelcome! \nHere you can create a csv file.", "blue") + "{}".format(description))

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

        if statement == "-e":

            user_input = input(tc.colored("\nAll cached data will be lost. Do you really want to clear "
                                          "your work list? y?\n", "red"))
            if user_input == "y":
                dictionary = clear_work_list(dictionary)

            continue

        if statement == "-a":
            # if dictionary is empty
            if not dictionary.keys():
                print(tc.colored("\nThere is no table header created. Create a table header to add data!\n", "red"))
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
            print("\n-a  You can add a row of data to your work list.")
            print("\n-c  Lets you create a table header for your work list.")
            print("\n-d  Deletes the last row of your work list")
            print("\n-e  Clears your work list")
            print("\n-h  Shows you a description to a command's function.")
            print("\n-q  Eventually exits the application.")
            print("\n-r  Displays you the content of an arbitrary csv file and handles it as work list.")
            print("\n-s  Saves your work list as a csv file.")
            continue

        if statement == "-s":
            while True:
                file_name = input("\nPlease name your file to save it.\n") + ".csv"
                print("{} - y?\n".format(file_name))
                accept = input()
                if accept == "y":
                    # saves data from dictionary in pandas dataframe to create a csv without indices
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

                if filename == "-q.csv":
                    break

                try:
                    # reads a csv file from pandas csv reader
                    dataframe = pd.read_csv(filename)
                    print(dataframe)
                    break

                except FileNotFoundError:
                    print(tc.colored("There's not such a file. Try again!\n", "red"))
                    continue

        else:
            print(tc.colored("\nThis was no valid statement.{}".format(description), "red"))
            continue


def create_dataset(dictionary):
    columns = input("How many columns shall your file have?  ")

    try:
        # necessary to check if correct type of input before printing
        amount = int(columns)
        print("\nPlease name the columns.\n")
        for i in range(amount):
            name = input("\nName of column {}:  ".format(i + 1))
            # saves the names of columns in dictionary as key with empty list as value
            dictionary[name] = []
        print("\nCreated a table header with %s columns.\n" % columns)

        return dictionary

    except ValueError:
        print(tc.colored("\n Please enter a valid number!\n", "red"))


def add_data(dictionary):

    # iterates through all keys in dictionary and saves for each key the user input as value (list)
    for table_element in dictionary.keys():
        data_input = input("\n{}:  ".format(table_element))
        dictionary[table_element].append(data_input)

    return dictionary


def delete_last_row(dictionary):

    for table_element in dictionary.keys():
        dictionary[table_element].pop()

    print("\nLast row deleted.", tc.colored("Save the file to keep the changes.\n", "blue"))

    return dictionary


def clear_work_list(dictionary):
    dictionary.clear()
    print("Work list cleared.")
    return dictionary


if __name__ == '__main__':
    create_csv_file()
