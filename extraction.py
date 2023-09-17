import pandas as pd
import requests

def extract():
    # Make the API request
    response = requests.get('https://api.apify.com/v2/datasets/PwUQCqgKsYFs8o1If/items?token=apify_api_9vdZqCoRCFP9pv9RomI1D837ZTOAWY0B5dLt')  
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response JSON into a Python dictionary
        extracted_data = response.json()
        return extracted_data  # Return the JSON data

    else:
        print('Failed to retrieve data from the API.')

# Extract data from the API
api_data = extract()

# Create a DataFrame from the extracted JSON data
dataframe = pd.DataFrame(api_data)
dataframe = dataframe[['title', 'city','address','phone','textTranslated','publishedAtDate']]