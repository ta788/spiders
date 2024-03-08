# PDF Spider

This is a Scrapy spider designed to extract specific fields from PDF documents hosted online publically.
It uses PyPDF2 library to extract text from PDFs and regular expressions to parse the text and extract specific fields.

## Requirements

- Python 3.x
- Scrapy
- Requests
- PyPDF2

#Install dependencies using:

pip install scrapy requests pypdf2

#Run the spider using the following command:

scrapy crawl pdf_spider -o output.json


