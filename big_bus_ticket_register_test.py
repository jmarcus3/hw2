import big_bus_ticket_register_classes as bbtrc
import big_bus_ticket_register as bbtr

import unittest
import datetime

class RegisterTest(unittest.TestCase):
    #seller = bbtrc.Seller()

    def test_1_buy(self):
        register = bbtr.AppShell()
        message = register._buy(1, 4, 26, 2018, 'red')
        self.assertEqual(message, "Total price: 10")

    def test_2_buy_input(self):
        register = bbtr.AppShell()
        message = register._buy('f', 'k', 'z', 'x', 'j')
        self.assertEqual(message, "Invalid input")

    def test_3_buy_input_2(self):
        register = bbtr.AppShell()        
        message = register._buy(1, 15, 72, 2018, 'red')
        self.assertEqual(message, "Invalid input")

    def test_4_refund_refactor(self):
        register = bbtr.AppShell()        
        register._buy(1, 4, 26, 2018, 'red')
        message = register._refund(1)
        self.assertEqual(message, "Ticket ID# 1 returned. \n Total refund: 10")

    def test_5_refund_refactor_2(self):
        register = bbtr.AppShell()               
        register._buy(1, 4, 26, 2018, 'red')
        message = register._refund(1)
        self.assertEqual(message, "Ticket ID# 1 returned. \n Total refund: 10")

    def test_6_refund_refactor_3(self):
        register = bbtr.AppShell()
        register._buy(1, 4, 21, 2018, 'red') #refund should be weekend price now
        message = register._refund(1)
        self.assertEqual(message, "Ticket ID# 1 returned. \n Total refund: 12")

    def test_7_refund_input(self):
        register = bbtr.AppShell()
        register._buy(1, 4, 21, 2018, 'red')
        message = register._refund('1')
        self.assertEqual(message, "Ticket ID# 1 returned. \n Total refund: 12")    

    def test_8_refund_input_2(self):
        register = bbtr.AppShell()
        register._buy(1, 4, 21, 2018, 'red')
        message = register._refund('r')
        self.assertEqual(message, "Invalid input")           

    def test_9_today_input(self):
        register = bbtr.AppShell()
        message = register._today('orange')
        self.assertEqual(message, "Entered line not valid")

    def test_10_report_input(self):
        register = bbtr.AppShell()
        message = register._report('a', 'j', 'c')
        self.assertEqual(message, "Invalid input")

    def test_11_setPrice_input(self):
        register = bbtr.AppShell()
        message = register._setPrice("j", 'b')
        self.assertEqual(message, "Invalid input")

    def test_12_setPrice_test(self):
        register = bbtr.AppShell()
        register._setPrice(9, 14)
        prices = [register.seller.WEEKDAY_PRICE, register.seller.WEEKEND_PRICE]
        self.assertEqual(prices, [9, 14])

    def test_13_addLine(self):
        register = bbtr.AppShell()
        register._add_line('orange', 5) #line name and number of buses on line
        self.assertTrue(type(register.seller._lines_log['orange']) is bbtrc.LinLog)


    

unittest.main()
