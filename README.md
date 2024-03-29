# deep

A htmx and django personal project with the goals of:
   - learning more about each with new challenges
   - how to write less code but more reusable code
   - just trying things out (django-cookiecutter, django-treebeard etc)

This project currently manages nested unordered (informally ordered, I guess) lists of text entries:
 - edit an entry (ctrl-click)
 - add a sibling (+)
 - add a child  (/)
 - delete self (x)

<img width="1271" alt="image" src="https://github.com/atcrank/deep/assets/26860752/5232f372-94bb-4595-b3e7-125fe2c88c2d">


Immediate goals:
 - additional methods on each element (show help string from obj.__doc__ for example)
 - use content types to make the content item generic
 - page and sub-page objects
 - user-awareness and per object group-permissions
 - django-ninja api setup

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy deep4

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
