from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import re

BASE_URL = 'https://free-proxy-list.net/'


class FreeProxyListCrawler(BaseCrawler):
    """
    FreeProxyList crawler, https://free-proxy-list.net/
    """
    urls = [BASE_URL]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('.table-responsive table tr:gt(0)').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = FreeProxyListCrawler()
    for proxy in crawler.crawl():
        print(proxy)
