from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import re

BASE_URL = 'https://www.proxynova.com/proxy-server-list/country-cn'


class ProxyNovaCrawler(BaseCrawler):
    """
    proxynova crawler, https://www.proxynova.com/proxy-server-list/country-cn
    """
    urls = [BASE_URL]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('#page_contents table tr:gt(0)').items()
        for tr in trs:
            anon = tr.find('td:nth-child(7)').text()
            if anon not in ["Elite", " 	Anonymous"]:
                continue
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ProxyNovaCrawler()
    for proxy in crawler.crawl():
        print(proxy)
