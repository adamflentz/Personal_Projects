import scrapy
import sqlite3
import json
from ..items import RecipescraperItem


class recipeSpider(scrapy.Spider):
    name = "recipe"
    recipes = []
    database = "/home/adam/database/recipedb.sqlite3"
    conn = sqlite3.connect(database)
    c = conn.cursor()

    def start_requests(self):
        urls = []
        urlfile = open('/home/adam/Personal Projects/scrapers/urlscraper/recipelist.txt', 'r')
        for line in urlfile:
             urls.append(line.strip())
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = RecipescraperItem()
        item['name'] = response.css('section.o-AssetTitle:nth-child(2) > h1:nth-child(1) > span:nth-child(1)::text').extract()[0].strip()
        try:
            item['author'] = response.css('.attribution > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1) > a:nth-child(1)::text').extract()[0].strip().encode(encoding='UTF-8')
        except:
            item['author'] = "Unknown"
        item['ingredients'] = response.css('div.o-Ingredients__m-Body:nth-child(3) > ul > li > label::text').extract()
        for ingredient in item['ingredients']:
            ingredient.encode(encoding='UTF-8')
        ingredientstr = json.dumps(item['ingredients'])
        try:
            item['recipeyield'] = response.css('div.l-Columns:nth-child(2) > section:nth-child(2) > section:nth-child(2) > dl:nth-child(1) > dd:nth-child(2)::text').extract()[0].strip().encode(encoding='UTF-8')
        except:
            item['recipeyield'] = "Unknown"
        try:
            item['difficulty'] = response.css('section.o-RecipeInfo:nth-child(4) > dl:nth-child(1) > dd:nth-child(2)::text').extract()[0].strip().encode(encoding='UTF-8')
        except:
            item['difficulty'] = "Unknown"
        try:
            item['totaltime'] = response.css('div.l-Columns:nth-child(2) > section:nth-child(1) > div:nth-child(1) > section:nth-child(1) > dl:nth-child(1) > dd:nth-child(2)::text').extract()[0].strip().encode(encoding='UTF-8')
        except:
            item['totaltime'] = "Unknown"
        try:
            item['activetime'] = response.css('div.l-Columns:nth-child(2) > section:nth-child(1) > div:nth-child(1) > section:nth-child(1) > dl:nth-child(1) > dd:nth-child(4)::text').extract()[0].strip().encode(encoding='UTF-8')
        except:
            item['activetime'] = "Unknown"
        item['directions'] = response.xpath('//*[@class="o-Method__m-Body"]/p//text()').extract()
        with open('directioncleaner.txt', 'wb') as directions:
            for i in item['directions']:
                directions.write(i.encode(encoding='UTF-8'))

        directionlist = []
        with open('directioncleaner.txt', 'rb') as i:
            for line in i:
                line = line.replace("\n", "").strip()
                if line != '':
                    directionlist.append(line)
        directionstr = " ".join(directionlist).decode(encoding='UTF-8')
        self.c.execute('''INSERT INTO recipe (name, author, ingredients, recipeyield, difficulty, totaltime, activetime, directions) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (item['name'], item['author'], ingredientstr, item['recipeyield'], item['difficulty'], item['totaltime'], item['activetime'], directionstr))
        self.conn.commit()




