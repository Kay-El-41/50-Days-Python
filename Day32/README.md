<h2>Day 32</h2>
<p>Today is October 28, 2022.</p>
<p>The coding time is 00:00.</p>
<hr/>

<p><b>Day 32: Password Validator</b></p>

<p>
Write a function called <b>password_validator</b>. The function asks the user to enter a password. A valid password should
have at least <b>one upper letter, one lower letter,</b> and <b>one number</b>. It should not be less than 8 characters long.
When the user enters a password, the function should check if the password is valid. If the password is valid, the function should
return the <b>valid password</b>. If the password is not valid, the function should tell the users the <b>errors</b> in the 
password and prompt the user to enter <b>another password</b>. The code should only stop once the user enters a valid password.
(use while loop).
</p>

<hr/>

<p><b>Extra Challenge: Valid Email</b></p>
<p> emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@mail.com']</p>

<p>Write a function called <b>email_validation</b> that takes a list of emails and checks if the emails are valid. The 
function returns a list of only valid emails. A valid emails address will have the following - <b>@ symbol</b> (if the @
sign is at the beginning of the name, the email is invalid. If there are more than one @signs, the email is invalid. All 
valid emails must have a <b>dot com at the end (.com)</b>, if not, the email is invalid. For example, the list of emails 
above should output the following as valid emails:
</p>
<p>['ben@mail.com', 'kenny@gmail.com']</p>
<p>If no emails in the list are valid, the function should return 'all emails are invalid'.</p>

<hr/>