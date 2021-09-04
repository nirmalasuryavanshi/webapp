import sqlite3
import sys
# Create a database
conn = sqlite3.connect('m1.db')

# Create cursor
c = conn.cursor()

# Creating a table
#c.execute(''' CREATE TABLE mo1 (name text , actor text , actress text , director text, year_of_release integer)''')

# make a list
'''
many_m1 = [

('Jai Santoshi Maa', 'Ashish Kumar', 'Kanan Kaushal', '1975', 'Vijay Sharma'),
('Home Alone' , 'Macaulay Culkin' , 'Catherine O Hara' , '1990', 'Chris Columbus'),
('SkyScraper', 'Dwayne Johnson' , 'Neve Campbell', '2018', 'Rawson Marshall Thurber'),
('Lagan', 'Aamir Khan', 'Gracy Singh', '2001', 'Ashutosh Gowariker'),
('Jumanji', 'Robin Williams' , 'Kirsten Dunst' , '1995' ,'Joe Johnston'),
              ]

# Insert the items in an database
c.executemany("INSERT INTO mo1 VALUES (?,?,?,?,?)", many_m1)
'''
# Query the database
c.execute(" SELECT * FROM mo1")

item = c.fetchall()

print("\n Display all the rows of the table movies")
for i in item:
    print(i)

print("\n Display all movies name")
for j in item:
    print("\n", j[0])

print("\n The names of lead actor and actress")
for l in item:
    print("\n", l[1] + "\t\t" + l[2])

# to print the movies name based on it's actor's.
print("\n The name of Actors and thier movies")
c.execute(" SELECT name, actor, actress from mo1")
row = c.fetchall()
for rows in row:
    print("\n", rows[0], "\t", rows[1], "\t", rows[2])

val = input("\n What is the name of movie whose actor is:\t")

c.execute(" SELECT name, actor, actress FROM mo1 where actor=? OR actress=?", (val,val))
r = c.fetchall()

for r1 in r:
    if val in r1[1]:
        print("\n Name of the movie is: \t", r1[0])
        sys.exit()
    elif val in r1[2]:
        print("\n Name of the movie is: \t", r1[0])
        sys.exit()
if not val in r:
      print("\n Data is not present with respect to given input.")


'''
    elif not val in r1[1]:
        print("\n Data is not present with respect to given input.")
    elif not val in r1[2]:
        print("\n Data is not present with respect to given input.")
'''
# Commit Changes
conn.commit()

# Close Connection
conn.close()


