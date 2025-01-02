import re
from locators.book_locators import BookLocators
from logger_config import logger


class BookParser:
    """
    This class to take in an HTML page (or part of it),
    and find properties of an item in it.
    """

    RATINGS = {
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }


    def __init__(self, parent):
        #logger.debug(f'New book parser created from {parent}')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price} ({self.rating} stars)>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Found book name, `{item_name}`.')
        return item_name
    
    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator)
        link_name = item_link.attrs['href']
        logger.debug(f'Found book link, `{link_name}`.')
        return link_name
    
    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        logger.debug(f'Found book price, `{float(matcher.group(1))}`.')
        return float(matcher.group(1))
    
    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class'] # ['star-rating', 'Three']
        rating_class = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_class[0])
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_class[0]
    