import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_dict = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E':40}
    multi_offers_dict = {'A': {5:200, 3:130}, 'B': {2:45}}
    one_free_offers_dict = {'E': (2,'B')}

    shopping_cart = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

    for char in skus:
        if char in shopping_cart:
            shopping_cart[char] += 1
        else:
            return -1

    total = 0

    for item in shopping_cart:
        if item in multi_offers_dict:
            for offer in multi_offers_dict[item]:
                if shopping_cart[item] > offer:
                    total += (math.floor(shopping_cart[item] / offer) * multi_offers_dict[item][offer])
                    remainder = shopping_cart[item] % offer
                    shopping_cart[item] = remainder

                    break
        
        print(item)
        if item in one_free_offers_dict:
            free_item = one_free_offers_dict[item][1]
            offer_item_num = shopping_cart[item]

            while offer_item_num >= one_free_offers_dict[item][0] and shopping_cart[free_item]:
                print('decreasing')
                shopping_cart[free_item] -= 1
                offer_item_num -= one_free_offers_dict[item][0]


    
    for item in shopping_cart:
        total += price_dict[item] * shopping_cart[item]

    

    return total


price = checkout('AAABBEEE')
print(price) 

