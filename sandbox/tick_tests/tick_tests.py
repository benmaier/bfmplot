"""
A class to compute nicer axis limits,
adapted from https://stackoverflow.com/a/16959142/4177832

This file is licensed unter the CC BY-SA 3.0 license
https://creativecommons.org/licenses/by-sa/3.0/
"""
import math

class NiceScale():

    def __init__(self, minv, maxv):

        self.maxTicks = 6
        self.tickSpacing = 0
        self.lst = 10
        self.niceMin = 0
        self.niceMax = 0
        self.minPoint = minv
        self.maxPoint = maxv
        self.calculate()

    def calculate(self):

        self.lst = self.niceNum(self.maxPoint - self.minPoint, False)
        self.tickSpacing = self.niceNum(self.lst / (self.maxTicks - 1), True)
        self.niceMin = math.floor(self.minPoint / self.tickSpacing) * self.tickSpacing
        self.niceMax = math.ceil(self.maxPoint / self.tickSpacing) * self.tickSpacing

    def niceNum(self, lst, rround):

        self.lst = lst
        exponent = 0 # exponent of range */
        fraction = 0 # fractional part of range */
        niceFraction = 0 # nice, rounded fraction */

        exponent = math.floor(math.log10(self.lst));
        fraction = self.lst / math.pow(10, exponent);

        if (rround):
            if (fraction < 1.5):
                niceFraction = 1
            elif (fraction < 3):
                niceFraction = 2
            elif (fraction < 7):
                niceFraction = 5;
            else:
                niceFraction = 10;
        else :
            if (fraction <= 1):
                niceFraction = 1
            elif (fraction <= 2):
                niceFraction = 2
            elif (fraction <= 5):
                niceFraction = 5
            else:
                niceFraction = 10

        return niceFraction * math.pow(10, exponent)

    def setMinMaxPoints(self, minPoint, maxPoint):
        self.minPoint = minPoint
        self.maxPoint = maxPoint
        self.calculate()

    def setMaxTicks(self, maxTicks):
        self.maxTicks = maxTicks;
        self.calculate()

    def __str__(self):

        s = ""
        s += "NiceScale.lst = " + str(self.lst)
        s += "\nNiceScale.maxPoint = " + str(self.maxPoint)
        s += "\nNiceScale.maxTicks = " + str(self.maxTicks)
        s += "\nNiceScale.minPoint = " + str(self.minPoint)
        s += "\nNiceScale.niceMax = " + str(self.niceMax)
        s += "\nNiceScale.niceMin = " + str(self.niceMin)
        s += "\nNiceScale.tickSpacing = " + str(self.tickSpacing)

        return s


if __name__=="__main__":

    a = NiceScale(14024, 17756)
    print(a)

    a = NiceScale(0, 0.3)
    print(a)
