
[![Maintainability](https://api.codeclimate.com/v1/badges/346e504f6f72b4a063e3/maintainability)](https://codeclimate.com/github/bashman1/iReporter_api/maintainability)
[![Build Status](https://travis-ci.org/bashman1/iReporter_api.svg?branch=incidents)](https://travis-ci.org/bashman1/iReporter_api)
[![Coverage Status](https://coveralls.io/repos/github/bashman1/iReporter_api/badge.svg?branch=incidents)](https://coveralls.io/github/bashman1/iReporter_api?branch=incidents)
[![Requirements Status](https://requires.io/github/bashman1/iReporter_api/requirements.svg?branch=incidents)](https://requires.io/github/bashman1/iReporter_api/requirements/?branch=incidents)


# iReporter_api
Corruption is a huge bane to Africa’s development. African countries must develop novel and  localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables  any/every citizen to bring any form of corruption to the notice of appropriate authorities and the  general public. Users can also report on things that needs government intervention 

# Features 
1. User Ragistration
2. User can create a Red-Flag or Intervention
3. User can Update his/her Red-Flag or Intervention
4. User can add Location to his/her Red-Flag or Intervention
5. User can add Image to his/her Red-Flag or Intervention
6. User can Delete his/her Red-Flag or Intervention
7. User can add Video to his/her Red-Flag or Intervention
8. User can Update the Location of his/her Red-Flag or Intervention
9. Admin can Update Status of Red-Flag or Intervention 

# Requirements
1. Working Computer with Windows, Mac, Linux OS and Python 3 Installed
2. Text Editor
3. Postman or Docker

# Installation
Clone the project from [GitHub](https://github.com/bashman1/iReporter_api.git)
navigate to the project folder
```
$ mkvirtualenv venv
$ pip install -r requirements.txt
$python run.py
```
## API endpoints

Prefix `/v1/api/` to the endpoints

| METHOD   | URL  | ACTION |
|---|---|---|
| POST | `/users` | user ragistration|
| POST | `/red-flags`| report a red-flag or intervation|
| GET  | `/red-flags` | retreave all red-flags and intervation|
| GET  | `/users` | retreave all users|
| GET  | `/red-flags/<int:red-flag_id>`| retreave a specific red-flag or intervation|
| PATCH | `/red-flags/<int:red-flag_id>/comment`| updating a specific red-flag or intervation comment|
| PATCH | `/red-flags/<int:red-flag_id>/location`| updating a specific red-flag or intervation location|
| DELETE | `/red-flags/<int:red-flag_id>`| deleting a specific red-flag or intervation|


## Build with
*Python 3
*Flask

## Tools
* vs code
* virtual envvironment
* Pylint
* Pytest

## Versioning
Version 1 of the API

## Author
Wamula Bashir Saidi
