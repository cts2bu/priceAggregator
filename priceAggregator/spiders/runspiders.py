import os


if __name__ == "__main__":
    os.system('scrapy crawl amzn -o amazon9.json -t json')
    os.system('scrapy crawl ebay -o ebay9.json -t json')
#    os.system('scrapy crawl walmart -o walmart1.csv -t csv')