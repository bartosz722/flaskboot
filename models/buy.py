class BuyItem:
    def __init__(self) -> None:
        self.name = ''
        self.description = ''
        self.image = ''

class BuyModel:
    def __init__(self) -> None:
        self.items: list[BuyItem] = []
        self.page = 0 # Numbered from 1.
        self.page_size = 0
        self.total_pages = 0
        self.total_items = 0
