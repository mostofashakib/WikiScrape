# WikiScrape

What does it do?
This Scrapper goes to wikipedia which has a list of US cities by population from which the scrapper picks the top 10 cities
by population and extracts data. After that the scrapper goes to their individual pages and collects a breakdown of data of 
different ethnic groups living in those cities. This csv file can be uploaded to a BigQuery Google Data Ananlytics tool to do Data Analysis on the
top 10 cities in the US.

Libraries imported: Requests, BeautifulSoup and csv
Requests: Requests is an Apache2 Licensed HTTP library which allows humans to automatically add query strings to URLS.
Beautiful Soup: Beautiful Soup is a Python package for parsing HTML and XML documents.
It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
Csv: CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or databas

Written by: Mostofa Adib Shakib
Language: Python 3
