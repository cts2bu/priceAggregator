import os


if __name__ == "__main__":
    os.system('scrapy crawl amzn -o amazon3.json -t json')
    os.system('scrapy crawl ebay -o ebay3.json -t json')
    os.system('scrapy crawl walmart -o walmart3.json -t json')