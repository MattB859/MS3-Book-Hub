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
| Log In         | Enter the correct user,<br>  password, email address<br>  will direct users to their<br> profile page with <br> name displayed and <br> a welcome flash<br> message    | Log in with correct <br> username/password/ <br> email address | Directs users to their<br> profile  page with their <br> name displayed and a <br> welcome message  | Pass       |
|                | Incorrect username/password/ <br> email address | Error showing "incorrect <br> username/password" | Flash message <br> displaying error | Pass|



## Registration

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Register   | Username and Password must <br> have a minimum length <br> of 5 characters | Attempt to enter username <br> and password with less than 5 <br> characters | error displays "please match the <br> requested formate" | Pass |
|          | Username and Password must <br> have a maximum length <br> of 15 characters | Attempt to enter username <br> and password with more than 15 <br> characters | Form restrcits the user from <br> using more than 15 characters | Pass |
|          | Users can not register <br> with an existing username | Attempt to register with <br> an existing username | error flash message <br> "Username already exists" | Pass |


## Add Review Page 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Write a <br> new review | New reviews are saved  to the <br> selected books page | Fill in the form  and  click <br> submit | Flash message "Review <br>Successfully Added" informs <br> user the review was successful. <br> New reviews are added to the <br>  bottom of the books page | Pass |                        

## Edit/Delete Review Page 

| <p align="center">Feature</p>    | <p align="center">Expected</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------  | -----------------------------     | -------------------------------    | ------------------------------ | :--------: |
| Edit function                    | Only users who are <br> logged in can edit <br> reviews | Log in as a regular user, <br> navigate to Review Books <br> click the Write A Review <br> button underneath the <br> selected book, scroll down <br> to locate a  previous review, <br> click the blue  edit button <br> underneath  the review,<br> click submit | Flash message displays <br> "Review Successfully <br> Updated" | Pass
| Delete function |  Only users who are <br> logged in can delete <br> their reviews | Log in as a regular user, <br> navigate to Review Books <br> click the Write A Review button <br> underneath the selected book, <br> scroll down to locate a previous <br> review, click the red delete button <br>underneath the review. <br> | Flash message displays <br> "Review Successfully <br> Deleted" | Pass         



## Testing User Stories from User Experience (UX)

| <p align="center">User Stories</p>    | <p align="center">Experience</p>    | <p align="center">Testing </p>     | <p align="center">Results</p>  | Pass/Fail  |
| -------------------------------       | -----------------------------       | -------------------------------    | ------------------------------ | :--------: |
|  First Time <br> Visitor | "I want to understand <br> the main purpose of the site" | On entering the site <br> users are greeted with <br> images of book covers <br> and some informative text | "Join the UK's No.1 Hub <br> & START REVIEWING <br> TOP SELLING BOOKS" | Pass |
|          | "As a First Time Visitor, <br> I want to easily navigate <br> throught the site <br> to find books" | On entering the site <br> visitors can scroll down <br> to find featured books <br> with links to buy| Books can be found <br> at the bottom of <br> the home page | Pass |
















-   ### Validator Testing    

    - The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   ### HTML5 

    -  [W3C Markup Validator](https://validator.w3.org/#validate_by_input+with_options)

-   ### CSS3

    -  [W3C CSS Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

        
    -   ###  All pages came back with no errors.

## Testing User Stories from User Experience (UX) Section






 