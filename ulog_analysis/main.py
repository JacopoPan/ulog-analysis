'''Main.

Notes:
    Main executable script.

'''
import os
import sys
import argparse
import csv
import pyulog
import tikzplotlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.interpolate import interp1d

def run(
    file: str= '',
):
    '''Main function.
    '''
    ulog = pyulog.ULog(file)
    data = ulog.data_list
    output_file_prefix = file
    if output_file_prefix.lower().endswith('.ulg'):
        output_file_prefix = output_file_prefix[:-4]

    dataframes = {}
    for d in data:
        fmt = '{0}_{1}_{2}.csv'
        output_file_name = fmt.format(output_file_prefix, d.name.replace('/', '_'), d.multi_id)
        print('Writing {0} ({1} data points)'.format(output_file_name, len(d.data['timestamp'])))
        with open(output_file_name, 'w', encoding='utf-8') as csvfile:

            # use same field order as in the log, except for the timestamp
            data_keys = [f.field_name for f in d.field_data]
            data_keys.remove('timestamp')
            data_keys.insert(0, 'timestamp')  # we want timestamp at first position

            # write the header
            csvfile.write(','.join(data_keys) + '\n')

            # write the data
            last_elem = len(data_keys)-1
            for i in range(0, len(d.data['timestamp'])):
                for k in range(len(data_keys)):
                    csvfile.write(str(d.data[data_keys[k]][i]))
                    if k != last_elem:
                        csvfile.write(',')
                csvfile.write('\n')

        dataframes[output_file_name] = pd.read_csv(output_file_name)
        print(dataframes[output_file_name].to_string()) 
        os.remove(output_file_name)

    print(dataframes)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Python parser for PX4 ulog files')
    parser.add_argument('--file',
                        default='',
                        type=str,
                        help='Relative path and filename of the ulog file',
                        )
    ARGS = parser.parse_args()
    run(**vars(ARGS))
