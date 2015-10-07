__author__ = 'shaleen'
from DataModels.webcrawler.quickr import QuickerCrawler
from DataModels.webcrawler.quickr import Parser


class QuickrService:
    _list = []

    def __init__(self):
        self.parser = Parser.Parser()
        self.crawler = QuickerCrawler.QuikrCrawler()

    def readEvalLoop(self):
        self.crawler.generateAllUrls()
        while not self.crawler.isURLListEmpty:
            page = self.crawler.crawlforhtml()
            self.crawler.writeToFile(page)
            self._list.append(self.parser.getAttributesFromHTMLPage(page, self.crawler.getCurrentUrl()))
        return self._list

    def readEvalLoopSingle(self):
        self.crawler.generateAllUrls()
        page = self.crawler.crawlforhtml()
        self.crawler.writeToFile(page)
        list = []
        list.append(self.parser.getAttributesFromHTMLPage(page, self.crawler.getCurrentUrl()))
        return list
