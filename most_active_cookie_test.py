import unittest
from collections import defaultdict
from most_active_cookie import *

class TestMostActiveCookie(unittest.TestCase):
    
    def test_list_int(self):
        date_and_time = "2018-12-09T14:19:19+00:00"
        date = convert_UTC_date(date_and_time)
        self.assertEqual(date, "2018-12-09")
    def test_find_max_cookie_count_for_date(self):
        date = "2018-12-09"
        data_dict = {'2018-12-09': defaultdict(int,
                         {'AtY0laUfhglK3lC7': 2,
                          'SAZuXPGUrfbcn5UA': 1,
                          '5UAVanZf6UtGyKVS': 1}),
             '2018-12-08': defaultdict(int,
                         {'SAZuXPGUrfbcn5UA': 1,
                          '4sMM2LxV07bPJzwf': 1,
                          'fbcn5UAVanZf6UtG': 1}),
             '2018-12-07': defaultdict(int, {'4sMM2LxV07bPJzwf': 1})}
        cookies_for_date, max_count = find_max_cookie_count_for_date(data_dict, date)
        
        expected_cookies_for_date = defaultdict(int)
        data_list = [('AtY0laUfhglK3lC7', 2), ('SAZuXPGUrfbcn5UA', 1), ('5UAVanZf6UtGyKVS', 1)]
        for cookie, count in data_list:
            expected_cookies_for_date[cookie]=count
        
        self.assertEqual(cookies_for_date, expected_cookies_for_date)
        self.assertEqual(max_count, 2)
    def test_find_most_active_cookies(self):
        cookies_for_date = defaultdict(int,
            {'SAZuXPGUrfbcn5UA': 2,
             '4sMM2LxV07bPJzwf': 1,
             'fbcn5UAVanZf6UtG': 1})
        max_count = 2
        most_active_cookies = find_most_active_cookies(cookies_for_date, max_count)
        expected_most_active_cookies = ['SAZuXPGUrfbcn5UA']
        self.assertEqual(most_active_cookies, expected_most_active_cookies)

if __name__ == '__main__':
    unittest.main()