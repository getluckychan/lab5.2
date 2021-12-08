import datetime
from sys import exit


class Empty(Exception):
    def __init__(self):
        pass


class Error(Exception):

    def __init__(self):
        self.massage = None

    def __str__(self):
        self.massage = "Введіть вірну дату"
        return self.massage


class E(Exception):
    def __init__(self):
        self.massage = None

    def __str__(self):
        self.massage = "Я не знаю що треба ввести щоб це викликати"
        return self.massage


def read():
    set_month = int(input("Введіть місяць: "))
    set_day = int(input("Введіть день:"))
    if set_month > 12:
        raise Error
    elif set_month == 2 and set_day > 28:
        raise Error
    elif set_month % 2 == 0 and set_day > 30:
        raise Error
    return [set_month, set_day]


def find_day():
    seted_date = read()
    intday = datetime.date(year=2021, month=int(seted_date[0]), day=int(seted_date[1])).weekday()
    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    return days[intday]


def fu():
    print("неочікована базова помилка")
    raise BaseException


def ft():
    exit("очікувана дуже пагана помилка")


def main():
    try:
        print(find_day())
    except Empty:
        exit("Викликана Empty")
    except Error:
        raise Error
    except ValueError:
        exit("введіть ціле число")
    except BaseException:
        raise E
    except:
        fu()


main()
