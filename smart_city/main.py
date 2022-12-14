import tkinter as tk
import DataSetUp
import matplotlib
from tkinter import *
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from ExcelReader import ExcelReader

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)

matplotlib.use('TkAgg')
excelReader = ExcelReader()


class App(tk.Tk):

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

        self.PM10_plot.set_title('Ilo???? py????w PM10 w powietrzu')
        self.PM10_plot.set_ylabel('ug/m^3')
        # create the barchart
        self.PM10_plot.bar(self.miesiace, dataDict)

        self.PM10_canvas.draw()

    def setCO(self, dataDict):
        self.CO_plot.clear()

        self.CO_plot.bar(self.miesiace, dataDict)

        self.CO_plot.set_title('ilo???? tlenku w??gla w powietrzu')
        self.CO_plot.set_ylabel('g/m^3')

        self.CO_canvas.draw()

    def setNO2(self, dataDict):
        self.NO2_plot.clear()

        self.NO2_plot.bar(self.miesiace, dataDict)

        self.NO2_plot.set_title('ilo???? dwutlenku azotu w powietrzu')
        self.NO2_plot.set_ylabel('g/m^3')

        self.NO2_canvas.draw()

    def __init__(self):
        super().__init__()

        self.title('Interaktywna mapa ilustruj??ca ??rednie zanieczyszczenie powietrza w 2021 roku')
        self.makesFigures()
        self.miesiace = ['sty', 'lut', 'mar', 'kwi', 'maj', 'czer', 'lip', 'sie', 'wrz',
                         'pa??', 'lis', 'gru']
        self.brakDanych = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # initialize plots
        self.setPM10(self.brakDanych)
        self.setCO(self.brakDanych)
        self.setNO2(self.brakDanych)

        def createNewData(newData1, newData2, newData3):
            self.setPM10(newData1)
            self.setCO(newData2)
            self.setNO2(newData3)
            self.update()

        def motion(event):
            x, y = event.x, event.y
            # PMGdyPorebsk
            if 130 > x > 1 and 80 > y > 9:
                newDataP = DataSetUp.get_avg_month_value(excelReader.PorebskPM10)
                newDataC = DataSetUp.get_avg_month_value(excelReader.PorebskCO)
                newDataN = DataSetUp.get_avg_month_value(excelReader.PorebskNO2)
                createNewData(newDataP, newDataC, newDataN)
            # PmGdySzafran
            if 140 > x > 40 and 100 > y > 80:
                newDataP = DataSetUp.get_avg_month_value(excelReader.SzafranPM10)
                newDataC = DataSetUp.get_avg_month_value(excelReader.PorebskCO)
                newDataN = DataSetUp.get_avg_month_value(excelReader.SzafranNO2)
                createNewData(newDataP, newDataC, newDataN)
            # PmSopBiPlowc
            if 135 > x > 70 and 140 > y > 100:
                newDataP = DataSetUp.get_avg_month_value(excelReader.SzafranPM10)
                newDataC = DataSetUp.get_avg_month_value(excelReader.BiPlowcCO)
                newDataN = DataSetUp.get_avg_month_value(excelReader.SzafranNO2)
                createNewData(newDataP, newDataC, newDataN)
            # PmGdaWyzwole
            if 345 > x > 90 and 200 > y > 140:
                newDataP = DataSetUp.get_avg_month_value(excelReader.WyzwolePM10)
                newDataC = DataSetUp.get_avg_month_value(excelReader.WyzwoleCO)
                newDataN = DataSetUp.get_avg_month_value(excelReader.WyzwoleNO2)
                createNewData(newDataP, newDataC, newDataN)
            # PmGdaLeczkow
            if 185 > x > 150 and 200 > y > 180:
                newDataP = DataSetUp.get_avg_month_value(excelReader.LeczkowPM10)
                newDataC = DataSetUp.get_avg_month_value(excelReader.LeczkowCO)
                newDataN = DataSetUp.get_avg_month_value(excelReader.LeczkowNO2)
                createNewData(newDataP, newDataC, newDataN)
            # PmGdaPowWars
            if 150 > x > 100 and 230 > y > 180:
                newDataP = DataSetUp.get_avg_month_value(excelReader.PowWarsPM10)
                newDataC = DataSetUp.get_avg_month_value(excelReader.PowWarsCO)
                newDataN = DataSetUp.get_avg_month_value(excelReader.PowWarsNO2)
                createNewData(newDataP, newDataC, newDataN)

        self.bind('<Motion>', motion)


app = App()
app.mainloop()
