# PDS-PPI Review Website

This project uses Wagtail/Django, and is built using Python v3.8.

## How To Run

This web application was designed to run in a docker container (see Dockerfile for an example setup file). Before modifying this code, it is adviseable to review Wagtail's [getting started documentation](https://docs.wagtail.io/en/stable/getting_started/tutorial.html).

You can run a local instance of the web application for testing by running the following commands as listed in the Wagtail documentation.

```
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
```

Please note that this repository uses an SQLite3 database.  This can be changed to use PostgreSQL, or other database schemas if you wish, by modifying the `base.py` settings file, per Wagtail/Django documentation.

## Usage

_Basic usage instructions_
1. On first run, log in to the admin console (ex. http://localhost:8000/admin) and create a new root page, under **Pages**.
   1a. In the Settings->Sites page, click on your site, and have it point to that new root page.
2. Create a new mission index child page under your root page. This will serve as the current active reviews page.
3. Under the current reviews page, you can now add new child pages for each review.
   3a. Each top level review page allows you to assign the panel of reviewers (once created), scheduling, if the review is active ("featured"), descriptions for the review, and instructions for the different groups of reviewers.
   3b. Modify the visibility of this review page to only logged in users that are part of the review group can access these pages.
4. Create individual data, comments, and lien pages under each peer review
   4a. For data pages, just click to add a new data section, and fill out the appropriate name, URL to the data, and description of the data.
   4b. No action should need to be taken for the comments page. This new page that was created will allow for logged in users to leave comments.
   4c. NOTE: Lien pages are currently being worked on. This README will be updated once changes are pushed.
 
_Creating a users/groups/reviewers_
1. Create a new user by going to Settings->Users
2. Create a new group by going to Settings->Groups. No permissions modifications needs to happen here.
3. Assign groups to users by viewing the User in Settings, and applying the group under **Roles**.
4. Under Snippits->Affiliations, and Snippits->Roles, ensure that the appropriate information exists.
   4a. i.e., Under affiliations, something like "UCLA - PDS/PPI"
   4b. i.e., Under roles, "Data Reviewer", "Standards Reviewer", etc.
5. Now under Snippits->Reviewer, create a new reviewer, and perform the following:
   5a. Give the reviewer a name (this is to help keep anonymity, if requested.)
   5b. Select the user account (UID)
   5c. Select the appropriate affiliation and role.
6. You can now assign this new reviewer to the appropriate peer review, by editing the review page and choosing the reviewers that were set up.

## Current To-Do's
- Allow for uploading of documents on the comments page.
- Modify liens page programming to allow for linking in external documents (e.g. Google Doc/Sheet).
- Cleaning up web application UI, and generated website styling.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[APLv2](https://www.apache.org/licenses/LICENSE-2.0)
