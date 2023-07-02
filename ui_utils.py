from models import Pagination
from utils import get_page_count

def set_pagination(pag: Pagination, curr_page, page_size, total_items):
    pag.page = curr_page
    pag.page_size = page_size
    pag.total_pages = get_page_count(total_items, page_size)
    pag.total_items = total_items
    _set_nav(pag, 5)

def _set_nav(pag: Pagination, page_buttons: int):
    curr = pag.page
    total = pag.total_pages

    pag.nav_prev_disabled = pag.page == 1
    pag.nav_next_disabled = pag.page == total

    if page_buttons >= total:
        pag.nav_from = 1
        pag.nav_to = total
        return

    left = right = page_buttons // 2
    if page_buttons % 2 == 0:
        left -= 1
    
    pag.nav_from = curr - left
    pag.nav_to = curr + right

    if pag.nav_from < 1:
        pag.nav_to += 1 - pag.nav_from
        pag.nav_from = 1

    if pag.nav_to > total:
        pag.nav_from -= pag.nav_to - total
        pag.nav_to = total
