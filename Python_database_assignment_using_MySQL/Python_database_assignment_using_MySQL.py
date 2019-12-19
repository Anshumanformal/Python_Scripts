import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

class restaurant:
    
    def rst(self):
        try:
            if conn.is_connected():
                db_Info = conn.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
            #Creating rst table for Restaurant in restaurant database.
            curr.execute('CREATE TABLE rst(ID INTEGER(3), RestaurantName VARCHAR(25), Address VARCHAR(25), ContactNumber VARCHAR(20), Rating FLOAT(3), HomeDelivery VARCHAR(3));')    
            curr.execute('select database();')
            record = curr.fetchone()
            print("You're connected to database: ", record)         
            
            #Inserting records into rst table for Restaurant in restaurant database.
            #print("This choice will show the inserted data into the database.\n")
            mysql_insert_query = 'INSERT INTO rst(ID, RestaurantName, Address, ContactNumber, Rating, HomeDelivery) VALUES(%s, %s, %s, %s, %s, %s);'
            records_to_insert = [(1,'Bikanerwala','Delhi_6',9293818106,4.4,'YES'),
                                     (2,'Ram Bhojanalaya','Delhi_4',9193357101,3.4,'YES'),
                                     (3,'Mohan Halwai','Rajouri Garden',9045398519,3.9,'NO'),
                                     (4,'Happy Cafe','Rajiv Chowk',9102305629,4.1,'YES'),
                                     (5,'Dominos','Canaught Place',8485120945,4.8,'YES'),
                                     (6,'Bhandari Ki Rasoi','Chandni Chowk',8820193481,3.1,'NO')]

            result = curr.executemany(mysql_insert_query, records_to_insert)
            conn.commit()
            #print(curr.rowcount, 'Records inserted successfully into rst table.')
            #curr.close()
            while(1):
                print("\n\nEnter your choice:\n1. Run the select query.\n2. Run the update query.\n3. Run the delete query.\n")
                n = int(input())
                if(n == 1):
                    try:
                        #select_query1 = 'SELECT * from rst;'
                        #Selecting records in rst table for Restaurant in restaurant database.
                        print("Enter the select query for rst table to view records for IDs between 1 to 6.")
                        select_query1 = input()
                        #curr.execute('SELECT * FROM rst;')
                        curr.execute(select_query1)
                        records = curr.fetchall()
                        print("Total number of rows in rst is: ", curr.rowcount,"\n")
                        print("*******************************RECORDS**************************************************************")
                        for i in records:
                            print("ID = ", i[0], )
                            print("RestaurantName = ", i[1])
                            print("Address = ", i[2])
                            print("ContactNumber = ", i[3])
                            print("Rating = ", i[4])
                            print("HomeDelivery = ", i[5], "\n")
                        conn.commit()
                        print("Records displayed successfully.")
                        #curr.close()
                    except mysql.connector.Error as error:
                        print("Can not display record.".format(error))
                        #curr.close()
                   
                elif(n == 2):
                    #Updating records in rst table for Restaurant in restaurant database.
                    print("This choice will show the updated data into the database.\n")
                    try:
                        #update_query1 = 'UPDATE rst set Rating = 4.6 WHERE id = 4;'
                        print("Enter any update query for rst table for IDs between 1 to 6.")
                        update_query1 = input()
                        curr.execute(update_query1)
                        conn.commit()
                        print("Record Updated successfully.")
                        curr.execute('SELECT * FROM rst;')
                        #curr.execute(select_query1)
                        records = curr.fetchall()
                        print("Total number of rows in rst is: ", curr.rowcount,"\n")
                        print("*******************************RECORDS**************************************************************")
                        for i in records:
                            print("ID = ", i[0], )
                            print("RestaurantName = ", i[1])
                            print("Address = ", i[2])
                            print("ContactNumber = ", i[3])
                            print("Rating = ", i[4])
                            print("HomeDelivery = ", i[5], "\n")
                        conn.commit()
                        print("Records displayed successfully.")
                        #curr.close()
                    except mysql.connector.Error as error:
                        print("Can not update record.".format(error))    
                        #curr.close()
                elif(n == 3):
                    #Deleting records in rst table for Restaurant in restaurant database.
                    print("This choice will show the deleted data into the database.\n")
                    try:
                        #delete_query1 = 'DELETE FROM rst WHERE id = 5;'
                        print("Enter any delete query for rst table for IDs between 1 to 6.")
                        delete_query1 = input()
                        curr.execute(delete_query1)
                        conn.commit()
                        print("Record deleted successfully.")
                        curr.execute('SELECT * FROM rst;')
                        #curr.execute(select_query1)
                        records = curr.fetchall()
                        print("Total number of rows in rst is: ", curr.rowcount,"\n")
                        print("*******************************RECORDS**************************************************************")
                        for i in records:
                            print("ID = ", i[0], )
                            print("RestaurantName = ", i[1])
                            print("Address = ", i[2])
                            print("ContactNumber = ", i[3])
                            print("Rating = ", i[4])
                            print("HomeDelivery = ", i[5], "\n")
                        conn.commit()
                        print("Records displayed successfully.")
                        #curr.close()
                    except mysql.connector.Error as error:
                        print("Can not delete record.".format(error))
                        #curr.close()
                              
                else:
                    print("You have entered a number other than 1,2 or 3.\n")
                    print("What do you want to do?\n")
                    print("Enter 1 to repeat the program.\nEnter 2 for terminating the program.\n")
                    a = int(input())
                    if(a == 1):
                        pass
                    if(a == 2):
                        break
                    

        except mysql.connector.Error as error:
            print("Failed to create rst table {}".format(error))
        finally:
            if (conn.is_connected()):
                curr.close()
                conn.close()
                print("MySQL connection is closed")
            
    def cust(self):        
        #Creating cust table for Customer in restaurant database.
        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
        curr.execute('select database();')
        record = curr.fetchone()
        print("You're connected to database: ", record)   
                    
        try:
            curr.execute('CREATE TABLE cust(ID INTEGER(3), CustomerName VARCHAR(25), Address VARCHAR(25), ContactNumber VARCHAR(20), Age INTEGER(3));')    
            #Inserting records into cust table for Customer in restaurant database.
            #print("This choice will show the inserted data into the database.\n")
            insert_cust_query = 'INSERT INTO cust(ID, CustomerName, Address, ContactNumber, Age) VALUES(%s, %s, %s, %s, %s);'
            records_cust_query = [(1,'Ram','Rajouri Garden',9293818106,44),
                                     (2,'Mohan','Chandni Chowk',9193357101,54),
                                     (3,'Sohan','Delhi_6',9045398519,56),
                                     (4,'Bhola','Delhi_4',9102305629,41),
                                     (5,'Gopal','Canaught Place',8485120945,66),
                                     (6,'Ramesh','Rajiv Chowk',8820193481,27)]

            result1 = curr.executemany(insert_cust_query, records_cust_query)
            conn.commit()
            #print(curr.rowcount, 'Records inserted successfully into cust table.')
            #curr.close()
            while(1):
                print("\n\nEnter your choice:\n1. Run the select query.\n2. Run the update query.\n3. Run the delete query.\n")
                n = int(input())
                if(n == 1):
                    try:
                        #select_query2 = 'SELECT * FROM cust;'
                        #Selecting records in cust table for Customer in restaurant database.
                        print("Enter the select query for cust table to view records for IDs between 1 to 6.")
                        select_query2 = input()
                        #curr.execute('SELECT * FROM cust;')
                        curr.execute(select_query2)
                        records = curr.fetchall()
                        print("Total number of rows in cust is: ", curr.rowcount,"\n")
                        print("*******************************RECORDS************************************************************")
                        for i in records:
                            print("ID = ", i[0])
                            print("CustomerName = ", i[1])
                            print("Address = ", i[2])
                            print("ContactNumber = ", i[3])
                            print("Age = ", i[4], "\n")
                        conn.commit()
                        print("Records displayed successfully.")
                        #curr.close()
                    except mysql.connector.Error as error:
                        print("Can not display record.".format(error))
                        #curr.close()    

                elif(n ==2):
                    print("This choice will show the updated data into the database.\n")    
                        #Updating records in cust table for Customer in restaurant database.
                    try:
                        #update_query2 = 'UPDATE cust set Age = 61 WHERE id = 5;'
                        print("Enter any update query for cust table for IDs between 1 to 6.")
                        update_query2 = input()
                        curr.execute(update_query2)
                        conn.commit()
                        print("Record Updated successfully.")
                        curr.execute('SELECT * FROM cust;')
                        #curr.execute(select_query2)
                        records = curr.fetchall()
                        print("Total number of rows in cust is: ", curr.rowcount,"\n")
                        print("*******************************RECORDS************************************************************")
                        for i in records:
                            print("ID = ", i[0])
                            print("CustomerName = ", i[1])
                            print("Address = ", i[2])
                            print("ContactNumber = ", i[3])
                            print("Age = ", i[4], "\n")
                        conn.commit()
                        print("Records displayed successfully.")
                        #curr.close()
                    except mysql.connector.Error as error:
                        print("Can not update record.".format(error))
                        #curr.close()

                elif(n ==3):
                    print("This choice will show the deleted data into the database.\n")
                    #Deleting records in cust table for Customer in restaurant database.
                    try:
                        #delete_query2 = 'DELETE FROM cust where id = 3;'
                        print("Enter any delete query for cust table for IDs between 1 to 6.")
                        delete_query2 = input()
                        curr.execute(delete_query2)
                        conn.commit()
                        print("Record deleted successfully.")
                        curr.execute('SELECT * FROM cust;')
                        #curr.execute(select_query2)
                        records = curr.fetchall()
                        print("Total number of rows in cust is: ", curr.rowcount,"\n")
                        print("*******************************RECORDS************************************************************")
                        for i in records:
                            print("ID = ", i[0])
                            print("CustomerName = ", i[1])
                            print("Address = ", i[2])
                            print("ContactNumber = ", i[3])
                            print("Age = ", i[4], "\n")
                        conn.commit()
                        print("Records displayed successfully.")
                        #curr.close()
                    except mysql.connector.Error as error:
                        print("Can not delete record.".format(error))
                        #curr.close() 
                        
                else:
                    print("You have entered a number other than 1,2 or 3.")
                    print("What do you want to do?\n")
                    print("Enter 1 to repeat the program.\nEnter 2 for terminating the program.\n")
                    a = int(input())
                    if(a == 1):
                        pass
                    if(a == 2):
                        break
                    
                    #curr.close()
                  
        except mysql.connector.Error as error:
            print("Failed to create cust table {}".format(error))
        finally:
            if (conn.is_connected()):
                curr.close()
                conn.close()
                print("MySQL connection is closed")

    
# Main function.         
if __name__ == "__main__":
    
    print("Restaurant Database Management System in Python - by Anshuman Ranjan")
    print("Enter the table name which you wish to see or modify:\n")
    print("1. Restaurant Table - Enter 1")
    print("2. Customer Table - Enter 2")
    conn = mysql.connector.connect(host="localhost", user="root", password="anshu", database = "restaurant")
    curr = conn.cursor()
    #curr.execute('create database restaurant;')                                      
    a = int(input())
    obj = restaurant()
    if(a == 1): 
        obj.rst()
    elif(a == 2):
        obj.cust()
    else:
        print("You entered a number out of 1 or 2. Please re-run the program.")
        
        
