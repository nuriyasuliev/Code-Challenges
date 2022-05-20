
def capital_indexes(text):
    return [order for order, letter in enumerate(text) if letter.isupper()]
print(capital_indexes('HeLlo')) 
