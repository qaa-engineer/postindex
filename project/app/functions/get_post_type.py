def get_post_type(post_type):
    """
    Функция «Расшифровка аббревиатур» из столбца базы данных.
    :param post_type: str
    :return: str
    """
    if post_type != None:
        if post_type == "ФГУП":
            post_type = "Федеральное государственное унитарное предприятие (ФГУП)"
        elif post_type == "УМСЦ":
            post_type = "Участок магистрального сортировочного центра (УМСЦ)"
        elif post_type == "УДУ":
            post_type = "Участок дистанционного управления (УДУ)"
        elif post_type == "Участок":
            post_type = "Участок почтового отделения"
        elif post_type == "МСО":
            post_type = "Магистральное сортировачное отделение (МСО)"
        elif post_type == "МСЦ":
            post_type = "Магистральный сортировочный центр (МСЦ)"
        elif post_type == "ОП":
            post_type = "Отделение почты"
        elif post_type == "ПЕРЕДВИЖНОЕ ОС":
            post_type = "Передвижное отделение связи"
        elif post_type == "ПЖДП":
            post_type = "Прижелезнодорожный почтамт (ПЖДП)"
        elif post_type == "УФПС":
            post_type = "Управление Федеральной почтовой связи (УФПС)"
        elif post_type == "Склад ТМЦ":
            post_type = "Склад товарно-материальных ценностей (ТМЦ)"
        elif post_type == "ПВПО":
            post_type = "Почтовый вагон почтового отделения (ПВПО)"
        elif post_type == "МРП":
            post_type = "Межрайонный почтамт (МРП)"
        elif post_type == "П":
            post_type = "Почтамт"
        elif post_type == "ОПП":
            post_type = "Отделение перевозки почты (ООП)"
        elif post_type == "ТИ":
            post_type = "Технологический индекс"
        elif post_type == "О":
            post_type = "Отделение почтовой связи"
        elif post_type == "Цех":
            post_type = "Сортировачный цех посылок"
        elif post_type == "УКД":
            post_type = "Участок курьерской доставки (УКД)"
        elif post_type == "ММПО":
            post_type = "Место международного почтового обмена (ММПО)"
        elif post_type == "ППС":
            post_type = "Полевая почтовая станция (ППС)"
        elif post_type == "АОПП":
            post_type = "Авиационное отделение перевозки почты (АОПП)"
        elif post_type == "СЦ":
            post_type = "Сортировочный центр (СЦ)"
        elif post_type == "ГСП":
            post_type = "Городская служебная почта (ГСП)"
        elif post_type == "ДТИ":
            post_type = "Дополнительный технологический индекс (ДТИ)"
        elif post_type == "Почтомат":
            post_type = "Почтомат"
    return post_type
