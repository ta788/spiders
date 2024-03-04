import scrapy
from pathlib import Path


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]


    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        detail = {}

        #Save the content as file
        #Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        cards = response.css(".product_pod")
        for card in cards:
            title = card.css("h3>a::text").get()
            print(title)

            rating = card.css(".star-rating").attrib["class"].split(" ")[1]
            print(rating)

            image = card.css(".image_container img")
            print(image.attrib["src"])


            price = card.css(".price_color::text").get()
            print(price)


            availability = card.css(".availability")

            if len(availability.css(".icon-ok")) > 0:
                inStock = True
            else:
                inStock = False



