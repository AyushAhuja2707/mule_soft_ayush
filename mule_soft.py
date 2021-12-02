import mysql.connector as mysql
from tabulate import tabulate
import datetime

print('*********** WELCOME *************')
database_l =input("Enter Database Name : ")
mydb = mysql.connect(host="localhost", user="root", password="abc456")
cur = mydb.cursor()
try:
	sql  = "create database "+database_l
	cur.execute(sql)
	print("Database Created!")
except Exception as e:
	mydb.rollback()
        # print(e)
	print("Welcome to Database "+database_l)
finally:
	cur.execute("commit")
	mydb.close()

def createtable():
	conn = mysql.connect(host="localhost", user="root", password="abc456",database=database_l)
	cur = conn.cursor()
	try:
		cur.execute("CREATE TABLE movies ( id int(50) NOT NULL auto_increment, name varchar(50), release_date date, director varchar(100), lead_actor varchar(50), lead_actress varchar(50), PRIMARY KEY(id) );")
		print("Movie Table Created")
	except Exception as e:
		conn.rollback()
        # print(e)
		print("Table already exists")
	finally:
		cur.execute("commit")
		conn.close()

def show():
	conn = mysql.connect(host="localhost",user="root",password="abc456",database=database_l)
	cur = conn.cursor()
	cur.execute("SELECT id,name, release_date, director, lead_actor, lead_actress FROM movies ORDER BY release_date ASC")
	records = cur.fetchall()
	head = ["id","Name", "Release Date","Director","Actors","Actress"]
	print("All Movies: ")
	print(tabulate(records, headers=head, tablefmt="grid"))
	cur.execute("commit")
	conn.close()

def find(query):
	conn = mysql.connect(host="localhost",user="root",password="abc456",database=database_l)
	cur = conn.cursor()
	try:
		cur.execute("SELECT name, release_date, director, lead_actor, lead_actress FROM movies where lead_actor LIKE '%" + query +"%' or lead_actress LIKE '%" + query +"%' ORDER BY release_date ASC")
		records = cur.fetchall()
		if records:
			head = ["Name", "Release Date","Director","Actors","Actress"]
			print("Search Results: ")
			print(tabulate(records, headers=head, tablefmt="grid"))
		else:
			print("No results found..")
	except Exception as e:
		print(e)
	finally:
		cur.execute("commit")
		conn.close()

def insert(name,release_date,director,actor,actress):
	conn = mysql.connect(host="localhost", user="root", password="abc456", database=database_l)
	cur = conn.cursor()
	try:
		cur.execute("INSERT INTO movies (name,release_date,director,lead_actor,lead_actress) VALUES (%s,%s,%s,%s,%s)", (name, release_date, director, actor,actress))
		print("Data Inserted!!!")
	except Exception as e:
		print(e)
	finally:
		cur.execute("commit")
		conn.close()
def delete():
	de = int(input("Enter Movie id Which is to be deleted : "))
	de =str(de)
	# print("To view Movie ID")
	conn = mysql.connect(host="localhost", user="root", password="abc456", database=database_l)
	cur = conn.cursor()
	try:
		cur.execute("DELETE from movies where id = "+ str(de))
		print("Movie Deleted !!!")
	except Exception as e:
		print(e)
	finally:
		cur.execute("commit")
		conn.close()


repeat = 1
while(repeat):
	print("\n")
	print("*****MENU******")
	# print("1. Create Database")
	print("1. Create Table")
	print("2. Insert a Movie")
	print("3. Show all Movies")
	print("4. Delete Movie")
	print("5. Search by Actors name")

	print("6. Enter '-1' to exit")
	choice = int(input("Enter Your Choice: "))
	# print("\n")
	# if choice==1:
	# 	createdb()
	if choice==1:
		createtable()
	elif choice==2:
		name = input("Enter Movie Name: ")
		release_date = input("Release date in YYYY-MM-DD format: ")
		director = input("Director Name: ")
		actor = input("Lead Actor Name: ")
		actress = input("Actress Name: ")
		insert(name,release_date,director,actor,actress)
	elif choice==3:
		show()
	elif choice==4:
		delete()
	elif choice==5:
		query = input("Enter Actor/Actress Name: ")
		find(query)
	elif choice==6:
		repeat=0
	else:
		print("Invalid Choice")