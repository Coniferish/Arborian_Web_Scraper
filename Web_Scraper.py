import requests
from bs4 import BeautifulSoup
import pandas as pd
import ast

website = 'https://3g8hkyvn3l.execute-api.us-east-1.amazonaws.com/production/product?size=6&page=1'
page = requests.get(website)
soup = BeautifulSoup(page.content, 'html.parser')
p_soup = soup.prettify()
# print(p_soup)

d_soup = ast.literal_eval(p_soup)
# print(d_soup.keys())
# print(d_soup.values())
# for product in d_soup['products']:
#     #print(product)
#     for key, value in product.items():
#         print('key =', key,'\n  value =', value)

product_df = pd.DataFrame(d_soup['products'])
# print(product_df.head())

# Exercise 1
def product_info(brand):
    """Retreive product information for a given brand"""
    temp = []
    brand_df = pd.DataFrame() # Create empty dataframe

    if brand in product_df['brand'].values: # Check if a product ID is already in the master df
        temp.append(brand)
    else:
        print("That brand isn't carried.")
            
    brand_df = pd.concat([brand_df, product_df.loc[product_df['brand'].isin(temp)]], ignore_index=True, sort = False) # Concatenate the dataframes for new and existing products
    # print(brand_df[['productId', 'name', 'currentPrice']])
    brand_df[['productId', 'name', 'currentPrice']].to_csv('Exercise1.csv', encoding='utf-8', index = False)
    return(print("Your brand file is saved."))

product_info('Foo INC')

# Exercise 2
idlst = [296804,198765,750518,688028,127853,261549,382587,389471,251184,601484]

def inventory_check(lst):
    """Check the inventory for a list of products"""
    inventory_df = pd.DataFrame() # Create empty dataframe
    temp_df = product_df[['productId', 'inStock']] # Create new dataframe with relevant columns from master df
    temp_df = temp_df.astype({'productId': 'str'})
    temp = []
    # print(temp_df['productId'].dtypes)
    for item in lst:
        item = str(item)
        # print(type(item))
        if item in temp_df['productId'].values: # Check if a product ID is already in the master df
            temp.append(item)
        else:
            inventory_df = inventory_df.append({'productId': item, 'inStock': 0}, ignore_index = True) # Add new product ID to dataframe if it didn't exist in master df
    inventory_df = pd.concat([inventory_df, temp_df.loc[temp_df['productId'].isin(temp)]], ignore_index=True, sort = False) # Concatenate the dataframes for new and existing products
    inventory_df.to_csv('Exercise2.csv', encoding='utf-8', index = False) # Save CSV file
    return(print("Your product ID file is saved."))

inventory_check(idlst)