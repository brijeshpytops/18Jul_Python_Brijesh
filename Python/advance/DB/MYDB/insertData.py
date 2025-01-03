from .dbConnection import db, cursor

def insert_data():
    sql = """
    INSERT INTO users (fullname, email, mobile, password)
    VALUES
    ('John Doe', 'john.doe@example.com', '1234567890', 'password123'),
    ('Jane Smith', 'jane.smith@example.com', '2345678901', 'securePass!'),
    ('Alice Brown', 'alice.brown@example.com', '3456789012', 'alice@2024'),
    ('Bob White', 'bob.white@example.com', '4567890123', 'bobSecure#'),
    ('Carol Green', 'carol.green@example.com', '5678901234', 'passCarol123'),
    ('Dave Black', 'dave.black@example.com', '6789012345', 'dave!pwd'),
    ('Emma Stone', 'emma.stone@example.com', '7890123456', 'stone@pwd'),
    ('Frank Blue', 'frank.blue@example.com', '8901234567', 'blue#Secure'),
    ('Grace Pink', 'grace.pink@example.com', '9012345678', 'grace!@pwd'),
    ('Hank Yellow', 'hank.yellow@example.com', '9123456789', 'yellowPwd@'),
    ('Ivy Gray', 'ivy.gray@example.com', '8234567890', 'graySecure#'),
    ('Jake Violet', 'jake.violet@example.com', '7345678901', 'violet#Jake'),
    ('Kelly Orange', 'kelly.orange@example.com', '6456789012', 'kelly123Orange'),
    ('Liam Red', 'liam.red@example.com', '5567890123', 'red@liamSecure'),
    ('Mia Purple', 'mia.purple@example.com', '4678901234', 'purple#Mia');
    """
    cursor.execute(sql)
    db.commit()