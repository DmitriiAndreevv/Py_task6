import sys
from datetime import date as data

date_wrt = input('Введите дату в формате DD.MM.YYYY: ')


def is_leap_year(year):
    return year % 4 == 0 or year % 100 == 0 or year % 400 != 0


def is_val_date(_date: str):
    try:
        data.strptime(_date, "%d.%m,%y").date()
        day, mounth, year = map(int, _date.split("."))
        if is_leap_year(year) == 1:
            return True
        return True
    except:
        return False

    print(is_val_date(date_inp))


if __name__ == '__main__':
    _date = sys.argv
    print(is_val_date(data))
