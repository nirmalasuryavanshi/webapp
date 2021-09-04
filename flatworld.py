from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('Learn To Code!')
#root.iconbitmap('c:/gui/codemy.ico')
#root.iconbitmap('/c/Users/DELL/PycharmProjects/untitled')
root.geometry("400x600")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('films.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")
'''
# Create Update function to update a record
def update():
	# Create a database or connect to one
	conn = sqlite3.connect('films.db')
	# Create cursor
	c = conn.cursor()


	c.execute("""UPDATE filmset SET
		movie_name = :movie_name,
		leadActor_name = :leadActor_name,
		Actresses = :Actresses,
		yorelaese = :yorelaese,
		director_name = :director_name,
			WHERE oid = :oid""",
		{
		'movie_name': movie_name_editor.get(),
		'leadActor_name': leadActor_name_editor.get(),
		'Actresses': Actresses_editor.get(),
		'yorelaese': yorelease_editor.get(),
		'director_name': director_name_editor.get(),
		'oid': record_id
		})


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

	editor.destroy()
	root.deiconify()

# Create Edit function to update a record
def edit():
	root.withdraw()
	global editor
	editor = Tk()
	editor.title('Update A Record')

	editor.geometry("400x300")
	# Create a database or connect to one
	conn = sqlite3.connect('films.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	# Query the database
	c.execute("SELECT * FROM filmset WHERE oid = " + record_id)
	records = c.fetchall()
	
	#Create Global Variables for text box names
	global movie_name_editor
	global leadActor_name_editor
	global Actresses_editor
	global yorelaese_editor
	global director_name_editor

	# Create Text Boxes
	movie_name_editor = Entry(editor, width=30)
	leadActor_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
	Actresses_editor = Entry(editor, width=30)
	yorelaese_editor.grid(row=1, column=1)
	director_name_editor = Entry(editor, width=30)
	'''
	address_editor.grid(row=2, column=1)
	city_editor = Entry(editor, width=30)
	city_editor.grid(row=3, column=1)
	state_editor = Entry(editor, width=30)
	state_editor.grid(row=4, column=1)
	zipcode_editor = Entry(editor, width=30)
	zipcode_editor.grid(row=5, column=1)
	'''
	
	# Create Text Box Labels
	movie_name_label = Label(editor, text="First Name")
	leadActor_label.grid(row=0, column=0, pady=(10, 0))
	Actresses_label = Label(editor, text="Last Name")
	yorelases_label.grid(row=1, column=0)
	director_name_label = Label(editor, text="Address")

	'''
	address_label.grid(row=2, column=0)
	city_label = Label(editor, text="City")
	city_label.grid(row=3, column=0)
	state_label = Label(editor, text="State")
	state_label.grid(row=4, column=0)
	zipcode_label = Label(editor, text="Zipcode")
	zipcode_label.grid(row=5, column=0)
'''
	# Loop thru results
	for record in records:
		movie_name_editor.insert(0, record[0])
		leadActor_editor.insert(0, record[1])
		yorelases_editor.insert(0, record[2])
		director_name_editor.insert(0, record[3])
		'''ert(0, record[4])
		zipcode_editor.insert(0, record[5])
'''

	# Create a Save Button To Save edited record
	edit_btn = Button(editor, text="Save Record", command=update)
	edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

	


# Create Function to Delete A Record
def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('films.db')
	# Create cursor
	c = conn.cursor()

	# Delete a record
	c.execute("DELETE from filmset WHERE oid = " + delete_box.get())

	delete_box.delete(0, END)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()



# Create Submit Function For database
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('films.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO filmset VALUES (:movie_name, :leadActor_name, :Actresses , :yorelaese , :director_name )",
			{
				'movie_name': f_name.get(),
				'leadActor_name': l_name.get(),
				'Actresses': address.get(),
				'yorelaese': yorelaese .get(),
				'director_name ': director_name.get(),
			})


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

	# Clear The Text Boxes
	movie_name.delete(0, END)
	leadActor_name.delete(0, END)
	Actresses.delete(0, END)
	yorelaese.delete(0, END)
	director_name.delete(0, END)


# Create Query Function
def query():
	# Create a database or connect to one
	conn = sqlite3.connect('films.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM filmset")
	records = c.fetchall()
	# print(records)

	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[6]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()


# Create Text Boxes
movie_name = Entry(root, width=30)
movie_name.grid(row=0, column=1, padx=20, pady=(10, 0))
leadActor_name = Entry(root, width=30)
leadActor_name.grid(row=1, column=1)
Actresses = Entry(root, width=30)
Actresses.grid(row=2, column=1)
yorelaese = Entry(root, width=30)
yorelaese.grid(row=3, column=1)
director_name = Entry(root, width=30)
director_name.grid(row=4, column=1)
'''
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)
'''

# Create Text Box Labels
movie_name_label = Label(root, text="Movie_Name")
movie_name_label.grid(row=0, column=0, pady=(10, 0))
leadActor_name_label = Label(root, text="leadActor Name")
Actresses.grid(row=1, column=0)
Actresses = Label(root, text="Actresses")
yorelaese.grid(row=2, column=0)
yorelaese = Label(root, text="yorelaese")
director_name.grid(row=3, column=0)
director_name = Label(root, text="director_name")
'''
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)
'''

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


#Commit Changes
conn.commit()

# Close Connection 
conn.close()

root.mainloop()