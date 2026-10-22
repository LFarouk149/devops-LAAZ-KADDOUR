TAX_RATE= 0.19
def average(prices):
   if not prices:
      return 0
   return sum(prices) / len(prices)
def total(prices):
    """Cart total,taxesincluded."""
    return round(sum(prices)*(1+ TAX_RATE),2)