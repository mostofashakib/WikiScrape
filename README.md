# WikiScrape

This Scraper goes to Wikipedia which has a list of US cities by population from which the scrapper picks the top 10 cities by population and extracts data. After that, the scraper goes to their individual pages and collects a breakdown of data of different ethnic groups living in those cities. This CSV file can be uploaded to a BigQuery Google Data Analytics tool to do Data Analysis on the top 10 cities in the US.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See 
what you need to have in order to get this scrapper to work.

### Prerequisites

What things you need to in order to get this scrapper to work.

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

Installing BeautifulSoup4 and Requests using Python 3 commandline(pip)

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
* [Python3](https://www.python.org/downloads/)

## Authors

Mostofa Adib Shakib

## License

This project is licensed under the MIT License.
