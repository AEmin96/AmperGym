<h1>AmperGym</h1>
<h2>Deployed Project: <a href="https://ampergym-7d2381aee37e.herokuapp.com/" target="_blank">AmperGym</a></h2>




<h2>1. Purpose of the Project</h2>
<p>The purpose of the AmperGym project is to provide an interactive and user-friendly gym website that offers users the ability to sign up, manage, and upgrade their subscriptions seamlessly. Integrating Stripe for secure payments, the site facilitates easy subscription selection and management, enhancing the overall user experience. The project aims to motivate users with accessible gym information, including location, opening times, and user testimonials, while also providing personalized user accounts for managing personal information and subscriptions.</p>

![Screenshot 2024-02-17 at 20 27 31](https://github.com/AEmin96/AmperGym/assets/126208272/769c4a03-8350-43ad-88f8-d4dfdc6d511b)



<h1>Entity & Relationship Diagram</h1>


![333 drawio](https://github.com/AEmin96/AmperGym/assets/126208272/129caf31-4fb8-42d2-983c-be572e94daba)

<em> ERD created using  <a href="https://app.diagrams.net/" target="_blank" class="text-black mr-3"> Draw.io </a> </p> </em>

<h1> Wireframes </h1>

<h2> Home Screen </h2>

![Website Sample (1)](https://github.com/AEmin96/AmperGym/assets/126208272/2e2782cc-b8b7-4e35-9c5f-a7c5bee2e664)

<h2> Location </h2>

![Website Sample (2)](https://github.com/AEmin96/AmperGym/assets/126208272/420713bc-8bd6-498f-b4a0-a5eb61ba1ffc)



<h2> Testimonials </h2>

![Website Sample (5)](https://github.com/AEmin96/AmperGym/assets/126208272/6b0f5126-1c7d-4bdf-9bde-fa25effa688a)


<h2> About Us </h2>

![Website Sample (7)](https://github.com/AEmin96/AmperGym/assets/126208272/4b1a7b9e-5333-42af-9871-3bd9bd75f5fe)

<h2> Subscriptions </h2>

![Website Sample (8)](https://github.com/AEmin96/AmperGym/assets/126208272/9aa9e579-0abf-4286-9345-f4114e00fccc)


<h2>2. User Stories</h2>
<em>As a Guest User (Non-Logged In):</em>
<ul>
<li>As a potential gym member, I want a clear and intuitive website design that allows me to easily navigate through different sections, so I can quickly find information about classes, facilities, and membership options without feeling overwhelmed.</li>
<li>As a user interested in joining the gym, I want a straightforward and hassle-free online signup process, allowing me to create an account, choose a suitable membership plan, and make a secure payment, so that I can become a member with minimal effort.</li>
<li>As a user exploring gym plans, I want detailed information on each membership option, including pricing, class access, and any additional perks, so that I can make an informed decision based on my fitness needs and budget.</li>
<li>As a user considering the gym, I want to read reviews and testimonials from other members to get insights into their experiences and gauge the overall satisfaction of the gym's community, helping me make a more confident decision about joining.</li>
</ul>

<em>As a Registered User (Logged In):</em>
<ul>
<li>As a current gym member, I want a user-friendly dashboard where I can log in, view my subscription details, and easily manage my account settings, such as updating personal information or changing my subscription plan, to ensure a seamless experience.</li>
<li>As a subscriber, I want to receive regular email notifications about upcoming classes, special events, and any changes to the gym schedule, so that I can stay informed and plan my workouts accordingly.</li>
<li>As a mobile user, I want the gym website to be responsive and mobile-friendly, allowing me to sign up, manage my account, and access important information easily from my smartphone, providing a convenient and on-the-go user experience.</li>
</ul>

<em>As an Admin:</em>
<ul>
<li>Access user subscriptions in the Django admin to edit or cancel them.</li>
</ul>

<h2>3. Features</h2>
<ul>
  <li><h3>User-friendly navigation and responsive design.</h3>
    <p>Screens:</p>
    <img width="2038" alt="Screenshot 2024-02-25 at 18 50 04" src="https://github.com/AEmin96/AmperGym/assets/126208272/7b194180-980c-46d1-8968-bcc0aa7f34ba">
    <p>Mobiles:</p>
    <img width="430" alt="Screenshot 2024-02-25 at 18 52 35" src="https://github.com/AEmin96/AmperGym/assets/126208272/e4313a0b-4f98-4296-84bd-4680b135a1e1">
  </li>
  
  <li><h3>Stripe integration for secure payment processing.</h3>
    <img width="2038" alt="Screenshot 2024-02-25 at 18 46 08" src="https://github.com/AEmin96/AmperGym/assets/126208272/ebcaf220-ff03-48be-8418-c2f60c8edc07">
  </li>
  
  <li><h3>Dynamic content for users based on login status.</h3>
    <p>Non-Logged In User:</p>
    <img width="2038" alt="Screenshot 2024-02-25 at 18 50 04" src="https://github.com/AEmin96/AmperGym/assets/126208272/7b194180-980c-46d1-8968-bcc0aa7f34ba">
    <p>Logged In User:</p>
    <img width="2038" alt="Screenshot 2024-02-25 at 18 49 56" src="https://github.com/AEmin96/AmperGym/assets/126208272/d6ebc3f5-7577-467c-8910-53cadf6fe834">
  </li>
  
  <li><h3>Google Maps API for gym location.</h3>
    <img width="2038" alt="Screenshot 2024-02-25 at 18 46 52" src="https://github.com/AEmin96/AmperGym/assets/126208272/68b9e64d-5cc3-4bc4-8de8-8305f5d21ccc">
  </li>
  
  <li><h3>Facebook Business Page.</h3>
    <img width="996" alt="Screenshot 2024-02-25 at 18 47 56" src="https://github.com/AEmin96/AmperGym/assets/126208272/dd26df60-40c0-4488-94c9-a783e80855a5">
  </li>
  
  <li><h3>Testimonial feature for public user feedback.</h3>
    <img width="2045" alt="Screenshot 2024-02-25 at 18 48 24" src="https://github.com/AEmin96/AmperGym/assets/126208272/7ac82dd1-94ee-49e3-b512-da175cfa9c4e">
  </li>
  
  <li><h3>Personalized user dashboard for subscription and profile management.</h3>
    <img width="2040" alt="Screenshot 2024-02-25 at 18 49 01" src="https://github.com/AEmin96/AmperGym/assets/126208272/910c5e8f-68ae-4d25-af91-91cae2785bd9">
  </li>
</ul>

<h2>4. Future Features</h2>
<ul>
<li>Workout planner integration.</li>
<li>Online personal training bookings.</li>
<li>Gym equipment availability checking.</li>
</ul>

<h2>5. Technology</h2>
<ul>
<li>GitHub for version control.</li>
<li>Django for the web framework.</li>
<li>Stripe for secure payment processing.</li>
<li>Heroku for deployment.</li>
<li>PostgreSQL for database management.</li>
</ul>

<h2>6. Testing</h2>
<h3>6.1 Manual Testing</h3>


| Test                                          | Expected Result                                                                                           | Actual Result                                                                                        | Resolved by                                                                                                          | Test Result       |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------|
| Email verification                            | Prevent the use of one email to open multiple accounts                                                    | One email could be used to create multiple accounts                                                  | Implemented email uniqueness validation on account creation. If an email is already in use, a "This email is already in use" message is shown.   | Pass              |
| Subscribing to 2 plans at the same time      | User can only have one subscription at a time. Selecting another plan updates the current subscription    | Users were able to subscribe to multiple plans simultaneously                                        | Modified subscription logic to automatically cancel the current subscription and activate the new selection upon change.                        | Pass              |
| Cancelling subscription                       | A confirmation modal appears to ensure the user wants to cancel their subscription                        | The subscription would cancel immediately without confirmation                                       | Implemented a confirmation modal that triggers upon the cancel subscription action, requiring user confirmation to proceed.                     | Pass              |
| Location navigation link                      | Expected result when clicked to take you to location page                                                 | Clicked and navigated to the location page as expected                                               | N/A                                                                                                                  | Pass              |
| Testimonials navigation link                 | Expected result when clicked to take you to the testimonials page                                         | Clicked and navigated to the testimonials page as expected                                           | N/A                                                                                                                  | Pass              |
| About Us navigation link                      | Expected result when clicked to take you to the About Us page                                             | Clicked and navigated to the About Us page as expected                                               | N/A                                                                                                                  | Pass              |
| Log In page navigation link                   | Expected result when clicked to take you to the Log In page                                               | Clicked and navigated to the Log In page as expected                                                 | N/A                                                                                                                  | Pass              |
| Become a Member page navigation link         | Expected result when clicked to take you to the Become a Member page                                      | Clicked and navigated to the Become a Member page as expected                                        | N/A                                                                                                                  | Pass              |
| Subscriptions page navigation link           | Expected result when clicked to take you to the Subscriptions page                                        | Clicked and navigated to the Subscriptions page as expected                                          | N/A                                                                                                                  | Pass              |
| Testimonial addition and rating display      | Testimonials could be added successfully and their ratings should be displayed                            | Testimonials could be added successfully, however, the rating wasn't showing                        | Implemented the star icon from Font Awesome and fixed the formatting issue to ensure ratings are displayed correctly.                          | Fail (Resolved)   |



<h3>6.2 Test Cases (User Story Based with Screenshots)</h3>

<ul>
  <li> <h4> As a user considering the gym, I want to read reviews and testimonials from other members to get insights into their experiences and gauge the overall satisfaction of the gym's community, helping me make a more confident decision about joining.  </h4>
  <em> Testimonial Page Added : </em> 
  </li>

![testi](https://github.com/AEmin96/AmperGym/assets/126208272/a14c410d-1b63-453d-85cc-877246648bd5)

  <li> <h4> As a current gym member, I want a user-friendly dashboard where I can log in, view my subscription details, and easily manage my account settings, such as updating personal information or changing my subscription plan, to ensure a seamless experience. </h4>
  <em> Subscriptions Page Features Easy Uprade & Cancel Membership Interface : </em> 
  </li>

  ![Screenshot 2024-02-16 at 18 14 00](https://github.com/AEmin96/AmperGym/assets/126208272/82592e3b-6b41-4bfa-a606-0ca17525010a)

 
</ul>

<h3>6.3 Validator Testing</h3>
<h3>HTML Validator</h3>

![Screenshot 2024-02-16 at 18 34 28](https://github.com/AEmin96/AmperGym/assets/126208272/71156a5b-4126-4163-8f2c-fdcbe9d43182)


<h3>CSS Validator</h3>

![Screenshot 2024-02-16 at 18 38 32](https://github.com/AEmin96/AmperGym/assets/126208272/5285ee6a-7f1a-4303-828d-1f7d188d195e)


<h3>6.4 Fixed Bugs</h3>
<table border="1">
  <tr>
    <th>Bug</th>
    <th>Expected Result</th>
    <th>Actual Result</th>
    <th>Solution</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>Access Denied for Non-Logged-In Users to Subscriptions Page</td>
    <td>Non-logged-in users should be able to view the subscriptions page.</td>
    <td>Non-logged-in users were denied access.</td>
    <td>The access restriction was lifted by removing the @login_required decorator.</td>
    <td>Resolved</td>
  </tr>
  <tr>
    <td>Subscriptions Not Recorded in Database Post-Checkout</td>
    <td>Subscriptions should be added to the database after checkout.</td>
    <td>Subscriptions were not being recorded in the database.</td>
    <td>The issue was resolved by correcting a naming conflict within two functions in the same view.</td>
    <td>Resolved</td>
  </tr>
  <tr>
    <td>Password Auto-save or Wrong Password in Old Password Field Prevents User Info Updates</td>
    <td>User info should update upon form submission if all required fields are correctly filled.</td>
    <td>The form would not save any updated info if the old password was auto-saved or incorrect, without providing clear feedback to the user.</td>
    <td>Added the required attribute for the old password field and implemented modal messages for successful updates or errors.</td>
    <td>Resolved</td>
  </tr>
</table>


<h3>Deployment</h3>

<h4>Local and Heroku Deployment</h4>

<h5>Local Deployment</h5>

<h6>Step 1: Cloning the Repository</h6>
<ul>
    <li>I navigated to the GitHub repository, clicked on the "Code" button, and copied the URL provided.</li>
    <li>In my preferred IDE, I opened a terminal session in the directory where I wanted to clone the repository.</li>
    <li>I typed <code>git clone</code> followed by the URL I had copied and pressed enter to clone the repository.</li>
</ul>

<h6>Step 2: Installing Dependencies</h6>
<ul>
    <li>Using the terminal, I executed <code>pip install -r requirements.txt</code> to install the necessary project dependencies.</li>
</ul>

<h6>Step 3: Setting Up Environment Variables</h6>
<ul>
    <li>I set up the required environment variables in my local environment as described in the "Environment Variables" section for proper configuration.</li>
</ul>

<h6>Step 4: Database Setup and Migrations</h6>
<ul>
    <li>I connected my chosen database and ran <code>python manage.py migrate</code> in the terminal to apply migrations.</li>
</ul>

<h6>Step 5: Creating a Superuser</h6>
<ul>
    <li>To create a superuser account, I executed <code>python manage.py createsuperuser</code> in the terminal and followed the on-screen prompts.</li>
</ul>

<h6>Step 6: Running the Application</h6>
<ul>
    <li>Finally, I started the application by typing <code>python manage.py runserver</code> in the terminal and opened the provided URL in my browser to view the app.</li>
</ul>

<h5>Heroku Deployment</h5>

<h6>Step 1: Heroku App Creation</h6>
<ul>
    <li>I logged into the Heroku dashboard and created a new app by following the setup prompts.</li>
</ul>

<h6>Step 2: GitHub Repository Connection</h6>
<ul>
    <li>I connected my GitHub repository to my Heroku app through the Heroku dashboard, enabling code sync between GitHub and Heroku.</li>
</ul>

<h6>Step 3: Buildpack Configuration</h6>
<ul>
    <li>In the "Settings" tab of my Heroku app, I ensured that the Python Buildpack was added to allow Heroku to recognize and build the project as a Python app.</li>
</ul>

<h6>Step 4: Setting Environment Variables on Heroku</h6>
<ul>
    <li>I set the necessary environment variables in the "Config Vars" section of the "Settings" tab to match the local setup.</li>
</ul>

<h6>Step 5: Deployment Trigger</h6>
<ul>
    <li>In the "Deploy" tab, I enabled automatic deploys from my connected GitHub repository and manually triggered a deployment by clicking the "Deploy Branch" button.</li>
</ul>

<h6>Step 6: Launching the App</h6>
<ul>
    <li>Once deployment was successful, I clicked on the "Open App" button to view my live application hosted on Heroku.</li>
</ul>



<h3>8. Credits</h3>
<p>Code Institute for the project template and guidance.</p>
<p> Background Video : <a href="https://www.pexels.com/@cottonbro/" target="_blank" class="text-black mr-3"> @cottonbro </a> </p>
         <p> Background Images : <a href="https://www.pexels.com/@goumbik" target="_blank" class="text-black mr-3"> @goumbik</a> </p>
