#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 17th, 2022.
# This program asks the user to enter a decimal number and how many places
# they'd like the decimal moved to. Depending on the number they entered, it
# moves the decimal place that many times & displays it to the user.


# this function rounds the number user.
def round_decimal(num_user, dec_place):
    num_user[0] = num_user[0] * (10 ** dec_place)
    num_user[0] = num_user[0] + 0.5
    num_user[0] = int(num_user[0])
    num_user[0] = num_user[0] / (10 ** dec_place)


def main():

    print("This program rounds a decimal to the number of places entered.")
    print("")

    # create a list
    user_num = []

    # get user input from user
    dec_num_str = input("Enter a decimal number: ")

    try:
        # convert string into a float.
        dec_num_float = float(dec_num_str)

        # adds to list
        user_num.append(dec_num_float)

        # gets user input
        dec_place_string = input("Enter the number of decimal places: ")

        try:
            # converts string into int
            dec_num_place_int = int(dec_place_string)

            # sets a range
            if dec_num_place_int < 0:
                print("{} is not a positive integer".format(dec_num_place_int))
            else:
                # calls function
                round_decimal(user_num, dec_num_place_int)

                # displays rounded answer to user.
                print("{} rounded to {} decimal places is {}."
                      .format(dec_num_float, dec_num_place_int, user_num[0]))

        # handles error case
        except Exception:
            print("{} is not a valid input.".format(dec_place_string))

    # handles error case.
    except Exception:
        print("{} is not a decimal number.".format(dec_num_str))


if __name__ == "__main__":
    main()
