# API development, API testing and API documentation

This repo includes coding exercises from the API Development and Documentation course at Udacity.

# Pre-requisites
* Install python3
* Install pip3
* Install pipenv

# How to run?
1. Clone this repo on your local environment
2. Navigate to the cloned repo, e.g.,
```
cd ~/dev/udacity.api.course/FirstFlaskApp/flaskr
```
3. Create a virtual environment and install dependencies
```
python3 -m venv venv
source venv/bin/activate 
pipenv shell
pipenv install
```
4. Start the flask app
    * Navigate to app folder, e.g.,
    ```
    cd ~/dev/udacity.api.course/FirstFlaskApp/
    ```
    * Run in debug mode
    ```
    flask run --debug
    ```
5. Verify app is running
    * Open a browser
    * Navigate to http://127.0.0.1:5000/smiley
    * You should see a smiley =)


## Tech Stack
* python
* flask
* pytest
