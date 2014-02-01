# -*- coding: utf-8 -*-
import csv


with open('./list.csv') as files:
    csv_files = csv.reader(files)
    csv_files = [','.join(i) for i in csv_files]
    print csv_files[1]
