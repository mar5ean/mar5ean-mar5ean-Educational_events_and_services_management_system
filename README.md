Event Management System Documentation

Project Overview

This project is an Event Management System for educational institutions. It allows users (students and teachers) to create, view, and manage events. Events include details like title, description, date, location, time, participant type (teacher or student), and contact information. Students can also be grouped if necessary. The system uses Kivy for the GUI and SQLite for data storage.
________________________________________
Project Structure

•	main.py: The main application file containing all screens, database interactions, and app launch.

•	db.py: Module for interacting with the SQLite database. Includes functions for creating, inserting, and loading events.

•	event_app.kv (optional): If used, this file describes the GUI layout in Kivy's language. In this case, the layout is defined directly in Python.
________________________________________
Installation

1.	Install Python (3.7+ recommended).
	
2.	Install Kivy
	
3.	SQLite is included with Python by default.
________________________________________
Key Components

Screens:

1.	MainScreen:

o	Welcome screen with buttons to navigate to the event list or create a new event.

2.	EventScreen

o	Displays a list of all events. Each event is a button that leads to a detailed event view.

3.	EventDetailsScreen:

o	Shows detailed information about a selected event (title, description, date, location, and contact info).

4.	AddEventScreen:

o	Form for creating new events with fields for:

	Title, description, date, time, location.

	Participant type (teacher or student).

	Group (if student) and contact info (phone/email).

o	Back button returns to the main screen.

Functions in db.py:

•	create_db(): Creates the SQLite database and the events table if they do not exist.

•	insert_event(...): Adds a new event to the database.

•	load_events(): Loads and returns all events from the database.

________________________________________
User Interaction

1.	Main Screen: Users see a welcome message with options to view events or create a new event.
   
2.	Event List: Clicking an event shows its details. Events are displayed as buttons.
   
3.	Create Event: Fill out a form to add a new event, then click Create Event to save it to the database.
________________________________________
Database Schema

The events table in SQLite has the following columns:

Column	Type	Description

id	INTEGER	Unique event ID (Primary Key, AUTOINCREMENT)

title	TEXT	Event title

description	TEXT	Event description

date	TEXT	Event date (YYYY-MM-DD format)

location	TEXT	Event location

time_block	TEXT	Event time

user_id	INTEGER	ID of the creator (teacher/student)

group	TEXT	Group (if participant is a student)

contact_info	TEXT	Contact info (phone/email)
________________________________________
Possible Improvements

1.	User Authentication: Implement login for teachers and students.
   
2.	Event Filters: Add filters for event sorting (e.g., by date, participant type).
	
3.	Edit/Delete Events: Allow users to edit or delete their own events.
________________________________________
This is not the final version of the project!

