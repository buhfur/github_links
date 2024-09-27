import scrapy

# Created using Chatgpt 
# Author : Ryan McVicker 

class GithubSpider(scrapy.Spider):
    name = 'github_spider'
    # Starting URL(s)
    start_urls = ['https://example.com']  # Replace with the target website

def parse(self, response):
    # Extract all links on the page
    links = response.css('a::attr(href)').getall()

    # Filter for GitHub links
    github_links = [link for link in links if 'github.com' in link]

    # Save the links to a file
    with open('github_links.txt', 'a') as f:
        for link in github_links:
            f.write(link + '\n')

    # Follow pagination links (optional)
    for next_page in response.css('a::attr(href)').getall():
        yield response.follow(next_page, self.parse)

