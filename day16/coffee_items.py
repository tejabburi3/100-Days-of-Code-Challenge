storage={'coffee':550,'milk':3000,'water':5000}

menu = {
    'Espresso': {
        'items': {'water':50, 'coffee':18},
        'cost': 52
    },
    'Latte': {
        'items': {'water':200, 'coffee':24, 'milk':150},
        'cost': 88
    },
    'Cappuccino': {
        'items': {'water':250, 'coffee':24, 'milk':100},
        'cost': 122
    }
}

def Coffee(a):
    for item in menu[a]['items']:
        if storage[item] < menu[a]['items'][item]:
            return 'out of stock ' + item
    
    for item in menu[a]['items']:
        storage[item] -= menu[a]['items'][item]
    return 'ok'
