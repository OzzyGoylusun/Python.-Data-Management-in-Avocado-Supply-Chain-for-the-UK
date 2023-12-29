#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd

# 1. Defining three different functions to avoid various repetitive tasks:

# After working through the project, I realised that if I were to bundle all fundamental operations under a
# few functions, that would help with the efficiency as well as producing a cleaner code.


# In[48]:


# 1.1 Defining two separate Read File functions, namely for .CSV and .TXT files:


# Please note that before defining these two functions, all datasets were first inspected and then configured
# accordingly!

def read_and_subset_csv_file(filepath):
    
    # In this project, the type of a file passed into this function represents a variety of information 
    # about a food item, including its category tags and country of origin.
    
    # As such, the return product of this function for a food item will represent its main dataset.
    
    
    # Reading an incoming .csv file...
    
    #'Low_Memory = False' means all columns will be read first before determining its data types.
    #'Sep='\t' means that 'Tab' is our delimiter, instead of a comma or a semicolon.
    
    csv_content = pd.read_csv(filepath, sep='\t', low_memory=False)
    

    # Preparing for subsetting all DataFrames into these columns only
    
    csv_rel_cols_for_key_ings = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 
                                                'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 
                                                'labels_tags', 'countries', 'countries_tags', 'origins', 
                                                'origins_tags']
    
    
    # Subsetting the incoming csv file before returning
    
    csv_content = csv_content[csv_rel_cols_for_key_ings]
    
    return csv_content



def read_text_file(filepath):
    
    # In this project, the type of a file passed into this function represents the accurate category tags of 
    # interest for a food item, for our research purposes.
    
    
    # Reading an incoming .txt file...
    
    file = open(filepath, "r")
    
    
    # Splitlines() function helps splitting strings into a list as a separate list item.
    
    rel_cat = file.read().splitlines() 
    
    # This is very important as we would then need to traverse through this reference list 
    # to find the matching category tags between the two sets for, for instance, avocados. 
    
    # In other words, to be able to classify an avocado product as avocado, the 'categories_tags' 
    # column of the main dataset of a food item must have at least 1 matching tag with its appropriate 
    # reference list.
    

    file.close()
    
    return rel_cat


# In[49]:


# 1.2 Defining a function designed to Manipulate and Analyse all of our DataFrames 
# for Avocado, Olive Oil and Sourdough data


def top_origin_country_identifier_for_UK(main_file, reference_file):
    
    # As there are multiple category tags for many rows/records in our main dataset, we are creating a new column 
    # out of 'categories_tags' and splitting each tag to be stored as a separate list item in the new column.
    
    main_file['categories_item_list'] = main_file.categories_tags.str.split(',')
    
    
    # Dropping resulting rows that have null values in the new column
    
    main_file = main_file.dropna(subset='categories_item_list')
    
    
    # Filtering rows that only have matching category tags from the reference list
    
    main_file = main_file[main_file['categories_item_list'].apply(lambda passed_list: 
                                                                  any([value for value in passed_list if value 
                                                                       in reference_file]))]
    
    
    # Filtering the data only for the UK
    
    main_file_uk = main_file[main_file['countries'] == 'United Kingdom']
    
    
    # Finding the top origin country for a food item, along with conducting some string manipulation tasks
    
    ingredient_origin_count = main_file_uk['origins_tags'].value_counts()
    top_ingredient_origin_country = ingredient_origin_count.index[0][3:].capitalize()
    
    return top_ingredient_origin_country



# In[50]:


# 2.2 Activating our army of ingredients by loading the data into numerious DataFrames


avocado_info = read_and_subset_csv_file('Datasets/avocado.csv') # Main Avocado DataFrame

olive_oil_info = read_and_subset_csv_file('Datasets/olive_oil.csv')

sourdough_info = read_and_subset_csv_file('Datasets/sourdough.csv')


# 2.2 Loading our reference category lists for each key ingredient

avocado_ref_tags = read_text_file("Datasets/relevant_avocado_categories.txt") # Only for a Point of Reference

olive_oil_ref_tags = read_text_file("Datasets/relevant_olive_oil_categories.txt")

sourdough_ref_tags = read_text_file("Datasets/relevant_sourdough_categories.txt")


# In[51]:


# 3. Identifying the top countries of origin for all the three (3) key ingredients being imported to the UK,
# which we would like to work on as part of this project.

# For instance, passing both our main dataset and reference dataset of category tags for Avocado into our 
# custom function down below:

top_avocado_origin_for_UK = top_origin_country_identifier_for_UK(avocado_info, avocado_ref_tags)
print(f"The majority of avocados for the UK are sourced from {top_avocado_origin_for_UK}.")
print('\n')


top_olive_oil_origin_for_UK = top_origin_country_identifier_for_UK(olive_oil_info, olive_oil_ref_tags)
print(f"The majority of olive oil for the UK is sourced from {top_olive_oil_origin_for_UK}.")
print('\n')


top_sourdough_origin_for_UK = top_origin_country_identifier_for_UK(sourdough_info, sourdough_ref_tags)


# Undertaking a number of string manipulation tasks for our top country of origin for Sourdough down below:

if 'United' in top_sourdough_origin_for_UK:
    
    word1, word2 = top_sourdough_origin_for_UK.split('-')                                              
    word2 = word2.capitalize()
    top_sourdough_origin_for_UK = word1 + ' ' + word2
    
    print(f"The majority of sourdough for the UK is sourced from the {top_sourdough_origin_for_UK}.")

