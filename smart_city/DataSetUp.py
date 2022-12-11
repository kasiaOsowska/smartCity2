from datetime import datetime
from turtle import pd

import numpy


def get_avg_month_value(tab):
    months = numpy.empty(12, dtype=float)
    howmanyData = numpy.empty(12, dtype=int)

    for x in range(12):
        months[x] = 0
        howmanyData[x] = 0

    for element in tab:
        datetime_object = datetime.strptime(element.date, '%Y-%m-%d %H:%M:%S')
        month = datetime_object.month
        if element.amount != None:
            months[month-1] += element.amount
            howmanyData += 1

    for x in range(12):
        months[x] = months[x] / howmanyData[x]

    return months


