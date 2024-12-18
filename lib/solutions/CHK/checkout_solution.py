import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_dict = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E':40, 'F':10, 'G':20, 'H':10, 'I':35, 'J':60, 'K':70, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30, 'R':50, 'S':20, 'T':20, 'U':40, 'V':50, 'W':20, 'X':17, 'Y':20, 'Z':21}

    multi_offers_dict = {'A': {5:200, 3:130}, 'B': {2:45}, 'H': {10:80, 5:45}, 'K':{2:120}, 'P':{5:200}, 'Q':{3:80}, 'V':{3:130, 2:90}}
    one_free_offers_dict = {'E': (2,'B'), 'F':(2,'F'), 'N':(3,'M'), 'R':(3,'Q'), 'U':(3,'U')}
    group_offers_dict = {45: (3, ['Z', 'Y', 'S', 'T', 'X'])}



    shopping_cart = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

    # count items in cart
    for char in skus:
        if char in shopping_cart:
            shopping_cart[char] += 1
        else:
            return -1

    total = 0

    # apply one free offers first
    for item in shopping_cart:

        if item in one_free_offers_dict:
            free_item = one_free_offers_dict[item][1]
            offer_item_num = shopping_cart[item]

            if free_item != item:
                while offer_item_num >= one_free_offers_dict[item][0] and shopping_cart[free_item]:
                    shopping_cart[free_item] -= 1
                    offer_item_num -= one_free_offers_dict[item][0]
            else: 
                while offer_item_num > one_free_offers_dict[item][0] and shopping_cart[free_item]:
                    shopping_cart[free_item] -= 1
                    offer_item_num -= one_free_offers_dict[item][0]

    # then multi offers
    for item in shopping_cart:
        if item in multi_offers_dict:

            smallest_offer = list(multi_offers_dict[item].keys())[-1]

            while shopping_cart[item] >= smallest_offer:
                for offer in multi_offers_dict[item]:
                    if shopping_cart[item] >= offer:
                        total += (math.floor(shopping_cart[item] / offer) * multi_offers_dict[item][offer])
                        remainder = shopping_cart[item] % offer
                        shopping_cart[item] = remainder

                        break

    for offer in group_offers_dict:
        print('offering')
        threshold = group_offers_dict[offer][0]
        print(threshold)
        item_num_list = []
        for item in group_offers_dict[offer][1]:
            item_num_list.append(shopping_cart[item])
        # group_offers_dict = {45: (3, ['Z', 'Y', 'S', 'T', 'X'])}
        print(item_num_list)
        x = 0
        count = 0
        while True:
            item = group_offers_dict[offer][1][x]
            
            # above threshold, apply discount
            if count + item_num_list[x] >= threshold:
                total += offer
                item_num_list[x] -= (threshold-count)
                count = 0
                for y in range(0, x):
                    shopping_cart[group_offers_dict[offer][1][y]] = item_num_list[y]
            else:
                x += 1
                print('x:' + str(x))
                if x > len(item_num_list)-1:
                    break
                count += item_num_list[x]
                item_num_list[x] = 0




    for item in shopping_cart:
        total += price_dict[item] * shopping_cart[item]


    return total

price = checkout('XYZ')
print(price)


