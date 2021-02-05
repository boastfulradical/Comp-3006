import os
import Project_02
import argparse
from os import path

# Project_02.count_to_csv()

# test = Project_02.no_flags("text_1")
# print(test)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Args for word count:')

    parser.add_argument('-c', '--count', help='Count Flags')
    parser.add_argument('-l', '--length', nargs=2, help='Specify String')
    parser.add_argument('-z', '--alphabet', help='Count all alphabet')
    args = parser.parse_args()

    # Deletes CSV and replaces with new file
    if path.exists("out.csv"):
        os.remove("out.csv")

    # Results capture result from each file
    if args.count:
        result = Project_02.capital_letters(args.count)
        Project_02.count_to_csv(result)
    if args.length:
        result = Project_02.l_flag(args.length[1], args.length[0])
        Project_02.count_to_csv(result)
    if args.alphabet:
        result = Project_02.alpha(args.alphabet)
        Project_02.count_to_csv(result)
