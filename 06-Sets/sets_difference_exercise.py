favourites = {
    'door screen',
    'frying pan',
    'roller blind',
    'football',
    'coffee grinder',
    'bush hat',
    'stirling engine',
    'cachemira cd',
    'shirt',
}

basket = {
    'garlic crusher',
    'stirling engine',
    'frying pan',
    'shirt',
    'bush hat',
}

suggestions = sorted(favourites.difference(basket))
print(suggestions)
