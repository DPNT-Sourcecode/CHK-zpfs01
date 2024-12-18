import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_dict = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offers_dict = {'A': (3,130), 'B': (2,45)}

    shopping_cart = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    for char in skus:
        if char in shopping_cart:
            shopping_cart[char] += 1
        else:
            return -1

    total = 0

    for item in shopping_cart:
        if item in offers_dict:
            remainder = shopping_cart[item] % offers_dict[item][0]
            total += (math.floor(shopping_cart[item] / offers_dict[item][0]) * offers_dict[item][1]) + (price_dict[item]*remainder)
        else:
            total += price_dict[item] * shopping_cart[item]

    return total

