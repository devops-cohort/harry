# Stargazing Companion App

### Resources:
* Presentation: https://docs.google.com/presentation/d/1C0J2M6T_B_fquxnGgjRV6K_arbpyLvmv8f2Z-C-wYa0/edit?usp=sharing
* Trello: https://trello.com/b/UfMXjN8h/constellations
* Website: 35.214.26.193:8001
* Jenkins: (update on the day):8080
* Development Site: (update on the day):5000

## Contents
* [Brief](##brief)

## Brief
The brief provided to us for this project sets the following out as its overall objective:
"To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training."

In other words, I have been tasked with creating an application that utilises create, read, update and delete functions in order to function, such that I can demonstrate that I've learnt something over the last few weeks.

### Additional Requirements
In addition to what has been set out in the brief, I am also required to include the following:
* A Trello board
* A relational database, consisting of at least two tables
* Clear documentation of the design phase, app architecture and risk assessment
* A python-based functional application that follows best practices and design principles
* Test suites for the application, which will include automated tests for validation of the application
* A front-end website, created using Flask
* Code integrated into a Version Control System which will be built through a CI server and deployed to a cloud-based virtual machine

### My Approach
To achieve this, I have decided to produce a simple stargazing companion app that must allow the user to do the following:
* Refer to a database of stars and corresponding constellations with coordinate data
* Add/delete records of stars and constellations in the database
* Record observations that they have made on a particular day/time at a particular location
The following is functionality I would like to implement into the application but are not necessary to satisfy the brief:
* Ability to call up every star that belongs to a certain constellation

### Scope
For the sake of simplicity, I will only be adding a limited number of constellations into the database by default. I'm aiming to add the 12 elliptical constellations, but I may not even achieve this as data-entry is a long and laborious task, and I'm being tasked to make a great app, not an exhaustive database. Same applies to the stars, of which there are much, much more in the night sky.

## Architecture
### Database Structure
Pictured below is an entity relationship diagram (ERD) showing the structure of the database. Everything in green has been implemented into the app, while everything in red has not.

![ERD][erd1]

As shown in the ERD, the app models a many-to-many relationship between User entities and Observation entities using an association table. This allows the user to create observation posts and tag multiple users in the database with one observation. Similarly, many observations can therefore be associated with a user.

### CI Pipeline
![ci][ci]

Pictured above is the continuous integration pipeline with the associated frameworks and services related to them. This pipeline allows for rapid and simple development-to-deployment by automating the integration process, i.e. I can produce code on my local machine and push it to GitHub, which will automatically push the new code to Jenkins via a webhook to be automatically installed on the cloud VM. From there, tests are automatically run and reports are produced. A testing environment for the app is also run in debugger mode, allowing for dynamic testing.

This process is handled by a Jenkins 'pipeline' job with distinct build stages. The design of this type of job means that if a previous build stage fails, the job will fail altogether and provide you with detailed information as to where this occurred. The more modular you make this system, the easier it is to pinpoint where your code is failing. As pictured below, the four build stages are:
* 'Checkout SCM' (pull code from Git respository)
* 'Build' (would be more accurately named 'Installation' as Python doesn't require building, in the strictest sense)
* 'Test' (run pytest, produce coverage report) 
* 'Run' (start the flask-app service on the local VM, belonging to systemctl)

![buildstages][buildstages]

Once the app is considered stable, it is then pushed to a separate VM for deployment. This service is run using the Python-based HTTP web server Gunicorn, which is designed around the concept of 'workers' who split the CPU resources of the VM equally. When users connect to the server, a worker is assigned to that connection with their dedicated resources. This system is beneficial .

## Project Tracking
Trello was used to track the progress of the project (pictured below). You can find the link to this board here: https://trello.com/b/UfMXjN8h/constellations

![trello][trello]

## Risk Assessment
The risk assessment for this project can be found in full here: https://docs.google.com/spreadsheets/d/1WfKQAjsBfErpQOywRmnZbCe6zw7yFxESFB8WhQd69Es/edit?usp=sharing

Here's a quick screenshot:

![RiskAssessment][riskassessment]

## Testing
pytest is used to run unit tests on the app. These are designed to assert that if a certain function is run, the output should be a known value. Jenkins produces 

![pytestconsole][pytestconsole]

![coverage][coverage]

## Deployment



## Front-End Design


## Future Improvements
* Implementation of other solar system objects that require realtime updates, e.g. planets whose locations in the sky are always changing

## Authors
Harry Volker

## Acknowledgements


[erd1]: https://i.imgur.com/p9wji5S.png
[ci]: https://i.imgur.com/2G7joFp.png
[riskassessment]: https://i.imgur.com/btY8HRY.png
[coverage]: https://i.imgur.com/WDaANiD.png
[pytestconsole]: https://i.imgur.com/qaa3uzp.png
[trello]: https://i.imgur.com/etDOlwa.png
[buildstages]: https://i.imgur.com/ba7ntAo.png
