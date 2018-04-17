# Python 3
# Example for how to build a command-line application

import cmd
import datetime
import big_bus_ticket_register_classes


class AppShell(cmd.Cmd):
    def __init__(self):
      super().__init__()
      self.intro = "\nWelcome to the My App!\nType `help` or `?` to list commands.\n"
      self.prompt = '> '
      self.event = None
      self.seller = big_bus_ticket_register_classes.Seller()

    def do_quit(self, arg):
      """Quit"""
      return True

    def do_buy(self, args):
      """Buy a Ticket"""
      #print("TO DO: Implement buying a ticket")
      count = input("Enter number of tickets: ")
      print("Enter ticket date:")
      month = input("   Month (1-12): ")
      day = input("   Day (1-31): ")
      year = input("   Year (xxxx): ")
      line = input("Enter line: ")
      print(self._buy(count, month, day, year, line))

    def _buy(self, count, month, day, year, line):
        try:
            count = int(count)
            month = int(month)
            day = int(day)
            year = int(year)
            date = datetime.date(year, month, day)
        except:
            return "Invalid input"

        return self.seller.sell(count, date, line)
    

    def do_refund(self, args):
      """Refund a Ticket"""
      #print("TO DO: Implement refunding a ticket")
      ticket_id = input("Enter ticket ID number: ")
      print(self._refund(ticket_id))
    
    def _refund(self, ticket_id):
      try:
        ticket_id = int(ticket_id)
      except:
        return "Invalid input"
      return self.seller.refund(ticket_id)

    def do_today(self, args):
      """Generate a current report for today's sales on a specified line"""
      line = input("Enter line for report: ")
      print(self._today(line))

    def _today(self, line):
      purchase_date = datetime.date.today()
      try:
        return f"--REPORT FOR TODAY--\nLINE: {line}\nTIME STAMP: {datetime.datetime.today()}\nTICKETS SOLD: {self.seller.dateLog(line, purchase_date)}"
      except:
        return"Entered line not valid"


    def do_report(self, args):
      """Generate a report for the sales on a specified date for all lines"""
      print("Enter date for report:")
      month = input("   Month (1-12): ")
      day = input("   Day (1-31): ")
      year = input("   Year (xxxx): ")
      self._report(month, day, year)

    def _report(self, month, day, year):
      try:
        purchase_date = datetime.date(int(year), int(month), int(day))
      except:
        print("Invalid input")
        return "Invalid input" #for testing and to hop out of the method
      report = self.seller.log(purchase_date)
      total = 0
      print(f"--REPORT FOR {purchase_date}--")
      for entry in report:
        x = report[entry]
        total += x
        print(f"  {entry}: {x}")
      print(f"  Total: {total}")


    def do_setPrice(self, args):
      """Set weekday and weekend prices"""
      weekday = input("Enter weekday price: ")
      weekend = input("Enter weekend price: ")
      self._setPrice(weekday, weekend)


    def _setPrice(self, weekday, weekend):
      try:
        weekday = int(weekday)
        weekend = int(weekend)
      except:
        print("Invalid input")
        return("Invalid input")
      if weekday >= weekend:
        print("Weekend price must be greater than weekday price. Prices not updated.")
      else:
        self.seller.WEEKDAY_PRICE = weekday
        self.seller.WEEKEND_PRICE = weekend
        print("Prices updated.")  

    def do_addLine(self, args):
     """Add a new bus line"""
     line = input("Enter name of new line: ")
     buses = input("Enter number of buses on line: ")
     print(self._addLine(line, buses))

    def _addLine(self, line, buses):
      try:
        return(self.seller.addLine(line, int(buses))) 
      except:
        return "Number of buses must be an integer" 


if __name__ == '__main__':
    AppShell().cmdloop()
