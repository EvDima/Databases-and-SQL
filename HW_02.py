import mysql.connector

# try:

#     connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="rgrgr",
#     )
#     with connection.cursor() as cursor:
#         create_db_query = "CREATE DATABASE HW_2"
#         cursor.execute(create_db_query)

# except mysql.connector.Error as e:
#     print(e)


try:

    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dfgrfr",
    database="HW_2"
    )

    print(connection)

    try:

        create_movies_table_query = """
        CREATE TABLE sale(
            id INT AUTO_INCREMENT PRIMARY KEY,
            order_date DATE,
            count_product INT
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            connection.commit()

        
        insert_query = """INSERT INTO sale (order_date, count_product) 
            VALUES
            ('2022-01-01', 156),
            ("2022-01-02", 180),
            ('2022-01-03', 21),
            ('2022-01-04', 124),
            ('2022-01-05', 341);"""
        with connection.cursor() as cursor:
            cursor.execute(insert_query)
            connection.commit()

        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE sale"
        #     cursor.execute(drop_table_query)

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM sale"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        with connection.cursor() as cursor:
            order_type = '''
            SELECT id,
                CASE 
                    WHEN count_product < 100 THEN 'Маленький заказ' 
                    WHEN count_product between 100 and 300 THEN 'Средний заказ' 
                    WHEN count_product > 300 THEN 'Большой заказ' 
                    ELSE 'НЕ определено'
                END AS 'Тип заказа'
            FROM sale; '''
            cursor.execute(order_type)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    finally:
       connection.close()


    try:

        create_orders_table_query = """
        CREATE TABLE Orders(
            id INT AUTO_INCREMENT PRIMARY KEY,
            employee_id VARCHAR(10),
            amount FLOAT,
            order_status VARCHAR(20)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_orders_table_query)
            connection.commit()

        
        insert_query = """INSERT INTO Orders (employee_id, amount, order_status) 
            VALUES
            ('e03', '15.00', 'OPEN'),
            ("e01", '25.60', 'OPEN'),
            ('e05', '100.70', 'CLOSED'),
            ('e02', '22.18', 'OPEN'),
            ('e04', '9.50', 'CANCELLED');"""
        with connection.cursor() as cursor:
            cursor.execute(insert_query)
            connection.commit()

        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE Orders"
        #     cursor.execute(drop_table_query)

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM Orders"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        with connection.cursor() as cursor:
            order_type = '''
            SELECT id, employee_id, amount,
                CASE 
                    WHEN order_status = 'OPEN' THEN 'Order is in open state' 
                    WHEN order_status = 'CLOSED' THEN 'Order is closed' 
                    WHEN order_status = 'CANCELLED' THEN 'Order is cancelled' 
                    ELSE 'НЕ определено'
                END AS full_order_status
            FROM Orders; '''
            cursor.execute(order_type)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    finally:
        connection.close()

except mysql.connector.Error as e:
    print(e)

