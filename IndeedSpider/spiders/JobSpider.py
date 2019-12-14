import scrapy
from IndeedSpider.items import Job
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
from time import sleep

class JobSpider(scrapy.Spider):

    name = "jobs"
    allowed_domains = [
    'www.indeed.com'
    ]

    def __init__(self, position=None, city=None, state=None, *args, **kwargs):
        super(JobSpider, self).__init__(*args, **kwargs)
        query = '?q='+'+'.join(position.split(' ')) + '&l=' +city+ '%2C+' +state
        self.start_url = 'https://www.indeed.com/jobs'+ query

    def start_requests(self):
        urls = [self.start_url]
        #add urls for next pages
        for i in range(10,80,10):
            urls.append(urls[0] + '&start' + str(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        #get all links to job pages
        links = response.xpath(".//div[@class='title']/a/@href").extract()
        base_url = "https://www.indeed.com"
        for link in links:
            sleep(2)
            yield scrapy.Request(url=(base_url + link), callback=self.parsePage)


    def parsePage(self, response):
        #parse job page and create job item
        job = Job()

        job["title"] = response.xpath("//h3[@class='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title']/text()").extract()
        try:
            job["employer"] = response.xpath("//div[@class='jobsearch-InlineCompanyRating icl-u-xs-mt--xs  jobsearch-DesktopStickyContainer-companyrating']/div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']/descendant-or-self::*/text()").extract()[0]
        except:
            job["employer"] = response.xpath("//div[@class='jobsearch-InlineCompanyRating icl-u-xs-mt--xs  jobsearch-DesktopStickyContainer-companyrating']/div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']/text()").extract()

        job["employer_link"] = response.xpath("//div[@class='jobsearch-InlineCompanyRating icl-u-xs-mt--xs  jobsearch-DesktopStickyContainer-companyrating']/div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']/a/@href").extract()
        job["rating"] = response.xpath("//div[@class='sjcl']/span[@class='ratingsDisplay']/a/span/text()").extract()
        job["location"] = response.xpath("//div[@class='jobsearch-InlineCompanyRating icl-u-xs-mt--xs  jobsearch-DesktopStickyContainer-companyrating']/div/text()").extract()[-1]
        job["salary"] = response.xpath("//div[@class='jobsearch-JobMetadataHeader-item ']/span/text()").extract()
        job["date"] = response.xpath("//div[@class='jobsearch-JobMetadataFooter']/text()").extract()
        job["description"] = response.xpath("//div[@class='jobsearch-jobDescriptionText']/descendant-or-self::*/text()").extract()

        job["url"] = response.url

        yield job

