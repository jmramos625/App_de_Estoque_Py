import mysql.connector as mc




def insert_data():
    try:
        mydb = mc.connect(
            host = "localhost",
            user = "DomJhon",
            password = "PdV36f1!Y~1Z",
            database = "app_estoque",
            port=3306
        )
        
        if mydb.is_connected():
            print("Connected to MySQL database!")
            cursor = mydb.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"MySQL Server Version: {version}")
            cursor.close()
        
        # creating the cursor to execute the SQL commands.
        mycursor = mydb.cursor()
            
        # setting the SQL command to insert the data in the table.
        username = input("Enter your username: ")
        password = input("Enter your password: ")
            
        query = "INSERT INTO users_pass (username, password) VALUES (%s, %s)"
        values = (username, password) # this is the values to be inserted in the table.
        
        # executing the SQL command.
        mycursor.execute(query, values) # taking the values to be inserted and the SQL command.
        
        mydb.commit() # commiting the changes in the database.
            
        print("User " + username + " added successfully") # to give the feedback to the user.
    except mc.Error as e:
        print("Error: " + str(e))

insert_data()