# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"J173200","system":"readv2"},{"code":"J502.00","system":"readv2"},{"code":"J502200","system":"readv2"},{"code":"J502z00","system":"readv2"},{"code":"15594.0","system":"med"},{"code":"17831.0","system":"med"},{"code":"23573.0","system":"med"},{"code":"3403.0","system":"med"},{"code":"4385.0","system":"med"},{"code":"50797.0","system":"med"},{"code":"54395.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('volvulus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["volvulus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["volvulus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["volvulus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
