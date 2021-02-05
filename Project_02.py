import csv


print()


def desc():
    '''Returns a count of all characters,
regardless of lower or uppercase.'''
    return None

print(desc.__doc__)
print()

# PART A
def no_flags(text_1):
    f = open(text_1, "r")
    all_freq = {}
    for line in f:
        line = line.rstrip()
        #Only difference, convert everything to lower case, then count the frequencies similar to above
        line = line.lower()
        for value in line:
            if value in all_freq:
                all_freq[value] += 1
            else:
                all_freq[value] = 1
    del all_freq[" "]

    for j in all_freq:
        print(j + "," +  str(all_freq[j]))


    return all_freq
#no_flags("text_1")

############################
############################

def desc2():
    '''Returns a count of all characters,
with regards to lower and uppercase.'''
    return None

print(desc2.__doc__)
print()


#PART B
def capital_letters(text_1):
    f = open(text_1, "r")
    # map that stores all the counts
    all_freq = {}
    # goes through each individual word and checks if it's lower case or capital
    for line in f:
        # Use rstrip to get rid of \n in the file line
        line = line.rstrip()
        # going through each line in the map
        for value in line:

            if value in all_freq:
                # if the value has been counted before, add one to it
                all_freq[value] += 1
            else:
                # other wise set it to one because we wouldn't have counted it yet
                all_freq[value] = 1
    #spaces are included so delete the key values that has all the spaces
    del all_freq[" "]


    # going through our frequency array and printing out the format (With the comma)
    for j in all_freq:
        print(j + "," +  str(all_freq[j]))


    return all_freq
#capital_letters("text_1")

############################
############################

def desc3():
    '''Returns a count of all characters that
are argument letters.'''
    return None

print(desc3.__doc__)
print()

# PART C
def l_flag(text_1, string_query):
    all_freq = {}
    f = open(text_1, "r")
    for line in f:
        line = line.rstrip()
        line = line.lower()
        for value in line:
        # go through our string like an array
            for i in string_query:
            # check the line and CHECK if individual character is in the freq map
                if i in value:
                    if i in all_freq:
                        all_freq[i] += 1
                    else:
                        all_freq[i] = 1

    for j in all_freq:
        print(j + "," + str(all_freq[j]))
    return all_freq
#l_flag("text_1","ab")

###########################
###########################

def desc4():
    '''Convert everything to lower case then,
count the frequencies of all characters. '''
    return None

print(desc4.__doc__)
print()

# #Only difference, convert everything to lower case, then count the frequencies similar to above
# PART D
def alpha(text_1):
    all_freq = {}
    f = open(text_1, "r")
    count = 0
    for line in f:
        for i in range(97, 123):
        # Going thru unicode lower case table
        # test converts current number to letter
            test = str(chr(i))
            for j in range(1):
            # Go through our string
                line = line.lower()
            # Check to see how many time alpha letter occurs in string
                for value in line:
                    if test in value:
                        if test in all_freq:
                            all_freq[test] += 1
                        else:
                            all_freq[test] = 1

            if test not in all_freq:
                all_freq[test] = 0

    for j in all_freq:
        print(j + "," + str(all_freq[j]))

    return all_freq
# alpha("text_1")


def count_to_csv(test_dict):
#     # read to CSV file
#     with open ('out.csv', newline='') as csvfile:
#         word_count = csv.reader(csvfile, delimiter = '', quotechar='|')
#        #goes line by line in CSV file, anything seperated by a common is brought together
#         for row in word_count:
#             print(', '.join(row))
# Write to CSV file
    with open('out.csv', 'a')as csvfile:
        for key in test_dict.keys():
            csvfile.write("%s, %s\n" %(key, test_dict[key]))
