#!/usr/bin/env python

from __future__ import division

import argparse
import h5py

parser = argparse.ArgumentParser(description="Prints a glimpse of a LALInference HDF5 files.")

parser.add_argument('-p', '--posterior', type=str, help='posterior HDF5 file.')
parser.add_argument('-d', '--dataset', type=str, help='dataset in HDF5 file.',
                    default='lalinference/lalinference_mcmc/posterior_samples')

args = parser.parse_args()

data=h5py.File(args.posterior, 'r')

post = data[args.dataset]

def single_line(item):
    return [item.ljust(20),
            str(post[item][-1]).ljust(16),
            str(post[item][-2]).ljust(16),
            str(post[item][-3]).ljust(16),
            ' ... ',
            str(post[item][0]).ljust(16)]

lines=['\t'.join(single_line(item)) for item in post.dtype.names]

print '\n'.join(lines)
