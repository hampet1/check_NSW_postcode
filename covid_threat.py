import requests
from bs4 import BeautifulSoup
import pandas as pd




def scrape_table_of_regions
    """
    scraping oficial postcode website for NSW (Australia)
    """
    base_site = "https://www.training.nsw.gov.au/about_us/postcodes_byregion.html"

    # connect to webpage
    r = requests.get(base_site)
    # To extract all tables on a page, use pandas.read_html()
    # It takes either raw HTML or the page URL as a parameter
    # list of tables - this one is at index 0
    tables = pd.read_html(base_site)

    table_of_sites = tables[0]
    # first create dictionary
    return table_of_sites

def match_regions_with_postbox():
    """
    based on scraped data match sites and poboxes to reveal regions in lockdown
    """
    scraped_table = scrape_table_of_regions()
    # initialize dictionary
    all_nsw_sites = {i:''for i in range(2000,2915)}

    length = 0
    while length < len(tables[0]):
        first, second = 0,0
        if len(table_of_sites['Postcode Range'].iloc[length]) == 11:
            first, second = int(table_of_sites['Postcode Range'].iloc[length][0:4]), int(table_of_sites['Postcode Range'].iloc[length][7:11])
        else:
            first = int(table_of_sites['Postcode Range'].iloc[length][0:4])
            
        if first and second:    
            for i in all_nsw_sites.keys():
                if  i >= first and i <= second:
                    all_nsw_sites[i] = table_of_sites['Training Services NSW Centre'].iloc[length]  
        else:
            all_nsw_sites[first] = table_of_sites['Training Services NSW Centre'].iloc[length]  

        length += 1
    return all_nsw_sites



    
def enter_postcode(postcode):

    postcode = int(postcode)
    if postcode >= 2000 and postcode <=2914:
        all_nsw_sites = match_regions_with_postbox()
        result = all_nsw_sites[postcode]
        if result in ['Central & Northern Sydney', 'Southern & South Western Sydney',
           'Western Sydney & Blue Mountains', 'Hunter & Central Coast',
           'Illawarra & South East NSW']:
            return f"this is {result} high change of being in lockdown"
        else:
            return "you can let him in, low covid threat"
    else:
        raise Exception("the postcode is out of range, the postcode must be between 2000 and 2914 included")

        



    
if __name__ == '__main__':
    try:
        postcode = int(input("enter a postcode: "))
        print(enter_postcode(postcode))
    except ValueError:
        print("the input is not integer")