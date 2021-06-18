import requests
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from yarl import URL
from typing import Dict, Optional

from .item import Item
from ..const import OSRS_WIKI_PRICES_API, USER_AGENT


class ItemDB(object):
    def __init__(self) -> None:
        # self.db_path = pathlib.Path(__file__).parent.absolute() / 'db.sqlite'
        self.db: TinyDB = TinyDB(storage=MemoryStorage)
        self.url = URL(OSRS_WIKI_PRICES_API) / "mapping"
        self.request_headers = {"User-Agent": USER_AGENT}
        self.reload()

    def open(self):
        pass

    def close(self):
        self.db.close()

    def reload(self) -> None:
        newitems = self._fetch_items()
        self.db.insert_multiple(newitems)

    def _fetch_items(self) -> Optional[Dict]:
        try:
            resp = requests.get(self.url, headers=self.request_headers)
            resp.raise_for_status()
            items = resp.json()
            return items
        except requests.HTTPError as e:
            raise e

    def get_item_by_id(self, id: int) -> Optional[Item]:
        q = Query()
        item = self.db.get(q.id == id)
        if item:
            return Item.from_dict(item)
        return None
