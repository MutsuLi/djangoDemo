# !/usr/bin/python3
# business class with Strategy mode


class BusinessAbstract(object):
    def handle(self, queryStr):
        pass


class firstBusiness(BusinessAbstract):

    def __init__(self, * args):
        pass

    def handle(self, queryStr=''):
        pass


class secondBusiness:

    def __init__(self, * args):
        pass

    def handle(self, queryStr=''):
        pass


class thirdBusiness:

    def __init__(self, *args):
        pass

    def handle(self, queryStr=''):
        pass


class BusinessContext(object):
    BusinessTypeStrategy = {"firstBusiness": firstBusiness,
                            "secondBusiness": secondBusiness, 'thirdBusiness': thirdBusiness}

    def __init__(self, *args):
        args = args + (None,) * (3 - len(args))
        # self.strategyType = strategyType
        # self.connStr = connStr
        self.__strategy = self.init__strategy(args[0])(args[1:])

    def init__strategy(self, strategyType):
        if strategyType not in BusinessContext.BusinessTypeStrategy:
            raise Exception('策略未实现:'+strategyType)
        return BusinessContext.BusinessTypeStrategy.get(strategyType)

    def handleSanction(self, queryStr):
        if queryStr is None:
            queryStr = self.queryStr
        return self.__strategy.handle(queryStr)


if __name__ == '__main__':
    pass
