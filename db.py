from models import BuyItem, BuyItemDetails, BuyItemModel, BuyModel
from ui_utils import set_pagination
from utils import get_start_end_indexes


_names = ['Rzecz', 'Przedmiot', 'Coś niesamowitego', 'Zabawka']
_prices = [10, 1000, 22, 39, 53]

def get_buy_model(page, page_size):
    total_items = 35
    ret = BuyModel()
    start, end = get_start_end_indexes(page, page_size, total_items)
    if start < 0:
        return ret    
    set_pagination(ret.pag, page, page_size, total_items)
    
    for i in range(start, end):
        item = BuyItem()
        item.id = str(i + 1)
        item.name = _names[i % len(_names)] + f' {i + 1}'
        item.description = 'To jest {}.'.format(item.name[0].lower() + item.name[1:])
        item.image = f'/static/item{i % 6}.jpg'
        item.price = _prices[i % len(_names)] * (i + 1)
        ret.items.append(item)

    return ret

def get_buy_item_model(item_id):
    items = get_buy_model(1, 1000)
    model = BuyItemModel()
    try:
        item = next(i for i in items.items if i.id == item_id)
        model.item = item
        _set_buy_item_model_details(model)
    except:
        pass
    return model

def _set_buy_item_model_details(model: BuyItemModel):
    model.details = BuyItemDetails()
    model.details.long_descr = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla malesuada vel velit ut bibendum. Phasellus at nisi in sem vestibulum tincidunt et vitae lorem. Nunc rutrum augue sit amet tellus elementum iaculis. Etiam ut ipsum felis. Aenean a euismod augue. Mauris condimentum nibh pharetra, interdum enim quis, viverra neque. Pellentesque vitae ipsum in erat fermentum dictum quis eget nisi. Morbi quis felis nulla. Vestibulum viverra lectus sit amet mauris vehicula, vitae tempus augue viverra. Vestibulum ac ullamcorper massa, in varius lectus. Sed eget dapibus ante, vel laoreet eros.'
    model.details.attrs['aaa'] = 'aaa 123'
    model.details.attrs['bbbb'] = 'bbbb 1234'
    model.details.attrs['ccccc'] = 'ccccc 12345'

