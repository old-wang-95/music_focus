import unittest

from music_focus.api import chrome_api


class MyTestCase(unittest.TestCase):

    def test(self):
        url = 'https://m.weibo.cn/u/1757519727'
        selector = '.card.m-panel.card9.weibo-member'
        for i, element in enumerate(chrome_api.find_elements_in_page(url, selector)):
            chrome_api.screenshot(element, 'post-{}.png'.format(i), 'tests/data')


if __name__ == '__main__':
    unittest.main()
