# FatBoysPizza

FatBoysPizza is a restaurant booking web app for a fictional pizza restaurant based in Chelmsford, Essex. The app allows restaurant staff and customers to easily manage restaurant bookings. The customer can register, login and create a booking for a date and time that suits them. They can then edit this booking or cancel the booking via the web app. The live link can be found here: <link>

Insert mockup when complete

## Table of contents
- [FatBoysPizza](#fatboysPizza)
    - [Table of contents](#table-of-contents)
- [Site goals](#site-goals)
- [Planning](#planning)
    - [Agile](#agile)
        - [User stories](#user-stories)
    - [Wireframes](#wireframes)
- [Features](#features)
    - [Features left to implement](#features-left-to-implement)
- [Database design](#database-design)
- [Security](#security)
- [Technologies](#technologies)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Version control](#version-control)
    - [Heroku deployment](#heroku-deployment)
    - [Run locally](#run-locally)
- [Credits](#credits)

# Site goals

The website aims to help the restaurant to take bookings online and allow staff to easily keep track of upcoming bookings and make changes to bookings when neccessary.

The website also aims to help customers to easily view the restaurant's menu and book a table online. They will also be able to edit the booking and cancel the booking via the website.

 # Planning
 ## Agile

To develop this project I used an Agile approach, dividing the work into phases and building the website iteratively to maximise efficiency. I used a kanban board with tickets containing different user stories with prioritised labels that included 'Must have', 'Should have' and 'Could have'. Each ticket defined the user story and the acceptance criteria.

![Kanban](docs/readme-images/kanban.png)

## User Stories

**Base set up**

As a developer, I need to create the base.html page and structure so that other pages can reuse the layout

As a developer, I need to create the header.html and footer.html pages so that other pages can resume the layout

As a developer, I need to create folders and files for images, css and javascript

As a developer, I need to include the social links in the footer.html so it appears on every page

As a developer, I need to create the nav bar so users can easily navigate the website

**Authentication app**

As a developer, I need to set up allauth so that users can easily register and login to the website

As a developer, I need to style the allauth pages to have the same styling as the rest of the website

**Menu**

As a user, I would like to be able to view the menu, so that I can see what types of pizza are available.

**Booking**

As a user, I wan to be able to select a date, time and number of guests so that I can book a table at the restaurant.

As a user, I want to view my existing bookings, so I can keep track of my reservations.

As a user, I want to edit my booking, so that I can change the details if needed.

As a user, I want to cancel my booking, so I can let the restaurant know I no longer need the table.

**Documentation**

As a developer, I need to create a reade.md file, so that other developers can easily understand my website

As a developer, I need to create a testing.md file, so that I can show the tests I completed for the website

## Wireframes

- Home page

![Home page](docs/wireframes/FatBoysPizza%20-%20Home.png)

- Menu

![Menu](docs/wireframes/FatBoysPizza%20-%20Menu.png)

- Register

![Register](docs/wireframes/FatBoysPizza%20-%20Register.png)

- Log in

![Log in](docs/wireframes/FatBoysPizza%20-%20Log%20in.png)

- Add booking

![Add booking](docs/wireframes/FatBoysPizza%20-%20Add%20Booking.png)

- Your bookings

![Your bookings](docs/wireframes/FatBoysPizza%20-%20Your%20Bookings.png)

- Edit booking

![Edit booking](docs/wireframes/FatBoysPizza%20-%20Edit%20Booking.png)

- Delete booking

![Delete booking](docs/wireframes/FatBoysPizza%20-%20Delete%20Booking.png)

- Sign out

![Sign out](docs/wireframes/FatBoysPizza%20-%20Sign%20out.png)

- 403 error

![403 error](docs/wireframes/FatBoysPizza%20-%20403%20Error.png)

- 404 error

![404 error](docs/wireframes/FatBoysPizza%20-%20404%20Error.png)

- 500 error

![500 error](docs/wireframes/FatBoysPizza%20-%20500%20Error.png)

# Features

**Navigation bar**

The navigation bar is visible on all pages and includes links to Home, Bookings, Menu, Register, Log in and Log out when a user is logged in. The navigation converts to a hamburger menu on smaller devices so the user can view and navigate the site on all devices.

The following nav links appear on every screen:

- Home (routes to index.html) - visible to all users
- Bookings (drop down)
    - Manage bookings (routes to manage-bookings.html) - visible to all users
    - Add booking (routes to add-booking.html) - visible to all users
- Menu (routes to menu.html) - visible to all users
- Register (routes to signup.html) - visible to logged out users
- Log in (routes to login.html) - visible to logged out users
- Log out (routes to logout.html) - visible to logged in users

![Navbar](docs/readme-images/Navbar.png)

**Home page**

The home page hero section incldudes a welcome headline and some introductory content that immediately informs the user what the website is for.

There are buttons to 'Book a table' and 'View menu' so the user can easily achieve what they want to achieve whilst visiting the website.

There is a 'What makes us different?' section that explains why a user should visit the restaurant. Plus, there is a 'What our customers say' section that shows some of the reviews from the restaurant's customers.

At the bottom of the home page, there is an embeded Google map so users can easily find us. And there is an opening times section so users know when we're open.

![Home page header](docs/readme-images/home-header.png)

**Home page - what makes us different?**
![What makes us different](docs/readme-images/home-what-makes-us-different.png)

**Home page - what our customers say**
![What our customers say](docs/readme-images/home-what-our-customers-say.png)

**Home page - find us here and opening times**
![Find us and opening times](docs/readme-images/home-find-us-opening-times.png)

**Footer**

The footer includes links to the restaurant's social media pages so the user can easily follow us online. This includes links to LinkedIn, Instagram, X and YouTube.

![Footer](docs/readme-images/footer.png)

**Add booking**

The add booking page is designed so that users can easily book a table at the restaurant. They can select the customer, enter their name, add a phone number, select their table, choose a time, date and number of guests. They can then select the 'Add booking' button which will take them to the 

![Add booking](docs/readme-images/add-booking.png)

**Booking confirmed**

On the booking confirmed page, the user can see all the details of their booking and select the 'Manage Bookings' button to view their other bookings.

![Booking confirmed](docs/readme-images/booking-confirmed.png)

**Manage bookings**

The manage bookings page allows the user to view all their bookings with the restaurant. They can see the name, date, time, table and guests for each booking. On this page, they can edit the booking or delete the booking.

![Manage bookings](docs/readme-images/manage-bookings.png)

**Edit booking**

When the user selects 'Edit' on the manage bookings page, they will be taken to the edit booking page where they can amend the details of the bookings.

![Edit booking](docs/readme-images/edit-booking.png)

**Confirm booking deletion**

When a user selects 'Delete' on the manage bookings page, they will be taken to the confirm booking deletion page. Here they will see all the details of their booking and asked to confirm the booking deletion. The user can select 'Delete' or 'Cancel'.

![Confirm booking deletion](docs/readme-images/confirm-booking-deletion.png)

**Menu**

The Menu page displays all the items sold at the pizza restaurant. This is so the user can see what's on offer before the attend the restaurant. The menu lists the pizzas, includes details of the create your own pizza options, sides, drinks and desserts.

![Menu](docs/readme-images/menu.png)

**Favicon**

A favicon is used to help users find the website when they have a lot of tabs open.

![Favicon](docs/readme-images/Favicon.png)

**403 page**

A 403 page has been included to notify users when they have attempted to access a page they're not authorised to access. It will allow users to easily navigate their way back to the home page with a 'Home' button.

**404 page**

A 404 page has been included for when a user tries to navigate to a broken link. It will inform the users that the page they're trying to navigate to does not exist and provide them an easy way to return to the home page with a 'Home' button.

**500 page**

When an internal server error occurs, the user will see a 500 erro page. The user will easily be able to return to the home page via the 'Home' button.

## Features left to implement

- In a future release I would like to add functionality to the website that allows restaurant staff to add, edit a delete menus. This feature would allow staff to easily update the menu as and when menu items change.

# Database design

The database was designed to allow CRUD functionality to be used by registered customers when they are signed in to the website.

This allows the users to be able to create a booking, view a booking, update a booking and delete a booking.

The entity relationship diagram was created using DBVisualizer and shows the schemas for each of the models and how they are connected.

![Database model](docs/readme-images/Database%20model.png)

# Technologies

- HTML
    - The website structure was developed using HTML
- CSS
    - To style the website, I used custom css in external files
- Python
    - Python is the main programming language used for the web booking application using the Django Framework
- Visual Studio Code
    - The website was developed using the Visual Studio Code code editor
- GitHub
    - The source code is hosted on GitHub
- Git
    - Git was used to commit and push code during the development of the website
- Favicon.io
    - A favicon was used for the website tab
- Figma
    - Wireframes were created using Figma

# Testing

Test results can be found in the [TESTING.md](TESTING.md) file.

# Deployment

### Version control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository 'fat-boys-pizza'.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m "commit message"``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku deployment

Add instructions...

### Run locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.


# Credits 

### Code

- Daisy McGirr YouTube Tutorials (https://www.youtube.com/watch?v=cPfvhpdYaNY)
- CodeInstitute - 'Working with database management systems' module helped me to gain a good understanding of databases and how best to use them for this project.
- CodeInstitute - 'I Think Therefore I Blog' module helped me to understand the basics of setting up a full stack project.
- StackOverflow - Helped me to troubleshoot issues I was having throughout the project.
