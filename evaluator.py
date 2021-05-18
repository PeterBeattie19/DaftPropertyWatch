from email_handler import EmailHandler
from property_dao import PropertyDao
from daft_scraper import DaftScraper
from metrics_helper import MetricsHelper


class Evaluator:

    def __init__(self, **query_params):
        self._DEFAULT_LOCATIONS = ["rathmines-dublin"]
        self._DEFAULT_PRICE_RANGE = (0, 2000)

        self._locations = self._DEFAULT_LOCATIONS if "locations" not in query_params else query_params["locations"]
        self._price_range = \
            self._DEFAULT_PRICE_RANGE if "price_range" not in query_params else query_params["price_range"]

        print(self._locations)
        print(self._price_range)

        self._daft_scraper = DaftScraper(self._locations, self._price_range)
        self._property_dao = PropertyDao()
        self._email_handler = EmailHandler()
        self._metrics_helper = MetricsHelper() 

    def run(self):
        _current_daft_snapshot = self._daft_scraper.query_all_properties()
        _db_daft_snapshot = self._property_dao.return_all_properties()

        _db_daft_snapshot_ids = self._return_property_ids(_db_daft_snapshot)

        print(len(_current_daft_snapshot))
        self._metrics_helper.put_metric_data("NumberOfPropertiesReturned", len(_current_daft_snapshot), "Count") 
        _new_properties = list(filter(lambda x: x.id not in _db_daft_snapshot_ids, _current_daft_snapshot))
        print(len(_new_properties))
        print(_new_properties)

        if len(_new_properties) > 0:
            self._update_db_with_new_properties(_new_properties)
            self._call_email_handler(_new_properties)

    @staticmethod
    def _return_property_ids(properties):
        return set(map(lambda x: x.id, properties))

    def _update_db_with_new_properties(self, properties):
        for property_ in properties:
            self._property_dao.add_property(property_)

    def _call_email_handler(self, properties):
        self._email_handler.send_new_prop_emails(properties)
