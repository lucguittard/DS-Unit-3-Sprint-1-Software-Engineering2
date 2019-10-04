from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

# function to generate a list of products
def generate_products(num_products=30):
    products = []
    price = []
    weight = []
    flammability = []
    total_price = 0
    total_weight = 0
    total_flammability = 0
    for i in range(num_products):
        tt = Product(name = '{} {}'.format(sample(ADJECTIVES,1),
            sample(NOUNS,1)),
            price=randint(5,100),
            weight=randint(5,100),
            flammability=uniform(0,3)
            )
        products.append(tt.name)
        #products.append(tt.price)
        #products.append(tt.weight)
        #products.append(tt.flammability)
        total_price += tt.price
        total_weight += tt.weight
        total_flammability += tt.flammability

    return products, total_price, total_weight, total_flammability

# funtion to generate an inventory report
def inventory_report(products): #,price,weight,flammability):
    unique_products_count = len(products)


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
