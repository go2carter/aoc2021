from argparse import ArgumentParser
import logging

import numpy as np


logging.basicConfig(level=logging.INFO)


def parse_args():
    """ parse args """
    argparser = ArgumentParser()
    argparser.add_argument('input_file', help='.')
    argparser.add_argument('--convolve', '-c', action='store_true')
    return argparser.parse_args()


def compute_increases(input_file: str, convolve: bool) -> int:
    with open(input_file) as f:
        data = f.read()
    depths = data.split('\n')
    depths = np.array([int(d) for d in depths])
    if convolve:
        logging.info('Convolving...')
        depths = np.convolve([1,1,1], depths, 'valid')
    delta = np.diff(depths)
    n_incr = np.sum(delta > 0)
    return n_incr

def main():
    args = parse_args()
    n_incr = compute_increases(args.input_file, args.convolve)
    print(f'Increasing depths: {n_incr}')


if __name__ == '__main__':
    main()
