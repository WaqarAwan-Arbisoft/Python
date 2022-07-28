import profile


def maximumProfit(priceList):
    profit = 0
    for index, buyingPrice in enumerate(priceList):
        sellingPrice = max(priceList[index:])
        profit = max(profit, (sellingPrice-buyingPrice))

    return profit


eth_prices = [455, 460, 465, 451, 414, 415, 441]
print(maximumProfit(eth_prices))
