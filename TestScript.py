import csv
import random
import datetime

# Define a function to get the local timezone offset
def get_timezone_offset():
    now = datetime.datetime.now()
    offset = now.astimezone().utcoffset()
    hours = int(offset.total_seconds() / 3600)
    minutes = int((offset.total_seconds() % 3600) / 60)
    return f'{hours:+03d}:{minutes:02d}'

# Generate a list of 10 random numbers between 0 and 100
numbers = [random.randint(0, 100) for _ in range(10)]

# Generate a list of 5 random animal names to use as headers
animals = ['lion', 'tiger', 'bear', 'elephant', 'giraffe']
headers = random.sample(animals, 5)

# Get the current timestamp with timezone offset
now = datetime.datetime.now()
offset = get_timezone_offset()
timestamp = now.strftime(f'%d_%B_%Y_%H:%M (UTC{offset})')

# Write the numbers and timestamp to a CSV file with animal names as headers
with open(f'data_{timestamp}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Created on ' + str(timestamp)])
    writer.writerow(headers)
    for number in numbers:
        writer.writerow([number for _ in range(5)])