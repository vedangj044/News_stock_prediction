class InvalidTicker(Exception):
    def __init__(self, msg='Can\'t find ticker of this brand name.'):
        """ The brand is registered using a different ticker
            or the brand name is invalid. The history data can't
            be fetched.
        """
        super().__init__(msg)

class InvalidQuery(Exception):
    def __init__(self, msg="""Google can\'t find enough news data for this query: Invalid query"""):
        """The query is either gibberish or irrelevent"""
        super().__init__(msg)
