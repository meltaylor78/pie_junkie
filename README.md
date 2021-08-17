# **Pie Junkie - Raspberry Pi Store** 

<a href="https://pie-junkie.herokuapp.com"><img src="readme_assets/images/site_banner.jpg" target="_blank"
alt="site banner image" style="max-width:100%;"></img></a>

This project is an e-commerce site developed to for Raspberry Pi products developed for submission as my Milestone 4 project
as part of the Diploma in Software Development with the <a href="https://codeinstitute.net/" target="_blank">Code Institute</a>,
 the live version of the site deployed on Heroku is available <a href="https://pie-junkie.herokuapp.com" target="_blank">HERE</a>

## Index

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
## **<ins>Project_Motivation</ins>**
The project was motivated by the need to develope and e-commerece store to demenostrate my knowledge of Django
The Pie-Junkie 

## **<ins>UX</ins>**

### <ins>User_Stories</ins>

**Customer;**

As a customer I want to;
1. view Raspberry Pi products that I might be interested in buying
2. navigate the site with ease, view products by categories, search for items I am looking for.
3. view details of the products that I am interested in.
4. see review of products from other customers, leave my own review
5. add products to my cart as I browse the site and see a running total of the cost.
6. review the contents of my cart with ability to adjust quantities or remove items before I check out.
7. have a secure checkout, that ensures my credit card details are safe.
8. have the ability to create an account and save my details for return visits
9. confirmation of my order once places and details emailed to me as a record

**Site Owner;**

As the owner I want to;
1. provide a site that is inviting to customers, easy to use and intuitive to navigate
2. provide customers with a method to leave reviews on products and view reviews from other customers
2. allow customers to checkout without needing to register but include the option to to register and save details if they wish to.
3. add new products to the site
4. be able to edit or remove existing products as required
5. ensure the site is secure, limit actions based on login profiles (add / edit / delete products | write / edit / delete review)
6. provide a secure method for payment processing to protect customer payment details and site reputation


### <ins>Wireframes</ins>
During the planning stage of the project, wireframes were drawn up for each of the pages of the site.
The wireframes, (linked below) were used as guides during the development with some minor tweaks during the build process
to improve the site.

| Title | Link to Wireframe (pdf) |
| --- | --- |
| Wireframes | <a href="https://app.box.com/s/4rylun14revkk27psyoy68ejt7n5canp" target="_blank">Pie Junkie Wirerames</a>|


[Index](#Index)
- - - -

## **<ins>Features</ins>**
The site consists od 5 individual apps within the main Django framework. 
- Profile

    Contains the profile page that allows an autenticated customer to save their deliver details and 
    view a list of past orders

    <details><summary>Profile Page</summary>
        <img src="readme_assets/images/profile_page.jpg">
    </details>
    <br>

- Home

    Home app, conatins the main home (index.html) page with links to information and tutroials on Raspberry Pi
    
    <details><summary>Home Page</summary>
        <img src="readme_assets/images/home_page.jpg">
    </details>
    <br>

- Products

    The producs app contains all the producs, filter options (filter by product types, ) and sort options.
    The site consists of two html pages, 
        
    1. Products page, displays all products in the DB.
    Products are displayed in a bootstrap card with the number per row, varying depending on screen size. The image for  each product is a link to open the details for the selected product.

    <details><summary>Products Page</summary>
        <img src="readme_assets/images/product_page.jpg">
    </details>
    <br>

    2. Detail page, that provides all products details to the customer. 

    The details page also provides the interface to select the quantity and add the product to the cart.

    <details><summary>Details Page</summary>
        <img src="readme_assets/images/product_details_page.jpg">
    </details>
    <br>

    Two additional elements in the product model, Ram & Power are selectable from the details page. When a product has either or both options set in the DB additional options are included on the page. Allowing the customer to select the option; Ram - Options > 2Gb / 4Gb / 8Gb Power - Options > Ire_Up / EU / Europe

    3. User Reviews
    Integrated into the products details page, is a customer review section. This section of the page displays any reviews in the DB for the current product. If the user is logged in they have the option to write a review, other wise they are invited to login to create a review.

    <details><summary>Customer Reviews</summary>
        <img src="readme_assets/images/customer_reviews.jpg">
    </details>
    <br>
    
    3.1. Write a Review The write a review form is integrated into the details form and open using jQuery when the customer wants to write a review. In the review model, it records the user that submits the review and the product it is written for.

    <details><summary> Reviews</summary>
        <img src="readme_assets/images/customer_reviews.jpg">
    </details>
    <br>


    3.2. Edit / Delete a review Customers that wrote a review can see two options within their review. Only reviews submitted by the current users have the delete & edit options shown. additionally the views file has a login required check to prevent others circumventing the hidden options.
    Review Options Reviews

    <details><summary> Review Options</summary>
        <img src="readme_assets/images/edit_delete_review.jpg">
    </details>
    <br>

    Delete The delete link will delete the review from the DB and reload the page on the same product.

    Edit The edit option will open a new page with the review form refilled with the review data, which the customer can edit and resubmit to the DB.
    Edit Reviews

    <details><summary>Review Options</summary>
        <img src="readme_assets/images/edit_review.jpg">
    </details>
    <br>

- Cart

    <details><summary>Cart Page</summary>
        <img src="readme_assets/images/cart_page.jpg">
    </details>

- Checkout

    <details><summary>Checkout Page</summary>
        <img src="readme_assets/images/checkout_page.jpg">
    </details>

    <details><summary>Checkout Success Page</summary>
        <img src="readme_assets/images/checkout_success_page.jpg">
    </details>


### <ins>Existing_Features</ins>
The following featuures have been implemented in the current deployment of the e-commerce site.
Features described in the user stories have been priortised for the inital deployment
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

**Amazon Web Services** https://aws.amazon.com
- Used to host static files and media images for the site

**Google Fonts** https://fonts.google.com/
- Google fonts provided fonts for the project (Roboto Condensed & Serrat)

**Bootstrap** https://getbootstrap.com/
- CSS Framework

**Font Awesome** https://fontawesome.com/
- Icons used through the web site are sourced from Font Awesome

**Django** https://www.djangoproject.com/
- Open source web framework.

**Python3** https://www.python.org/
- Backend programming language, use in Django

**jQuery** https://jquery.com/
- jQuery Javascript for additional functionality on the site

**SQLite** https://www.sqlite.org/index.html
- SQLite DB (integrated in Django) use as the DB in development environment

**PostgreSQL** https://www.postgresql.org/
- PostgreSQL DB (integrated in Heroku) use as the DB in production environment

**Stripe** https://stripe.com
- For payment processing

**Stripe** https://stripe.com
- For payment processing

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


[Index](#Index)
- - - -
