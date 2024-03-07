import scrapy
import requests
from PyPDF2 import PdfReader
from io import BytesIO
import re


class PDFSpider(scrapy.Spider):
    name = 'pdf_spider'
    start_urls = ['https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1718-2022.pdf']

    def parse(self, response):
        # Request the PDF content
        pdf_response = requests.get(response.url)
        pdf_content = pdf_response.content

        # Extract fields from PDF content
        fields = self.extract_fields_from_pdf(pdf_content)

        # Output as JSON
        yield fields

    def extract_fields_from_pdf(self, pdf_content):
        # Create PDF file object
        pdf_file = BytesIO(pdf_content)

        # Create PDF reader object
        pdf_reader = PdfReader(pdf_file)

        # Extract text from each page
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()

        # Extracting values using regular expressions
        source_url = self.extract_value(text, "Source URL: (.+)")
        contract_type = self.extract_value(text, "Contract Type: (.+)")
        title = self.extract_value(text, "Title: (.+)")
        contract_number = self.extract_value(text, "Contract Number: (.+)")
        effective = self.extract_value(text, "Effective: (.+)")
        expiration = self.extract_value(text, "Expiration: (.+)")
        files = self.extract_value(text, "Files: (.+)")
        renewals_allowed = self.extract_value(text, "Renewals Allowed: (.+)")
        renewal_term = self.extract_value(text, "Renewal Term: (.+)")
        supplier_contacts = self.extract_value(text, "Supplier Contacts: (.+)")
        buyer_contacts = self.extract_value(text, "Buyer Contacts: (.+)")

        return {
            'source_url': source_url,
            'contract_type': contract_type,
            'title': title,
            'contract_number': contract_number,
            'effective': effective,
            'expiration': expiration,
            'files': files,
            'renewals_allowed': renewals_allowed,
            'renewal_term': renewal_term,
            'supplier_contacts': supplier_contacts,
            'buyer_contacts': buyer_contacts
        }

    def extract_value(self, text, pattern):
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
        else:
            return ""
