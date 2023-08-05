'''Main.

Notes:
    Main executable script.

'''
import argparse
import csv
import sys
import tikzplotlib
import pyulog

import matplotlib.pyplot as plt
import numpy as np

from scipy.interpolate import interp1d

def run(
    file: str= '',
):
    '''Main function.
    '''
    print(file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Python parser for PX4 ulog files')
    parser.add_argument('--file',
                        default='',
                        type=str,
                        help='Relative path and filename of the ulog file',
                        )
    ARGS = parser.parse_args()
    run(**vars(ARGS))
