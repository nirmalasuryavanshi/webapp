import sqlite3
from colorama import Fore, Back, Style

# Create a database 
conn = sqlite3.connect('movie.db')

# Create cursor
c = conn.cursor()

#Creating a table
c.execute(''' CREATE TABLE movies (name text , actor text , actress text , director text, year_of_release integer)''')

#make a list
many_movies = [

('Jai Santoshi Maa', 'Ashish Kumar', 'Kanan Kaushal', '1975', 'Vijay Sharma'), 
('Home Alone' , 'Macaulay Culkin' , 'Catherine O Hara' , '1990', 'Chris Columbus'), 
('SkyScraper', 'Dwayne Johnson' , 'Neve Campbell', '2018', 'Rawson Marshall Thurber'), 
('Lagan', 'Aamir Khan', 'Gracy Singh', '2001', 'Ashutosh Gowariker'),
('Rampage', 'Dwayne Johnson' , 'Naomie Harris' , '2018' ,'Brad Peyton'),
              ]      

# Insert the items in an database
c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", many_movies)

# Query the database
c.execute(" SELECT * FROM movies")
item = c.fetchall()

print(Fore.RED + "\n Display all the rows of the table movies")
for i in item:
	print(i)

print(Fore.BLUE +"\n Display all movies name")
for j in item:
	print("\n",j[0])

print(Fore.GREEN +"\n The names of lead actor and actress")
for l in item:
	print("\n", l[1] + "\t\t" + l[2])

# to print the movies name based on it's actor's.
print(Fore.YELLOW +"\n The name of Actors and thier movies")
c.execute(" SELECT name, actor, actress from movies")
row = c.fetchall()
for rows in row:
	print ("\n", rows[0], "\t", rows[1], "\t", rows[2])

val=input(Fore.RED +"\n What is the name of movie whose actor is:\t")

c.execute(" SELECT name, actor, actress FROM movies where actor=? OR actress=?", (val,val))
r = c.fetchall()

for r1 in r:
	if val in r1[1]:
		print(Fore.RED + "\n Name of the movie is: \t",r1[0])
	elif val in r1[2]:
		print(Fore.RED + "\n Name of the movie is: \t",r1[0])

print(Fore.RED + "\n Data is not present with respect to given input.")

#Commit Changes
conn.commit()

# Close Connection 
conn.close()


