class StartUrls():
    def __init__(self, input):
        self.search = input.replace(" ", "+")

        url = "http://www.ebay.com/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0."+self.search+"&_nkw="+self.search+"&_sacat=0&_from=R40"
        self.ebayurl = url

        url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+self.search
        self.amazonurl = url

        url = "http://www.walmart.com/search/search-ng.do?ic=16_0&Find=Find&search_query="+self.search
        self.walmarturl = url