#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: October 2025
# This program checks if the year given by user is a leap year


def main():

    # get year from user
    user_year = input("Hey! Enter a year: ")
    # type cast to integer
    try:
        user_year = int(user_year)

        # check if divisible by 4
        if user_year % 4 == 0:
            # now check if divisible by 100
            if user_year % 100 == 0:
                # check if divisible by 400
                if user_year % 400 == 0:
                    print("{} is a leap year.".format(user_year))
                else:
                    print("{} is not a leap year.".format(user_year))
            else:
                print("{} is a leap year.".format(user_year))
        else:
            print("{} is not a leap year.".format(user_year))
    except ValueError:
        # exception handling
        print("ERROR! You have to enter a valid year!")
    # end game
    finally:
        print("Thanks for playing my game!")


if __name__ == "__main__":
    main()
