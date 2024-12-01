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

soup = BeautifulSoup(ITEM_HTML, 'html.parser')

"""
We will learn how to locate items in the HTML
"""


def find_title():
    locator = "article.product_pod h3 a"
    link = soup.select_one(locator)
    item_name = link.attrs['title']
    return item_name

def find_href():
    locator = "article.product_pod h3 a"
    link = soup.select_one(locator)
    item_name = link.attrs['href']
    return item_name

def find_price():
    locator = "article.product_pod" # article has class product_pod
    link = soup.select_one(locator)
    item_price = link.find('p', {'class':'price_color'})
    price = item_price.string
    expression = '\£[0-9]*\.[0-9]*'
    matches = re.search(expression, price)
    return matches.group(0)

# The following is the another way to find the price
def find_item_price():
    locator = 'article.product_pod p.price_color'
    item_price = soup.select_one(locator).string
    
    pattern = "£([0-9]+\.[0-9]+)"
    matches = re.search(pattern, item_price)
    return float(matches.group(1))


def find_rating():
    locator = 'article.product_pod p.star-rating'
    rating_tag = soup.select_one(locator)
    classes = rating_tag.attrs['class'] # ['star-rating', 'Three']
    # To filter only the star-rating
    rating_classes = filter(lambda x: x != 'star-rating', classes)
    return rating_classes.__next__()


print(find_title())
print(find_href())
print(find_price())
print(find_item_price())
print(find_rating())