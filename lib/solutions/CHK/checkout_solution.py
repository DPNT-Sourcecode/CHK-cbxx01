# noinspection PyUnusedLocal
# skus = unicode string

import itertools
from .stock import GROUP_DISCOUNT
from .stock import STOCK

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
            if item not in STOCK:
                return False

        return True

    def get_promo_items(self, item, amount):
        """Calculate price of gift items."""
        print(self.skus, item, amount)
        if item in self.grouped:
            if self.grouped[item]['amount'] > amount:
                self.grouped[item]['amount'] -= amount
                self.calculate_item(item, extra=False)
            else:
                del self.grouped[item]

    @staticmethod
    def get_price_index(amount, pricelist):
        """Return pricelist index for amount."""
        return len(list(filter((amount).__ge__, pricelist[AMOUNTS]))) - 1

    def calculate_price(self, amount, pricelist, extra=True):
        """Calculate promotional prices."""
        idx = self.get_price_index(amount, pricelist)

        pricelist_extra_item = None
        pricelist_amount = pricelist[AMOUNTS][idx]
        if isinstance(pricelist[PRICES][idx], (tuple, list)):
            pricelist_price = pricelist[PRICES][idx][EXTRA_PRICE]
            if extra:
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

    def calculate_item(self, item, extra=True):
        """Calculate summary value for kind of item.

        :param item: item name
        :param amount: amount of item
        :param extra: turn on/of extra examples counting
        """
        pricelist = STOCK[item]
        amount = self.grouped[item]['amount']
        self.grouped[item]['total_price'] = self.calculate_price(amount, pricelist, extra)

    def group_discount(self):
        """Apply group discount(s)."""
        # select products
        discount_amount = GROUP_DISCOUNT['amount']
        discount_price = GROUP_DISCOUNT['price']
        in_discount_items = set(GROUP_DISCOUNT['items'])
        in_cart_items = self.grouped.keys()
        to_discount_items = list(in_discount_items.intersection(in_cart_items))

        amounts = []
        prices = []
        for item in to_discount_items:
            amounts.append(self.grouped[item]['amount'])
            prices.append(STOCK[item][PRICES][0])

        # order by price desc
        prices, to_discount_items, amounts = (
            list(t) for t in zip(*sorted(zip(prices, to_discount_items, amounts)))
        )
        total_amount = sum(amounts)
        if total_amount >= discount_amount:
            # recalculate
            in_discount_amount = int(total_amount / discount_amount)
            out_discount_amount = total_amount % discount_amount
            in_discount_price = in_discount_amount * discount_price

            # add discount entry
            self.grouped['discount']['total_price'] = in_discount_price

            # attach not discounted
            for item in to_discount_items:
                if out_discount_amount == 0:
                    del self.grouped[item]
                if self.grouped[item]['amount'] < out_discount_amount:
                    out_discount_amount -= self.grouped[item]['amount']
                    self.calculate_item(item)

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

        for item in self.grouped.keys():
            self.calculate_item(item)

        for pricelist_extra_item, amount in self.pricelist_extra_items:
            self.get_promo_items(pricelist_extra_item, amount)

        self.group_discount()

        return sum([item['total_price'] for item in self.grouped.values()])


def checkout(skus):
    """Get value for shopping."""
    market = Market()
    return market.checkout(skus)

