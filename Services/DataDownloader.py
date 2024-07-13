from Interfaces import DataDownloaderI
import requests

class DataDownloader(DataDownloaderI.DataDownloaderI):

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def get(self) -> str:

        try:

            response: object = requests.get(self.uri)
        
        except requests.exceptions as err:
            raise Exception(err)

        return response.text