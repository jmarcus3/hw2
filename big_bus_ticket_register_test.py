import big_bus_ticket_register_classes as bbtrc
import big_bus_ticket_register as bbtr

import unittest
import datetime

class RegisterTest(unittest.TestCase):
    seller = bbtrc.Seller()
    register = bbtr.AppShell()

    def test_buy(self):
        message = self.register._buy(1, 4, 26, 2018, 'red')
        self.assertEqual(message, "Total price: 10")
unittest.main()
