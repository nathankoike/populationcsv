import sys
from csv import writer

def main():
    # get the input file name
    ifname = sys.argv[1]

    # get the output file name
    ofname = sys.argv[2]

    # open the files
    ifile = open(ifname, "r")
    ofile = open(ofname, "a+")

    # make the csv writer
    csv_writer = writer(ofile)

    # get a list of all the elements to add
    element_list = []

    for line in ifile:
        # element_list.append(line.split())

        l = line.split()
        if len(l) > 2:
            l = [(l[0] + " " + l[1]), l[2]]
        element_list.append(l)

    # for i in range(len(element_list)):
    #     e = element_list[i]
    #     # split the data into months and years
    #     if len(e) < 3:
    #         [m, y] = e[0].split(".")
    #     else:
    #         [m, y] = [e[0], e[1]]
    #
    #     # replace the months with the number
    #     if m == "Jan":
    #         m = "01"
    #     elif m == "Feb":
    #         m = "02"
    #     elif m == "Mar":
    #         m = "03"
    #     elif m == "Apr":
    #         m = "04"
    #     elif m == "May":
    #         m = "05"
    #     elif m == "Jun":
    #         m = "06"
    #     elif m == "Jul":
    #         m = "07"
    #     elif m == "Aug":
    #         m = "08"
    #     elif m == "Sep":
    #         m = "09"
    #     elif m == "Oct":
    #         m = "10"
    #     elif m == "Nov":
    #         m = "11"
    #     elif m == "Dec":
    #         m = "12"
    #
    #     e_last = e[-1]
    #
    #     # format the date
    #     e_first = y + m
    #
    #     e = [e_first, e_last]
    #
    #     element_list[i] = e

    # write the contents of the file to a csv file
    for e in element_list:
        print(e)
        csv_writer.writerow(e)

main()
