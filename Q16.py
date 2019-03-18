import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))

    today = datetime.date(2019,3,18)
    tomorrow = today + datetime.timedelta(days=1)
    last = today.replace(year=today.year-1)

    print(today.strftime('%d/%m/%Y'))
    print(tomorrow.strftime('%d/%m/%Y'))
    print(last.strftime('%d/%m/%Y'))