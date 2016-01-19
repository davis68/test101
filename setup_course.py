"""
Presumes a tree structure of:
    admin/
        rpt_all_students.csv
    autograded/
    feedback/
    release/
    source/
    submitted/
    gradebook.db
    
"""

# Script parameters
studentDB = './admin/rpt_all_students.csv'

# Remove an existing database.
import os
if os.path.exists("gradebook.db"):
    os.remove("gradebook.db")

# Create the database.
from nbgrader.api import Gradebook
gb = Gradebook('sqlite:///gradebook.db')

# Load the student data from disk.
import csv
dbReader = None
try:
    with open(studentDB) as dbFile:
        dbReader = csv.DictReader(dbFile)
        
        # Populate the database.
        for entry in dbReader:
            gb.add_student(entry['Net ID'],
                           first_name=entry['First Name'],
                           last_name=entry['Last Name'],
                           email='%s@illinois.edu'%entry['Net ID'])
except IOError as exc:
    print exc
    print 'Unable to access database at %s.'%dbFile

# Add some test students as well.
gb.add_student('stormhold',
               first_name='King',
               last_name='Stormhold',
               email='%s@illinois.edu'%'davis68')
gb.add_student('tristan',
               first_name='Tristan',
               last_name='of Wall',
               email='%s@illinois.edu'%'davis68')
gb.add_student('yvaine',
               first_name='Yvaine',
               last_name='Star',
               email='%s@illinois.edu'%'davis68')
gb.add_student('davis68',
               first_name='Neal',
               last_name='Davis',
               email='%s@illinois.edu'%'davis68')
