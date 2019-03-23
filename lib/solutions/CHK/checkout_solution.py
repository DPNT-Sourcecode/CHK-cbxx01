# noinspection PyUnusedLocal
# skus = unicode string

import itertools

stock = {
    # 'item': [
    #     (amount1, amount2, ...),
    #     (price1, (price2, extra), ...),
    # ],
    'A': [
        (1, 3, 5),
        (50, 130, 200),
    ],
    'B': [
        (1, 2),
        (30, 45),
    ],
    'C': [
        (1,),
        (20,),
    ],
    'D': [
        (1,),
        (15,),
    ],
    'E': [
        (1, 2),
        (40, (40, 'B'))
    ],
}

AMOUNTS = 0
PRICES = 1

EXTRA_PRICE = 0
EXTRA_ITEM = 1


def check_input(skus):
    """Validate input.

    :returns: True for validated else False.
    """

    if not isinstance(skus, str):
        return False

    for item in skus:
        if item not in stock:
            return False

    return True


def calculate_items(items):
    """Calculate summary value for kind of item.

    :param items: string of same items
    :returns: total value for item
    """

    amount, item = items

    pricelist = stock[item]
    price = pricelist[PRICES][0]

    promo_amount = len(filter((amount).__ge__, pricelist[AMOUNTS]))
    promo_price = 0

    if len(pricelist[0]) == 3:  # calculate special price
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

    grouped = [(k, sum(1 for _ in g)) for k, g in itertools.groupby(skus)]

    for items in grouped:
        value += calculate_items(items)

    return value



