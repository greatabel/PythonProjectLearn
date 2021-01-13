from math import *
from csv_reader import csv_reader


def d_index(data1, data2, w):
    results = []
    for i in range(len(data1)):
        s = 0
        for j in range(len(w)):
            d = data1[i][j] - data2[i][j]
            s += w[j] * abs(d)
        results.append(s)
    return results


if __name__ == "__main__":
    data1 = csv_reader("samples1.csv")
    data2 = csv_reader("samples2.csv")
    w = csv_reader("weights.csv")[0]
    results = d_index(data1, data2, w)
    dsum = 0
    for i in range(len(results)):
        dsum = dsum + results[i]
    print("d-index:", dsum / len(results))
