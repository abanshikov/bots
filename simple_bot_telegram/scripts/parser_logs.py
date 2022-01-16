#!/usr/bin/env python
import re
from collections import Counter
from itertools import groupby

'''
To avoid errors with access rights:
$ sudo vim /etc/logrotate.d/nginx
/var/log/nginx/*.log {
    ...
    create 0644 www-data adm
    ...
}
$ sudo systemctl restart nginx &&
sudo service nginx restart &&
sudo systemctl status nginx
'''

FILE_NAME = '/var/log/nginx/access.log.1'
PATTERN_IP = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
PATTERN_WORDS = ['admin', 'stalker', 'config', 'wp-login', 'gponform', 'diag_form', 'tmp', 'gpon', 'env', 'vendor', 'storage',
                'public', 'getuser', 'ignition', 'execute-solution', 'vendor', 'login']
COUNT_IP = 10
DELIMETER = '-' * 50


def parser_log() -> tuple:
    """
    Поиск в файле логов количества повторений ip и поиск слов в логе
    return: (data_ip_count, data_words)
        data_ip_count = {'ip_1': count, 'ip_2':  count, ...}
        data_words = {'ip_1': 'word', 'ip_2': 'word', ...}
    """
    data_ip_count = {}
    data_words = {}

    # serch count ip
    with open(FILE_NAME, 'r', encoding="utf-8") as file:
        text_from_file = file.read()

    ips = re.findall(PATTERN_IP, text_from_file)
    result = Counter(ips).most_common()

    for ip, count in result:
        if count > 10:
            data_ip_count[ip] = count

    # search words
    with open(FILE_NAME, 'r', encoding="utf-8") as file:
        lines_from_file = file.readlines()

    for word in PATTERN_WORDS:
        for line in lines_from_file:
            if word in line.lower():
                ip = re.search(PATTERN_IP, line).group(0)
                data_words[ip] = word

    return data_ip_count, data_words


def print_result():
    data_ip_count, data_words = parser_log()
    all_ip = []

    print(DELIMETER)
    print('Количество запросов с ip:')
    for ip in data_ip_count:
        all_ip.append(ip)
        print(ip, ' - ', data_ip_count[ip])

    print('\n', DELIMETER)
    print('Запросы слов с ip:')
    for ip in data_words:
        all_ip.append(ip)
        print(ip, ' - ', data_words[ip])

    all_ip = [el for el, _ in groupby(all_ip)]
    print('\n', DELIMETER)
    print('Список для добавления в чёрный список\nsudo vim /etc/nginx/blockips.conf\nsudo service nginx restart')
    for ip in all_ip:
        print(f'deny {ip};')


print_result()
