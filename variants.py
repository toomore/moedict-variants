# -*- coding: utf-8 -*-
import csv


with open('./list.csv') as files:
    csv_files = csv.reader(files)
    with open('./list-1.csv', 'w') as files_w:
        csv_files_w = csv.writer(files_w)

        # Remove png words.
        for words in csv_files:
            if 'png' not in words[-1]:
                csv_files_w.writerow(words)
