import datetime

class Ticket:
    
    def __init__(self, ticket_id, purchase_date, ride_date, line, price):
        self.ticket_id = ticket_id 
        self.purchase_date = purchase_date # date of purchase
        self.ride_date = ride_date # date for ride
        self.line = line
        self.price = price

class LinLog:
    def __init__(self):
        self._ride_date_log = {} # logging ride dates
        self._purchase_date_log = {} # logging purchase dates

    def add(self, ride_date, purchase_date):
        if ride_date in self._ride_date_log:
            self._ride_date_log[ride_date] += 1
        else:
            self._ride_date_log[ride_date] = 1
        if purchase_date in self._purchase_date_log:
            self._purchase_date_log[purchase_date] += 1
        else:
            self._purchase_date_log[purchase_date] = 1

    def sub(self, ride_date, purchase_date):
        self._ride_date_log[ride_date] -= 1
        self._purchase_date_log[purchase_date] -= 1

    def getCount(self, purchase_date):
        if purchase_date in self._purchase_date_log:
            return self._purchase_date_log[purchase_date]
        else:
            return 0

class Seller:
    def __init__(self):
        self._id_counter = 0
        self._ticket_log = {}
        self._lines_log = {"red" : LinLog(), "green" : LinLog(), "blue" : LinLog()}
        self._maxes = {"red" : 5*89, "green" : 4*89, "blue" : 2*89}
        self.WEEKDAY_PRICE = 10 #base price for weekdays (default values)
        self.WEEKEND_PRICE = 12 #weekend surcharge (default values)

    def _sell(self, today, date, line, price):
        self._id_counter += 1
        tick = Ticket(self._id_counter, today, date, line, price)
        self._ticket_log[tick.ticket_id] = tick
        self._lines_log[line].add(date, today)        
        print(f"Ticket ID# {tick.ticket_id} sold successfully")

    def sell(self, count, date, line):
        today = datetime.date.today()
        sale = self.WEEKDAY_PRICE
        total = 0

        if date.weekday() >= 4: #if ticket date is fri-sun, add surcharge 
            sale = self.WEEKEND_PRICE        

        if (date - today).days < 0 or (date - today).days > 10:
            return "Invalid ticket date"
        
        if count > 4:
            return "Invalid number of tickets"

        if self._lines_log[line].getCount(date) + count > self._maxes[line]:
            return "Not enough tickets left on this line"

        if count == 4:
            sale = .9 * sale

        for i in range(count):
            self._sell(today, date, line, sale)
            total += sale

        return f"Total price: {total}"

    def refund(self, ticket_id):
        refund = 0
        
        if ticket_id in self._ticket_log:            
            tick = self._ticket_log[ticket_id]
            if (tick.ride_date - datetime.date.today()).days > 0: 
                self._lines_log[tick.line].sub(tick.ride_date, tick.purchase_date)
                refund = tick.price
                del self._ticket_log[ticket_id]
                return f"Ticket ID# {ticket_id} returned. \n Total refund: {refund}"
            else:
                return "Cannot refund ticket on or after trip date"
        else:
            return "No record of purchase"

    def dateLog(self, line, purchase_date):
        sold = self._lines_log[line].getCount(purchase_date)
        return sold
    
    def log(self, purchase_date):
        report = {}
        for line in self._lines_log:
            report[line] = self.dateLog(line, purchase_date)
        return report

    def addLine(self, line, buses):
        if line in self. _lines_log:
            return "Bus line already exists, did you mean changeLine?"
        self._lines_log[line] = LinLog()
        self._maxes[line] = buses * 89
        return "New line entered successfully" 

    def changeLine(self, line, buses):
        self._maxes[line] = buses * 89