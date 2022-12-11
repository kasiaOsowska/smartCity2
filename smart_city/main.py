import tkinter as tk
import DataSetUp
import matplotlib
from tkinter import *
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from datetime import datetime

from ExcelReader import ExcelReader

matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

# przyklad
excelReader = ExcelReader()
tab = DataSetUp.get_avg_month_value(excelReader.LeczkowCO)
#


class App(tk.Tk):
    dataPollen = {
        'luty': 1,
        'marzec': 2,
        'kwiecien': 4,
    }
    dataC = {
        'luty': 1,
        'marzec': 2
    }
    dataN = {
        'luty': 3,
        'marzec': 1
    }

    # Potrzebuję strukture danych ktora bedzie dzialala tak: data = nazwaKlasy.NazwaStacji.date i po takiej operacji bede
    # miec w data liste wszystki dat od najstarszej do najmłodszej, analogicznie tak samo powinny działac wartosci
    # przyklad
    #    excelReader = ExcelReader()
    #    date = excelReader.PowWarsCO.date
    #    amount = excelReader.PowWarsCO.amount

    def makesFigures(self):
        # prepare data

        ####################################################################
        # PM10
        ####################################################################

        # create a figure
        PM10_fig = Figure(figsize=(5, 2), dpi=100)
        # create FigureCanvasTkAgg object
        self.PM10_canvas = FigureCanvasTkAgg(PM10_fig, self)
        # create plot
        self.PM10_plot = PM10_fig.add_subplot()

        # Put plot into grid        
        self.PM10_canvas.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)

        ####################################################################
        # CO
        ####################################################################
        # create a figure
        CO_fig = Figure(figsize=(5, 2), dpi=100)
        # create FigureCanvasTkAgg object
        self.CO_canvas = FigureCanvasTkAgg(CO_fig, self)
        # create plot
        self.CO_plot = CO_fig.add_subplot()

        # Put plot into grid        
        self.CO_canvas.get_tk_widget().grid(row=1, column=0, padx=20, pady=20)

        ####################################################################
        # NO2
        ####################################################################
        # create a figure
        NO2_fig = Figure(figsize=(5, 2), dpi=100)
        # create FigureCanvasTkAgg object
        self.NO2_canvas = FigureCanvasTkAgg(NO2_fig, self)
        # create plot
        self.NO2_plot = NO2_fig.add_subplot()

        # Put plot into grid        
        self.NO2_canvas.get_tk_widget().grid(row=1, column=1, padx=20, pady=20)

        ####################################################################
        # Agglomeration image
        ####################################################################
        image = Image.open("1.gif")

        resize_image = image.resize((390, 260))
        img = ImageTk.PhotoImage(resize_image)

        label1 = Label(image=img)
        label1.image = img
        label1.grid(row=0, column=1, padx=20, pady=20)

    def setPM10(self, dataDict):
        self.PM10_plot.clear()

        self.PM10_plot.set_title('Ilość pyłów PM10 w powietrzu')
        self.PM10_plot.set_ylabel('ug/m^3')
        # create the barchart
        self.PM10_plot.bar(dataDict.keys(), dataDict.values())

        self.PM10_canvas.draw()

    def setCO(self, dataDict):
        self.CO_plot.clear()

        self.CO_plot.bar(dataDict.keys(), dataDict.values())

        self.CO_plot.set_title('ilość tlenku węgla w powietrzu')
        self.CO_plot.set_ylabel('g/m^3')

        self.CO_canvas.draw()

    def setNO2(self, dataDict):
        self.NO2_plot.clear()

        self.NO2_plot.bar(dataDict.keys(), dataDict.values())

        self.NO2_plot.set_title('ilość dwutlenku azotu w powietrzu')
        self.NO2_plot.set_ylabel('g/m^3')

        self.NO2_canvas.draw()

    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')
        self.makesFigures()

        # initialize plots
        self.setPM10(App.dataPollen)
        self.setCO(App.dataC)
        self.setNO2(App.dataN)

        def createNewData(newData):
            self.setPM10(newData)
            self.setCO(newData)
            self.setNO2(newData)
            self.update()

        def motion(event):
            x, y = event.x, event.y
            print('{}, {}'.format(x, y))
            # PMGdyPorebsk
            if x < 130 and x > 1 and y < 80 and y > 9:
                newData = {
                    'porebsk': y,
                    'marzec': x
                }
                createNewData(newData)
            # PmGdySzafran
            if x < 140 and x > 40 and y < 100 and y > 80:
                newData = {
                    'szafran': y,
                    'marzec': x
                }
                createNewData(newData)
            # PmSopBiPlowc
            if x < 135 and x > 70 and y < 140 and y > 100:
                newData = {
                    'Plowc': y,
                    'marzec': x
                }
                createNewData(newData)
            # PmGdaPowWiel
            if x < 185 and x > 90 and y < 175 and y > 140:
                newData = {
                    'Wiel': y,
                    'marzec': x
                }
                createNewData(newData)
            # PmGdaWyzwole
            if x < 345 and x > 185 and y < 200 and y > 175:
                newData = {
                    'Wyzwole': y,
                    'marzec': x
                }
                createNewData(newData)
            # PmGdaLeczkow
            if x < 185 and x > 150 and y < 200 and y > 180:
                newData = {
                    'leczkow': y,
                    'marzec': x
                }
                createNewData(newData)
            # PmGdaPowWars
            if x < 150 and x > 100 and y < 230 and y > 180:
                newData = {
                    'PowWars': y,
                    'marzec': x
                }
                createNewData(newData)

        self.bind('<Motion>', motion)


# example how to read data
# excelReader = ExcelReader()
# for data in excelReader.PowWarsCO:
#   print(data.date + " " + str(data.amount))
app = App()
app.mainloop()
