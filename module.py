from datetime import datetime as data

__all__ = ['date_checking']


def date_checking(date_is_right):
    try:
        day, month, year = map(int, date_is_right.split('.'))
    except:
        return False
    try:
        data(year=year, month=month, day=day)
    except:
        return False
    return True


print(date_checking(input('Введите дату: ')))
print(date_checking(input('Введите дату: ')))


if __name__ == "__main__":
    __all__ = ['date_checking']
