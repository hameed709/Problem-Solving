def bestTime(stocks):
    min_price = stocks[0]
    max_profit = 0
    for price in stocks[1:]:
        if price < min_price :
            min_price = price
        profit = price - min_price
        max_profit = max(max_profit,profit)

    return max_profit


print(bestTime([7,1,5,3,6,4]))
print(bestTime([7,6,4,3,1]))
print(bestTime([2,4,1,7]))
print(bestTime([1,2,3,4,5]))