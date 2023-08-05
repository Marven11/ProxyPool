from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler


BASE_URL = 'https://cn.proxy-tools.com/proxy/anonymous?page={page}'
MAX_PAGE = 6

PORTS = [80, 999, 3456, 4567, 5678, 6789, 7890] + list(range(1080, 1090)) + list(range(8080, 8090)) + list(range(9090, 9100))


class ProxyToolsCrawler(BaseCrawler):
    """
    ProxyTools crawler, https://cn.proxy-tools.com/proxy/anonymous
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('.containerbox table tr:gt(0)').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            proxy_type = tr.find('td:nth-child(3)').text()
            if proxy_type != "HTTP":
                continue
            for port in PORTS:
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ProxyToolsCrawler()
    for proxy in crawler.crawl():
        print(proxy)
