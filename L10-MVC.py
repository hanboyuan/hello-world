#/usr/bin/env python
# -*- coding=utf-8 -*-
#################################
class Model(object):
    products = {
        "book": {'price': 150, 'quantity': 10},
        "meat": {'price': 20, 'quantity': 100},
        "cloth": {'price': 200, 'quantity': 10}
    }


class View(object):
    def product_list(self, product_list):
        print 'PRODUCT LIST:'
        for product in product_list:
            print (product)
        print ('')

    def product_info(self, product, product_info):
        print ('Name:%s ,Price:%s ,Quantity:%d' % (
            product.title(), product_info.get('price', 0), product_info.get('quantity', 0)))

    def product_not_found(self, product):
        print ('That product %s does not exist in the records' % product)


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_product_list(self):
        product_list = self.model.products.keys()
        self.view.product_list(product_list)

    def get_product_info(self,product):
        product_info = self.model.products.get(product,None)
        if product_info is not None:
            self.view.product_info(product,product_info)
        else:
            self.view.product_not_found(product)

def main():
    controller = Controller()
    controller.get_product_list()
    controller.get_product_info('book')
    controller.get_product_info('meat')
    controller.get_product_info('cloth')
    controller.get_product_info('computer')
    #controller.set_product_info('computer')

if __name__ == "__main__":
    main()
