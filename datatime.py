'''
Created on 11-Sep, 2017

Create a datafile suitable for import to Hive with a range of dates

@author: jamey
'''

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from random import choice, randint
import string
import uuid

def CreateRecord (num_years):
    ''' Create num_records over num_years 
    (positive num_years means in the future, negative is in the past)
    Interval is hour.
    Outupt is:
        uuid,
        <random_string>,
        date(YYYY-MM-DD)
        date(YYYY-MM)
    '''   
    rand_str = lambda n: ''.join([choice(string.ascii_letters) for i in range(n)])
    
    record = []
    
    # UUID
    record.append(str(uuid.uuid4()))
    
    # random, 10-character word
    record.append(rand_str(10))
    
    # random integer between 0 and 100
    record.append(randint(0, 100))
        
    # random datetime over num_years
    # interval is minutes
    # 365.25 * 24 * 60 * 60 = 31,557,600 seconds / year
    SEC_IN_YEAR = 31557600
    delta_sec_range = num_years * SEC_IN_YEAR
    
    # swap the position of 0 and delta_sec_range if num_years <0
    if num_years < 0:
        delta_sec = randint(delta_sec_range, 0)
    else:
        delta_sec = randint(0, delta_sec_range)
    record_datetime = datetime.now() + timedelta(seconds = delta_sec)
     
    record.append(record_datetime.strftime('%Y%m'))
    record.append(record_datetime.strftime('%d-%b-%Y'))
    record.append(record_datetime.isoformat())
    
    return(record)

def main():
    NUM_RECORDS = 100000
    YEAR_RANGE = -10
    FILE_NAME = 'sample_date.csv'
    
    f = open(FILE_NAME, 'w')
    
    for i in range(1, NUM_RECORDS + 1):
        row = ''
        for cell in CreateRecord(YEAR_RANGE):
            row += (str(cell) + ', ')
        row = row[:-2] # remove final ', '
        row += '\n'
        f.write(row)
    f.close()
    
    print(str(NUM_RECORDS) + ' records written to ' + FILE_NAME)
    
if __name__ == '__main__':
    main()