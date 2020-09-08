# Display Reference Webpage
class References(scrapy.Spider):
    name = "Display References"
    start_urls = ['http://172.18.58.238/creative/']
# Create references.json in directory
    open("Output References\\references.json", 'w').close()

    def parse(self, response):
# Open references.json folder and append its results into references.json
        References = open("Output References\\references.json", 'a')
        for link in response.css('a'):
            link_results = link.css('a::attr(href)').get()
            References.write(str({'References': link_results}) + "\n")
        References.close()

#To recurse next page
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse