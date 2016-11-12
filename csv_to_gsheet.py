import csv
import logging
import os
import sys

import gsheet_tools


def csvs_to_gsheet(spreadsheet_name, file_names, encoding='utf-8'):
    """Write all input files as separate sheets (plies) in one Google Spread Sheet.

    :param spreadsheet_name: how shall we call the spreadsheet?
    :param file_names: the paths of the files to read
    :param encoding: encoding of the input files
    :return: spreadsheet id of the new spreadsheet
    """
    def get_sheet_name(fn):
        return os.path.split(os.path.splitext(fn)[0])[-1]

    sheet_names = set(get_sheet_name(file_name) for file_name in file_names)
    if len(sheet_names) < len(file_names):
        raise Exception("Repeating file name, can't import")

    data = {}
    for file_name in file_names:
        logging.debug("Importing %s" % file_name)
        with open(file_name, 'r', encoding=encoding) as f:
            data[get_sheet_name(file_name)] = [tuple(r) for r in csv.reader(f)]
    return gsheet_tools.to_gsheet(spreadsheet_name, data)


def gsheet_to_csvs(spreadsheet_id, output_folder):
    for range_name, range_data in gsheet_tools.from_gsheet(spreadsheet_id):
        with open(os.path.join(output_folder, range_name + '.csv'), 'w', encoding='utf8') as f:
            writer = csv.writer(f, lineterminator='\n')
            for r in range_data:
                writer.writerow(r)


def main():
    if sys.argv[1] == 'c2g':
        csvs_to_gsheet(sys.argv[2], sys.argv[3:])
    elif sys.argv[1] == 'g2c':
        csvs_to_gsheet(sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main()
