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

    grouped = None
    pricelist_extra_items = None
    skus = None
    total_price = 0

    def __init__(self):
        """Set up."""
        self.pricelist_extra_items = []

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

    def get_promo_items(self, item, amount):
        """Calculate price of gift items."""
        grouped = dict(self.grouped)
        if item in grouped:
            if grouped[item] < amount:
                extra_amount = grouped[item]
            else:
                extra_amount = amount
            return self.process_item((item, extra_amount))
        return 0

    @staticmethod
    def get_price_index(amount, pricelist):
        """Return pricelist index for amount."""
        return len(list(filter((amount).__ge__, pricelist[AMOUNTS]))) - 1

    def calculate_price(self, amount, pricelist):
        """Calculate promotional prices."""
        idx = self.get_price_index(amount, pricelist)
        pricelist_extra_item = None
        if idx:
            pricelist_amount = pricelist[AMOUNTS][idx]
            if isinstance(pricelist[PRICES][idx], (tuple, list)):
                pricelist_price = pricelist[PRICES][idx][EXTRA_PRICE]
                pricelist_extra_item = pricelist[PRICES][idx][EXTRA_ITEM]
            else:
                pricelist_price = pricelist[PRICES][idx]

            calculated_amount = int(amount / pricelist_amount)
            amount = amount % pricelist_amount
            price = calculated_amount * pricelist_price

            if pricelist_extra_item:
                self.pricelist_extra_items.append((pricelist_extra_item, calculated_amount))

            if amount > 0:
                price += self.calculate_price(amount, pricelist)
            return price
        return 0

    def calculate_item(self, item, amount):
        """Calculate summary value for kind of item.

        :param item: item name
        :param amount: amount of item
        """
        pricelist = stock[item]
        self.grouped[item]['total_price'] = self.calculate_price(amount, pricelist)

    def checkout(self, skus):
        """Supermarket checkout.

        :param skus: Stock Keeping Units
        :returns: the total price of a number of items
        """
        self.skus = skus

        if not self.check_skus():
            return -1

        self.total_price = 0
        self.skus = sorted(self.skus)
        self.grouped = dict([
            (k, {'amount': sum(1 for _ in g), 'total_price': 0})
            for k, g in itertools.groupby(self.skus)
        ])

        for item, data in self.grouped.items():
            self.calculate_item(item, data['amount'])

        # for pricelist_promo_item, promo_amount in self.pricelist_extra_items:
        #     self.get_promo_items(pricelist_promo_item, promo_amount)

        return self.total_price


def checkout(skus):
    """Get value for shopping."""
    market = Market()
    return market.checkout(skus)


