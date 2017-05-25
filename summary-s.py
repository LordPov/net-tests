#!/usr/bin/env python

import summary


def extract_speeds(file):
    for line in open(file):
        if 'Download:' in line:
            download = float(line.split(' ')[1])
        elif 'Upload:' in line:
            upload = float(line.split(' ')[1])

    return download, upload


def output(speeds):
    return 'min: %.2f, max: %.2f, avg: %.2f' % ((min(speeds)), (max(speeds)), (summary.list_average(speeds)))


def output_both(pattern):
    downloads, uploads = [output(speeds) for speeds in zip(*[extract_speeds(file) for file in summary.find_files(pattern)])]
    print('Downloads (Mbit/s) -', downloads)
    print('Uploads (Mbit/s) -', uploads)


if __name__ == '__main__':
    output_both('st-*')
