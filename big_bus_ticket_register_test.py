import big_bus_ticket_register_classes as bbtrc
import big_bus_ticket_register as bbtr

import unittest
import datetime

class RegisterTest(unittest.TestCase):
    seller = bbtrc.Seller()
    register = bbtr.AppShell()

    def test_1_buy(self):
        message = self.register._buy(1, 4, 26, 2018, 'red')
        self.assertEqual(message, "Total price: 10")

    def test_2_buy_input(self):
        message = self.register._buy('f', 'k', 'z', 'x', 'j')
        self.assertEqual(message, "Invalid input")

    def test_3_buy_input_2(self):
        message = self.register._buy(1, 15, 72, 2018, 'red')
        self.assertEqual(message, "Invalid input")

    def test_4_refund_refactor(self):
        self.register._buy(1, 4, 26, 2018, 'red')
        message = self.register._refund(2)
        self.assertEqual(message, "Ticket ID# 2 returned. \n Total refund: 10")

    def test_5_refund_refactor_2(self):
        self.register._buy(1, 4, 26, 2018, 'red')
        message = self.register._refund(3)
        self.assertEqual(message, "Ticket ID# 3 returned. \n Total refund: 10")

    def test_6_refund_refactor_3(self):
        self.register._buy(1, 4, 21, 2018, 'red') #refund should be weekend price now
        message = self.register._refund(4)
        self.assertEqual(message, "Ticket ID# 4 returned. \n Total refund: 12")

    def test_7_refund_input(self):
        self.register._buy(1, 4, 21, 2018, 'red')
        message = self.register._refund('5')
        self.assertEqual(message, "Ticket ID# 5 returned. \n Total refund: 12")    

    def test_8_today_input(self):
        message = self.register._today('orange')
        self.assertEqual(message, "Entered line not valid")

    


unittest.main()
