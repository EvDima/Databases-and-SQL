import mysql.connector

# try:

    # connection = mysql.connector.connect(
    # host="localhost",
    # user="root",
    # password="fefef",
    # )
    # with connection.cursor() as cursor:
    #     create_db_query = "CREATE DATABASE HW_03"
    #     cursor.execute(create_db_query)

# except mysql.connector.Error as e:
#     print(e)


try:

    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="efeff",
    database="HW_03"
    )

    print(connection)

    try:
        create_movies_table_query = """
        CREATE TABLE staff(
            id INT AUTO_INCREMENT PRIMARY KEY,
            firstname VARCHAR(45),
            lastname VARCHAR(45),
            post VARCHAR(45),
            seniority INT,
            salary INT,
            age INT
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            connection.commit()

        
        insert_query = """INSERT INTO staff (firstname, lastname, post, seniority, salary, age) 
            VALUES
            ('Вася', 'Петров', 'Начальник', '40', 100000, 60),
            ('Петр', 'Власов', 'Начальник', '8', 70000, 30),
            ('Катя', 'Катина', 'Инженер', '2', 70000, 25),
            ('Саша', 'Сасин', 'Инженер', '12', 50000, 35),
            ('Иван', 'Иванов', 'Рабочий', '40', 30000, 59),
            ('Петр', 'Петров', 'Рабочий', '20', 25000, 40),
            ('Сидр', 'Сидоров', 'Рабочий', '10', 20000, 35),
            ('Антон', 'Антонов', 'Рабочий', '8', 19000, 28),
            ('Юрий', 'Юрков', 'Рабочий', '5', 15000, 25),
            ('Максим', 'Максимов', 'Рабочий', '2', 11000, 22),
            ('Юрий', 'Галкин', 'Рабочий', '3', 12000, 24),
            ('Людмила', 'Маркина', 'Уборщик', '10', 10000, 49);"""
        with connection.cursor() as cursor:
            cursor.execute(insert_query)
            connection.commit()

        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE sale;"
        #     cursor.execute(drop_table_query)

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM staff;"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        # 1) Отсортируйте данные по полю заработная плата (salary) в порядке: убывания; возрастания
        with connection.cursor() as cursor:
            sort_salary = """
            SELECT * FROM staff
            ORDER BY salary DESC;;
            """
            cursor.execute(sort_salary)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        # 2) Выведите 5 максимальных заработных плат (saraly)
        with connection.cursor() as cursor:
            max_salary = """
            SELECT salary  FROM staff
            ORDER BY salary DESC
            LIMIT 5;"""
            cursor.execute(max_salary)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        # 3) Посчитайте суммарную зарплату (salary) по каждой специальности (роst)
        with connection.cursor() as cursor:
            sum_post_salary = """
            SELECT post, SUM(salary)  FROM staff
            GROUP BY post;"""
            cursor.execute(sum_post_salary)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        # 4) Найдите кол-во сотрудников с специальностью (post) «Рабочий» в возрасте от 24 до 49 лет включительно.
        with connection.cursor() as cursor:
            quantity_post_age = """
            SELECT count(post)  FROM staff
            WHERE post = 'Рабочий' and Age >= 24 and age <= 49
            GROUP BY post;"""
            cursor.execute(quantity_post_age)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

         # 5) Найдите количество специальностей
        with connection.cursor() as cursor:
            quantity_post = """
            SELECT count(distinct post)  FROM staff;"""
            cursor.execute(quantity_post)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        
        # 6) Выведите специальности, у которых средний возраст сотрудников меньше 30 лет
        with connection.cursor() as cursor:
            avg_age = """
            SELECT post, AVG(age) as avg_age FROM staff 
            GROUP BY post
            HAVING avg_age <= 30;"""
            cursor.execute(avg_age)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except mysql.connector.Error as e:
        print(e)

except mysql.connector.Error as e:
    print(e)
