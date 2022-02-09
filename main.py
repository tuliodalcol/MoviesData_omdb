from modules.etl import omdb_api
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

def main(content_type, content_name) -> None:
    '''
        Function 
        1. extracts data from omdb api
        2. formats the raw data and get it flatten
        3. transform flatten list of dictionary to a dataframe
        4. export data as CSV to local directory
    '''
    # LOAD ENV VARIABLES
    load_dotenv() # take environment variables from .env file
    OUTPUT_DIR = os.getenv('OUTPUT_DIR')
    API_KEY = os.getenv('API_KEY')

    # EXTRACT DATA
    logger.info('Started program execution')
    omdb = omdb_api(API_KEY, content_type, content_name, output_path=OUTPUT_DIR)
    omdb.api_extract()

    # TRANSFORM DATA
    omdb.format() 
    omdb.transform_df()
    
    # LOAD CSV
    omdb.export_csv()
    logger.info('Finished program execution')
    
if __name__ == '__main__':
    content_type = input("What is the content type ? (Movie/Series) ")
    content_name = input("What is the content name ? ")
    main(content_type, content_name)


