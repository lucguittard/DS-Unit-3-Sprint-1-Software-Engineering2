from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        product = sample(NOUNS, 1)
        products.append(product)
    return products

def inventory_report(products):
    Name = '{} {}'.format(sample(ADJECTIVES,1),
        sample(NOUNS,1))
    tt = Product(
        name=Name,
        price=randint(5,100),
        weight=randint(5,100),
        flammability=uniform(0.0,2.5)
        )

    #for i in products: come back to later
    #For the report, you should calculate and print the following values:
    # Average (mean) price, weight, and flammability of listed products
    # loop over products to calculate report

    unique_products = set(products)
    unique_products_count = len(unique_products)

    return 'There are {} unique products'.format(unique_products_count)

if __name__ == '__main__':
    inventory_report(generate_products())
