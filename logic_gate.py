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

        self.PinA = None
        self.PinB = None

    def get_pin_a(self):
        return int(input("Enter Pin A input for gate " + self.get_label()+"-->"))

    def get_pin_b(self):
        return int(input("Enter Pin B input for gate " + self.get_label()+"-->"))


class UnaryGate(self, n):


    def __init__(self):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        return int(input("Enter Pin input for gate " + self.get_label()+"-->"))

