class StartUrls():
    searchterms = ["thai+diet", "slug+soda+rare"]
    ebayurls = []
    for term in searchterms:
        url = "http://www.ebay.com/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0."+term+"&_nkw="+term+"&_sacat=0&_from=R40"
        ebayurls.append(url)
