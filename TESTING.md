# Testing

## Navigation 


| <p align="center">Feature</p>    | <p align="center">Expected</p> | <p align="center">Testing </p> | <p align="center">Results </p> | Pass/Fail  |
| -------------------------------- | -----------------------------  | ------------------------       | ---------------------------    | :--------: |
| Nav links     | Clicking home will redirect <br>  users to the home page  | Click Home   | navigates to home page   | Pass          
|               | Clicking review books takes <br> users to the book review page   | Click Review books     | navigates to the book review page   | Pass   |
|               | Clicking Profile takes users <br> to their profile page   | Click Profile   | navigates to the  priofile page    | Pass       |
|               | Clicking Log Out <br> logs out the user     | Click Log Out   | User is logged out and taken <br> back to the log in page    | Pass
| Social Media <br> Links   | Redirect to Facebook <br> in a new tap    | Click Facebook Icon  | Facebook page opens in new tap | Pass       |
|               | Redirects to Twitter <br> in new tap   | Click Twitter  Icon   | Twitter page opens <br> in new tap  | Pass       |
|                 | Redirects to Instagram <br> in new tap     | Click Instagram Icon  | Instagram page opens <br> in new tab     | Pass     |


## Buttons 

| <p align="center">Feature</p>  | <p align="center">Expected</p> | <p align="center">Testing</p>    | <p align="center">Results </p>  | Pass/Fail  |
| ------------------------------ | -----------------------------  | -------------------------------- | ------------------------------  | :--------: |
| Buy Now       | Clicking Buy Now button will <br> direct users to Amazon.co.uk  | Click Buy Now   | navigates to the Amazon website   | Pass       |
| Write A Review| Clicking the Write A Review <br> button will direct users to <br> the books add review page   | Click Write A Review   | navigates users to the <br> books add review page  | Pass    |
| Scroll Up     | Click the scroll up button <br> to redirect users back <br> to the top of the page    | Click Scroll Up | Takes users back to <br> the top of the page     | Pass       |


## Log In 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| ------------------------------   | -----------------------------     | ------------------------------     | ----------------------------   | :--------: |
| Log In         | Enter the correct user, password, <br> email address will direct users <br> to their profile page with name  <br> displayed and a welcome flash <br> message    | Log in with correct <br> username/password/ <br> email address | Directs users to their profile page <br> with their name displayed and <br> a welcome message  | Pass       |
|                | Incorrect username/password/ <br> email address | Error showing "incorrect <br> username/password" | Flash message <br> displaying error | Pass|



## Registration

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Register   | Username and Password must <br> have a minimum length <br> of 5 characters | Attempt to enter username <br> and password with less than <br> 5 characters | error displays "please match the <br> requested formate" | Pass |
|          | Username and Password must <br> have a maximum length <br> of 15 characters | Attempt to enter username <br> and password with more <br> than 15 characters | Form restrcits the user from <br> using more than 15 characters | Pass |
|          | Users can not register <br> with an existing username | Attempt to register with <br> an existing username | error flash message <br> "Username already exists" | Pass |


## Add Review Page 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Write a <br> new review | New reviews are saved  to the <br> selected books page | Fill in the form  and  click <br> submit | Flash message "Review <br>Successfully Added" informs user <br> the review was successful. <br> New reviews are added to the <br>  bottom of the books page | Pass |                        

## Edit/Delete Review Page 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Edit function                    | Only users who are <br> logged in can edit <br> reviews | Log in as a regular user, <br> navigate to Review Books <br> click the Write A Review <br> button underneath the <br> selected book, scroll <br> down  to locate a  previous <br> review, click the blue  edit <br> button underneath  the review,<br> click submit | Flash message displays <br> "Review Successfully <br> Updated" | Pass
| Delete function |  Only users who are <br> logged in can delete <br> their reviews | Log in as a regular user, <br> navigate to Review Books <br> click the Write A Review button <br> underneath the selected book, <br> scroll down to locate a previous <br> review, click the red delete<br> button underneath the review. <br> | Flash message displays "Review <br> Successfully Deleted" | Pass         



## Testing User Stories from User Experience (UX)

| <p align="center">User Stories</p>    | <p align="center">Expectation</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------       | -----------------------------       | -------------------------------    | ------------------------------ | :--------: |
|  First Time <br> User | "I want to understand <br> the main purpose of the site" | On entering the site <br> users are greeted with <br> book cover images <br> and some informative text | "Join the UK's No.1 Hub <br> & START REVIEWING <br> TOP SELLING BOOKS" | Pass |
|          | "I want to easily navigate <br> through out the site <br> to find books" | On entering the site <br> users can scroll down <br> to find books. | Books can be found <br> at the bottom of <br> the home page | Pass |
|          | "I want the site to be <br> responsive on all devices"| Navigate to site on laptop, <br> tablet and mobile, move <br> around the site to test for <br> responsiveness | Site responsive on all <br> devices | Pass |
|          | "I want to be recommended  <br> books to buy using the <br> links provided" | On entering the site <br> users can scroll down <br> to find top recommended <br> books. | Visitors will find <br> "This Weeks Top Picks" <br> underneath each book <br> is a 'BUY NOW' link to <br>  Amazon.co.uk| Pass |
|  As a <br> Returning <br> User | "I want to register my <br> details to  create an <br> account" | Click Register, fill in a <br> username, email-address, <br> password, click register. | Registration successful | Pass |
|        | "I want to log in  <br> and read reviews" | Navigate to review books <br> page, click on the book <br> you wish to see the  review <br> for, scroll down to find all reviews | All the latest reviews <br> for the chosen book <br> can be found below <br> | Pass|
|         | "I want to see a good <br> selection of books <br> available to review" | Users can find all the <br> available books to review <br> by navigate to Review books page | users have a variety <br> of different books to review | Pass |
| As a Frequent <br> User | "I want to add new <br> reviews" | Navigate to review books, <br> click the 'Write a Review' button,  fill in the <br> 'Create Review' form <br> and press submit | A Flash message will <br> displays to the user <br> "Review <br>Successfully  Added" | Pass | 
|       | "I want to be informed <br> when  new books are <br> becoming available to review. | Navigate to review books | users can find a <br> message which  says <br>'coming soon to review' | Pass
|          | "I want to see reviews I <br> have written saved to my profile page" | On logging into the site <br> users are taken to their <br> profile page <br> where they can find <br> all of their reviews | At the top of each <br> review box user names<br> can be seen | Pass |
|          | "I want my reviews to <br> be safe and secure" | Jinja if statements were <br>used  to hide the edit and <br> delete buttons on reviews <br> not made by the user. |users are restricted  <br> from editing and deleting <br> other users reviews | Pass |
|         | "I want to have the option <br> of deleting my reviews" | Navigate to the profile <br> page find a review press delete | Flash message will display <br> "Review Successfully <br> Deleted" | Pass |
|         | "I want to have the option <br> of editing my reviews"  | Navigate to the profile <br> page find a review press <br>the edit button, once the <br> review  has been edited <br> press update | Flash message will display <br> "Review Successfully <br> Updated" | Pass |
|          | "I want the option to <br> delete  my account where necessary" |  Navigate to the <br> account setting page | Click on the 'delete account' button <br> then press delete.  | Pass |
|         | "I want to see the <br> dates on all my reviews" | Navigate to users profile | The date can be seen <br> at the top of each review | Pass |

## Validator

## HTML Validator

HTML validated on [https://validator.w3.org/](https://validator.w3.org/)

- The W3C Markup Validator was used to validate all HTML pages to ensure there were no major errors in the project.

-   ### [HTML](/static/images/jigsaw.w3.org.png) 

-  ### Add Review Page
-  ### Log In Page
-  ### Register Page
-  ### Home Page
-  ### Profile Page
-  ### the power of now Page
-  ### the secret Page
-  ### Edit Power Page
-  ### Edit Secret Page
-  ### Delete User Page
 
 
## CSS Jigsaw

CSS3 Validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

-   ### [CSS](/static/images/jigsaw.w3.org.png) 

## PEP8

Python was checked to PEP8 compliance and passed with no errors [http://pep8online.com/](http://pep8online.com/)
-   ### [PEP8](/static/images/PEP8.png) 
   
## JSHint

JSHint was used to validate JavaScript with no major issues. [https://jshint.com/](https://jshint.com/)
 

## Debugging

-   ### Chrome Developer Tools

    -  Chrome Dev Tools was used for inspection of HTML, and CSS. It helped to diagnose problems, and debug issues right in the browers.

-   ### Further Testing

    -   All pages on the site were tested to be fully responsive on all devices

    -   The Website was tested on Google Chrome, Firefox, Microsoft Edge and Safari browsers.

    -   The website was viewed on a variety of devices such as 
        - Desktop 
        - Laptop 
        - Motorola G4 
        - Galaxy S5/7
        - Pixel 2
        - Pixel 2 XL 
        - iPhone 5/SE 
        - iPhone 6/7/8/Plus 
        - iPhone X, 
        - ipad/Pro.

    -   A large amount of testing was done to ensure that all pages were linking correctly.

    -   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

-   ### Bugs Found and not fixed

    -   On some mobile devices the top page is cut off.

    -   A modal message was used to confirm the deletion of a review a bug has caused random unorderly reviews to be deleted that were not indented. The feature has now been removed to prevent users from deleting the wrong review.


  