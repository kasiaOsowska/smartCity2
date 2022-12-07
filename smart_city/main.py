from smart_city.ExcelReader import ExcelReader


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

#example how to read data
excelReader = ExcelReader()
for data in excelReader.PowWarsCO:
    print(data.date + " " + str(data.amount))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
