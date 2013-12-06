class StartUrls():
    searches = ["thai diet", "slug soda rare"]
    ebayurls = []
    for search in searches:
        search.replace(" ","+")
        url = "http://www.ebay.com/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0."+search+"&_nkw="+search+"&_sacat=0&_from=R40"
        ebayurls.append(url)
