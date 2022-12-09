from smart_city.main import excelReader


def sredniadata(stacja):
    listamiesiecy=["Caly rok", "Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec", "Lipiec", "Sierpien", "Wrzesien", "Pazdziernik", "Listopad", "Grudzien"]
    print(listamiesiecy)

def sredniawyniki(stacja): #?XD
        listawartosci=[]
        suma=0
        licznik=0
        for data in excelReader.stacja: # <- jak to ma dzialac to ja nw
            suma = suma + float(data.amount)
            licznik=licznik+1
        listawartosci.append(suma/licznik)

        suma1 = 0
        licznik1 = 0
        for data in excelReader.stacja:
            if (data.date > 1 / 1 / 2021 and data.date < 2 / 1 / 2021):
                suma1 = suma1 + float(data.amount)
                licznik1 = licznik1 + float(data.amount)
        listawartosci.append(suma1 / licznik1)

        suma2 = 0
        licznik2 = 0
        for data in excelReader.stacja:
            if (data.date > 2 / 1 / 2021 and data.date < 3 / 1 / 2021):
                suma2 = suma2 + float(data.amount)
                licznik2 = licznik2 + float(data.amount)
        listawartosci.append(suma2 / licznik2)

        suma3 = 0
        licznik3 = 0
        for data in excelReader.stacja:
            if (data.date > 3 / 1 / 2021 and data.date < 4 / 1 / 2021):
                suma3 = suma3 + float(data.amount)
                licznik3 = licznik3 + float(data.amount)
        listawartosci.append(suma3 / licznik3)

        suma4 = 0
        licznik4 = 0
        for data in excelReader.stacja:
            if (data.date > 4 / 1 / 2021 and data.date < 5 / 1 / 2021):
                suma4 = suma4 + float(data.amount)
                licznik4 = licznik4 + float(data.amount)
        listawartosci.append(suma4 / licznik4)

        suma5 = 0
        licznik5 = 0
        for data in excelReader.stacja:
            if (data.date > 5 / 1 / 2021 and data.date < 6 / 1 / 2021):
                suma5 = suma5 + float(data.amount)
                licznik5 = licznik5 + float(data.amount)
        listawartosci.append(suma5 / licznik5)

        suma6 = 0
        licznik6 = 0
        for data in excelReader.stacja:
            if (data.date > 6 / 1 / 2021 and data.date < 7 / 1 / 2021):
                suma6 = suma6 + float(data.amount)
                licznik6 = licznik6 + float(data.amount)
        listawartosci.append(suma6 / licznik6)

        suma7 = 0
        licznik7 = 0
        for data in excelReader.stacja:
            if (data.date > 7 / 1 / 2021 and data.date < 8 / 1 / 2021):
                suma7 = suma7 + float(data.amount)
                licznik7 = licznik7 + float(data.amount)
        listawartosci.append(suma7 / licznik7)

        suma8 = 0
        licznik8 = 0
        for data in excelReader.stacja:
            if (data.date > 8 / 1 / 2021 and data.date < 9 / 1 / 2021):
                suma8 = suma8 + float(data.amount)
                licznik8 = licznik8 + float(data.amount)
        listawartosci.append(suma8 / licznik8)

        suma9 = 0
        licznik9 = 0
        for data in excelReader.stacja:
            if (data.date > 9 / 1 / 2021 and data.date < 10 / 1 / 2021):
                suma9 = suma9 + float(data.amount)
                licznik9 = licznik9 + float(data.amount)
        listawartosci.append(suma9 / licznik9)

        suma10 = 0
        licznik10 = 0
        for data in excelReader.stacja:
            if (data.date > 10 / 1 / 2021 and data.date < 11 / 1 / 2021):
                suma10 = suma10 + float(data.amount)
                licznik10 = licznik10 + float(data.amount)
        listawartosci.append(suma10 / licznik10)

        suma11 = 0
        licznik11 = 0
        for data in excelReader.stacja:
            if (data.date > 11 / 1 / 2021 and data.date < 12 / 1 / 2021):
                suma11 = suma11 + float(data.amount)
                licznik11 = licznik11 + float(data.amount)
        listawartosci.append(suma11 / licznik11)

        suma12 = 0
        licznik12 = 0
        for data in excelReader.stacja:
            if (data.date > 12 / 1 / 2021):
                suma12 = suma12 + float(data.amount)
                licznik12 = licznik12 + float(data.amount)
        listawartosci.append(suma12 / licznik12)