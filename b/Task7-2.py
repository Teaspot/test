squares = [value ** 2 for value in range(1, 101)]
import csv
file_name = 'squares.csv'
with open(file_name, 'w', newline='') as f:
    write_csv = csv.writer(f)
    for square in squares:
        write_csv.writerow([str(square)])