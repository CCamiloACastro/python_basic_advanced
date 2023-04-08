from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta
# Se crea un objeto datetime
now = datetime.now()
print(now)


def print_date(date):
    print('Uso del método datetime')
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    # La propiedad del evento timeStamp devuelve la cantidad de milisegundos desde que el documento terminó de
    # cargarse hasta que se creó el evento específico.
    print(date.timestamp())


print_date(now)
# Se necesita minimo el año el mes y el día
year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# Time

print('Uso del método Time')
current_time = time(21, 6, 0)
print(current_time)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# Date

print('Uso del método Date')
current_date = date.today()
print(current_date)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)
print(current_date)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(f'Mes añadido {current_date.month}')

# Operaciones con fechas

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# Timedelta


start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)