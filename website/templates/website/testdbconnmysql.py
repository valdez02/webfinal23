import mysql.connector



def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', password='password', host='localhost', database='customerdb')
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        info = cursor.fetchone()
        print("Connection established to: ",info)

    except Exception as e:
        print(e)
    return conn

def insert_data(conn, customer):
    
    sql = ''' INSERT INTO customer(id,name1,name2,phone,petName,species)
              VALUES(%s,%s,%s,%s) '''
    cur = conn.cursor()
    cur.execute (sql, customer)
    conn.commit()
    return cur.lastrowid

def get_data_from_customer():
    sid = input("Customer ID: ")
    name1 = input("First Name: ")
    name2 = input("Last Name: ")
    phone = input("Phone Number: ")
    petName = input("Pet's Name: ")
    species = input("Species: ")
    return (sid,name1,name2,phone,petName,species)

def get_data_from_db(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM CUSTOMER''')
    rs = cursor.fetchall()
    return rs

def display_data(rset):
    for st in rset:
        print(st)
    
    
if __name__ == '__main__':
    connection = create_connection()
    
    i = insert_data(connection, get_data_from_customer())
    print("Last Row inserted :",i)
    rs = get_data_from_db(connection)
    display_data(rs)
    
                
