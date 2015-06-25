#!usr/local/bin/python

#Logic Gates and Circuits

class LogicGate:


    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):


    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter Pin A input for gate " + self.get_label()+"-->"))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter Pin B input for gate " + self.get_label()+"-->"))
        else:
            return self.pin_b.get_from().get_output()


class UnaryGate(self, n):


    def __init__(self):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        return int(input("Enter Pin input for gate " + self.get_label()+"-->"))


class AndGate(BinaryGate):


    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class Connector:


    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        self.fromgate

    def get_to(self):
        self.togate


def set_next_pin(self, source):
    if self.pin_a == None:
        self.pin_a = source
    else:
        if self.pin_b == None:
            self.pin_b = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
