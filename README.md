# WikiScrape

This Scrapper goes to wikipedia which has a list of US cities by population from which the scrapper picks the top 10 cities
by population and extracts data. After that the scrapper goes to their individual pages and collects a breakdown of data of 
different ethnic groups living in those cities. This csv file can be uploaded to a BigQuery Google Data Ananlytics tool to do Data Analysis on the top 10 cities in the US.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

Libraries imported: Requests, BeautifulSoup and csv
```
Requests: Requests is an Apache2 Licensed HTTP library which allows
humans to automatically add query strings to URLS.
```

```
Beautiful Soup: Beautiful Soup is a Python package for parsing HTML and XML documents.
It creates a parse tree for parsed pages that can be used to extract data from HTML,
which is useful for web scraping.

```

Csv: CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database

### Installing

Installing BeautifulSoup4 and Requests using Python 3 commandline

```
pip3 install bs4 
```

```
pip3 install requests 
```

End with an example of getting some data out of the system or using it for a little demo


## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](https://2.python-requests.org/en/master/)

## Authors

Mostofa Adib Shakib

## License

This project is licensed under the MIT License.
