from Interfaces import SearchI
from Interfaces import DataDownloaderI
import re

class SearchUrl(SearchI.SearchI):

    def __init__(self, data_downloader: DataDownloaderI.DataDownloaderI) -> None:

        self.data_downloader = data_downloader
        self.hrefs: list = []

    def find_all_hrefs(self) -> None:
        document: list = self.data_downloader.get().split(">")
        splited: list = []
        url: str = ''

        for i in document:

            if re.search('^<a', i):

                splited = i.split(' ')

                url = self.__get_url(splited)

                self.hrefs.append(url[1:len(url) - 1])
        

    def __get_url(self, splited: list) -> str:

        tempArr: list =[]
        url: str = ''

        for i in splited:

            if re.search('^href', i):

                tempArr = i.split('=')

                url = tempArr[1]

                return url
            
        return ''

    def get_all_href(self) -> list:
        return self.hrefs