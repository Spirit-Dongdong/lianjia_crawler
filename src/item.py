# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

'''
    desc: 标题描述
    url: 链接
    total_price: 房屋总价
    single_price: 每平米价格
    level: 楼层
    total_level: 一共几层
    build_year: 哪年建的
    xiaoqu: 小区名称
    area1, area2, area3: 所在区域, 可能多级
    huxing: 基本属性-房屋户型
    total_size: 基本属性-建筑面积
    usage_size: 基本属性-套内面积
    direction: 基本属性-房屋朝向
    decoration: 基本属性-装修情况
    warm_type: 基本属性-供暖方式
    holding_age: 基本属性-产权年限
    room_type: 基本属性-户型结构
    construct_type: 基本属性-建筑类型
    construct_con: 基本属性-建筑结构
    lift_type: 基本属性-梯户比例
    has_lift: 基本属性-配备电梯

    trade_created: 交易属性-挂牌时间
    last_trade: 交易属性-上次交易
    house_year: 交易属性-房屋年限
    mortgage: 交易属性-抵押信息
    trade_belong: 交易属性-交易权属
    house_usage: 交易属性-房屋用途
    property_right: 交易属性-产权所属
'''


class Entity:

    def __init__(self, soup, id):
        self.id = id
        self.url = 'https://bj.lianjia.com/ershoufang/%s.html' % id

        price = soup.find('div', {'class':'price'})
        self.total_price = price.find('span', {'class':'total'}).get_text()
        self.single_price = price.find('span', {'class':'unitPriceValue'}).get_text()
        self.level =




    def insert_sql(self, cur):
        return cur.mogrify(
            'insert into lianjia (id,desc,total_price,single_price,level,total_level,total_size,build_year,xiaoqu,'
            'area1,area2,area3,huxing,usage_size,direction,decoration,warm_type,holding_age,room_type,construct_type,'
            'construct_con,lift_type,has_lift,trade_created,last_trade,house_year,mortgage,trade_belong,house_usage,property_right,url) '
            'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (self.id, self.desc, self.total_price, self.single_price, self.level, self.total_level, self.total_size,
             self.build_year, self.xioaqu, self.area1, self.area2, self.area3, self.huxing, self.usage_size, self.direction,
             self.decoration, self.warm_type, self.construct_type, self.construct_con, self.lift_type, self.has_lift,
             self.trade_created, self.last_trade, self.house_year, self.mortgate, self.trade_belong, self.house_usage,
             self.property_right, self.url))



if __name__ == '__main__':
    id = '101101686988'
    soup = BeautifulSoup(open('/Users/Spirit/git/lianjia_crawler/detail/101101686988.html'), 'html.parser')
    entity = Entity(soup, id)
