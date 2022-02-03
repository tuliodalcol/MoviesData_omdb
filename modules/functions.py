import numpy as np
import pandas as pd
import json
import os

def mk_dir(output_dir):
    # mkdir if doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def string2float(s):
    # Transform strings to float from key='Ratings' in api response
    if '%' in s:
        return float(s.strip('%'))/100
    elif '/' in s:
        num, denom = s.split('/')
        return float(num)/float(denom)
    else:
        return float(s)

def export_response(response:dict, file_name, path):
    with open(f'{path}/response_{file_name}.json', 'w') as outfile:
        json.dump(response, outfile)
    print (f'\nResponse exported to {path}/response_{file_name}.json')

def export_csv(api_response:dict, file_name, path):
    #df = pd.DataFrame.from_dict(self.data, orient='index').reset_index()
    df = pd.DataFrame(api_response, index=[0])
    df.to_csv(f'{path}/{file_name}.csv', index=True)
    print (f'CSV exported to {path}/{file_name}.csv')
