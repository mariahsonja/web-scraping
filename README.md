# Web Scraping

![Python](https://img.shields.io/badge/Python-3.8-brightgreen.svg)

In this repo I share some high level examples of how to "web scrap" and details of python most used libraries.

**What is Web Scraping?**

Web scraping, also know as web harvesting, web crawling or web data extraction is used for extracting data from websites. 

*"The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser."*

**The two step process**

- Systematically identify and download web pages
- Extract information from  the web pages

The most used python libraries for web scrapping are:

- **Scrapy:** It is used to do a big-scale web scraping and for automated tests.
- **Requests:** Requests is the most straight forward HTTP library. It's used with API tp contact. Requests allow the user to sent requests to the HTTP server and GET response back in the form of HTML or JSON response. It also allows the user to send POST requests to the server to modify or add some content.
- **Urllib:** It allows the developer to open and parse information from HTTP or FTP protocols.
- **Beautiful Soup:** Considered a parser library, it is used to extract information from XML and HTML files - specially good for not structured documents.
- **Selenium:** It is a web-driver, so it can be used to open a webpage, click on a button, and get results - data in javascript.

## Running Locally

### Environment Dependencies

- python `3.8`
- scrapy `2.5.0`
- requests `2.25.1`
- urllib3 `1.26.4`
- beautifulsoup4 `4.9.3`
- selenium `3.141.0`

### Building the Environment

Create new environment:

`conda env create --file environment.yml`

Activate the environment you just created:

`source activate web-scraper`

If you want to deactivate the environment:

`conda deactivate`

## Using Scrapy

Go to `scrapy` folder:

`cd scrapy`

Run the `scraper script`:

`scrapy runspider scraper.py`

## Using Requests
Go to `requests` folder:

`cd requests`

Run the following command:

`python requests_sample.py`

Enter a movie name:

`titanic`

## Using Urllib
Go to `urllib` folder:

`cd urllib`

Run the following command:

`python urllib_sample.py`

## Using Beautiful Soap
Go to `beautiful_soap` folder:

`cd beautiful_soap`

Run the following command:

`python beautiful_sample.py`

## Using Selenium
Go to `selenium` folder:

`cd selenium`

Run the following command:

`python selenium_sample.py`

**Note:** If you are on MAC, you may need to install `chromedriver`.

```
brew update
brew install chromedriver
```

### References

- [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)
- [Web Scraping](https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3)
- [Wikipedia](https://en.wikipedia.org/wiki/Web_scraping)
- [Towards Data Science](https://towardsdatascience.com/choose-the-best-python-web-scraping-library-for-your-application-91a68bc81c4f)
