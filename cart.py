TAX_RATE= 0.19
def average(prices):
    return sum(prices)/len(prices)
def total(prices):
    """Cart total,taxesincluded."""
    return round(sum(prices)*(1+ TAX_RATE),2)

def apply_discount(prices,percent):
    return [p *(1-percent/100)for pin prices]    
