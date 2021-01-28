class Property:

    def __init__(self, id_, url_suffix):
        self._id = id_
        self._url_suffix = url_suffix
        self._url_prefix = "https://www.daft.ie"

    @property
    def id(self):
        return self._id

    @property
    def url(self):
        return "{}{}".format(self._url_prefix, self._url_suffix)

    def __repr__(self):
        return "Property URL: {} \n Property: {}".format(self.url, self._id)

    def __eq__(self, other):
        return self._id == other.id
