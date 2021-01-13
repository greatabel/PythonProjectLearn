from math import *
from csv_reader import csv_reader
import argparse


def parser():
    parser = argparse.ArgumentParser(description="workflow parameters")
    parser.add_argument(
        "--data1_path",
        type=str,
        default="data1.csv",
        help="path of data1.csv",
    )
    parser.add_argument(
        "--data2_path",
        type=str,
        default="data2.csv",
        help="path of data2.csv",
    )
    parser.add_argument(
        "--w",
        type=str,
        default="weights.csv",
        help="path of weight",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=5,
        help="threshold of critical",
    )
    args = parser.parse_args()
    return args


def check_none_existence(record):
    for item in record:
        # print('check_none_existence>', item)
        if item == None:
            return False
    return True


def sample_difference(data1, data2, w):
    results = []
    for i in range(len(data1)):
        if check_none_existence(data1[i]):
            s = 0
            for j in range(len(w)):
                d = data1[i][j] - data2[i][j]
                s += w[j] * abs(d)
            results.append(s)
    return results


def discrepancy(data1, data2, w):
    results = []
    for i in range(len(data1)):
        if check_none_existence(data1[i]):
            s = 0
            for j in range(len(w)):
                d = data1[i][j] - data2[i][j]
                s += sqrt(w[j] * abs(d**2))
            results.append(s)
    return results


if __name__ == "__main__":
    threshold = 5
    args = parser()
    print(args)
    data1_path, data2_path, w_path, threshold = args.data1_path, args.data2_path, args.w, args.threshold
    data1 = csv_reader(data1_path)
    data2 = csv_reader(data2_path)
    w = csv_reader(w_path)[0]
    
    # print(data1, data2, w)
    
    # results = sample_difference(data1, data2, w)
    results = discrepancy(data1, data2, w)
    print('results=', results)
    critical = 0
    for i in range(len(results)):
        if results[i] > threshold:
            critical = critical + 1
    if critical == 1:
        print("criticality: 1 result above 5")
    else:
        print("criticality:", critical, "results above 5")
