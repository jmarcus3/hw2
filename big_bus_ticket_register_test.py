import big_bus_ticket_register_classes as bbtrc
import big_bus_ticket_register as bbtr

import unittest
import datetime

class RegisterTest(unittest.TestCase):
    #seller = bbtrc.Seller()

    def generate_valid_weekend(self):
        the_date = datetime.date.today()
        if the_date.weekday() >= 4:
            the_date += datetime.timedelta(days = 7)
        else:
            the_date += datetime.timedelta(days = 4 - the_date.weekday())

        return the_date

    def generate_valid_weekday(self):
        the_date = datetime.date.today()
        if the_date.weekday() >= 4:
            the_date += datetime.timedelta(days = 3)
        else:
            the_date += datetime.timedelta(days = 7)

        return the_date


    def test_1_buy(self):
        register = bbtr.AppShell()
        ride_date = self.generate_valid_weekday()
        message = register._buy(1, ride_date.month, ride_date.day, ride_date.year, 'red')
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
        ride_date = self.generate_valid_weekday()
        register._buy(1, ride_date.month, ride_date.day, ride_date.year, 'red')
        message = register._refund(1)
        self.assertEqual(message, "Ticket ID# 1 returned. \n Total refund: 10")

    def test_5_refund_refactor_2(self):
        register = bbtr.AppShell()               
        ride_date = self.generate_valid_weekday()
        register._buy(1, ride_date.month, ride_date.day, ride_date.year, 'red')
        message = register._refund(1)
        self.assertEqual(message, "Ticket ID# 1 returned. \n Total refund: 10")

    def test_6_refund_refactor_3(self):
        register = bbtr.AppShell()
        ride_date = self.generate_valid_weekend()
        register._buy(1, ride_date.month, ride_date.day, ride_date.year, 'red') #refund should be weekend price now
        message = register._refund(1)
        self.assertEqual(message, "Ticket ID# 1 returned. \n Total refund: 12")

    def test_7_refund_input(self):
        register = bbtr.AppShell()
        ride_date = self.generate_valid_weekend()
        register._buy(1, ride_date.month, ride_date.day, ride_date.year, 'red')
        message = register._refund('1')
        self.assertEqual(message, "Ticket ID# 1 returned. \n Total refund: 12")    

    def test_8_refund_input_2(self):
        register = bbtr.AppShell()
        ride_date = self.generate_valid_weekend()
        register._buy(1, ride_date.month, ride_date.day, ride_date.year, 'red')
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
        register._addLine('orange', 5) #line name and number of buses on line
        self.assertTrue(type(register.seller._lines_log['orange']) is bbtrc.LinLog)

    def test_14_addLine2(self):
        register = bbtr.AppShell()
        register._addLine('orange', 5)
        self.assertTrue(register.seller._maxes['orange'] == 5*89)

    def test_15_addLine3(self):
        register = bbtr.AppShell()
        register._addLine('orange', 4)
        self.assertTrue(register.seller._maxes['orange'] == 4*89) 

    def test_16_addLine4(self):
        register = bbtr.AppShell()
        message = register._addLine('orange', 4)
        self.assertEquals(message, "New line entered successfully")

    def test_17_addLine_input(self):
        register = bbtr.AppShell()
        message = register._addLine('pink', 'j')
        self.assertEquals(message, "Number of buses must be an integer") 

    def test_18_addLine_input2(self):
        register = bbtr.AppShell()
        message = register._addLine("green", 1)
        self.assertEquals(message, "Bus line already exists, did you mean changeLine?")   

    def test_19_changeLine(self):   
        register = bbtr.AppShell()
        register._changeLine("red", 9)
        self.assertTrue(register.seller._maxes['red'] == 9*89)

    def test_20_changeLine_input(self):
        register = bbtr.AppShell()
        message = register._changeLine("orange", 5)
        self.assertEquals(message, "Bus line doesn't exist, did you mean addLine?")

    def test_21_changeLine_input2(self):        
        register = bbtr.AppShell()
        message = register._changeLine("red", 5)
        self.assertEquals(message, "Line changed successfully")

    def test_22_changeLine_input3(self):
        register = bbtr.AppShell()
        message = register._changeLine("red", 'j')
        self.assertEquals(message, "Number of buses must be an integer")

    def test_23_changeCapacity(self):
        register = bbtr.AppShell()
        register._changeCapacity(92)
        self.assertTrue(register.seller._maxes["red"] == 5*92 and register.seller._maxes["green"] == 4*92 and register.seller._maxes["blue"] == 2*92)

    def test_24_changeCapacity_Message_Success(self):
        register = bbtr.AppShell()
        message = register._changeCapacity(95)
        self.assertEquals(message, "Capacity changed successfully")

    def test_25_changeCapacity_Message_Failure_For_Bad_Number(self):
        register = bbtr.AppShell()
        message = register._changeCapacity(0)
        self.assertEquals(message, "Capacity must be greater than 0")

    def test_26_changeCapacity_With_String_Input(self):
        register = bbtr.AppShell()
        message = register._changeCapacity('92')
        self.assertTrue(register.seller._maxes["red"] == 5*92 and register.seller._maxes["green"] == 4*92 and register.seller._maxes["blue"] == 2*92)        
        self.assertEquals(message, "Capacity changed successfully")        

unittest.main()
