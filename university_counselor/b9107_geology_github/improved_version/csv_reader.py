def csv_reader(filename):
    # print(filename, 'in csv_reader')
    with open(filename) as file1:
        lines1 = file1.readlines()
        data1 = []
        for line in lines1:
            row = []
            for n in line.split(","):
                row.append(float(n.strip()))
            data1.append(row)
    return data1
