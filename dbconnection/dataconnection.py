import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            database='Gabito394',
            user='Gabriel',
            password='rimoldi1',
            host='database-2.c584ehk0ij4i.us-east-1.rds.amazonaws.com',
            port='5432'
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
        return None


connection = create_connection()


def _test():
    print(connection)


if __name__ == '__main__':
    _test()