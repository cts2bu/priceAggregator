import os

class StartUrls():

    searches = ["thai diet", "slug soda rare"]

    ebayurls = []
    amazonurls = []
    walmarturls = []

    for search in searches:

        search.replace(" ","+")

        url = "http://www.ebay.com/sch/i.html?_trksid=p2050601.m570.l1313.TR0.TRC0."+search+"&_nkw="+search+"&_sacat=0&_from=R40"
        ebayurls.append(url)

        url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+search
        amazonurls.append(url)

        url = "http://www.walmart.com/search/search-ng.do?ic=16_0&Find=Find&search_query="+search
        walmarturls.append(url)


if __name__ == "__main__":
    os.system('scrapy crawl walmart -o walmart.csv -t csv')