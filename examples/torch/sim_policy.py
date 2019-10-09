#!/usr/bin/env python3

import argparse

import joblib
import tensorflow as tf

from garage.misc.console import query_yes_no
from garage.sampler.utils import rollout

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='path to the snapshot file')
    parser.add_argument(
        '--max_path_length',
        type=int,
        default=1000,
        help='Max length of rollout')
    parser.add_argument('--speedup', type=float, default=1, help='Speedup')
    args = parser.parse_args()

    # If the snapshot file use tensorflow, do:
    # import tensorflow as tf
    # with tf.compat.v1.Session():
    #     [rest of the code]
    data = joblib.load(args.file)
    policy = data['algo'].policy
    env = data['env']
    while True:
        path = rollout(
            env,
            policy,
            max_path_length=args.max_path_length,
            animated=True,
            speedup=args.speedup)
        if not query_yes_no('Continue simulation?'):
            break