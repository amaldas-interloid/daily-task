def read_csv(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip().split(",")
for row in read_csv("/home/intercpu012/Downloads/customers-100.csv"):
    print(row)