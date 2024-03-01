import unittest
from unittest.mock import MagicMock, patch, AsyncMock
import asyncio
from amazonScraper import AmazonScraper

class TestAmazonScraper(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # Define some sample user-agents and a mock response for HTTP requests
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
        ]
        self.mock_response = MagicMock()

    async def test_scrape_product(self):
        # Mock the fetch method to return a sample HTML response
        with patch('amazon_scraper.AmazonScraper.fetch', new_callable=AsyncMock) as mock_fetch:
            mock_fetch.return_value.text.return_value = '<html><body><a class="a-link-normal" href="https://example.com/product"></a></body></html>'
            scraper = AmazonScraper(user_agents=self.user_agents)
            product_info = await scraper.scrape_product("laptop")
            self.assertIsNotNone(product_info)
            # Assert that the correct product information is extracted
            self.assertEqual(product_info['title'], 'Test Product')
            self.assertEqual(product_info['price'], '$999.99')
            self.assertEqual(product_info['reviews'], '1000 reviews')
            self.assertEqual(product_info['ratings'], '4.5 out of 5 stars')
            self.assertEqual(product_info['seller_info']['name'], 'Test Seller')
            self.assertEqual(product_info['seller_info']['rating'], '4.8 out of 5')
            self.assertEqual(product_info['seller_info']['feedback'], '100% positive feedback')
            self.assertEqual(product_info['shipping_info'], 'Free Shipping')
            self.assertEqual(product_info['image_url'], 'https://example.com/product/image.jpg')

    async def test_search_products(self):
        # Mock the fetch method to return a sample HTML response with product links
        with patch('amazon_scraper.AmazonScraper.fetch', new_callable=AsyncMock) as mock_fetch:
            mock_fetch.return_value.text.return_value = '<html><body><a class="a-link-normal" href="/product/1"></a><a class="a-link-normal" href="/product/2"></a></body></html>'
            scraper = AmazonScraper(user_agents=self.user_agents)
            product_urls = await scraper.search_products("laptop", num_pages=1)
            self.assertEqual(len(product_urls), 2)
            self.assertIn('https://www.amazon.com/product/1', product_urls)
            self.assertIn('https://www.amazon.com/product/2', product_urls)

if __name__ == '__main__':
    unittest.main()
