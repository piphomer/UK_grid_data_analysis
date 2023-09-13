# Python3
# https://bscdocs.elexon.co.uk/guidance-notes/bmrs-api-and-data-push-user-guide

import requests
import pandas as pd

ELEXON_API_KEY = 'vgoj23z4aqj0q7p'

def get_request():

    url = "https://api.bmreports.com/BMRS/B1630/v1?APIKey={}&SettlementDate=2023-06-01&Period=1&ServiceType=CSV".format(ELEXON_API_KEY)

    r = requests.get(url=url)

    results = r.text.split("*")[-1]

    results = results.split("\n")[0:-1]


    results_df = pd.DataFrame(results)

    # Make top row the column headers
    results_df.columns = results_df.iloc[0]
    results_df = results_df[1:]

    print(results_df)

    return r

if __name__ == '__main__':

    get_request()
