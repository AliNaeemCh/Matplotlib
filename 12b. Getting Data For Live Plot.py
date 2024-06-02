import os
import time
import requests

counter = 0
delete = True
# Open the file in write mode ('w')
with open('dataset/btc price.csv', 'w') as file:
    # Write content to the file
    file.write('time,price')
def write_to_csv (file_name, record, delete):
    # Input file path
    input_file = file_name

    # Open the input CSV file in read mode
    with open(input_file, 'r+') as file:
        if delete:
            # Read the first line (header)
            header = file.readline()

            # Find the position of the start of the third line (after the first and second lines)
            file.readline()  # Skip the second line
            start_pos = file.tell()

            # Move the content after the second line to the beginning of the file
            file.seek(start_pos)
            remaining_content = file.read()
            file.seek(0)
            file.write(header + remaining_content)
            file.truncate()

        # Add a new line at the end of the file
        file.seek(0, os.SEEK_END)
        file.write('\n'+record)

    # Optional: Rename the file back to the original name if needed
    # This step is optional and depends on your specific use case
    os.rename(file_name, input_file)

# Fetching current BTC price from API every 30 seconds

while True:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    record = data['time']['updatedISO'][11:19] + ',' + str(int(data['bpi']['USD']['rate_float']))
    counter += 1
    if(counter <= 60):
        delete = False
    write_to_csv('dataset/btc price.csv', record, delete)
    time.sleep(30)