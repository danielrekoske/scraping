
import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
import random

class AmazonScraper:
    def __init__(self, proxies=None, user_agents=None):
        self.base_url = "https://www.amazon.com"
        self.proxies = proxies
        self.user_agents = user_agents
    
    def get_random_user_agent(self):
        """
        Get a random user-agent string from the provided list.
        """
        if self.user_agents:
            return random.choice(self.user_agents)
        else:
            return None

    async def fetch(self, session, url, headers):
        async with session.get(url, headers=headers, proxy=self.proxies) as response:
            return await response.text()

    async def scrape_product(self, product_name):
        try:
            search_url = f"{self.base_url}/s?k={product_name}"
            headers = {'User-Agent': self.get_random_user_agent()}
            async with aiohttp.ClientSession() as session:
                html = await self.fetch(session, search_url, headers)
                soup = BeautifulSoup(html, 'html.parser')
                product_link = soup.find('a', class_='a-link-normal')
                if product_link:
                    product_url = self.base_url + product_link['href']
                    product_info = await self.scrape_product_details(product_url)
                    return product_info
                else:
                    print("Product not found")
                    return None
        except Exception as e:
            print("An error occurred:", e)
            return None

    async def scrape_product_details(self, product_url):
        try:
            headers = {'User-Agent': self.get_random_user_agent()}
            async with aiohttp.ClientSession() as session:
                html = await self.fetch(session, product_url, headers)
                soup = BeautifulSoup(html, 'html.parser')
                product_info = {}
                product_info['title'] = self.extract_title(soup)
                product_info['price'] = self.extract_price(soup)
                product_info['reviews'] = self.extract_reviews(soup)
                product_info['ratings'] = self.extract_ratings(soup)
                product_info['seller_info'] = self.extract_seller_info(soup)
                product_info['shipping_info'] = self.extract_shipping_info(soup)
                product_info['image_url'] = self.extract_image_url(soup)
                return product_info
        except Exception as e:
            print("An error occurred:", e)
            return None

    async def search_products(self, query, num_pages=1):
        try:
            product_urls = []
            for page in range(1, num_pages + 1):
                headers = {'User-Agent': self.get_random_user_agent()}
                search_url = f"{self.base_url}/s?k={query}&page={page}"
                async with aiohttp.ClientSession() as session:
                    html = await self.fetch(session, search_url, headers)
                    soup = BeautifulSoup(html, 'html.parser')
                    for link in soup.find_all('a', class_='a-link-normal'):
                        product_urls.append(self.base_url + link['href'])
            return product_urls
        except Exception as e:
            print("An error occurred:", e)
            return None
    def extract_title(self, soup):
        """
        Extract the title of the product.
        """
        title_element = soup.find('span', id='productTitle')
        if title_element:
            return title_element.text.strip()
        else:
            return None

    def extract_price(self, soup):
        """
        Extract the price of the product.
        """
        price_element = soup.find('span', id='priceblock_ourprice') or soup.find('span', id='priceblock_dealprice')
        if price_element:
            return price_element.text.strip()
        else:
            return None

    def extract_reviews(self, soup):
        """
        Extract the number of reviews for the product.
        """
        reviews_element = soup.find('span', id='acrCustomerReviewText')
        if reviews_element:
            return reviews_element.text.strip()
        else:
            return None

    def extract_ratings(self, soup):
        """
        Extract the rating of the product.
        """
        ratings_element = soup.find('span', class_='a-icon-alt')
        if ratings_element:
            return ratings_element.text.strip()
        else:
            return None

    def extract_seller_info(self, soup):
        """
        Extract information about the seller.
        """
        seller_info = {}
        seller_name_element = soup.find('a', id='sellerProfileTriggerId')
        if seller_name_element:
            seller_info['name'] = seller_name_element.text.strip()
        else:
            seller_info['name'] = None
        
        seller_rating_element = soup.find('span', class_='seller-rating')
        if seller_rating_element:
            seller_info['rating'] = seller_rating_element.text.strip()
        else:
            seller_info['rating'] = None
        
        seller_feedback_element = soup.find('a', class_='seller-feedback')
        if seller_feedback_element:
            seller_info['feedback'] = seller_feedback_element.text.strip()
        else:
            seller_info['feedback'] = None

        return seller_info
    
    def extract_shipping_info(self, soup):
        """
        Extract shipping information of the product.
        """
        shipping_info_element = soup.find('div', id='merchant-info')
        if shipping_info_element:
            shipping_info = shipping_info_element.find('span', class_='a-color-secondary').text.strip()
            return shipping_info
        else:
            return None
    
    def extract_image_url(self, soup):
        """
        Extract the URL of the product image.
        """
        try:
            image_element = soup.find('img', class_='s-image')
            if image_element:
                return image_element['src']
            else:
                return None
        except Exception as e:
            print("An error occurred while extracting image URL:", e)
            return None

        
async def main():
    # Instantiate the scraper with user-agents
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
    ]

    scraper = AmazonScraper(user_agents=user_agents)

    # Search for products asynchronously
    product_urls = await scraper.search_products("laptop", num_pages=1)
    if product_urls:
        # Scrape product details asynchronously
        tasks = [scraper.scrape_product(url) for url in product_urls]
        product_infos = await asyncio.gather(*tasks)
        for product_info in product_infos:
            print(product_info)

# Run the event loop
asyncio.run(main())