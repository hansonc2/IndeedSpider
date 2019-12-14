# IndeedSpider
Scrapy spider for retrieving job postings from Indeed.com

##Requirements
scrapy==1.8.0

##Usage 
'''
scrapy crawl jobs -a position='software engineer' -a city='chicago' -a state='IL'
'''
Output to csv:
'''
scrapy crawl jobs -a position='software engineer' -a city='chicago' -a state='IL' -o jobs.csv
'''

##Job Fields
*title
*employer
*employer_link
*rating 
*location
*salary
*date
*url
*description

##Warning
Indeed's robots.txt file https://www.indeed.com/robots.txt -!automatic allows for crawlers to parse lists of /jobs but **NOT** job pages like /viewjob?.

to bypass these bot rules, set '''ROBOTSTXT_OBEY = False''' in settings.py

Should you do this, be careful not to flood the server with requests. always sleep() before performing a disallowed request. 

