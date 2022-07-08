#!/usr/bin/env bash

cd ./backend/liaison-arduino && python test.py
cd ./backend/ && python manage.py runserver



