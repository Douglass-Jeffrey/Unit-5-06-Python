#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Nov 2019
# This program turns inputs into a proper address format


def rounding(number, rounder):
    # This function rounds the user's number

    # Process
    rounded_number = (number[0]*(10**rounder))
    rounded_number = rounded_number + 0.5
    rounded_number = int(rounded_number)
    rounded_number = rounded_number/(10**rounder)

    return rounded_number


def main():
    # This function takes the user's number then outputs the number rounded

    # rounder list
    rounding_number = []

    # Process
    while True:
        decimal = input("Enter the number you wish to be rounded: ")
        rounder = input("Enter how many decimal places you want left: ")

        try:
            decimal = float(decimal)
            rounder = int(rounder)
            rounding_number.append(decimal)
            if decimal == float(decimal) and \
               rounder == int(rounder):
                rounded_val = rounding(rounding_number, rounder)
                print("")
                print("Your number rounded is", rounded_val)
                break
            else:
                print("Please input proper values")
        except Exception:
            print("Please input proper values")
            print("")


if __name__ == "__main__":
    main()
