# Stargazing Companion App

### Presentation Resources:
Presentation: https://docs.google.com/presentation/d/1C0J2M6T_B_fquxnGgjRV6K_arbpyLvmv8f2Z-C-wYa0/edit?usp=sharing
Trello: https://trello.com/b/UfMXjN8h/constellations
Website: 35.214.26.193:8001
Jenkins: (update on the day):8080
Development Site: (update on the day):5000

## Contents

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
![ERD][erd1]
![ci][ci]

## Project Tracking
Trello was used to track the progress of the project.
![trello][trello]

## Risk Assessment
The risk assessment for this project can be found in full here: https://docs.google.com/spreadsheets/d/1WfKQAjsBfErpQOywRmnZbCe6zw7yFxESFB8WhQd69Es/edit?usp=sharing

Here's a quick screenshot:
![RiskAssessment][riskassessment]

## Testing
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
[pytestconstole]: https://i.imgur.com/qaa3uzp.png
[trello]: https://i.imgur.com/etDOlwa.png
