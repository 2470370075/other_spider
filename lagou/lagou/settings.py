# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lagou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
COOKIES_DEBUG = True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie': 'user_trace_token=20200425124743-5273d79b-f908-4845-88f5-27da30cb3ffc; _ga=GA1.2.2083221733.1587789941; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587789941,1587806294,1587806295,1587825893; LGUID=20200425124744-fbc7ec26-70df-481f-8cba-75065f3fc714; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171afa7e3597d-0f6e66ab39fcdd8-153a7440-1327104-171afa7e35a405%22%2C%22%24device_id%22%3A%22171afa7e3597d-0f6e66ab39fcdd8-153a7440-1327104-171afa7e35a405%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sajssdk_2015_cross_new_user=1; _gid=GA1.2.1384856302.1587789948; gate_login_token=0a4aee0e5c7cafb1a699e2443abb3a4d4f0466e01a6b3f99e42e3a27d54c4603; LG_LOGIN_USER_ID=b1a7924ce1c16abf4fa1de963adb72b38c2fcd7bf0eba3ffb9c05f5b54d7baa4; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=255; index_location_city=%E5%85%A8%E5%9B%BD; privacyPolicyPopup=false; SEARCH_ID=d8427d149c4b40b9b0fe95db66d100d1; LGRID=20200425235946-43281ce1-06c8-4206-ae20-a40ebd449398; JSESSIONID=ABAAABAABEIABCI1E12DFCD6235E4D10CC87B4ED66C7356; X_HTTP_TOKEN=37f5eccf3a1844ff683038785116e08ec86431237a; WEBTJ-ID=20200425171814-171b0a150f90-049b8c50329525-153a7440-1327104-171b0a150fa470; _putrc=2A0C4F15ECB073E1123F89F2B170EADC; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587830264; login=true; unick=%E7%8E%8B%E4%BD%B3%E5%85%B4; TG-TRACK-CODE=index_navigation; X_MIDDLE_TOKEN=c41be4d1bb03df35bfd38b5787826d02; LGSID=20200425235946-89663233-fb2b-470e-bf9e-337169df604e; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagou.middlewares.LagouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lagou.middlewares.LagouDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'lagou.pipelines.LagouPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
