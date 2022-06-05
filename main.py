import pandas as pd


def create_csv_file():
    list_prenames = []
    list_lastnames = []
    list_courses = []

    print("Welcome! \nHere you can create a csv file.\n\n-c for creating\n-s for saving\n-r for reading\n-q for quitting\n")

    while True:

        statement = input("\nWhat do you want to do?  ")

        if statement == "-q":
            print("Thank you for using the tool. Goodbye.")
            break

        if statement == "-c":
            list_prenames, list_lastnames, list_courses = create_dataset(list_prenames, list_lastnames, list_courses)
            continue

        if statement == "-s":
            while True:
                file_name = input("Please name your file to save it.\n") + ".csv"
                print("%s - y?\n" % file_name)
                y_or_n = input()
                if y_or_n == "y":
                    dictionary = {"Prename": list_prenames, "Lastname": list_lastnames, "Course": list_courses}
                    dataframe = pd.DataFrame(dictionary)
                    dataframe.to_csv(file_name, index=False)
                    break

                else:
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
                    print("There's not such a file. Try again!\n")
                    continue

        else:
            print("This was no valid statement.\n\n-c for creating\n-s for saving\n-q for quitting\n")
            continue


def create_dataset(list_prenames, list_lastnames, list_courses):

    prename, lastname, course = add_row()

    list_prenames.append(prename)
    list_lastnames.append(lastname)
    list_courses.append(course)

    return list_prenames, list_lastnames, list_courses


def add_row():
    prename = input("Prename: ")
    lastname = input("Lastname: ")
    course = input("Course: ")
    return prename, lastname, course


if __name__ == '__main__':
    create_csv_file()