from typing import Dict

import requests
from requests import get


def _make_response(method: str, url: str, header: Dict, params: Dict, timeout: int, success: 200):
    response = requests.request(
        method,
        url,
        headers=header,
        params=params,
        timeout=timeout,
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


def get_details(url: str, header: Dict, params: Dict, timeout: int, success: 200):


#def api_request(method_endswith,  # Меняется в зависимости от запроса. locations/v3/search либо properties/v2/list
#                params,  # Параметры, если locations/v3/search, то {'q': 'Рига', 'locale': 'ru_RU'}
#                method_type  # Метод\тип запроса GET\POST
#                ):
#    url = f"https://hotels4.p.rapidapi.com/{method_endswith}"
#
#    # В зависимости от типа запроса вызываем соответствующую функцию
#    if method_type == 'GET':
#        return get_request(
#            url=url,
#            params=params
#        )
#    else:
#        return post_request(
#            url=url,
#            params=params
#        )
#
#
#def get_request(url, params):
#    try:
#        response = get(
#            url,
#            headers=...,
#            params=params,
#            timeout=15
#        )
#        if response.status_code == requests.codes.ok:
#            return response.json()
#   except Exception:
#        print('Что-то пошло не так')
#
#def post_request(url, params):
#    try:
#        response = get(
#            url,
#            headers=...,
#            params=params,
#            timeout=15
#        )
#        if response.status_code == requests.codes.ok:
#            return response.json()
#    except Exception:
#        print('Что-то пошло не так')