from math import *
from csv_reader import csv_reader


def sample_difference(data1, data2, w):
    results = []
    for i in range(len(data1)):
        s = 0
        for j in range(len(w)):
            d = data1[i][j] - data2[i][j]
            s += w[j] * abs(d)
        results.append(s)
    return results


if __name__ == "__main__":
    data1 = csv_reader("data1.csv")
    data2 = csv_reader("data2.csv")
    w = csv_reader("weights.csv")[0]
    # print(data1, data2, w)
    results = sample_difference(data1, data2, w)
    # print('results=', results)
    critical = 0
    for i in range(len(results)):
        if results[i] > 5:
            critical = critical + 1
    if critical == 1:
        print("criticality: 1 result above 5")
    else:
        print("criticality:", critical, "results above 5")
