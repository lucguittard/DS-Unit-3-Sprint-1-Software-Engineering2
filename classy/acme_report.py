from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

# function to generate a list of products
def generate_products(num_products=30):
    """Docstring"""

    products = []

    for i in range(num_products):
        tt = Product(
            name = '{} {}'.format(sample(ADJECTIVES, 1)[0],
            sample(NOUNS, 1)[0]),
            price=randint(5, 100),
            weight=randint(5, 100),
            flammability=uniform(0.0, 2.5)
            )
        products.append(Product(tt.name=name, tt.price=price, tt.weight=weight, tt.flammability=flammability))

    return products

# funtion to generate an inventory report
def inventory_report(products): #,price,weight,flammability):
    """Docstring""" #should be used inplace of comment(26)
    
    unique_products_count = len(products)

    names = set()
    total_price = 0
    total_weight = 0
    total_flammability = 0

    for i in products:
        names.add(i.name)
        total_price += i.price
        total_weight += i.weight
        total_flammability += i.flammability

    avg_price = total_price/len(products)
    avg_weight = total_weight/len(products)
    avg_flammability = total_flammability/len(products)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('There are {} unique products'.format(unique_products_count))
    print('Average price:', avg_price)
    print('Average weight', avg_weight)
    print('Average flammability', avg_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
