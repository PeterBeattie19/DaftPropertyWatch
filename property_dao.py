from property_ import Property
from tinydb import TinyDB, Query
from tinydb.queries import where


class PropertyDao:

    def __init__(self):
        self._db_json_path = "db.json"
        self._db = TinyDB(self._db_json_path)
        self._URL = "URL"
        self._ID = "ID"

    def does_property_exist(self, property_):
        _id = Query()
        _search_results = self._db.search(_id.ID == property_.id)
        return len(_search_results) > 0

    def add_property(self, property_):
        self._db.insert({self._URL: property_.url, self._ID: property_.id})

    def return_all_properties(self):
        return list(map(lambda x: self._convert_db_entry_to_property(x), self._db.all()))

    def delete_property(self, property_):
        _id = Query()
        self._db.remove(where(self._ID) == property_.id)

    def _convert_db_entry_to_property(self, db_entry):
        property_ = Property(db_entry[self._ID], db_entry[self._URL])
        return property_
