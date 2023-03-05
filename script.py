import csv
import random

# Generate a list of 10 random numbers between 0 and 100
numbers = [random.randint(0, 100) for _ in range(10)]

# Generate a list of 5 random animal names to use as headers
animals = ['lion', 'tiger', 'bear', 'elephant', 'giraffe']
headers = random.sample(animals, 5)

# Write the numbers to a CSV file with animal names as headers
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for number in numbers:
        writer.writerow([number for _ in range(5)])