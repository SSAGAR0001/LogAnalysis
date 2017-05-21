# Project Log Analysis

## Introduction
Its a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

# Steps to run this file
* Download virtual Machine from here [VM](https://www.virtualbox.org/wiki/Downloads).
* Download vagrant from here [vagrant](https://www.vagrantup.com/downloads.html).
* Clone the VM Configuration from [here](https://github.com/udacity/fullstack-nanodegree-vm).
* Type the command `vagrant up` and `vagrant ssh`.
* Copy the contents of zip file into /vagrant folder.
* Run psql -d news -f newsdata.sql to load the data.
* If you want to check,update or delete the schema use `psql news`. 
* Open sql and import the given sql file by using \i log.sql to your database.
* After all, run the python file.

