import mysql.connector

try:

    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="efef",
    database="lesson_4"
    )

    print(connection)

    try:

        # 1) Создайте представление, в которое попадет информация о  пользователях (имя, фамилия, город и пол), которые не старше 20 лет.
        with connection.cursor() as cursor:
            total_likes = """
            CREATE OR REPLACE VIEW view_user AS 
            SELECT firstname, lastname, hometown, gender AS 'Пользователи (младше 20 лет)'
            FROM users u
            JOIN profiles p ON u.id = p.user_id
            WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) < 20
            GROUP BY u.id;
            """
            cursor.execute(total_likes)
            connection.commit()

        with connection.cursor() as cursor:
            select_view = "SELECT * FROM view_user;"
            cursor.execute(select_view)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        
        # with connection.cursor() as cursor:
        #     drop_view = "DROP VIEW view_user;"
        #     cursor.execute(drop_view)

        # 2) Найдите кол-во,  отправленных сообщений каждым пользователем и  выведите ранжированный список пользователей, 
        # указав имя и фамилию пользователя, количество отправленных сообщений и место в рейтинге (первое место у пользователя с максимальным количеством сообщений). 
        # (используйте DENSE_RANK)
        with connection.cursor() as cursor:
            dense_rank = """
            SELECT 
                DENSE_RANK() OVER (ORDER BY COUNT(from_user_id) DESC) AS 'Место в рейтинге',
                COUNT(from_user_id) AS 'Количество отправленных сообщений',
                CONCAT(firstname, ' ', lastname) AS 'Пользователи'
            FROM users u
            JOIN messages m ON u.id = m.from_user_id
            GROUP BY u.id;"""
            cursor.execute(dense_rank)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        # 3) Выберите все сообщения, отсортируйте сообщения по возрастанию даты отправления (created_at) и 
        # найдите разницу дат отправления между соседними сообщениями, получившегося списка. (используйте LEAD или LAG)
        with connection.cursor() as cursor:
            lead_and_lag = """
            SELECT *, 
            LAG(created_at, 1, 0) OVER (PARTITION BY TIMESTAMPDIFF(SECOND, created_at, created_at)) AS lag_created_at,
            LEAD(created_at) OVER (PARTITION BY TIMESTAMPDIFF(SECOND, created_at, created_at)) AS lead_created_at
            FROM messages ORDER BY TIMESTAMPDIFF(SECOND, created_at, NOW()) DESC;"""
            cursor.execute(lead_and_lag)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except mysql.connector.Error as e:
        print(e)

except mysql.connector.Error as e:
    print(e)