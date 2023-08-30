import sys
import requests
import base64


def main():
    print('Этот скрипт выводит данные о транзакциях из блока.')
    if len(sys.argv) < 2:
        print('Укажите номер блока')
        exit(1)
    elif sys.argv[1].isdigit() is False:
        print('Введите число.')
        exit(1)
    elif int(sys.argv[1]) < 11362001:
        print(
            'Номера блоков начинаются с 11362001. Введите больший номер блока.'
        )
        exit(1)
    block_id = sys.argv[1]
    try:
        get_block(block_id)
    except AttributeError:
        print('Запрашиваемый блок отсутсвует. Введите меньший номер блока')


def get_block(block_id):
    response = requests.get(
        f'https://rest-akash.ecostake.com/blocks/{block_id}'
    )
    block = response.json().get('block')
    data = block.get('data')
    transactions = data.get('txs')
    if transactions:
        for item in transactions:
            encoded_item = base64.b64decode(item)
            print(encoded_item)
    else:
        print('Транзакции в данном блоке отсутствуют.')


if __name__ == '__main__':
    main()
