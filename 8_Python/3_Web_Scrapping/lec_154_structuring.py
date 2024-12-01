from bs4 import BeautifulSoup
import re

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''

class ParsedItemLocator:
    """
    This class is used to saved the locators for the HTML
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:

    def __init__(self, page):
        self.soup = BeautifulSoup(ITEM_HTML, 'html.parser')
    
    @property
    def find_title(self):
        locator = ParsedItemLocator.NAME_LOCATOR
        link = self.soup.select_one(locator)
        item_name = link.attrs['title']
        return item_name

    @property
    def find_href(self):
        locator = ParsedItemLocator.NAME_LOCATOR
        link = self.soup.select_one(locator)
        item_name = link.attrs['href']
        return item_name
    
    @property
    def find_price(self):
        locator = "article.product_pod" # article has class product_pod
        link = self.soup.select_one(locator)
        item_price = link.find('p', {'class':'price_color'})
        price = item_price.string
        expression = '\£[0-9]*\.[0-9]*'
        matches = re.search(expression, price)
        return matches.group(0)

    
    # The following is the another way to find the price
    @property
    def find_item_price(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string
        
        pattern = "£([0-9]+\.[0-9]+)"
        matches = re.search(pattern, item_price)
        return float(matches.group(1))

    @property
    def find_rating(self):
        locator = ParsedItemLocator.RATING_LOCATOR
        rating_tag = self.soup.select_one(locator)
        classes = rating_tag.attrs['class'] # ['star-rating', 'Three']
        # To filter only the star-rating
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        return rating_classes.__next__()


mypage = ParsedItem(ITEM_HTML)

print(mypage.find_title)
print(mypage.find_href)
print(mypage.find_price)
print(mypage.find_item_price)
print(mypage.find_rating)