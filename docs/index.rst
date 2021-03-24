.. linkedin-cli documentation master file, created by
   sphinx-quickstart on Wed Mar 24 01:50:42 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

linkedin-cli
========

Linkedin command line interface (cli) is a python 3 console application to handle authentication and communication with LinkedIn API v2.

Linkedin-cli requires a linkedin application client id and client secret to authenticate a user on the linkedin api v2. `Create a linkedin application <https://www.linkedin.com/developers/apps/new/>`_ on linkedin developer site if you don't have already.

Follow `Tigillo <https://www.linkedin.com/company/tigillo>`_ on linkedin or visit `Tigillo Startup and DevOps Consultancy <https://tigillo.com/>`_ for the latest updates.


Requirements
============
python 3

Installation
============
    python3 -m pip install linkedin-cli

Running
=======
    python3 -m linkedin


Usage
=====
    usage: linkedin <command> [<args?]

    These are common linkedin commands used in various situations:

        config       Get and set linkedin-cli options
        login        Login with a user for api access
        me           Display logged in user details
        post         Share a post

    Other commands

        help         Print help (this message)
        version      Print the version information

Configure Linkedin Application
==============================
Run below command and provide your client id and secret of your linkedin application. Configuration will be saved to `~/.linkedin/config.json` file.

    linkedin configure set application

Linkedin Application Configuration
==================================
Go to `auth` page of your linkedin application and add `http://localhost:4625` address as the `Authorized redirect URLs for your app` on the *OAuth 2.0 settings* section.

Login
=====
Run below command and authenticate your linkedin application for your user on the opened web dialog. Once approved your api token will be stored to `~/.linkedin/config.json` file.

    linkedin login


Share a Post
============
Put content between double quotes, new lines supported. Only text content supported currently.

    linkedin post "Hello connections!

    Sent from my terminal via linkedin-cli"


Post Visibility
===============
Default visibility option for post command is `connections`. Visibility option can be set as `connections` or `public`.

    linkedin post -v public "Hello world!

    Sent from my terminal via linkedin-cli"


Build
=====
    python3 setup.py build
