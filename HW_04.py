import mysql.connector

try:

    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fhtrh",
    database="lesson_4"
    )

    print(connection)

    try:

        # 1) Подсчитать общее количество лайков, которые получили пользователи младше 12 лет.
        with connection.cursor() as cursor:
            total_likes = """
            SELECT COUNT(*) 'likes count'
            FROM likes l JOIN profiles p 
            WHERE p.user_id = l.user_id AND TIMESTAMPDIFF(YEAR, p.birthday, NOW()) < 12;
            """
            cursor.execute(total_likes)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        # 2) Определить кто больше поставил лайков (всего): мужчины или женщины.
        with connection.cursor() as cursor:
            likes = """
            SELECT CASE (gender)
                WHEN 'm' THEN 'мужчин'
                WHEN 'f' THEN 'женщин'
                END AS 'Кого больше', COUNT(*) as 'лайков'
            FROM profiles p 
            JOIN likes l 
            WHERE l.user_id = p.user_id
            GROUP BY gender;"""
            cursor.execute(likes)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        # 3) Вывести всех пользователей, которые не отправляли сообщения.
        with connection.cursor() as cursor:
            not_send_messages = """
            SELECT u.id, u.firstname, u.lastname
            FROM users u
            WHERE NOT EXISTS (
                SELECT m.from_user_id
                FROM messages m
                WHERE m.from_user_id = u.id);"""
            cursor.execute(not_send_messages)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        # 4) Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех общался с выбранным пользователем (написал ему сообщений).
        with connection.cursor() as cursor:
            talked_most = """
            SELECT u.firstname, u.lastname 
            FROM users u
            JOIN messages m
            WHERE m.from_user_id = u.id AND m.to_user_id = 1 
            GROUP BY u.firstname, u.lastname
            ORDER BY COUNT(from_user_id) DESC
            LIMIT 1;"""
            cursor.execute(talked_most)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except mysql.connector.Error as e:
        print(e)

except mysql.connector.Error as e:
    print(e)