from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class AbstractDataImporter(ABC):
    @abstractmethod
    def import_data(self) -> str:
        raise NotImplementedError()

    def initialize_data_matrix(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        characters = [span.text for span in soup.find_all('span')]
        data = [characters[i:i+5] for i in range(0, len(characters), 5)]
        return data
