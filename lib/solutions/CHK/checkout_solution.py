# noinspection PyUnusedLocal
# skus = unicode string

import itertools

stock = {
    'A': (50, 3, 130),
    'B': (30, 2, 45),
    'C': (20),
    'D': (15),
}

PRICE = 0
PROMO_AMOUNT = 1
PROMO_PRICE = 2

def check_input(skus):
    """Validate input.

    :returns: True for validated else False.
    """

    for item in skus:
        if item not in stock:
            return False
    return True


def calculate_items(items):
    """Calculate summary value for kind of item.

    :param items: string of same items
    :returns: total value for item
    """

    item = items[0]
    amount = len(item)
    promo_price = 0

    print(item, amount)

    if len(stock[item]) == 3:  # calculate special price
        promo_amount = int(amount / stock[item][PROMO_AMOUNT])
        amount = amount % stock[item][PROMO_AMOUNT]
        promo_price = promo_amount * stock[item][PROMO_PRICE]

    return amount * stock[item][PRICE] + promo_price


def checkout(skus):
    """Supermarket checkout.

    :param skus: Stock Keeping Units
    :returns: the total price of a number of items
    """

    if not check_input(skus):
        return -1

    value = 0
    skus = sorted(skus)

    # groupped = [print(grp)
    for k, grp in itertools.groupby(skus):
        print(grp.__dict__)

    # for items in groupped:
    #     value += calculate_items(items)

    # return value



