from dataclasses import dataclass
from typing import TypeVar, List, Any
from alive_progress import alive_bar

T = TypeVar("T")


@dataclass
class SpannerTable:

    list_items: list[List[Any]]

    def __init__(self):
        print("init")

    def load(self, client):
        print("Loading {}".format(self.list_items[0][0].__class__.__name__))
        with alive_bar(len(self.list_items)) as bar:
            for chunk in self.list_items:
                try:
                    client.run_in_transaction(self.writeSpanner, chunk)
                except:
                    print(
                        "retrying {} {}".format(
                            self.list_items[0][0].__class__.__name__, len(chunk)
                        )
                    )
                    client.run_in_transaction(self.writeSpanner, chunk)
                bar()

    def chunk(self, data: List[Any], chunk_size: int = 1000) -> List[List[Any]]:
        result = []
        for i in range(0, len(data), chunk_size):
            result.append(data[i : i + chunk_size])
        return result

    def loadItems(self, items):
        self.list_items = self.chunk(items)

    def writeSpanner(self, transaction, c, debug=False):
        rows = []
        columns = c[0].__dataclass_fields__.keys()
        if debug:
            print(columns)
        for item in c:
            rows.append(tuple(item.__dict__.values()))
        if len(rows) > 0:
            try:
                transaction.insert(
                    table=c[0].__class__.__name__, columns=columns, values=rows
                )
            except:
                print(rows)
                exit(1)
