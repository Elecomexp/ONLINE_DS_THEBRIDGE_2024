import time

import numpy as np
import pandas as pd
import requests


def fetch_data_aemet(url, headers, querystring, retries = 3, wait_time = 65):
    """
    Fetch data from the AEMET API with retry logic for rate limiting.

    This function sends a GET request to the specified AEMET API endpoint and handles the response. 
    If the request is rate limited (HTTP 429), it waits for a specified amount of time before 
    retrying. The function will retry the request up to the specified number of retries. If the
    request is successful, the data is returned as a pandas DataFrame.

    Parameters
    ----------
    url : str
        The URL of the AEMET API endpoint.  
    headers : dict
        A dictionary of HTTP headers to send with the request.
    querystring : dict      
        A dictionary of query parameters to send with the request.
    retries : int, optional     
        The number of times to retry the request if rate limited. Default is 3.
    wait_time : int, optional       
        The number of seconds to wait before retrying if rate limited. Default is 70.

    Returns
    -------
    pd.DataFrame: A pandas DataFrame containing the response data if the request is successful.

    Raises
    ------
    requests.exceptions.HTTPError: If an HTTP error other than rate limiting occurs.
    KeyError: If the 'datos' key is not found in the JSON response.
    """
    for attempt in range(retries):
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            response.raise_for_status()  # Raise an exception for HTTP errors 4xx/5xx
            print('Request Status Code: ', response.status_code)
            # print('Request Info: ', response.json())
        
            response = requests.get(response.json()['datos'])
            print('Data Accessing Status code: ', response.status_code)
            # print('Data Info: ', response.json())
            
            return pd.DataFrame(response.json())
            
        except KeyError:
            print('Data Info: ', response.json())
            break
        
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 429:  # Requests limit exceeded
                print(f'Requests limit exceeded. Waiting {wait_time} seconds before retrying...')
                time.sleep(wait_time) 
            else:
                print(f'Error HTTP: {http_err}')  # Handle other HTTP errors
                break 
    