import pandas as pd


# Input data
data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'


# Split lines
rows_raw = data.split('\n')
rows_raw.pop()


# Process header
header = rows_raw[0].split(';')
to_from = header.pop()
header = header + to_from.split('_')


# Process data rows
row_data = [rows_raw[i].split(';') for i in range(1, len(rows_raw))]
for i in range(len(row_data)):
    to_from_val = row_data[i].pop()
    row_data[i] = row_data[i] + to_from_val.split('_')


# Create table for further processing
table = pd.DataFrame(row_data, columns=header)


# Process each column 
# To/From
table['To'] = [s.upper() for s in table['To']]
table['From'] = [s.upper() for s in table['From']]


# FlightCodes
table['FlightCodes'] = [int(float(table['FlightCodes'][0])) + i*10 for i in range(5)]


# AirlineCode 
new_airline_code = []


for string in table['Airline Code']:
    new_string = ''
    for c in string:
        if c.isalpha() or c == ' ': new_string += c
    new_airline_code.append(new_string.strip())
    
table['Airline Code'] = new_airline_code


# Final result
print(table)