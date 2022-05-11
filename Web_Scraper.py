import requests
import pandas as pd

website = 'https://3g8hkyvn3l.execute-api.us-east-1.amazonaws.com/production/product?size=6&page=1'
page = requests.get(website)
product_df = pd.DataFrame(page.json()['products'])

# Exercise 1
def get_product_info(brand):
    """Retreive product information for a given brand"""
    temp = []
    brand_df = pd.DataFrame()

    brands = product_df['brand'].values

    if brand in brands:
        temp.append(brand)
    else:
        print("That brand isn't carried.")
            
    brand_df = pd.concat([brand_df, product_df.loc[product_df['brand'].isin(temp)]], ignore_index=True, sort = False)
    brand_df[['productId', 'name', 'currentPrice']].to_csv('Exercise1.csv', encoding='utf-8', index = False)
    return(print("Your brand file is saved."))


# Exercise 2
id_list = [296804,198765,750518,688028,127853,261549,382587,389471,251184,601484]

def check_inventory(id_list):
    """Check the inventory for a list of products"""
    inventory_df = pd.DataFrame() 
    temp_df = product_df[['productId', 'inStock']]
    temp_df = temp_df.astype({'productId': 'str'})
    temp = []
    for item in id_list:
        item = str(item)
        if item in temp_df['productId'].values:
            temp.append(item)
        else:
            inventory_df = inventory_df.append({'productId': item, 'inStock': 0}, ignore_index = True)
    inventory_df = pd.concat([inventory_df, temp_df.loc[temp_df['productId'].isin(temp)]], ignore_index=True, sort = False)
    inventory_df.to_csv('Exercise2.csv', encoding='utf-8', index = False)
    return(print("Your product ID file is saved."))


if __name__ == '__main__':
    get_product_info('Foo INC')
    check_inventory(id_list)