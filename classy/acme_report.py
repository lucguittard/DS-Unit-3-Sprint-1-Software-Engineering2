from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

# function to generate a list of products
def generate_products(num_products=30):
    products = []

    for i in range(num_products):
        tt = Product(
            name = '{} {}'.format(sample(ADJECTIVES,1),
            sample(NOUNS,1)),
            price=randint(5,100),
            weight=randint(5,100),
            flammability=uniform(0,3)
            )
        products.append(Product(tt.name=name, tt.price=price, tt.weight=weight, tt.flammability=flammability))

    return products

# funtion to generate an inventory report
def inventory_report(products): #,price,weight,flammability):
    unique_products_count = len(products)

    total_price = 0
    total_weight = 0
    total_flammability = 0

    for i in range(products):
        p = Product()
        total_price += p.price
        total_weight += p.weight
        total_flammability += p.flammability

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
