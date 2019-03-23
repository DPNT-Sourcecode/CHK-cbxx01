

# noinspection PyUnusedLocal
# skus = unicode string

stock = {
    'A': (50, 3, 130),
    'B': (30, 2, 45),
    'C': (20),
    'D': (15),
}


def calculate_item(item):
    """Calculate summary value for kind of item."""


def checkout(skus):
    """Supermarket checkout.

    :param skus: Stock Keeping Units
    :returns: the total price of a number of items
    """

    skus.sort()

    value = 0
    for item in skus:
        value += calculate_item(item)

    return value

