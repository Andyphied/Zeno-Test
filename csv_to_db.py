from pymongo import MongoClient
import pandas as pd

file_name = input('Input Name of File along with its extension(eg .csv or .xlsx): ')
client = MongoClient() #Connects to the local server
db = client.py_test
df = pd.read_csv(file_name)

def run():
    action = input('Create a fresh collection input Y/N: ')
    csv_to_db(action)

def csv_to_db(action):
    records_ = df.to_dict(orient = 'records')
    if action.lower() == 'y':
        print('Droping old Collection')
        db.temp_measurements.drop()
    elif action.lower() == 'n':
        print('If collection exist would add to it')
    else:
        print('Wrong Input')
        return run()
    result = db.temp_measurements.insert_many(records_ )
    print('Done Importing')

if  __name__ == '__main__':
    run()
    #assert db.temp_measurements.count() == len(df.index)


