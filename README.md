
load all from req.txt > pip3 install -r requirements.txt
> python3.8 -m pip install --upgrade pip
___________________________________________________________________________________________________________________________
                Notes to add to ReadMe.
___________________________________________________________________________________________________________________________
Features : Issues and fixes. 

As partt of the products page, I want to diaplay the category or its a search result as the page header. 
An issue arose, when selecting All Rasperberry Pi or all All kits, it displated each category in sequecny. 
To resolve the issue, I updated the main nav page to pass in "All xxx" as the first category, this is not a valid DB value, 
so in the views I extract the first item from the array if the array is more that one and secure it as varilable to be used in the template. 

Some products have special options:
  Ram - So Pi's have the option of 2 / 4 / 8 Gb of ram
  Power - Pi's, Kits or accessories with power supplies have the option for Ire/UK / EU / US plug types. 
Addtional coding was required in, the areas of prodduct views, cart view including the add to cart, update qty in 
the car or delete from the cart as all these options had to account for the fact that there were 4 possible options
    1. No Power Option or Ram Option
    2. Both Power Option and Ram Option
    3. Ram Option but no Power Option
    4. Power Option but no Ram option.

___________________________________________________________________________________________________________________________
                ReadMe Starts here
___________________________________________________________________________________________________________________________

# **Pie Junkie - Raspberry Pi Store ** 
<img src="/workspace/pie_junkie/readme_assets/images/site_banner.jpg">
readme_assets/site_banner.jpg
/workspace/pie_junkie/readme_assets/images/site_banner.jpg

- - - -

## Project Live Link : 
The project is deployed and live on Heroku

- - - -
## Index

- [Introduction](#Introduction)
- [Project Motivation](#Project_Motivation)
- [UX](#UX) 
    - [User Stories](#User_Stories)
    - [Wireframes](#Wireframes)
- [Features](#Features)
    - [Existing Features](#Existing_Features)
    - [Future Enhancements](#Future_Enhancements)
- [Technologies Used](#Technologies_Used)
- [Testing](#Testing)
    - [UX Testing](#UX_Testing)
    - [Functional Testing](#Functional_Testing)
    - [User Testing](#User_Testing)
    - [Code Validation](#Code_Validation)
- [Deployment](#Deployment)
    - [Live Deployment](#Live_Deployment)
    - [Local Deployment](#Local_Deployment)
- [Database](#Database) 
- [Credits](#Credits)
    - [Content](#Content)
    - [Media](#Media)
    - [Acknowledgements](#Acknowledgements)

- - - -
## **<ins>Introduction</ins>**


## **<ins>Project_Motivation</ins>**


## **<ins>UX</ins>**

### <ins>User_Stories</ins>



### <ins>Wireframes</ins>
Linked below, wireframes for the individual pages of the site.

| Title | Link to Wireframe (pdf) |
| --- | --- |
| Wireframes |  |

[Index](#Index)
- - - -

## **<ins>Features</ins>**

### <ins>Existing_Features</ins>

**User;**

**Admin**


### <ins>Future_Enhancements</ins>

In addition to the existing features, some future planned features included.

**User;**


**Admin**


[Index](#Index)
- - - -
## <ins>Technologies_Used</ins>
**Balsamiq**  https://balsamiq.com/wireframes/
- Basamiq was used in the design phase to create wireframes of the proposed web site.

**Github** https://github.com/
- Github is the repository used for version control & storage of the project.
- Github pages was used for the deployment of the site.

**Gitpod** https://www.gitpod.io/
- Gitpod was the IDE used for the development throughout the project.

**Heroku** https://id.heroku.com/login
- Heroku cloud used for hosting the live application

**MongoDB** https://www.mongodb.com
- MongoDB was used as the backend DB for the project

**Google Fonts** https://fonts.google.com/
- Google fonts provided fonts for the project (Roboto Condensed & Serrat)

**Materializec** https://materializecss.com/about.html
- CSS Framework

**Font Awesome** https://fontawesome.com/
- Icons used through the web site are sourced from Font Awesome

**W3C Validation Service** https://validator.w3.org/
- HTML & CSS code was checked on W3C validator at the end of the project.

**HTML Formatter** https://webformatter.com/html
- HTML code was run through HTML formatter to fix any indentation issues.

**JSHint** https://jshint.com/
- JavaScript code validate through JSHint

**ami.responsivedesign** http://ami.responsivedesign.is/#
- The project was tested on ami.responsivedesign
- image used in readme file was taken from ami.responsivedesign site

**w3schools** https://www.w3schools.com
- For additional code explanations & features to use.

[Index](#Index)
- - - -
## <ins>Testing</ins>

### <ins>UX_Testing</ins>
As part of the UX testing all pages were tested for the following criteria;

| Page | Desktop | Tablet | Mobile | Issues |
| --- | --- | --- | --- | --- |


[Index](#Index)
### <ins>Functional_Testing</ins>

[Index](#Index)

## **<ins>User_Testing</ins>**


### <ins>Code_Validation</ins>

|Code| Testing| Tool| Link|
| --- | --- | --- | --- |


[Index](#Index)
- - - -

## <ins>Deployment</ins>

### <ins>Live_Deployment</ins>

### <ins>Local_Deployment</ins>

[Index](#Index)
- - - -
## **<ins>Database</ins>**



[Index](#Index)
- - - -

### <ins>Acknowledgements</ins>
| Name | Area | Description |
| --- | --- | --- |
| Rahul Lakhanpal | Project Mentor | For all the guidance and input on UK and guiding me through the project with advise and direction. |
| Caroline Taylor | Testing | For help with User Testing and feedback |
|MongoDB | DB Hosting | For providing a free backend DB for the application|
|Heroku | Live Site Hosting |For providing a free cloud environment to host the application|

[Index](#Index)
- - - -
