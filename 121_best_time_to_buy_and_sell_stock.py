def best_time_to_sell_buy(prices):
    '''
    
    uses a sliding window (two pointers)
    O(n)
    :type prices: List[int]
    :rtype: int
    '''
    left_pointer = 0
    right_pointer = 1
    max_profit = 0
    while right_pointer < len(prices):
        profit = prices[right_pointer] - prices[left_pointer]

        if profit > 0:
            if profit > max_profit:
                max_profit = profit
        else:
            left_pointer = right_pointer

        right_pointer += 1
    return max_profit


prices = [7, 1, 5, 3, 6, 4]

print(best_time_to_sell_buy(prices))
