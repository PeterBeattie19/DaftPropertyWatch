from property_ import Property
import requests
from bs4 import BeautifulSoup
from daft_url_formatter import DaftUrlFormatter


class DaftScraper:
    def __init__(self, locations, price_range=(1000, 1500)):
        self._locations = locations
        self._price_range = price_range
        self._daft_url_formatter = DaftUrlFormatter(locations, price_range)

    @property
    def locations(self):
        return self._locations

    def query_all_properties(self):
        page = self._parse_url_results_and_return_prop_ids(self._daft_url_formatter.get_url())
        results = []
        while len(page) != 0:
            page = self._parse_url_results_and_return_prop_ids(self._daft_url_formatter.get_url())
            results = results + page
        self._daft_url_formatter.reset_pagination()
        return results

    @staticmethod
    def _parse_url_results_and_return_prop_ids(url):
        url_result = requests.get(url).content
        soup = BeautifulSoup(url_result, 'html.parser')
        search_results = soup.find_all("ul", class_=lambda x: x and x.startswith("SearchPage__SearchResults-"))
        soup.markup = search_results[0]
        properties = soup.find_all("li", class_=lambda x: x and x.startswith("SearchPage__Result"))
        property_objects = []
        for property_ in properties:
            soup_2 = BeautifulSoup(str(property_), 'html.parser')
            property_url = soup_2.find_all("a")[0]['href']
            property_id = property_url.split("/")[-1]
            property_objects.append(Property(property_id, property_url))
        return property_objects
