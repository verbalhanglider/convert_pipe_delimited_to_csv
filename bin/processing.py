"""a cli module to process a text file from sqlite stdout into something to display to stakeholders
"""

from argparse import ArgumentParser
import csv
from os import _exit

def _group_it(lines_in_file):
    big_dict = {}
    for a_line in lines_in_file:
        title, receipt, createdate = a_line.split('|')
        if big_dict.get(title, None) is None:
            big_dict[title] = {'records': [{'receipt': receipt, 'createdate': createdate}]}
        else:
            big_dict[title]['records'].append({'receipt':receipt, 'createdate':createdate})
    return big_dict


def main():
    """main function of cli module
    """
    parser = ArgumentParser(description="A tool to take a pipe-delimited SQLITE output " +
                            " and parse it into a hierarchy display of subgroups"
                           )
    parser.add_argument("pipe_delimited_file")
    parser.add_argument("output_file")
    arguments = parser.parse_args()
    data = None
    with open(arguments.pipe_delimited_file, "r", encoding="utf-8") as read_file:
        data = read_file.readlines()
    data_dict = _group_it(data)
    output = open(arguments.output_file, "a", encoding="utf-8")
    for n_item in data_dict:
        output.write("{}\n".format(n_item.strip()))
        for n_record in data_dict[n_item]["records"]:
            output.write('\t{} created on {}\n'.format(n_record["receipt"].strip(),
                                                       n_record["createdate"].strip()))
    with open("temp.csv", "w", encoding="utf-8") as write_file:
        csvwriter = csv.writer(write_file, quotechar="\"", delimiter=",", quoting=csv.QUOTE_ALL)
        for n_row in data:
            fields = n_row.strip().split('|')
            csvwriter.writerow(fields)

    return 0

if __name__ == "__main__":
    _exit(main())