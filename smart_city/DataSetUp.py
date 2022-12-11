from datetime import datetime
import numpy


def get_avg_month_value(tab):
    months = numpy.empty(12, dtype=float)
    amount_of_values = numpy.empty(12, dtype=int)

    for x in range(12):
        months[x] = 0
        amount_of_values[x] = 0

    for element in tab:
        datetime_object = datetime.strptime(element.date, '%Y-%m-%d %H:%M:%S')
        month = datetime_object.month
        if element.amount is not None:
            months[month - 1] += element.amount
            amount_of_values += 1

    for x in range(12):
        months[x] = months[x] / amount_of_values[x]

    return months
