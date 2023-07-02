def get_page_count(total_items, page_size):
    pages = total_items // page_size
    if total_items % page_size > 0:
        pages += 1
    return pages

def get_start_end_indexes(page, page_size, total_items) -> tuple[int, int]:
    a = (page - 1) * page_size
    if a >= total_items:
        return -1, -1
    b = a + page_size
    if b > total_items:
        b = total_items
    return a, b
