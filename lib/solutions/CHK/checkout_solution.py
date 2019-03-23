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
        (40, (80, 'B'))
    ],
}

AMOUNTS = 0
PRICES = 1

EXTRA_PRICE = 0
EXTRA_ITEM = 1


class Market(object):
    """Supermarket."""

    skus = None

    def __init__(self, skus):
        """Set up."""
        self.skus = skus

    def check_skus(self):
        """Validate input.

        :returns: True for validated else False.
        """
        if not isinstance(self.skus, str):
            return False

        for item in self.skus:
            if item not in stock:
                return False

        return True

    def calculate_items(self, items):
        """Calculate summary value for kind of item.

        :param items: string of same items
        :returns: total value for item
        """
        item, amount = items

        pricelist = stock[item]
        price = pricelist[PRICES][0]
        promo_price = 0

        idx = len(list(filter((amount).__ge__, pricelist[AMOUNTS]))) - 1

        if idx: # calculate special price
            pricelist_promo_amount = pricelist[AMOUNTS][idx]
            if isinstance(pricelist[PRICES][idx], (tuple, list)):
                pricelist_promo_price = pricelist[PRICES][idx][EXTRA_PRICE]
                pricelist_promo_item = pricelist[PRICES][idx][EXTRA_ITEM]
            else:
                pricelist_promo_price = pricelist[PRICES][idx]

            promo_amount = int(amount / pricelist_promo_amount)
            amount = amount % pricelist_promo_amount
            promo_price = promo_amount * pricelist_promo_price

        return amount * price + promo_price

    def checkout(self):
        """Supermarket checkout.

        :param skus: Stock Keeping Units
        :returns: the total price of a number of items
        """

        if not self.check_skus():
            return -1

        value = 0
        self.skus = sorted(self.skus)

        grouped = [(k, sum(1 for _ in g)) for k, g in itertools.groupby(self.skus)]

        for items in grouped:
            value += self.calculate_items(items)

        return value


def checkout(skus):
    """Get value for shopping."""
    market = Market(skus)
    return market.checkout()

