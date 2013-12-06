import os


if __name__ == "__main__":
    os.system('scrapy crawl amzn -o amazons1.csv -t csv')
    os.system('scrapy crawl ebay -o ebay1.csv -t csv')
    os.system('scrapy crawl walmart -o walmart1.csv -t csv')