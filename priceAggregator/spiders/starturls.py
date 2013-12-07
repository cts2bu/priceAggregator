class StartUrls():
    def __init__(self, search):
        self.search = search
        self.search.replace(" ","+")
        self.ebayurls = []
        self.amazonurls = []
        self.walmarturls = []
        # don't judge em joe brown

        url = "http://www.ebay.com/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0."+self.search+"&_nkw="+self.search+"&_sacat=0&_from=R40"
        self.ebayurls.append(url)

        url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+self.search
        self.amazonurls.append(url)

        url = "http://www.walmart.com/search/search-ng.do?ic=16_0&Find=Find&search_query="+self.search
        self.walmarturls.append(url)

    # searches = ["thai", "desk", "paper"]
    #
    # ebayurls = []
    # amazonurls = []
    # walmarturls = []
    # rakutenurls = []
    #
    # for search in searches:
    #
    #     search.replace(" ","+")
    #
    #     url = "http://www.ebay.com/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0."+search+"&_nkw="+search+"&_sacat=0&_from=R40"
    #     ebayurls.append(url)
    #
    #     url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+search
    #     amazonurls.append(url)
    #
    #     url = "http://www.walmart.com/search/search-ng.do?ic=16_0&Find=Find&search_query="+search
    #     walmarturls.append(url)
    #
    #     url = "http://www.rakuten.com/sr/searchresults.aspx?qu="+search
    #     rakutenurls.append(url)
