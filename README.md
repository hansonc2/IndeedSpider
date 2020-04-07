# IndeedSpider 🕸🕷
Scrapy spider for retrieving job postings from Indeed.com

## Requirements
scrapy==1.8.0

## Usage
The JobSpider up to 3 arguments
```
title= '', city='', state=''
```

```
scrapy crawl jobs -a title='software engineer' -a city='chicago' -a state='IL'
```
You can even output to csv:
```
scrapy crawl jobs -a title='software engineer' -a city='chicago' -a state='IL' -o jobs.csv
```

## Job Fields
* Title
* Employer
* Employer_link
* Rating
* Location
* Salary
* Date
* Url
* Description

## To Do:
- [ ] Update CSS selection rule set for all fields. 
- [ ] Update CLI options/args.
- [ ] Add position description parsing.
- [ ] Add custom middleware.
- [ ] Deploy, CI.

## Warning!

Indeed's [robots.txtfile](https://www.indeed.com/robots.txt)  allows for crawlers to parse lists of /jobs but **NOT** job pages like /viewjob?.

to bypass these bot rules, set 'ROBOTSTXT_OBEY = False' in settings.py

Should you do this, be careful not to flood the server with requests. always sleep() before performing a disallowed request.
