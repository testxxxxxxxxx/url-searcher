import Services.DataDownloader as DataDownloader
import Services.SearchUrl as SearchUrl

dataDownloader = DataDownloader.DataDownloader("https://www.wp.pl")
searchUrl = SearchUrl.SearchUrl(dataDownloader)

if __name__ == '__main__':
    searchUrl.find_all_hrefs()
    print(searchUrl.get_all_href())