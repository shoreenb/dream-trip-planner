<h1 align="center">
<a href="https://dream-trip-planner-project.herokuapp.com/" target="_blank"><img src="static/images/dtp-logo.png" alt="Dream Trip Planner Logo"/></a>
</h1>

# Testing for Dream Trip Planner

[Main README.md](README.md)

```
[Visit the Dream Trip Planner page](http://dream-trip-planner-project.herokuapp.com/)
```

## Table Of Contents

1. <a name="valid">Validation Services</a>
2. <a name="clientStories">Testing Client Stories</a>
3. <a name="manual">Manual Testing</a>

- <a name="desktop">Tests For Desktop</a>

- <a name="devices">Tests for Mobile Devices </a>

## [Validation Services](#valid)

The following validation services were used to check the validity of the website code.

- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML

- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS 

  ```
  <p>
      <a href="http://jigsaw.w3.org/css-validator/check/referer">
          <img style="border:0;width:88px;height:31px"
              src="http://jigsaw.w3.org/css-validator/images/vcss"
              alt="Valid CSS!" />
      </a>
  </p>
  <p>
  <a href="http://jigsaw.w3.org/css-validator/check/referer">
      <img style="border:0;width:88px;height:31px"
          src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
          alt="Valid CSS!" />
      </a>
  </p>
  ```

- [JSHint ](https://jshint.com/) was used to validate JavaScript

## [Testing Client Stories](#clientStories)

This section goes through each user story in the UX section of the README.md

As a new user of Dream Trip Planner, I want:

1. A collections of destinations organised in a way that I can easily choose the type of trip that I want to go on and  find information about the relevant destinations.
   - The 'Type of Trip' section organises the desitinations by type so that a user can easily filter the destinations they require
   
2. A collections of itineraries organised in a way that I can easily see them.

   - Using an accordion allows the itinerary details to be displayed in a compact way but the visitor can also easily access the full itinerary.
   - The search function also allows the user to quickly find the particular itinerary they are looking for

3. Clear navigation to easily maneuver through the site.

   - The navigation bar is clearly displayed at the top of every page and the logo and Title also navigate back to home.
   - Hovering over the navbar links highlights it so that the visitor can clearly see that it is a link.
4. To be able to create an new itinerary easily.
   - The 'Add Itinerary' from is a quick and easy link on the navigation bar and it contains concise field names and accompanying icons to allow the user to understand how to complete the form.
   - The form requires validation which alerts the user whether the field has successfully been completed or not.
   - The large 'Add Itinerary' button allows the user to understand that they will be adding the form to the list of itineraries.
5. To be able to my registration details in my account.
   - The account page displays all of the fields that the user completed in the registration form, along with the date the account was created.
   - A list of itineraries created by the user is also helpfully located in account with a link to the itineraries page should they wish to edit or remove that itinerary.
6. To contact or follow Dream Trip Planner on social media platforms.
   - All the social media platform links are located in the footer on every page.

     

As someone who has previously signed up with Dream Trip Planner I want:

1. The ability to go directly to my previously created Itineraries.
   - Once logged in, the user is directed to their account page where they can click on the itineraries that they have previously created, which links to the itineraries page where the full itinerary is located.
2. To be able to find information on a wide range of destinations.
   - The Cards in the 'Type of Trip' section filter the destinations in a way that will assist the user in deciding on what destination type they want information on. Once they click a type, they are taken to a page that has further information on each destination.
   - The 'Connect With Us' section also allow visitors to find Dream Trip Planner on various platforms if they want further information.
3. A resource that I can use to plan my everyday routine or the dream trip of a lifetime.
   - The Dream Trip Planner has the flexibility to plan any type of itinerary and a place that can always be referred back to so it won't get lost.
   - the password security gives peace of mind that any personal information is secure.
4. To be able to quickly search for a particular itinerary.
   - The search function located on the itineraries page allows the user to input their parameters to search for the itinerary they require.
5. To be able to edit or delete my itineraries.
   - Once logged in, the itineraries page becomes available, which displays an edit and remove button next to any itinerary created by the user.
6. The ability to connect with Dream Trip Planner to suggest destinations that could be added to the database.
   - The 'Connect With Us' section also allow visitors to find Dream Trip Planner on various platforms if they want to suggest a destination.

## [Manual Testing](#manual)

This section is a detailed account of all the manual testing that has been done to confirm all the areas of the site work as expected.

### [Tests For Desktop](#desktop)

The following steps were repeated using Chrome, Firefox and Internet Explorer and on screen sizes:

##### On all pages:

- Clicked on the logo to confirm it goes back to the home page.
- Confirmed that the navbar links are highlighted when hovered over.
- Checked that clicking on each navigation link leads to the correct page.
- Checked that the mouse changes to a pointer when hovering over the footer social links.
- Checked that each social icon opens in a new page when clicked.

##### Individual Pages:

**Home Pages**

- Opened the site in the selected browser to verify that the home page loads.
- Confirmed that the placement of the logo, title, text, buttons and footer are all correct.
- Checked that the cards have the correct formation for the screen size.
- Clicked each of the links to make sure they led to the correct page (login page for those not logged in).
- Checked that the correct home page card actions are displayed for registered users and unregistered users.

**Register**

- Checked that clicking the register button under the slider on the home page takes the user to the register page.
- Checked that clicking the log in prompt under the register form takes the user to the log in page.
- Checked that by clicking on the fields but not entering text makes the fields stay invalid.
- Checked completing some of the fields correctly does not allow the form to be submitted.
- Checked that if both password fields are not matching the fields are invalid.
- Checked that correctly completing the form directs the user to their new account page with a welcome flash message displaying their username and the fields are correctly populated with the information they just put into the register form.

**Login**

- Checked that clicking the log in button under the slider on the home page takes the user to the log in page

- Checked that if the user inputs an incorrect username, the page reloads and a flash message indicates that an incorrect username and/or password has been entered
- Checked that if the user inputs an incorrect password, the page reloads and a flash message indicates that an incorrect username and/or password has been entered
- Checked that correctly inputting the log in details takes the user to their account page

**Log Out**

- Checked that clicking the 'Log Out' button takes the user back to the 'Log In' page
- Checked that a flash message is displayed that tells the user that they have been logged out
- Checked that the navbar options have been reduced to Home, Log In and Register

**Once logged in:**

1. Account
   - Confirmed the flash message displays welcoming the user

   - Confirmed the user's profile title contains the username

   - Confirmed the details from the registration form are populated

     1.1 My Itineraries Accordion

     - Checked the titles of the itineraries created by the user are listed 
     - Checked that clicking on the accordion leads to the itineraries page

2. Add Itinerary

   - Checked that the icons and placeholders are displayed for each field.

   - Checked each of the select fields drop down and show the database collection when clicked, then hide the information when clicked again.

   - Checked that clicking an option populates the field and is validated.

     2.1	Checked that the field is invalid if the minimum required length of the 'Trip Name' field is not met.

     2.2	Checked that the datepicker appears when the date field is clicked.

     - Checked that the datepicker buttons can be clicked and the appropriate response 	happens.
     - Checked that the date field is invalid if a date is not selected.

     2.3	Checked that clicking on the country, city and Trip Type select fields stay invalid if an option is not chosen.

     - Checked each of the select fields drop down and show the database collection when clicked, then hide the information when clicked again.
     - Checked that clicking an option populates the field and is validated.

     2.4	Checked that the field is invalid if the minimum required length of the 'Activity Name' field is not met.

     2.5	Checked that the day number appears when the field is clicked.

     - Checked that if the day is not selected the field is invalid.

     2.6	Checked that the timepicker appears when the time field is clicked.

     - Checked that the timepicker buttons can be clicked and the appropriate response 	happens.
     - Checked that the time field is invalid if a time is not selected.

     2.7	Checked that the duration number appears in steps of 10 when the field is clicked.

     - Checked that if the duration is not selected the field is invalid.

     2.8	Checked that the field is invalid if the minimum required length of the 'Description' textarea is not met.

     2.9 Confirm that clicking 'Add Itinerary' button submits the itinerary and a flash message confirms that it has been successfully added.

3. Itineraries

   3.1	Check that search box filters the itineraries correctly.

   - Check that the 'Reset' button brings all the itineraries back.

   3.2 Accordion

   - Checked each of the titles drop down and show the information when clicked, then hide the information when clicked again.
   - Checked that the correct information is displayed.
   - Checked that the created by information matches the user.

4. Edit Itinerary

   - Checked that the correct information from the itinerary that was just clicked is in the fields.
   - Checked that the 'cancel' button returns to the main itineraries page.
   - Checked that amending the itinerary and clicking the 'Edit Itinerary' button returns a flash message that the itinerary as been successfully updated and the amended information has changed.

5. Remove Itinerary

   - Checked that clicking the 'Remove' button triggers a modal to confirm whether the user wants to delete the itinerary.
   - Confirm that clicking 'No' cancels the action.
   - Confirm that clicking 'YES' permanently removes the itinerary.

6. Manage Destinations

   - Checked that 'Manage Destinations' only appears in the navbar when 'admin' is logged in.
   - Checked that the Country name and City name populates the table from the database.
   - Checked that the edit and remove buttons are displayed for each row.
   - Checked that clicking edit button takes you to the 'Edit Destination' page.
     - Checked that the correct information from the destination that was just clicked is in the fields.
     - Checked that the 'cancel' button takes the user back to the 'Manage Destinations' page
     - Checked that amending the itinerary and clicking the 'Edit Destinations' button returns a flash message that the itinerary as been successfully updated and the amended information has changed.

7. Remove Destination

   - Checked that clicking the 'Remove' button triggers a modal to confirm whether the user wants to delete the destination.
   - Confirm that clicking 'No' cancels the action.
   - Confirm that clicking 'YES' permanently removes the destination.

### [Mobile Devices](#devices)

The following steps were repeated on physical devices available to the developer: Oppo X2 Lite, Motorola G8, Samsung and a tablet, as well as all the simulated devices and responsive options on the Chrome Developer Tools:

##### On all pages:

- Checked the size and placement of the navbar and footer logo on all device screen sizes
- Confirmed that font size is legible on all screen sizes, especially small and medium screens
- Checked that the navbar responsively collapses behind a button on small and medium screens
- Checked that the content at least fills the width of the screen with the footer at the bottom
- Checked that buttons and fields are large enough to click but still fit on the screen comfortably

##### Individual Pages:

1. Home Page
 - Checked that everything is displayed centrally and fits within the height of the screen.
 - Checked that the logo is central on the navbar for smaller screens
 - Checked that the register button under the slider disappears on smaller devices
2. Account
 - Checked that the accordion sits centrally within the card
 - Checked that the pagination text is visible and spaced well
3. Add Itinerary
 - Checked that the icons are visible and fields are displayed centrally
 - Checked that the Add Itinerary button is central
4. Itineraries
 - Checked that the accordion buttons and titles are visible
 - Some more work could be done to make the accordion more visually appealing on smaller screens
5. Manage Destinations
 - Checked that the title, text and image are central
 - Checked that the news article titles fit within the width of the page
 - Checked that the pagination buttons are stacked and do not overlap the article titles or footer
6. Connect With Us
 - Checked that the title, text and icons are central
 - Checked that the footer fits within the width of the page





