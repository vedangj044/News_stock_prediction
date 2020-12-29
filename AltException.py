class InvalidTicker(Exception):
    def __init__(self, msg='Can\'t find ticker of this brand name.'):
        super().__init__(msg)

class InvalidQuery(Exception):
    def __init__(self, msg="""Google can\'t find enough news data
                                for this query: Invalid query"""):
        super().__init__(msg)
