class Employee:
    """Класс для представления сотрудника."""

    # Переменная на уровне класса для подсчета количества сотрудников
    number_of_employees = 0

    def __init__(self, first, last, pay):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@email.com'

        Employee.number_of_employees += 1

# Создаем двух сотрудников
emp_1 = Employee('Ivan', 'Ivanov', 50000)
emp_2 = Employee('Petr', 'Petrov', 60000)

# Выводим количество сотрудников
print(Employee.number_of_employees)