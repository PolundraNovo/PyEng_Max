"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
#print(u'Пример вывода кириллического текста')

def task_12_1(ip_addr):
    access_ip = []
    unaccess_ip = []
    for item in ip_addr:
        command = 'ping '+item
        result = subprocess.run(command)
        if result.returncode == 0:
            access_ip.append(item)
        else:
            unaccess_ip.append(item)

    return (access_ip, unaccess_ip)

if __name__ == '__main__':

    ip_addr = ['8.8.8.8','22.22.22.22']
    access_ip, unaccess_ip = task_12_1(ip_addr)
    print(access_ip)
    print(unaccess_ip)

