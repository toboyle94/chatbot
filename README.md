# Django-Template

This project is intended to be a simple template to get a local Django web app started. The README will walk through the prerequisites required for the project, as well as the project setup.

## Prerequisites

1. Ensure you have a version of Python >= 3.6 installed

## Setup

1. Clone the repository `git clone https://github.com/buoy-engineering/django-template.git`
2. Go to the root of the project `cd django-template`
3. Initialize a virtual environment with venv (standard package in the python library) `python3 -m venv .`
4. Activate the virtual environment `source bin/activate`
5. Install the project dependencies `pip3 install -r requirements.txt`

## Starting the Local Server

1. Go to the root of the django_project `cd django_project`
2. Run the django management command `python3 manage.py run server 8001`

**Note - We are not running the default port 8000**
