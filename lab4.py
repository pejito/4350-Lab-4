# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:59:41 2021

@author: ryanf
"""


import sqlite3
from sqlite3 import Error
#import os.path

def create_connection(db_file):
    conn = None 
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table):
    try:
        c= conn.cursor()
        c.execute(create_table)
    except Exception as e:
        print(e)  

def add_entries_to_trip(conn):
 t1 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (101, 'Boston', 'Atlanta') '''
 t2 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (102, 'Atlanta', 'Boston') '''
 t3 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (103, 'San Francisco', 'Portland') '''
 t4 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (104, 'Portland', 'San Francisco') '''
 t5 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (105, 'Seattle', 'Chicago') '''
 t6 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (106, 'Chicago', 'Seattle') '''
 t7 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (107, 'Orlando', 'Las Vegas') '''
 t8 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (108, 'Las Vegas', 'Orlando') '''
 t9 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (109, 'Austin', 'New York City') '''
 t10 = ''' INSERT INTO trip(tripNumber, startLocationName, destinationName) VALUES (110, 'New York City', 'Austin') '''
 cur = conn.cursor()
 cur.execute(t1)
 cur.execute(t2)
 cur.execute(t3)
 cur.execute(t4)
 cur.execute(t5)
 cur.execute(t6)
 cur.execute(t7)
 cur.execute(t8)
 cur.execute(t9)
 cur.execute(t10)
 print("-------------------------------------------------------------")
 print("ORIGINAL TRIP TABLE: ")
 print("-------------------------------------------------------------")
 for row in cur.execute('SELECT * FROM trip'):
     print(row)
 conn.commit()

def add_entries_to_trip_offering(conn):
 to1 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (101, 'January 1, 2021', '8:00AM', '6:00PM', 'Rachel Green', 011) '''
 to2 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (102, 'February 1, 2021', '10:00AM', '8:00PM', 'Phoebe Buffay', 012) '''
 to3 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (103, 'March 1, 2021', '12:00PM', '9:00PM', 'Monica Geller', 120) '''
 to4 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (104, 'April 1, 2021', '1:00PM', '10:00PM', 'Joey Tribbiani', 018) '''
 to5 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (105, 'May 1, 2021', '6:30AM', '9:30PM', 'Chandler Bing', 013) '''
 to6 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (106, 'June 1, 2021', '8:15AM', '11:15PM', 'Ross Geller', 019) '''
 to7 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (107, 'July 1, 2021', '4:00AM', '11:00PM', 'Joey Tribbiani', 011) '''
 to8 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (108, 'August 1, 2021', '4:15AM', '11:15PM', 'Chandler Bing', 017) '''
 to9 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (109, 'September 1, 2021', '2:30AM', '10:30PM', 'Ross Geller', 011) '''
 to10 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (110, 'October 1, 2021', '3:15AM', '11:15PM', 'Ross Geller', 014) '''
 cur = conn.cursor()
 cur.execute(to1)
 cur.execute(to2)
 cur.execute(to3)
 cur.execute(to4)
 cur.execute(to5)
 cur.execute(to6)
 cur.execute(to7)
 cur.execute(to8)
 cur.execute(to9)
 cur.execute(to10)
 print("-------------------------------------------------------------")
 print("ORIGINAL TRIPOFFERING TABLE: ")
 print("-------------------------------------------------------------")
 for row in cur.execute('SELECT * FROM tripOffering'):
     print(row)
 conn.commit()
 
def add_entries_to_bus(conn):
 b1 = ''' INSERT INTO bus(busID, model, year) VALUES (011, 'Single deck', 1999) '''
 b2 = ''' INSERT INTO bus(busID, model, year) VALUES (012, 'Single deck', 2009) '''
 b3 = ''' INSERT INTO bus(busID, model, year) VALUES (013, 'Double decker', 2001) '''
 b4 = ''' INSERT INTO bus(busID, model, year) VALUES (014, 'Double decker', 2005) '''
 b5 = ''' INSERT INTO bus(busID, model, year) VALUES (015, 'Coach', 2007) '''
 b6 = ''' INSERT INTO bus(busID, model, year) VALUES (016, 'Coach', 1992) '''
 b7 = ''' INSERT INTO bus(busID, model, year) VALUES (017, 'School bus', 2015) '''
 b8 = ''' INSERT INTO bus(busID, model, year) VALUES (018, 'School bus', 2010) '''
 b9 = ''' INSERT INTO bus(busID, model, year) VALUES (019, 'Minibus', 2009) '''
 b10 = ''' INSERT INTO bus(busID, model, year) VALUES (120, 'Minibus', 2021) '''
 cur = conn.cursor()
 cur.execute(b1)
 cur.execute(b2)
 cur.execute(b3)
 cur.execute(b4)
 cur.execute(b5)
 cur.execute(b6)
 cur.execute(b7)
 cur.execute(b8)
 cur.execute(b9)
 cur.execute(b10)
 print("-------------------------------------------------------------")
 print("ORIGINAL BUS TABLE: ")
 print("-------------------------------------------------------------")
 for row in cur.execute('SELECT * FROM bus'):
     print(row)
 conn.commit()
 
def add_entries_to_driver(conn):
 d1 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Rachel Green', '9491234567') '''
 d2 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Monica Geller', '9497654321') '''
 d3 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Phoebe Buffay', '9492345678') '''
 d4 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Joey Tribbiani', '9498765432') '''
 d5 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Chandler Bing', '9493456789') '''
 d6 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Ross Geller', '9499876543') '''
 d7 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Mike Hannigan', '9494567890') '''
 d8 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Gunther Centralperk', '9490987654') '''
 d9 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Ben Geller', '9495678910') '''
 d10 = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Emma Green', '9491098765') '''
 cur = conn.cursor()
 cur.execute(d1)
 cur.execute(d2)
 cur.execute(d3)
 cur.execute(d4)
 cur.execute(d5)
 cur.execute(d6)
 cur.execute(d7)
 cur.execute(d8)
 cur.execute(d9)
 cur.execute(d10)
 print("-------------------------------------------------------------")
 print("ORIGINAL DRIVER TABLE: ")
 print("-------------------------------------------------------------")
 for row in cur.execute('SELECT * FROM driver'):
     print(row)
 conn.commit()
 
def add_entries_to_stop(conn):
 s1 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (201, '15 Bird Lane, Atlanta GA') '''
 s2 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (202, '22 Westbrook, Boston MA') '''
 s3 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (203, '36 Birch Road, Portland OR') '''
 s4 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (204, '11 Fairway, San Francisco CA') '''
 s5 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (205, '77 Broomfield, Chicago IL') '''
 s6 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (206, '42 Bedford, Seattle WA') '''
 s7 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (207, '83 Main Stree, Las Vegas NV') '''
 s8 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (208, '39 First Street, Orlando FL') '''
 s9 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (209, '88 Olive, New York City NY') '''
 s10 = ''' INSERT INTO stop(stopNumber, stopAddress) VALUES (210, '93 Bluejay, Austin TX') '''
 cur = conn.cursor()
 cur.execute(s1)
 cur.execute(s2)
 cur.execute(s3)
 cur.execute(s4)
 cur.execute(s5)
 cur.execute(s6)
 cur.execute(s7)
 cur.execute(s8)
 cur.execute(s9)
 cur.execute(s10)
 print("-------------------------------------------------------------")
 print("ORIGINAL STOP TABLE: ")
 print("-------------------------------------------------------------")
 for row in cur.execute('SELECT * FROM stop'):
     print(row)
 conn.commit()

def add_entries_to_actualTripStopInfo(conn):
 at1 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (101, 'January 1, 2021', 201, '6:00PM', '8:30AM', '6:30PM', 15, 8) '''
 at2 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (102, 'February 1, 2021', 201, '8:00PM', '10:30AM', '8:30PM', 30, 6) '''
 at3 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (103, 'March 1, 2021', 201, '9:00PM', '12:30PM', '9:30PM', 22, 20) '''
 at4 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (104, 'April 1, 2021', 201, '10:00PM', '1:30PM', '10:30PM', 4, 18) '''
 at5 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (105, 'May 1, 2021', 201, '9:30PM', '7:00AM', '10:00PM', 15, 8) '''
 at6 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (106, 'June 1, 2021', 201, '11:15PM', '8:45AM', '11:45PM', 17, 16) '''
 at7 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (107, 'July 1, 2021', 201, '11:00PM', '4:30AM', '11:30PM', 27, 9) '''
 at8 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (108, 'August 1, 2021', 201, '11:15PM', '4:45AM', '11:45PM', 10, 13) '''
 at9 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (109, 'September 1, 2021', 201, '10:30PM', '3:00AM', '11:0PM', 24, 20) '''
 at10 = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (110, 'October 1, 2021', 201, '11:15PM', '3:45AM', '11:45PM', 14, 16) '''
 cur = conn.cursor()
 cur.execute(at1)
 cur.execute(at2)
 cur.execute(at3)
 cur.execute(at4)
 cur.execute(at5)
 cur.execute(at6)
 cur.execute(at7)
 cur.execute(at8)
 cur.execute(at9)
 cur.execute(at10)
 print("-------------------------------------------------------------")
 print("ORIGINAL ActualTripStopInfo TABLE: ")
 print("-------------------------------------------------------------")
 for row in cur.execute('SELECT * FROM actual_trip_stop_info'):
     print(row)
 conn.commit()
 
def add_entries_to_tripStopInfo(conn):
 ts1 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (101, 201, 001, 10) '''
 ts2 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (102, 202, 001, 10) '''
 ts3 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (103, 203, 002, 9) '''
 ts4 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (104, 204, 002, 9) '''
 ts5 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (105, 205, 003, 15) '''
 ts6 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (106, 206, 003, 15) '''
 ts7 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (107, 207, 004, 19) '''
 ts8 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (108, 208, 004, 19) '''
 ts9 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (109, 209, 005, 20) '''
 ts10 = ''' INSERT INTO trip_stop_info(tripNumber, stopNumber, sequenceNumber, drivingTime) VALUES (110, 210, 005, 20) '''
 cur = conn.cursor()
 cur.execute(ts1)
 cur.execute(ts2)
 cur.execute(ts3)
 cur.execute(ts4)
 cur.execute(ts5)
 cur.execute(ts6)
 cur.execute(ts7)
 cur.execute(ts8)
 cur.execute(ts9)
 cur.execute(ts10)
 print("-------------------------------------------------------------")
 print("ORIGINAL TRIPSTOPINFO TABLE: ")
 print("-------------------------------------------------------------")
 for row in cur.execute('SELECT * FROM trip_stop_info'):
     print(row)
 conn.commit()

def displayScheduleOfAllTrips(conn):
    #trip(startlocationname, destinationname) tripoffering (date, scheduledstarttime, scheduledarrivaltime, drivername,busid), join on trip number
    join1 = ''' SELECT trip.startLocationName, trip.destinationName, tripOffering.date, tripOffering.scheduledStartTime, tripOffering.scheduledArrivalTime, tripOffering.driverName, tripOffering.busID FROM trip INNER JOIN tripOffering ON trip.tripNumber = tripOffering.tripNumber'''
    cur = conn.cursor()
    print("-------------------------------------------------------------")
    print("Schedule of all trips: ")
    print("-------------------------------------------------------------")
    for row in cur.execute(join1):
        print(row)
    conn.commit()

def delete_by_trip_num(conn):
    #delete a trip offering specified by trip
    dlt = ''' DELETE FROM tripOffering WHERE tripNumber = '101' AND date = 'January 1, 2021' AND scheduledStartTime = '8:00AM' '''
    cur = conn.cursor()
    cur.execute(dlt)
    print("-------------------------------------------------------------")
    print("AFTER DELETING SPECIFIC TRIP NUMBER FROM TRIP OFFERING: ")
    print("-------------------------------------------------------------")
    for row in cur.execute('SELECT * FROM tripOffering'):
     print(row)
    conn.commit()

def addTripOfferings(conn):
    #add trip offerings to the trip offering table
    tri1 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (111, 'January 11, 2021', '9:00AM', '1:00PM', 'Bob Smith', 017) '''
    tri2 = ''' INSERT INTO tripOffering(tripNumber, date, scheduledStartTime, scheduledArrivalTime, driverName, busID) VALUES (112, 'January 10, 2021', '11:00AM', '7:00PM', 'Smith Jim', 015) '''
    cur = conn.cursor()
    cur.execute(tri1)
    cur.execute(tri2)
    print("-------------------------------------------------------------")
    print("AFTER ADDING A SET OF TRIP OFFERINGS: ")
    print("-------------------------------------------------------------")
    for row in cur.execute('SELECT * FROM tripOffering'):
     print(row)
    conn.commit()

def updateTripOfferings(conn):
    #update attributes for given tripOfferings
    updtStatementDriver = ''' UPDATE tripOffering SET driverName = 'Joshua Bug' WHERE tripNumber = 105 '''
    updtStatementBus = ''' UPDATE tripOffering SET busID = 020 WHERE tripNumber = 101 '''
    cur = conn.cursor()
    cur.execute(updtStatementDriver)
    cur.execute(updtStatementBus)
    print("-------------------------------------------------------------")
    print("AFTER UPDATING A DRIVER AND BUS OF CERTAIN TRIP OFFERINGS: ")
    print("-------------------------------------------------------------")
    for row in cur.execute('SELECT * FROM tripOffering'):
     print(row)
    conn.commit()

def selectTripStopInfo(conn):
    matchingYearStatement = " SELECT * FROM trip_stop_info "
    cur = conn.cursor()
    print("-------------------------------------------------------------")
    print("Trip stop info: ")
    print("-------------------------------------------------------------")
    for row in cur.execute(matchingYearStatement):
        print(row)
    conn.commit()
    
def displayDriverSched(conn):
    join = ''' SELECT * FROM driver INNER JOIN TripOffering ON driver.driverName = tripOffering.driverName WHERE driver.driverName =  'Ross Geller' '''
    cur = conn.cursor()
    print("-------------------------------------------------------------")
    print("Ross Geller's (driver) schedule: ")
    print("-------------------------------------------------------------")
    for row in cur.execute(join):
        print(row)
    cur.execute(join)
    conn.commit()
    
def addDriver(conn):
    addDriver = ''' INSERT INTO driver(driverName, driverTelephoneNumber) VALUES ('Jimothy Turner', '6612229999') '''
    cur = conn.cursor()
    cur.execute(addDriver)
    print("-------------------------------------------------------------")
    print("DRIVER, AFTER ADDING A NEW DRIVER: ")
    print("-------------------------------------------------------------")
    for row in cur.execute('SELECT * FROM driver'):
     print(row)
    conn.commit()
    
def addBus(conn):
    add_Bus = ''' INSERT INTO bus(busID, model, year) VALUES (020, 'Triple Decker', 1988) '''
    cur = conn.cursor()
    cur.execute(add_Bus)
    print("-------------------------------------------------------------")
    print("BUS, AFTER ADDING A NEW BUS: ")
    print("-------------------------------------------------------------")
    for row in cur.execute('SELECT * FROM bus'):
     print(row)
    conn.commit()
    
def delBus(conn):    
    dltBus = ''' DELETE FROM bus WHERE busID = 011 '''
    cur = conn.cursor()
    cur.execute(dltBus)
    print("-------------------------------------------------------------")
    print("BUS, AFTER DELETING A BUS: ")
    print("-------------------------------------------------------------")
    for row in cur.execute('SELECT * FROM bus'):
     print(row)
    conn.commit()
    
def actualTripInfo(conn):
    add_actualTripInfo = ''' INSERT INTO actual_trip_stop_info(tripNumber, date, scheduledStartTime, scheduledArrivalTime, actualStartTime, actualArrivalTime, numberOfPassengerIn, numberOfPassengerOut) VALUES (111, 'January 1, 2021', 201, '6:00PM', '8:30AM', '6:30PM', 15, 8) '''
    cur = conn.cursor()
    cur.execute(add_actualTripInfo)
    print("-------------------------------------------------------------")
    print("ActualTripInfo, AFTER ADDING A NEW ENTRY: ")
    print("-------------------------------------------------------------")
    for row in cur.execute('SELECT * FROM actual_trip_stop_info'):
     print(row)
    conn.commit()
    

def main():
    database = r"C:\Users\ryanf\Desktop\SchoolStuff\CS4350\lab4\lab4.db"
    
    conn = create_connection(database)
    #conn.execute("PRAGMA foreign_keys = 1")
    print('creating tables now')
    trip = """ CREATE TABLE IF NOT EXISTS trip (
    tripNumber integer NOT NULL PRIMARY KEY,
    startLocationName text NOT NULL,
    destinationName text NOT NULL
    ); """
    
    print('table 1 made')
    
    trip_offering = """CREATE TABLE IF NOT EXISTS tripOffering (
    tripNumber integer NOT NULL PRIMARY KEY,
    date text NOT NULL,
    scheduledStartTime text NOT NULL,
    scheduledArrivalTime text NOT NULL,
    driverName text NOT NULL,
    busID integer NOT NULL
    );""" 
    print('table 2 done')
    
    bus = """ CREATE TABLE IF NOT EXISTS bus (
    busID integer NOT NULl PRIMARY KEY,
    model text NOT NULL,
    year text NOT NULL
    );"""
    print('table 3 done')
    
    driver = """ CREATE TABLE IF NOT EXISTS driver (
    driverName text NOT NULL,
    driverTelephoneNumber text NOT NULL,
    PRIMARY KEY(driverName, driverTelephoneNumber)
    );"""
    
    print('table 4 done')
    stop = """CREATE TABLE IF NOT EXISTS stop (
    stopNumber integer NOT NULl PRIMARY KEY,
    stopAddress text NOT NULL
    );"""
    
    print('table 5 done')
    actual_trip_stop_info = """CREATE TABLE IF NOT EXISTS actual_trip_stop_info (
    tripNumber integer NOT NULL PRIMARY KEY,
    date text NOT NULL,
    scheduledStartTime text NOT NULL,
    scheduledArrivalTime text NOT NULL,
    actualStartTime text NOT NULL,
    actualArrivalTime text NOT NULL,
    numberOfPassengerIn integer NOT NULL,
    numberOfPassengerOut integer NOT NULL
    );"""
    
    print('table 6 done')
    trip_stop_info = """CREATE TABLE IF NOT EXISTS trip_stop_info (
    tripNumber integer NOT NULL PRIMARY KEY,
    stopNumber integer NOT NULL,
    sequenceNumber integer NOT NULL,
    drivingTime integer NOT NULL
    ); """
    print('table 7 done')
    
    try:
     if conn is not None:
         create_table(conn, trip)
         create_table(conn, trip_offering)
         create_table(conn, bus)
         create_table(conn, driver)
         create_table(conn, stop)
         create_table(conn, actual_trip_stop_info)
         create_table(conn, trip_stop_info)
         
         #add dummy data to tables
         add_entries_to_trip(conn)
         add_entries_to_trip_offering(conn)
         add_entries_to_bus(conn)
         add_entries_to_driver(conn)
         add_entries_to_stop(conn)
         add_entries_to_actualTripStopInfo(conn)
         add_entries_to_tripStopInfo(conn)
         
         #display schedule of all trips
         displayScheduleOfAllTrips(conn)
         #delete trip from tripOffering
         delete_by_trip_num(conn)
         #add an entry to tripOffering
         addTripOfferings(conn)
         #edit entries in tripOffering
         updateTripOfferings(conn)
         #select all in tripStopInfo
         selectTripStopInfo(conn)
         #select driver schedule -> join driver and tripoffering
         displayDriverSched(conn)
         #add a driver
         addDriver(conn)
         #add an entry to bus
         addBus(conn)
         #delete an entry from bus
         delBus(conn)
         #insert an entry into actualTripStopInfo
         actualTripInfo(conn)
         
         
     else:
         print("error: cannot establish connection")
    finally:
        conn.close()
        print("connection to database has been closed")
if __name__ == '__main__':
    main()