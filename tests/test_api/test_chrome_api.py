import unittest

from music_focus.api import chrome_api
from music_focus.api.weibo_api import USER_POSTS_URL_FORMATTER, POSTS_CSS_SELECTOR


class MyTestCase(unittest.TestCase):

    def test(self):
        url = USER_POSTS_URL_FORMATTER.format(1757519727)
        selector = POSTS_CSS_SELECTOR
        for i, element in enumerate(chrome_api.find_elements_in_page(url, selector)):
            chrome_api.screenshot(element, 'tests/data/post-{}.png'.format(i))


if __name__ == '__main__':
    unittest.main()
