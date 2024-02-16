<h1>AmperGym</h1>
<h2>Deployed Project: <a href="https://ampergym-f292fdd6def8.herokuapp.com/">AmperGym</a></h2>


<h2>1. Purpose of the Project</h2>
<p>The purpose of the AmperGym project is to provide an interactive and user-friendly gym website that offers users the ability to sign up, manage, and upgrade their subscriptions seamlessly. Integrating Stripe for secure payments, the site facilitates easy subscription selection and management, enhancing the overall user experience. The project aims to motivate users with accessible gym information, including location, opening times, and user testimonials, while also providing personalized user accounts for managing personal information and subscriptions.</p>

<h1>Sneak Peak</h1>


https://github.com/AEmin96/AmperGym/assets/126208272/0aaf596b-d33b-469d-b315-6b2c01d81865


<h1>Entity & Relationship Diagram</h1>

![AmpergymERD drawio](https://github.com/AEmin96/AmperGym/assets/126208272/87818043-6ecf-4ea2-bf57-7324ad774c95)



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
<li>User-friendly navigation and responsive design.</li>
<li>Stripe integration for secure payment processing.</li>
<li>Dynamic content for users based on login status.</li>
<li>Google Maps API for gym location.</li>
<li>Testimonial feature for public user feedback.</li>
<li>Personalized user dashboard for subscription and profile management.</li>
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

| Test                                           | Expected Result                                                                                         | Actual Result                                                                                      | Resolved by                                                                                                        |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Email verification                             | Prevent the use of one email to open multiple accounts                                                 | One email could be used to create multiple accounts                                                | Implemented email uniqueness validation on account creation. If an email is already in use, a "This email is already in use" message is shown. |
| Subscribing to 2 plans at the same time       | User can only have one subscription at a time. Selecting another plan updates the current subscription | Users were able to subscribe to multiple plans simultaneously                                      | Modified subscription logic to automatically cancel the current subscription and activate the new selection upon change.                      |
| Cancelling subscription                        | A confirmation modal appears to ensure the user wants to cancel their subscription                      | The subscription would cancel immediately without confirmation                                     | Implemented a confirmation modal that triggers upon the cancel subscription action, requiring user confirmation to proceed.                   |


<h3>6.2 Test Cases (User Story Based with Screenshots)</h3>

<ul>
  <li> <h4> As a user considering the gym, I want to read reviews and testimonials from other members to get insights into their experiences and gauge the overall satisfaction of the gym's community, helping me make a more confident decision about joining.  </h4>
  <em> Testimonial Page Added : </em> 
  </li>
   ![Screenshot 2024-02-16 at 18 05 58](https://github.com/AEmin96/AmperGym/assets/126208272/60796bd1-d2ae-4fbf-a201-0614434f267a)


    
 
</ul>

<h3>6.3 Validator Testing</h3>
<h3>HTML Validator</h3>
<!-- Include HTML validator results -->
<h3>CSS Validator</h3>
<!-- Include CSS validator results -->

<h3>6.4 Fixed Bugs</h3>
<!-- List down the bugs found and fixed -->

<h3>7. Deployment</h3>
<!-- Provide steps for how the project was deployed -->

<h3>8. Credits</h3>
<p>Code Institute for the project template and guidance.</p>
