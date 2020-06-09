# Chatbot README

This project implements a simple model for a question and answer app. Question text is easy to update and old versions
of questions are kept. Responses tie back to the User who responded, the Question being answered, and the
QuestionText seen by the User at the time of answering. User's objects include some basic personal info.

Included is a simple interface for viewing all existing questions, updating question text, and seeing how question text
has changed over time.

The [django-admin site](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/) can be used to add new object
instances, including Users.

## Prerequisites

1. Ensure you have a version of Python >= 3.6 installed

## Setup

1. Clone the repository `git clone https://github.com/toboyle94/chatbot.git`
2. Go to the root of the project `cd django-template`
3. Initialize a virtual environment with venv (standard package in the python library) `python3 -m venv .`
4. Activate the virtual environment `source bin/activate`
5. Install the project dependencies `pip3 install -r requirements.txt`

## Starting the Local Server

1. Go to the root of the django_project `cd django_project`
2. Run the migrations `python3 manage.py migrate`
2. Run the django management command `python3 manage.py runserver 8001`

**Note - We are not running the default port 8000**

## Adding New Questions

1. Go to the root of the django_project `cd django_project`
2. Create a new superuser `python3 manage.py createsuperuser`
3. Start the local server `python3 manage.py runserver 8001`
4. [Click here](http://localhost:8001/admin/) to navigate to the admin portal in your favorite browser
5. Use the GUI to create new Question and QuestionText objects

## Viewing Question diffs and Changing Text

1. Follow "Starting the Local Server" instructions
2. [Click here](http://localhost:8001/question/) to navigate to the questions page
3. Click on a question
4. The Question's title and current text will be displayed, along with diffs between the current question text and old version of the question
5. To change the question text, input the new text into the "Update current text" form and click the "Submit" button
6. To go back to the full list of question click the "Back to Questions List" button

## Project Reflection

Implementing the data model requirements was fairly straightforward, and I was able to quickly come up with a decent way
to allow for updates to question text. It was trickier to think about what unspecified fields should be added. Linking
Response directly to QuestionText was my own idea, as I think it would be valuable to quickly see what version of a question the
User responded to (without checking timestamps), but with the limited context I'm unsure of the real-life value.

My method of storing old question versions is also lacking, e.g. there is no way to revert to an old version of the
Question without adding a new QuestionText object. This could be an attractive feature or a shortcoming depending on the
product requirements. A more flexible QuestionText could be implemented with some kind of `status` field on
QuestionText and some code to ensure only a single instance has an active status at any given time.

Another potential change to make depending on the product details is in the way old QuestionText versions are stored.
If older versions are infrequently accessed it may make sense to store them in a more compact format either by zipping
or encoding them. It may even make sense to only store the diffs and not hold onto the original text at all.

Some other obvious improvements to make are the addition of tests, display clean-ups to the admin site (show some more
values so objects are more easily identifiable by humans), GUI improvements (either prettier templates or building
a new frontend app with a modern framework), and the addition of basic user authentication (currently endpoints are
open to the public).