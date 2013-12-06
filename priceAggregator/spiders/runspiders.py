import os


if __name__ == "__main__":
    os.system('scrapy crawl amzn -o amazon11.json -t json')
    os.system('scrapy crawl ebay -o ebay11.json -t json')
    os.system('scrapy crawl walmart -o walmart11.json -t json')