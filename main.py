from modules.extract import omdb_api
from modules.functions import string2float, export_csv, mk_dir

from dotenv import load_dotenv
import os

def main(type, movie_name):
    # LOAD ENV VARIABLES
    load_dotenv() # take environment variables from .env file
    OUTPUT_DIR = os.getenv('OUTPUT_DIR')
    API_KEY = os.getenv('API_KEY')
    # Create output path (Directory) if doesnt exists
    mk_dir(OUTPUT_DIR)

    # API CALL
    omdb = omdb_api(API_KEY, type, movie_name, output_path=OUTPUT_DIR)
    omdb.api_extract()
    results = omdb.format() # store dict results

    # EXPORT CSV
    export_csv(results, movie_name, OUTPUT_DIR)

if __name__ == '__main__':
    type='movie'
    movie_name='inception'
    main(type, movie_name)

