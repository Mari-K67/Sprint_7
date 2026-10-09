class Url:
    main_url = 'https://qa-scooter.education-services.ru'
    
    #ручка создание курьера 
    create_courier_url = f'{main_url}/api/v1/courier'
    
    #ручка логин курьера в системе
    courier_login_in_sistem_url = f'{main_url}/api/v1/courier/login'
    
    #ручка создание заказа
    create_oder_url =  f'{main_url}/api/v1/orders'
    
    #ручка получение списка заказов
    get_oder_list_url = f'{main_url}/api/v1/orders'

    #ручка удаление курьера (без id)
    delete_courier = f'{main_url}/api/v1/courier/:'

class ResponseBody:
    #ручка создание курьера; код 201
    create_courier_code_201 = {"ok": True}
    
    #ручка создание курьера; код 409
    #Ответ по документации
    create_courier_code_409_documentation = {"message": "Этот логин уже используется"}
    #Ответ по реализации
    create_courier_code_409_release = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}

    #ручка создание курьера; код 400
    #Ответ по документации
    create_courier_code_400_documentation = {"message": "Недостаточно данных для создания учетной записи"}
    #Ответ по реализации
    create_courier_code_400_release = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

    #ручка авторизация курьера; код 400
    #Ответ по документации
    login_courier_code_400_documentation = {"message": "Недостаточно данных для входа"}
    #Ответ по реализации
    login_courier_code_400_release = {"code": 400, "message": "Недостаточно данных для входа"}

    #ручка авторизация курьера; код 404
    #Ответ по документации
    login_courier_code_404_documentation = {"message": "Учетная запись не найдена"}
    #Ответ по реализации
    login_courier_code_404_release = {"code": 404, "message": "Учетная запись не найдена"}

class OderInformation:
    color_black = ['BLACK']
    color_grey = ["GREY"]
    empty_color = []
    bouth_color = ["BLACK", "GREY"]
    