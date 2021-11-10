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
| Log In         | Enter the correct user, password, <br> email address will direct  users to <br> their profile page  with name <br> displayed and a welcome <br> flash message    | Log in with correct username/ <br> password/email address    | Directs users to their profile <br> page with their name displayed <br> and a welcome message  | Pass       |
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
| Edit function                    | Only users who are logged in <br> can edit reviews | Log in as a regular user, <br> navigate to Review Books <br> click the Write A Review button <br> underneath the selected book, <br> scroll down to locate a previous <br> review, click the blue edit button <br>underneath the review, click<br>  submit | Flash message displays "Review  <br> Successfully Updated" | Pass
| Delete function |  Only users who are logged in <br> can delete their reviews | Log in as a regular user, <br> navigate to Review Books <br> click the Write A Review button <br> underneath the selected book, <br> scroll down to locate a previous <br> review, click the red delete button <br>underneath the review. <br> | Flash message displays "Review  <br> Successfully Deleted" | Pass         








 