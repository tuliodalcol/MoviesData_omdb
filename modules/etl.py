import pandas as pd
import numpy as np
import requests
import json
import logging
import os

# Logging configuration
logging.basicConfig(filename='logs.txt', filemode='w', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def string2float(s):
    if isinstance(s, str):
        # Transform strings to float from key='Ratings' in api response
        if '%' in s: # convert percentage value
            return float(s.strip('%'))/100
        elif '/' in s: # convert division value
            num, denom = s.split('/')
            return float(num)/float(denom)
        else:
            return float(s)
    else:
        return float(s)

class omdb_api:
    '''
    Parameters
    ----------
        api_key : omdbapi key. 
                    Documentation: http://www.omdbapi.com/apikey.aspx
        type : movie, series, episode
        t : Content title to search for
        output_path : Directory where the api response will be exported to
    '''
    def __init__(self, api_key: str(), content_type: str(), content_name, output_path):            
        self.api_key = api_key
        self.content_type = content_type
        self.content_name = content_name
        self.output_path = output_path
        self.url_get = f'http://www.omdbapi.com/?apikey={self.api_key}'
        logger.info(f'Content_type={self.content_type}, Content_name={self.content_name}, output_dir={self.output_path}')

        # print error if content type input is not available
        if str.lower(self.content_type) not in ['movie', 'series']:
            print('Content type must be either Movie or Series!\n')
            logger.exception(f'{self.content_type} is invalid.')
            raise TypeError(f'{self.content_type} is invalid.')
        
        # create local directory if doesn't exist
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
            logger.debug(f'Directory name {self.output_path} created')

    def api_extract(self, year=''):
        '''
        Documentation: http://www.omdbapi.com/

        Parameters
        ----------
            type : movie, series, episode
            t : Content title to search for
            y : Year of release.
            plot : (short/full) Return short or full plot.
        '''
        params = {'t': self.content_name,
                  'type': self.content_type,
                  'y': year,
                  'plot': 'full'
        }
        r = requests.get(self.url_get, params=params) # api get request
        self.data = r.json() # convert response to json format
        
        if self.data['Response'] != 'True': # raise exception if api request fails
            error = self.data['Error']
            logger.error(f'API call failed. Error: {error}')
            raise Exception(f'{error}')
        logger.debug('Data extracted')

    def format(self):
        try: # format results
            rating_values = [string2float(i['Value']) for i in self.data['Ratings']] # trasnform string values to float
            self.data['avg_rate'] = round(np.mean(rating_values), 2) # store calculated rating mean value from results
            del self.data["Ratings"] # drop feature given by response
            del self.data["Response"] # drop feature given by response
            logger.debug('Data formatted')
        except: # raise exception if fails to format file
            logger.exception('Data cannot be formated')

    def export_response(self):
        # Export response json file to local directory 
        with open(f'{self.output_path}/{self.content_type}_{self.content_name}_response.json', 'w') as outfile:
            json.dump(self.data, outfile)
        logger.debug(f'Response file exported to {self.output_path}/{self.content_type}_{self.content_name}.json')

    def transform_df(self):
        # transform list of dictionary to dataframe
        self.df = pd.DataFrame(self.data, index=[0])
        logger.debug('Data transformed')

    def export_csv(self): 
        # Export formated csv file to local directory
        self.df.to_csv(f'{self.output_path}/{self.content_type}_{self.content_name}.csv', index=False)
        print(f'...\nResults were exported to {self.output_path} folder!')
        logger.debug(f'Data exported to {self.output_path}/{self.content_type}_{self.content_name}.csv')

