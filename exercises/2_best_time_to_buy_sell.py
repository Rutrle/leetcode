def brute_force(prices):
    maximum=0
    max_coord=[]

    for i, num_a in enumerate(prices):
        for j, num_b in enumerate(prices[i+1:]):
            if num_b - num_a > maximum:
                max_coord =[i, j+i+1]
                maximum = num_b - num_a 


    return maximum, max_coord

def two_pointers(prices):
    #still check everything, if right is lower than left than update left to right position
    pointer1 = 0
    pointer2 = 1
    profit=0

    while pointer2<len(prices)-1:
        if prices[pointer2] < prices[pointer1]:
            pointer1, pointer2 = pointer2, pointer2+1

        else:
            pointer2 +=1
            new_profit =  prices[pointer2] - prices[pointer1]
            if  new_profit > profit:
                profit = new_profit


    return profit



prices = [7,1,5,3,6,4]

prices2 = [7,6,4,3,1]

print(brute_force(prices))
print(brute_force(prices2))

print(two_pointers(prices))
print(two_pointers(prices2))