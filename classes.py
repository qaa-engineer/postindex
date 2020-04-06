class Postindex:
    def __init__(self, row):
        self.postindex = row[0]  # Почтовый индекс
        self.opsname = row[1]  # Отделение почты
        self.opstype = row[2]  # Тип почтового отделения
        self.opssubm = row[3]  # Индекс вышестоящего почтового отделения
        self.region = row[4]  # Регион
        self.autonom = row[5]  # Автономная область
        self.area = row[6]  # Район
        self.city = row[7]  # Населенный пункт
        self.city_1 = row[8]  # Подчиненный населенный пункт
        self.actdate = row[9]  # Дата актуализации информации
        self.indexold = row[10]  # Старый почтовый индекс (до 01.02.2000)

    def all_content(self):
        data=[]
        if self.postindex != None:
            postindex={"Почтовый индекс": self.postindex}
            data.append(postindex)
        if self.opsname != None:
            opsname={"Отделение почты":self.opsname}
            data.append(opsname)
        if self.opstype != None:
            if self.opstype == "ФГУП":
                self.opstype = "Федеральное государственное унитарное предприятие (ФГУП)"
            elif self.opstype == "УМСЦ":
                self.opstype = "Участок магистрального сортировочного центра (УМСЦ)"
            elif self.opstype == "УДУ":
                self.opstype = "Участок дистанционного управления (УДУ)"
            elif self.opstype == "Участок":
                self.opstype = "Участок почтового отделения"
            elif self.opstype == "МСО":
                self.opstype = "Магистральное сортировачное отделение (МСО)"
            elif self.opstype == "МСЦ":
                self.opstype = "Магистральный сортировочный центр (МСЦ)"
            elif self.opstype == "ОП":
                self.opstype = "Отделение почты (ОП)"
            elif self.opstype == "ПЕРЕДВИЖНОЕ ОС":
                self.opstype = "Передвижное отделение связи (ОС)"
            elif self.opstype == "ПЖДП":
                self.opstype = "Прижелезнодорожный почтамт (ПЖДП)"
            elif self.opstype == "УФПС":
                self.opstype = "Управление Федеральной почтовой связи (УФПС)"
            elif self.opstype == "Склад ТМЦ":
                self.opstype = "Склад товарно-материальных ценностей (ТМЦ)"
            elif self.opstype == "ПВПО":
                self.opstype = "Почтовый вагон почтового отделения (ПВПО)"
            elif self.opstype == "МРП":
                self.opstype = "Межрайонный почтамт (МРП)"
            elif self.opstype == "П":
                self.opstype = "Почтамт (П)"
            elif self.opstype == "ОПП":
                self.opstype = "Отделение перевозки почты (ООП)"
            elif self.opstype == "ТИ":
                self.opstype = "Технологический индекс (ТИ)"
            elif self.opstype == "О":
                self.opstype = "Отделение почтовой связи (О)"
            elif self.opstype == "Цех":
                self.opstype = "Сортировачный цех посылок"
            elif self.opstype == "УКД":
                self.opstype = "Участок курьерской доставки (УКД)"
            elif self.opstype == "ММПО":
                self.opstype = "Место международного почтового обмена (ММПО)"
            elif self.opstype == "ППС":
                self.opstype = "Полевая почтовая станция (ППС)"
            elif self.opstype == "АОПП":
                self.opstype = "Авиационное отделение перевозки почты (АОПП)"
            elif self.opstype == "СЦ":
                self.opstype = "Сортировочный центр (СЦ)"
            elif self.opstype == "ГСП":
                self.opstype = "Городская служебная почта (ГСП)"
            elif self.opstype == "ДТИ":
                self.opstype = "Дополнительный технологический индекс (ДТИ)"
            elif self.opstype == "Почтомат":
                self.opstype = "Почтомат"
            opstype={"Тип почтового отделения":self.opstype}
            data.append(opstype)
        if self.opssubm != None:
            opssubm={"Индекс вышестоящего почтового отделения": self.opssubm}
            data.append(opssubm)
        if self.region != None:
            region={"Регион": self.region}
            data.append(region)
        if self.autonom != None:
            autonom={"Автономная область": self.autonom}
        if self.area != None:
            area={"Район": self.area}
            data.append(area)
        if self.city != None:
            city={"Населенный пункт": self.city}
            data.append(city)
        if self.city_1 != None:
            city_1={"Подчиненный населенный пункт":self.city_1}
            data.append(city_1)
        if self.actdate != None:
            actdate={"Дата актуализации информации": self.actdate}
            data.append(actdate)
        if self.indexold != None:
            indexold={"Старый почтовый индекс (до 01.02.2000)": self.indexold}
            data.append(indexold)
        return data