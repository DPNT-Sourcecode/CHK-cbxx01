

# noinspection PyUnusedLocal
# skus = unicode string

stock = {
    'A': (50, 3, 130),
    'B': (30, 2, 45),
    'C': (20),
    'D': (15),
}


def check_input(skus):
    """Validate input.

    :returns: True for validated else False.
    """
    for item in skus:
        if item not in stock:
            return False
    return True


def calculate_item(item):
    """Calculate summary value for kind of item."""


def checkout(skus):
    """Supermarket checkout.

    :param skus: Stock Keeping Units
    :returns: the total price of a number of items
    """

    if not check_input(skus):
        return -1

    value = 0
    skus.sort()

    item = ''
    for item in skus:
        value += calculate_item(item)

    return value


