# -*- coding: utf-8 -*-
import csv


with open('./list.csv') as files:
    csv_files = csv.reader(files)
    with open('./list-1.csv', 'w') as files_w:
        print 'start list-1'
        csv_files_w = csv.writer(files_w)

        # Remove png words.
        for words in csv_files:
            if 'png' not in words[-1]:
                csv_files_w.writerow(words)
        print 'ending list-1'

    with open('./list-2.csv', 'w') as files_w_2:
        print 'start list-2'
        csv_w = csv.writer(files_w_2)
        with open('./list-1.csv') as files_r:
            csv_r = [i for i in csv.reader(files_r)]
            loops = 0
            for words in csv_r:
                loops += 1
                if '正' in words[1]:
                    target = words
                    for get_words in csv_r[loops:]:
                        if get_words[0].startswith(target[0]):
                            csv_w.writerow((get_words[-2], target[-2]))
                            continue
        print 'ending list-2'
