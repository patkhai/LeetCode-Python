'''
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]


Approach: 
To find the products of all the integers except the integer at each index, we'll go through our list greedily ↴ twice. 
First we get the products of all the integers before each index, and then we go backwards to get the products of all the integers after each index.

When we multiply all the products before and after each index, we get our answer—the products of all the integers except the integer at each index!
'''

#O(N) O(N)
def get_products_of_all_ints_except_at_index(int_list):

    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                            'indices requires at least 2 numbers')

    # We make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in range(len(int_list) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

    return products_of_all_ints_except_at_index


print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))