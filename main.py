import csv
from evaluation import evaluate


def laod_data(file_name):
    data = []
    with open(file_name, 'r') as my_file:
        reader = csv.reader(my_file)
        for row in reader:
            data.append({'x': row[:-1], 'y': row[-1]})
    return data


def avg(data):
    return sum(data) / len(data)


def test(data_file):
    for i in range(2, 9):
        results = []
        for j in range(10):
            car_data = laod_data(data_file)
            results.append(evaluate(car_data, i))
        print(f'walidacja k={i}: ', avg(results))
        


def main():
    #print('car:')
    #test('car.csv')

    print('breast cancer:')
    test('breast-cancer.csv')


if __name__ == "__main__":
    main()
