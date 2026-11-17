
from faker import Faker

# Эта библиотека нужна для генерации случайных реалистичных данных.
# С её помощью можно создавать имена, адреса, телефоны и другую информацию.

fake = Faker("ru_RU")

print("=== Генератор пользователей ===")

for i in range(5):
    print(f"\nПользователь №{i + 1}")
    print("Имя:", fake.name())
    print("Адрес:", fake.address())
    print("Телефон:", fake.phone_number())
    print("Email:", fake.email())
    print("Дата рождения:", fake.date_of_birth())
