import requests
from bs4 import BeautifulSoup
import pandas as pd
import ast

website = 'https://3g8hkyvn3l.execute-api.us-east-1.amazonaws.com/production/product?size=6&page=1'
page = requests.get(website)
soup = BeautifulSoup(page.content, 'html.parser')
pretty_soup = soup.prettify()

d_soup = ast.literal_eval(pretty_soup)

product_df = pd.DataFrame(d_soup['products'])

# Exercise 1
def product_info(brand):
    """Retreive product information for a given brand"""
    temp = []
    brand_df = pd.DataFrame()

    if brand in product_df['brand'].values:
        temp.append(brand)
    else:
        print("That brand isn't carried.")
            
    brand_df = pd.concat([brand_df, product_df.loc[product_df['brand'].isin(temp)]], ignore_index=True, sort = False)
    brand_df[['productId', 'name', 'currentPrice']].to_csv('Exercise1.csv', encoding='utf-8', index = False)
    return(print("Your brand file is saved."))

product_info('Foo INC')

# Exercise 2
idlst = [296804,198765,750518,688028,127853,261549,382587,389471,251184,601484]

def inventory_check(lst):
    """Check the inventory for a list of products"""
    inventory_df = pd.DataFrame() 
    temp_df = product_df[['productId', 'inStock']]
    temp_df = temp_df.astype({'productId': 'str'})
    temp = []
    for item in lst:
        item = str(item)
        if item in temp_df['productId'].values:
            temp.append(item)
        else:
            inventory_df = inventory_df.append({'productId': item, 'inStock': 0}, ignore_index = True)
    inventory_df = pd.concat([inventory_df, temp_df.loc[temp_df['productId'].isin(temp)]], ignore_index=True, sort = False)
    inventory_df.to_csv('Exercise2.csv', encoding='utf-8', index = False)
    return(print("Your product ID file is saved."))

inventory_check(idlst)