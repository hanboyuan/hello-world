#!/usr/bin/env python
# -*- coding=utf-8 -*-
##############################
import datetime


class Shopping(object):
    def __init__(self):
        """

        :rtype: 以字典形式初始化购物车
        """
        self.shoping = dict()

    def __str__(self):
        return '%s object ' % (self.shoping)

    __repr__ = __str__

    def add(self, product_id, product_num, product_price, product_name):
        '''
            商品加入购物车
        '''
        if product_id not in self.shoping.keys():
            self.shoping[product_id] = [0, product_price, product_name]
        self.shoping[product_id][0] = self.shoping[product_id][0] + 1
        # print self.shoping
        return self.shoping

    def reduce(self, product_id):
        '''
            购物车商品数量改变
        '''

        def is_zero():
            if self.shoping[product_id][0] == 0:
                return self.shoping.pop(product_id)

        self.shoping[product_id][0] = self.shoping[product_id][0] - 1
        is_zero()

    def empty_shoplist(self):
        '''
            清空购物车
        '''
        self.shoping = dict()
        return True

    def get_shoplist(self):
        '''
            获取购物车列表
        '''
        return self.shoping


class Account(object):
    def __init__(self):
        '''
            初始化交易总金额0和找零金额0
        '''
        self.total_price = 0
        self.change = 0

    def check(self, shop_result):
        '''
            生成交易订单和算出交易总额
        '''
        f = file('check_list', 'w')
        f.close()
        f = file('check_list', 'a')
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
        f.write('{0:10s} {1:10s} {2:10s} {3:10s} {4:10s}\n'.format('商品编号', '商品名称', '商品数量', '商品价格', '共计'))
        for key, value in shop_result.items():
            single_total = value[0] * value[1]
            f.write('{0:4s} {1:4s} {2:4d} {3:4.2f} {4:4.2f}\n'.format(key, value[-1], value[0], value[1],
                                                                      single_total))
        self.total_price = self.total_price + single_total
        f.write('总价:{0:3.2f}\n'.format(self.total_price))
        f.close()

    def get_change(self):
        '''
            获取消费后的零钱
        '''
        return self.change

    def account(self, cost):
        '''
            扣钱，交易运算
        '''
        if cost >= self.total_price:
            self.change = cost - self.total_price
            return True
        else:
            return False


'''
    测试程序运行情况，加减商品，通过购物车生成交易页，account传递进去现金20000
    如果现金大于订单总金额消费成功，交易页写入消费信息
    如果现金小于订单总金额，消费失败，只输出，不写入交易页面
'''
if __name__ == "__main__":
    a = Shopping()
    a.add('D200001', 1, 4999, 'iphone6')
    a.add('D200001', 1, 4999, 'iphone6')
    a.reduce('D200001')
    a.add('D200002', 1, 5999, 'iphone6 plus')
    # a.empty_shoplist()
    shop_result = a.get_shoplist()
    b = Account()
    b.check(shop_result)
    cost = b.account(20000)
    if cost:
        f = file('check_list', 'a')
        f.write('-' * 50)
        f.write('\n\n\n支付成功，找零{0:.2f}'.format(b.get_change()))
        f.close()
    else:
        print '支付失败'
