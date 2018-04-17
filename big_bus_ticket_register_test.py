import big_bus_ticket_register_classes as bbtrc

import unittest
import datetime

class RegisterTest(unittest.TestCase):
    seller = bbtrc.Seller()

    def test_sell_count_input(self):
        today = datetime.date.today()
        sold_message = self.seller.sell('j', today, 'blue')
        self.assertEqual("Number of tickets must be an integer", sold_message)

unittest.main()
