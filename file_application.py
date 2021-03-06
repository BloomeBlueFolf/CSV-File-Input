import pandas as pd
import pandas.errors
import termcolor as tc
import time
import logging
import os
import pathlib
import re


# main file
def create_csv_file():

    logger()
    logging.info("logger created")

    regex_file = re.compile("[^\\\/:*?\"<>|!\'#§$%&()=^+]")

    # global dictionary as work list
    dictionary = {}
    logging.info("empty work list created")

    description = "\n\n-a for adding data to the work list\n-c for creating a work list\n" \
                  "-d for deleting the last row\n" \
                  "-e for clearing the work list\n-h for help\n-i for importing a file to work list\n" \
                  "-q for quitting\n-r for reading a csv file\n-s for saving the work list\n" \
                  "-v for showing the work list\n"

    print(tc.colored("\nWelcome! \nHere you can manipulate csv files.", "blue") + "{}".format(description))
    logging.info("welcome text displayed")

    while True:

        statement = input("What do you want to do?  ")
        logging.info("statement required")

        if statement == "-q":
            print("\nThank you for using the tool. Goodbye.")
            time.sleep(4)
            logging.info("shutdown process initiated")
            break

        if statement == "-c":
            logging.info("creating a work list started")
            dictionary = create_dataset(dictionary)
            logging.info("work list created")
            continue

        if statement == "-d":
            logging.info("deleting the last row started")
            dictionary = delete_last_row(dictionary)
            logging.info("last row deleted")
            continue

        if statement == "-v":
            logging.info("displaying current work list started")
            show_work_list(dictionary)
            logging.info("current work list displayed")
            continue

        if statement == "-e":

            logging.info("erasing process for current work list initiated")
            user_input = input(tc.colored("\nAll cached data will be lost. Do you really want to clear "
                                          "your work list? If you want to continue press \"y\".\n", "red"))
            logging.info("request accepting question asked")
            if user_input == "y":
                logging.info("checking for valid command: ok")
                dictionary = clear_work_list(dictionary)
                logging.info("work list erased")

            continue

        if statement == "-i":
            logging.info("importing a file to work list started")
            import_csv_file(dictionary)
            logging.info("file imported as work list")
            continue

        if statement == "-a":
            logging.info("adding data to work list started")
            # if dictionary is empty
            if not dictionary.keys():
                print(tc.colored("\nThere is no table header created. Create a table header to add data!\n", "red"))
                logging.warning("no existing work list - adding data failed")
                continue

            else:
                print("Data input started.\n")

                next_row = True
                while next_row:
                    dictionary = add_data(dictionary)
                    logging.info("data added")
                    continue_data_input = input("\nIf you want to continue with adding data press \"y\".\n")
                    logging.info("question about adding more data asked")
                    if continue_data_input != "y":
                        logging.info("continuation declined")
                        next_row = False
                        logging.info("adding data finished")
                continue

        if statement == "-h":
            logging.info("displaying commands started")
            print("\n-a  You can add a row of data to your work list.")
            print("-c  Lets you create a table header for your work list.")
            print("-d  Deletes the last row of your work list.")
            print("-e  Clears your work list.")
            print("-h  Shows you a description to a command's function.")
            print("-i  Imports data of an existing csv file to work list.")
            print("-q  Eventually exits the application.")
            print("-r  Displays you the content of an arbitrary csv file and handles it as work list.")
            print("-s  Saves your work list as a csv file.")
            print("-v  Shows the current work list.")
            print("\n")
            logging.info("help information displayed")
            continue

        if statement == "-s":
            logging.info("saving work list process started")
            while True:
                file_name = input("\nPlease name your file to save it.\n") + ".csv"
                logging.info("naming file for saving required")
                if regex_file.match(file_name):
                    print("{} - y?\n".format(file_name))
                    logging.info("echo filename")
                    accept = input()
                    if accept == "y":
                        # saves data from dictionary in pandas dataframe to create a csv without indices
                        dataframe = pd.DataFrame(dictionary)
                        dataframe.to_csv(file_name, index=False)
                        logging.info("csv file created")
                        print("File created.")
                        break

                    else:
                        continue
                else:
                    print(tc.colored("\nPlease enter a valid file name!", "red"))
            continue

        if statement == "-r":
            logging.info("reading a csv file started")
            while True:
                print("Enter a filename!  ")

                filename = input() + ".csv"
                logging.info("entering a file name required")

                if filename == "-q.csv":
                    logging.info("quitting displaying a work list")
                    break

                try:
                    # reads a csv file from pandas csv reader
                    dataframe = pd.read_csv(filename)
                    print(dataframe)
                    break

                except FileNotFoundError:
                    print(tc.colored("There's not such a file. Try again!\n", "red"))
                    logging.error("file not found for reading")
                    continue

                except pandas.errors.EmptyDataError:
                    print(tc.colored("\nThat's an empty file and cannot be read!\n", "red"))
                    logging.error("empty file can not be read")
                    continue

                except OSError:
                    print(tc.colored("\nThat is not a valid file name!\n", "red"))
                    logging.error("no valid file requested")
                    continue

        else:
            print(tc.colored("\nThis was no valid statement.", "red"))
            print("\nPlease use:{}".format(description))
            logging.error("checking valid command: not ok")
            continue


def create_dataset(dictionary):
    columns = input("How many columns shall your file have?  ")
    logging.info("amount of columns required")

    try:
        # necessary to check if correct type of input before printing
        amount = int(columns)
        logging.info("amount of columns input")
        print("\nPlease name the columns.\n")
        for i in range(amount):
            name = input("\nName of column {}:  ".format(i + 1))
            # saves the names of columns in dictionary as key with empty list as value
            dictionary[name] = []
            logging.info("column named")
        print("\nCreated a table header with %s columns.\n" % columns)
        logging.info("%s columns named" % columns)

        return dictionary

    except ValueError:
        print(tc.colored("\n Please enter a valid number!\n", "red"))
        logging.error("no valid number input")


def add_data(dictionary):

    # iterates through all keys in dictionary and saves for each key the user input as value (list)
    for table_element in dictionary.keys():
        data_input = input("\n{}:  ".format(table_element))
        dictionary[table_element].append(data_input)

    logging.info("data input")

    return dictionary


def delete_last_row(dictionary):

    for table_element in dictionary.keys():
        dictionary[table_element].pop()

    print("\nLast row deleted.", tc.colored("Save the file to keep the changes.\n", "blue"))

    return dictionary


def clear_work_list(dictionary):
    dictionary.clear()
    print("Work list cleared.\n")
    return dictionary


def import_csv_file(dictionary):

    while True:
        filename = input("\nWhich csv file do you want to import to work list?\n") + ".csv"
        logging.info("csv file input required")

        if filename == "-q.csv":
            logging.info("file import quit")
            break

        try:
            dataframe = pd.read_csv(filename)

            for table_header in dataframe:
                # iterates all table headers in dataframe and creates an empty list for each
                dictionary[table_header] = []
                # iterates every column and puts the elements in dictionary lists
                for column in range(len(dataframe.columns)):
                    dictionary[table_header].append(dataframe.loc[column].at[table_header])

            logging.info("imported file to work list")

            return dictionary

        except FileNotFoundError:
            print(tc.colored("\nThere's no such file!\n", "red"))
            logging.error("required file not found")
            continue

        except OSError:
            print(tc.colored("\nThat is not a valid file name!\n", "red"))
            logging.error("no valid file requested")
            continue


def show_work_list(dictionary):
    print(dictionary)


def logger():
    log_dir = str(pathlib.Path(__file__).parent) + "\\logfiles"
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
        logging.info("log directory created")
    logging.basicConfig(filename=log_dir + "\\logging.log", encoding="utf-8", level=logging.INFO,
                        format="%(levelname)s - [%(asctime)s ] - %(message)s", datefmt=" %d.%m.%Y - %I:%M:%S %p",
                        filemode="w")


if __name__ == '__main__':
    create_csv_file()
