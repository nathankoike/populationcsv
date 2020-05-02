"""

Name: Nate Koike
Date: 31 March 2020
Desc: process the available population data of Japan
      data from: https://dashboard.e-stat.go.jp/en/graph?screenCode=00010
"""

import sys

# provide a default file name for the data set
Default_name = "date_population_dataset.txt"

# since the most recent data is from october we will start the year then
Year_start = "Oct"

# change the types of the data into useful types
def retype(data):
    # do this for every entry in the data set
    for i in range(len(data)):
        # get the data entry as a list, splitting on whitespace
        entry = data[i].split()

        # convert the population number into an integer
        entry[1] = int(entry[1])

        # insert the fixed data entry back into the dataset
        data[i] = entry

    return data

# find the month with the maximum population
def get_max(data):
    # the index with the max population and the value of the max population
    max = [0, 0]

    # for every entry of data
    for i in range(len(data)):
        entry = data[i]
        # always pick the most recent maximum point
        if entry[1] >= max[1]:
            max = [i, entry[1]]

    # we now have the index with the max population so we need to format it
    out = "MAX: " + (str(max[1])) + "000 at " + data[max[0]][0]

    print(out)

    # return the maximum index and count just in case we need it
    return max

# find the growth from year to year (assume that the year starts in october)
def get_growth_y(data):
    # collect all the entries that are in october
    dates = []
    for entry in data:
        if Year_start in entry[0]:
            dates.append(entry)

    # collect all the percent changes
    # the first entry cannot have a rate associated with it so we preemptively
    # fill this one
    rates = ["N/A"]

    # next remember the previous population
    prev = dates[0][1]

    # start by comparing the second entry to the first and continue this trend
    # until the end of the years available
    for i in range(1, len(dates)):
        # round to the nearest thousandth of a percent to make this cleaner
        # also use string formatting to have uniform accuracy
        rates.append(format(round((dates[i][1])/prev - 1, 3), "1.3f") )
        prev = dates[i][1]

    # get just the years for the dates
    years = []

    for date in dates:
        years.append(date[0][date[0].index('.') + 1:])

    # print the results NICELY
    for i in range(len(years)):
        print("    ", years[i], end=": ")

        # print a leading space to align all the '%' at the end
        if not '-' in rates[i]:
            print(end=' ')

        print(rates[i], end="")

        # if this is the first entry there is no need to attach a '%' to the N/A
        if i == 0:
            print()
        else:
            print("%")

    # return the years and rate of change just in case we need it for something
    # this should be a tuple so the data inside cannot be modified
    return (years, rates)

# find the rate of change of the rate of change of the data
# just find a simple slope from the first point to the last point because of the
# accuracy loss from the previous step
def get_roroc(years, rates):
    # first we need to clean the data
    # we only care about the first and last data points
    # we can ignore the first data points since there is no usable data for them
    first = [years[1], rates[1]]
    last = [years[-1], rates[-1]]

    # next remove the '%' from the end of the rates and make them a number again
    first[1] = float(first[1])
    last[1] = float(last[1])

    # next make the years integers
    first[0] = int(first[0])
    last[0] = int(last[0])

    # find a simple slope rounding to the nearest thousandth
    slope = (last[1] - first[1])/(last[0] - first[0])

    # output our findings
    print("    ", end=' ')
    # if the slope is negative
    if slope < 0:
        print(format(slope, "1.5f"))
    else:
        print('', format(slope, "1.5f"))

    # return the slop in case we need it for something
    return slope

def main():
    # try to get the file name (and possible path) from the command line
    try:
        fname = sys.argv[1]

    # if there is no command line call then use the default name from the global
    # variable
    except:
        fname = Default_name

    # open the file with read only permission
    file = open(fname, "r")

    # retrieve the data from the file
    dataset = []
    for line in file:
        line = line[:len(line) - 1]
        dataset.append(line)

    # clean the data into useful types
    dataset = retype(dataset)

    # now that the dataset has been cleaned, we can process it for usefulness
    # get the maximun population
    get_max(dataset)
    print()

    # find the population growth rates from year to year
    print("Population change from past year:")
    growth = get_growth_y(dataset)
    print()

    # find out how fast the rate of change of the population is changing
    print("Rate of change of population growth rate:")
    get_roroc(growth[0], growth[1])
    print()

    # wait for user input to end the program
    input("Press any key to exit.")

if __name__ == "__main__":
    main()
