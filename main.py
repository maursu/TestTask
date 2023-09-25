def text_validation(text: str) -> str :
    text = text.replace(',', '')
    list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']

    braces_check = lambda word: word.startswith("{") and word.endswith("}")
    keywords_in_text = list(filter(braces_check, text.split()))

    for keyword in keywords_in_text:
        if not keyword[1:-1] in list_keys:
            raise ValueError("Данные некорректны")

    return text


def count_elements(elements: list[list[str, int]]) -> list[list[str, int, int]]:
    elements = list(map(tuple, elements))
    elements_dict = {element: 0 for element in elements}

    for element in elements:
        elements_dict[element] += 1
    result = [list(element) + [count] for element, count in elements_dict.items()]

    return result


def search(tree, key):
    if key in tree:
        return tree[key]
    for value in tree.values():
        if isinstance(value, dict):
            tree = value
            return search(tree, key)


def json_diff(json_new: dict, old_json: dict, diff_list: list[str]) -> dict:
    result = {}
    path = []
    for key in diff_list:
        new_value = search(json_new, key)
        old_value = search(json_old, key)
        if not new_value == old_value:
            result[key] = new_value
    return result


Test_text = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''

task2_data = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]

json = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T11:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed': 1, 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False, 'paid_full': 0, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
json_old = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T11:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed': 1, 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False, 'paid_full': 0, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
json_new = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id': 11111111, 'company_id': 111111, 'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T13:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 2, 'confirmed': 1, 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, 'deleted': False, 'paid_full': 1, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}
Result = {'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], 'datetime': '2022-01-25T13:00:00+03:00'}
diff_list = ['services', 'staff', 'datetime']


# text_validation(Test_text)
assert count_elements(task2_data) == [['665587', 2, 1], ['669532', 1, 2], ['669537', 2, 1], ['665587', 1, 1]]
assert json_diff(json_new, json_old, diff_list) == Result




"""ЗАДАНИЕ №4"""

"""Если то, что документ должен быть удален из коллекции известно заранее,
то можно использовать TTL-индексы.

Еще один вариант, создать периодическую задачу с помощью Сelery beat,
а в документах, которые нужно будет удалить записать ключ с датой и временем, когда это нужно сделать

Таск при запуске будет просматривать документы с этим ключем и удалять их, если Date.now() >= expireTime
"""



"""ЗАДАНИЕ №5"""


"""
Создаем словарь, в котором ключем будут названия функций, а значениями сами функции.
Вытаскиваем из запроса по эндпоинту ключ function и вызываем ее из словаря, после проверки.

functions = {}

# Регистрация функций для обработки веб-хуков
def register_function(function_name, function):
    webhook_functions[function_name] = function

# Обработчик для приема веб-хуков
@app.route('/Datalore', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    function_name = data.get('function')

    # Проверка наличия функции для обработки
    if function_name in webhook_functions:
        result = webhook_functions[function_name](data)
        return jsonify({'result': result}), 200
    else:
        return jsonify({'error': 'Функция не найдена'}), 404
"""





