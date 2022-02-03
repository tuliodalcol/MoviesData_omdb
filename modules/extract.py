from modules.functions import string2float, export_response

import pandas as pd
import numpy as np
import requests
import json


class omdb_api:
    def __init__(self, api_key, type, movie_name, output_path):
        self.api_key = api_key
        self.type = type
        self.movie_name = movie_name
        self.output_path = output_path

    def api_extract(self):
        '''
        Parameters
        ----------
            type : movie, series, episode
            t : Movie title to search for
        Returns
        -------
        '''
        url_get = f'http://www.omdbapi.com/?apikey={self.api_key}&type={self.type}&t={self.movie_name}'

        r = requests.get(url_get)
        self.data = r.json()
        export_response(self.data, self.movie_name, self.output_path)

        if self.data['Response'] != 'True':
            error = self.data['Error']
            raise Exception(f'{error}')
    
    def format(self):
        rating_values = [string2float(i['Value']) for i in self.data['Ratings']]
        self.data['avg_rate'] = round(np.mean(rating_values), 2)
        del self.data["Ratings"]
        del self.data["Response"]
        return self.data




             
