# Python- Data Management and Analysis in Avocado Supply Chain

## Table of Contents

- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Findings](#findings)

### Project Overview
---

<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.Data-Management-in-Avocado-Supply-Chain/blob/main/Visuals/Avocados.jpeg"
 alt="Alfred Nobel">
</p>

This data management project in **Python** is intended to conduct a supply chain analysis of *three key ingredients* required in the making of **a high-quality avocado toast**, namely:

- Avocado
- Olive Oil
- Sourdough
  
The fundamental goal of this data management work is to highlight some aspects of the complex supply chain taking part in producing a simple and single dish.

### Data Sources

Three key pairs of datasets were utilised in this project for each of the three key ingredients. For instance, if we are to take into account avocados, 

- avocado.csv has detailed information about *the avocados*, including a variety of its products, nutritional info, country of origin and destination and so on/
- relevant_avocado_categories.csv merely contains the category tags of interest related to *the avocados*. 


### Tools

- [Anaconda Navigator: ](https://www.anaconda.com/download)
  - To access the Jupyter Notebook for **Python**


### Data Preparation

The following data preparation tasks were undertaken:

1. All datasets were first inspected before deciding how to load each dataset:
  - This involved determining which **read function**, available in Pandas or in the generic Python library, would suit best and what parameters (i.e., delimiters, headers, spacing) the pre-determined functions shall have taken.

2. Afterwards, seeing that the contents of all .csv files' are relatively large, a subset of columns were  pre-emptively utilised to be passed to each DataFrame to scale down the size.

3. In order to answer numerious questions, a variety of data manipulation tasks also needed to be completed (e.g., splitting some category tags of a string type for each row and passing them onto another DataFrame column as a list to traverse through)


### Exploratory Data Analysis

As the fundamental scope of the project was to zero in on the data management side on the avocado supply chain, limited exploratory data analysis work went into the equation.

Along these lines, the analysis sought to answer the following question:

- What are the most common country(s) of origin for?
  - Avocado
  - Olive Oil
  - Sourdough


### Data Analysis

While coding, what fascinated me most was to recognise that I would need to compare the category tags of our csv files for each food item to the content of the relevant tags found in txt files, resorting to a out-of-the-box technique.

The following is only to demonstrate how I initially prepared our main dataset for a food item.

```python
# To read the main dataset for avocados

avocado = pd.read_csv('avocado.csv', sep='\t')

avocado_relevant_cols = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands',
                        'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins',
                        'origins_tags']

avocado = avocado[avocado_relevant_cols] #Subsetting technique

# To read the reference category tags for avocados

file = open('relevant_avocado_categories.txt', "r")
avocado_reference_file  = file.read().splitlines() # To split a string into a list after reading
file.close()
```
Afterwards, I managed to write the following piece of code designed to filter avocado data based on the reference data sourced from its txt file, applying a function to the relevant column of the main dataset of each food item and using the any() function to traverse through the reference list of category tags. 

```python
avocado = avocado[avocado['categories_item_list'].apply(lambda passed_list_from_avocado:
                                      any([value for value in passed_list_from_avocado if value in avocado_reference_file]))]
```

### Findings

The critical analysis results are summarised as follows:

1. XX


### Limitations


### References

1. [DataCamp](https://www.datacamp.com/)
2. 
