#!/usr/bin/env python

import fnmatch
import os


def find_files(pattern, location='.'):
    for file in os.listdir(location):
        if fnmatch.fnmatch(file, pattern):
            yield file


def extract_times(file):
    all_times = []
    for line in open(file):
        if 'icmp_seq' in line:
            all_times.append(float(line[line.rfind('=')+1:line.rfind(' ')]))
        elif 'rtt min/avg/max/mdev' in line:
            _, avg, _, mdev = [float(time) for time in line[line.find('=')+2:line.rfind(' ')].split('/')]

    return [time for time in all_times if (mdev < avg or time < mdev / 2)]


def list_average(input_list):
    return sum(input_list) / len(input_list)


def summary(pattern):
    averages = [list_average(extract_times(file)) for file in find_files(pattern)]
    list_min = min(averages)
    list_max = max(averages)
    list_avg = list_average(averages)
    print('min: %.2f, max: %.2f, avg: %.2f' % (list_min, list_max, list_avg))
