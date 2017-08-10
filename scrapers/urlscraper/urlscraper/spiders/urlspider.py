import scrapy


class urlSpider(scrapy.Spider):
    recipelist = open('recipelist.txt', 'wb')
    name = "url"
    def start_requests(self):
        urls = []
        urlfile = open('/home/adam/Personal Projects/urlscraper/urlscraper/spiders/urllist.txt', 'r')
        for line in urlfile:
            urls.append(line.strip())
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        recipes = []
        url = response.xpath('//*[@id="site"]/div[3]/div[3]/div/div/div[1]/div/div/div/section[2]/div/div/ul/li/a/@href')
        for link in url.extract():
            recipes.append(link)
        self.recipelist.write(recipes)

