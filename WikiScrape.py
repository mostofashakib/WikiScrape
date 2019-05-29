"""
Libraries imported: Requests, BeautifulSoup and csv
Requests: Requests is an Apache2 Licensed HTTP library which allows humans to automatically add query strings to URLS.
Beautiful Soup: Beautiful Soup is a Python package for parsing HTML and XML documents.
It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
Csv: CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or databas

Written by: Mostofa Adib Shakib
Language: Python 3

What does it do?
This Scrapper goes to wikipedia which has a list of US cities by population from which the scrapper picks the top 10 cities
by population and extracts data. After that the scrapper goes to their individual pages and collects a breakdown of data of 
different ethnic groups living in those cities.

"""

import requests
from bs4 import BeautifulSoup
import csv

"""
This creates a Wikipedia class from which we later create an instate
"""

class Wikipedia:
    BASE_URL = 'https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population'

    @staticmethod
    def get_html(url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML, return the
        text content, otherwise handels the exception and return None.
        """
        try:
            Wikipedia = requests.get(url, timeout = 10)
            Wikipedia.raise_for_status()
        except Exception:
            return
        Wikipedia = Wikipedia.content
        unicode_str = Wikipedia.decode('utf8')
        encoded_str = unicode_str.encode("ascii",'ignore')
        html = BeautifulSoup(encoded_str, 'html.parser')
        return html

    @staticmethod
    def clean_string(string):
        """
        This function  takes in a String as the only parameter and returns a clean String without unwanted elements in it.
        """
        new_string = string.replace('&nbsp', '')
        new_string = new_string.strip().replace('\ufeff','')
        new_string = new_string.replace('\xa0mi', '')
        new_string = new_string.replace('\xa0sq', '')
        new_string = new_string.replace('\xa0km2', '')
        new_string = new_string.replace('2018', '')
        new_string = new_string.replace('/n', '')
        new_string = new_string.replace('2016', '')
        new_string = new_string.replace('2010', '')
        new_string = new_string.replace('[c]', '')
        new_string = new_string.replace('(1 New York City)', '')
        new_string = new_string.replace('(2 Los Angeles)', '')
        new_string = new_string.replace('(3 Chicago)', '')
        new_string = new_string.replace('(4 Houston)', '')
        new_string = new_string.replace('(6 Phoenix)', '')
        new_string = new_string.replace('(7 San Antonio)', '')
        new_string = new_string.replace('(5 Philadelphia)', '')
        new_string = new_string.replace('(8 San Diego)', '')
        new_string = new_string.replace('(9 Dallas)', '')
        new_string = new_string.replace('(10 San Jose)', '')
        new_string = new_string.replace('[112]b122839862_gravity_restricts', '')
        new_string = new_string.replace('[109][110]', '')
        new_string = new_string.replace('[42]', '')
        new_string = new_string.replace('[43]', '')
        new_string = new_string.replace('[111]', '')
        new_string = new_string.replace('[44]', '')
        new_string = new_string.replace('[46]', '')
        new_string = new_string.replace('[29]', '')
        new_string = new_string.replace('[28]', '')
        new_string = new_string.replace('[30]', '')
        new_string = new_string.replace('[18]', '')
        new_string = new_string.replace('[35]', '')
        new_string = new_string.replace('[50]', '')
        new_string = new_string.replace('[23]', '')
        new_string = new_string.replace('[32]', '')
        new_string = new_string.replace('[52]', '')
        new_string = new_string.replace('[53]', '')
        new_string = new_string.replace('[48][49]', '')
        new_string = new_string.replace('[161]', '')
        new_string = new_string.replace('[116]', '')
        new_string = new_string.replace('[117]', '')
        new_string = new_string.replace('[118]', '')
        new_string = new_string.replace('[119]', '')
        new_string = new_string.replace('[27]', '')
        new_string = new_string.replace('[143]', '')
        new_string = new_string.replace('[144]', '')
        new_string = new_string.replace('[104]', '')
        new_string = new_string.replace('[105]', '')
        new_string = new_string.replace('[98]', '')
        new_string = new_string.replace('[97]', '')
        new_string = new_string.replace('[99]', '')
        new_string = new_string.replace('[65]', '')
        new_string = new_string.replace('[66]', '')
        new_string = new_string.replace('[67]', '')
        new_string = new_string.replace('[101]', '')
        new_string = new_string.replace('[103]', '')
        new_string = new_string.replace('(X)', 'n/a')
        new_string = new_string.replace('63.8[f]', '63.8%')
        new_string = new_string.replace('[102]', '')
        new_string = new_string.replace('[56]', '')
        new_string = new_string.replace('[160]', '')
        new_string = new_string.replace('[162]', '')
        new_string = new_string.replace('[251]', '')
        new_string = new_string.replace('[252]', '')
        new_string = new_string.replace('[249]', '')
        new_string = new_string.replace('[100]', '')
        new_string = new_string.replace('[f]', '')
        new_string = new_string.replace('Census racial', 'Racial')
        new_string = new_string.replace('[[103]]', '')
        return new_string

    @staticmethod
    def clean_link(link):
    	""" This function takes in a link as the only parament and removes any unwanted links from it
    	"""
    	new_links = [i for i in link if '/California' not in i]
    	new_links = [i for i in new_links if '/Illinois' not in i]
    	new_links = [i for i in new_links if '/Arizona' not in i]
    	new_links = [i for i in new_links if '/Pennsylvania' not in i]
    	new_links = [i for i in new_links if 'state' not in i]
    	new_links = [i for i in new_links if '/Texas' not in i]
    	new_links = [i for i in new_links if '#cite_note' not in i]
    	return new_links

    @staticmethod
    def get_links(self):
        """
        This function gets the souce link of the top 10 cities in the US inorder to collect further data
        """
        html = Wikipedia.get_html(Wikipedia.BASE_URL)
        parsed_data = []
        for i in html.find_all(name='table', class_='wikitable'):
            for j in i.find_all(name='td'):
                for link in j.find_all('a', href=True):
                    parsed_data.append(link['href'])
        parsed_data = parsed_data[:29]
        decade_links = ['https://en.wikipedia.org' + i for i in parsed_data]
        new_links = [i for i in decade_links if 'geohack' not in i]
        new_links = Wikipedia.clean_link(new_links)
        return new_links

    @staticmethod
    def get_link_details(link):
        """
        This function class the ethnic information of a single city.
        """
        html = Wikipedia.get_html(link)
        stories = []
        if html:
            table = html.find('table', attrs={"class": "wikitable sortable collapsible"})
            for i in table.find_all('tr'):
                temp = Wikipedia.clean_string(i.text)
                stories.append(temp)
            return stories

    @staticmethod
    def details(self):
        """
        This function gets the ethnic information about all the top 10 cities and appends them to a list
        """
        topic_url = Wikipedia.get_links(self)
        history_data = []
        for i in topic_url:
            temp = Wikipedia.clean_link(Wikipedia.get_link_details(i))
            history_data.append(temp)
        return history_data
        

    def web_scrape(self):
        """
        This is the main function which uses the above utility functions to scrape data and writes them to a csv file
        """
        data = Wikipedia.details(self)
        html = Wikipedia.get_html(Wikipedia.BASE_URL)
        parsed_table_data = []
        table = html.find("table", attrs={"class": "wikitable sortable"})
        rows = table.findAll('tr')
        with open('output.csv', 'w', encoding='utf8') as f:
            write = csv.writer(f, delimiter=',')
            for row in rows:
                children = row.findChildren(recursive=False)
                row_text = []
                for child in children:
                    clean_text = child.text
                    clean_text = Wikipedia.clean_string(clean_text)
                    row_text.append(clean_text)
                parsed_table_data.append(row_text)
            for line in parsed_table_data[:11]:
                 write.writerow(line)
            for a in data[:25]:
                write.writerow(a)
        return parsed_table_data[:11]


"""
This instantiates and object ob of class Wikipedia and starts the web scraping process
"""
ob = Wikipedia()
ob.web_scrape()