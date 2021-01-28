class DaftUrlFormatter:

    def __init__(self, locations, price_range):
        self._daft_url_prefix = "https://www.daft.ie/property-for-rent/ireland?"
        self._default_page_size = 20
        self._number_of_paginations = 0
        self._locations = locations
        self._price_range = price_range

    def reset_pagination(self):
        self._number_of_paginations = 0

    @staticmethod
    def _create_price_range_query_string(price_range):
        return "rentalPrice_from={}".format(price_range[0]), "rentalPrice_to={}".format(price_range[1])

    @staticmethod
    def _create_locations_query_string(locations):
        return ["location={}".format(location) for location in locations]

    @staticmethod
    def _create_pagination_query_string(page_size, from_):
        return "pageSize={}".format(page_size), "from={}".format(from_)

    def get_url(self):
        location_query_string = '&'.join(self._create_locations_query_string(self._locations))
        price_range_query_string = '&'.join(self._create_price_range_query_string(self._price_range))
        pagination_query_string = '&'.join(self._create_pagination_query_string(
            self._default_page_size, self._number_of_paginations * self._default_page_size))

        entire_query = "&".join([location_query_string, price_range_query_string, pagination_query_string])
        self._number_of_paginations += 1
        return self._daft_url_prefix + entire_query
