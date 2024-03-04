import scrapy
from pathlib import Path


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["procurement.vt.edu"]
    start_urls = ["https://contractsearch.procurement.vt.edu/"]


    def start_requests(self):
        urls = [
            "https://contractsearch.procurement.vt.edu/?page=2",
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"data-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

