from dataclasses import dataclass

@dataclass
class Scraper:
    url: str
    headers: dict
    params: dict
    data: dict

    def __post_init__(self):
        self.session = requests.Session()
        self.session.headers = self.headers
        self.session.params = self.params
        self.session.data = self.data