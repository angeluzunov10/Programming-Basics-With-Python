# За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги.
# Понеже Жоро предпочита да играе с приятели навън, вашата задача е да му помогнете да изчисли колко часа на ден трябва да отделя, за да прочете необходимата литература.
# Вход
# От конзолата се четат 3 реда:
# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

pages = int(input())
pages_per_hour = int(input())
days_for_whole_book = int(input())

hours_reading = int(pages / pages_per_hour)
daily_reading_hours = int(hours_reading / days_for_whole_book)

print (daily_reading_hours)
