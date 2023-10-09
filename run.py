# getclass
import requests


def run():
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': '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',
    }

    data = '{"event_type": "class_1_2"}'

    response = requests.post(f'https://api.github.com/repos/payI0ad/wx_weather_class_push/dispatches',
                             headers=headers, data=data)


# 云函数入口
def main_handler(event, context):
    return run()

#####################################################################
# morning

import requests


def run():
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': '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',
    }

    data = '{"event_type": "morning"}'

    response = requests.post(f'https://api.github.com/repos/payI0ad/wx_weather_class_push/dispatches',
                             headers=headers, data=data)


# 云函数入口
def main_handler(event, context):
    return run()


#####################################################################
# eve

import requests


def run():
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': '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',
    }

    data = '{"event_type": "evening"}'

    response = requests.post(f'https://api.github.com/repos/payI0ad/wx_weather_class_push/dispatches',
                             headers=headers, data=data)


# 云函数入口
def main_handler(event, context):
    return run()