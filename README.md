# Help Eli Escape
Help Eli Escape is a text based adventure game also know as interactive fiction (IF). It runs on a terminal. The player uses text input to control the game, and the game state is relayed to the player via text output. The story is based on Eli who just robbed a bank and is trying to escape from the police. The goal of the player is to try and navigate Eli through various paths that will eventually lead Eli to freedom.  

## UX

### Terminal based game.
This is a text based adventure game that runs on a terminal. It does not have any graphical user interface. Ontop of terminal is a "RUN PROGRAM" button that restarts the game. The name of the game "Help Eli Escape" is clearly written on the top left corner of the terminal surrounded by a border.

![Help Eli Escape Image](documentation/eli-screenshot.png)

### Wireframes

Below is a sketch of the decision tree I created to help with plotting the paths and choices of the story I went with for the game. Also below are images of the entire story line used in the game.

![Decision Tree Wireframe Image](documentation/eli_decision_tree.jpg)
![Story1 Wireframe Image](documentation/story1.png)
![Story2 Wireframe Image](documentation/story2.png)
![Story3 Wireframe Image](documentation/story3.png)


## Features 

### Existing Features

- __Run Program Button__

  - It is a large and bold button  with the words Run Program written on it.  

![Run Program Button](documentation/run-program-button.png)

- __The Terminal__

  - The name of the game "Help Eli Escape" is clearly written on the top left corner of the terminal surrounded by a border.
 
![Terminal Image](documentation/terminal-image.png)

## Technologies Used

- I used Python programing language to write the code used in making the app.
- I used Gitpod as my code editors.
- I used Github to host my repositories.
- I used Git for version control of the app.
- I used Heroku to deploy the live version of the app.

## Testing 

- I confirmed that the run program button was functional.
- I checked that all input methods did not allow wrong user inputs.
- I checked that the clear function was working properly.
- I checked that at the end of each paths, the player could choose to restart the game or end it. 

### Validator Testing 

- Python
  - No errors were found when passing through the [PEP8 online](http://pep8online.com/checkresult)

## Deployment
The site was deployed using Heroku. The steps to deploy are as follows:
  * Set up an account on Heroku.
  * From the Heroku dashboard click the “Create new app” button and then name the app.
  * Select your region and then click "Create app".
  * Click on the settings tab and go to the Config vars section.
  * Click on the "Reveal Config Vars" button.
  * In the field for Key type PORT and in the field for Value type 8000 then click on the Add button.
  * Next go to the Buildpacks section and click on "Add buildpack", select Python and click "Save changes".
  * Click on the "Add buildpack" button again and this time select node.js and click "Save changes".
  * Next click on the Deploy tab and go to the Deployment method section, select Github and click on "Connect to Github".
  * Now search for the Github repository which is named help-eli-escape and then click on "Connect".
  * Next click on "Enable Automatic Deploys".
  * Click on the activity tab and wait for the status to say Build Succeeded and then click on the "Open App" button.

The live link can be found here - https://help-eli-escape.herokuapp.com/

### Local Deployment

To make a local copy of this project, you can clone it by typing the following in your IDE terminal:

- `git clone https://github.com/onabz/Vehicle-Quiz-Game.git`

Alternatively, if using Gitpod, you can click the green Gitpod button, or use [this link](https://gitpod.io/#https://github.com/onabz/Vehicle-Quiz-Game)

## Credits 
 
### Content 

- Many of the Javascript functions used in making the quiz functional were from [Build A Quiz App With JavaScript](https://www.youtube.com/watch?v=riDzcEQbX6k)
- Steps on how to style the user score text were from [Create a Quiz App using HTML CSS & JavaScript | Quiz Web App using JavaScript](https://www.youtube.com/watch?v=CqddbIrEM5I&t=933s)
- The line of code I used to create the restart button was from [Reload Page - HTML - Javascript lesson 4](https://www.youtube.com/watch?v=SQFwFjMUgUc)
- Explanations on how to go about calculating the user scores and displaying them were from my Menthor Tim Nelson. 
- The font used throughout the site called Roboto Condensed was from Google fonts [Google Fonts](https://fonts.google.com/specimen/Roboto+Condensed?preview.text=muscle%20gains%20power%20lifitng&preview.text_type=custom&query=roboto+#standard-styles)
- All the questions used in the quiz game were generated from  [Open Trivia Database](https://opentdb.com/api_config.php)

### Acknowledgements

- I would like to thank my Mentor Tim Nelson for his invaluable support all through this project. I would not have been able to put all this together if not for his patience and insight.
- I would like to thank [Student Care](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentecommerce/studentcare) for their regular check up on me to ensure that I was always on track to completing this project and to reassure me that they were always available if I needed any help.









![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome onabz,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!