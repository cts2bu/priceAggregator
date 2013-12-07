import unittest
from priceAggregator.parsers.AmazonCSVParser import AmazonCSVParser
from priceAggregator.parsers.eBayCSVParser import eBayCSVParser
from priceAggregator.parsers.WalmartCSVParser import WalmartCSVParser


#This tests spider crawling methods, particularly in relation to start-url activity generation.
class TestParsers(unittest.TestCase):
    def test_amazon_parser(self):
        testrow = (' $14.61', '$9.69,$5.97,$160.00', 'http://www.amazon.com/The-Brothers-Karamazov-Fyodor-Dostoevsky/dp/0374528373/ref=sr_1_1/183-3455075-0111269?ie=UTF8&qid=1386454473&sr=8-1&keywords=the+brothers+karamazov', 'The Brothers Karamazov')
        newparser = AmazonCSVParser()
        self.assertEquals(newparser.printCSV(testrow), 'The Brothers Karamazov $9.69')

    def test_ebay_parser(self):
        testrow = ('', '\n\t\t\t\t\t$21.48', 'http://www.ebay.com/itm/Deerhunter-Halcyon-Digest-Vinyl-New-/360680697978?pt=Music_on_Vinyl&hash=item53fa3eb07a', 'Deerhunter - Halcyon Digest [Vinyl New]')
        newparser = eBayCSVParser()
        self.assertEquals(newparser.printCSV(testrow), 'Deerhunter - Halcyon Digest [Vinyl New] $21.48')

    def test_walmart_parser(self):
        testrow = ('$26.', '$26.', 'www.walmart.com/ip/Elite-Rain-Premium-Fiberglass-Bubble-Umbrella/21731715', 'Elite Rain Premium Fiberglass Bubble Umbrella')
        newparser = WalmartCSVParser()
        self.assertEquals(newparser.printCSV(testrow), 'Elite Rain Premium Fiberglass Bubble Umbrella $26')

if __name__ == '__main__':
    unittest.main()