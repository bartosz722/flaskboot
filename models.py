class Pagination:
    def __init__(self) -> None:
        self.page = 0 # Numbered from 1.
        self.page_size = 0
        self.total_pages = 0
        self.total_items = 0
        self.nav_from = 0
        self.nav_to = 0
        self.nav_prev_disabled = False
        self.nav_next_disabled = False

class User:
    def __init__(self) -> None:
        self.name = '?'

class BuyItem:
    def __init__(self) -> None:
        self.name = ''
        self.description = ''
        self.image = ''

class BuyModel:
    def __init__(self) -> None:
        self.pag = Pagination()
        self.items: list[BuyItem] = []

