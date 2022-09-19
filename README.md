# Clean and Lean Blog

This is a full-stack project employing the programming and framework tools Django, Bootstrap, Python, HTML and CSS. The primary goals of the project were to provide a fully functioning and responsive website allowing users the ability to post up recipes, comment on recipes and also provide the option for users to like or unlike recipes.
<br><br>

## Site Overview

The Clean and Lean Blog is a site created with the intention of providing information on exciting recipes and also offering the user an opportunity to post up their own recipe ideas that they would like to share with other enthusiasts. The resource is created for those who enjoy cooking. It is designed to give a user a degree of knowledge and inspiration when it comes to all things culinary.
<br><br>

It is a website designed to be interacted with by people of all ages who have a keen interest in food and its use serves to provide a fun and interesting experience for those passionate about this artform.
<br><br>

The Home page of the blog is the primary source that reflects a strong and appealing visual of what the website is all about. The opening title highlights a relationship to the content and allows a user to create an account to allow them access to post up their own recipes. The Home page also gives a user the option to sign in should they be a previously registered user on the site.
<br><br>


![Image of Clean and Lean Blog](/static/images/cleanandlean.png)

<br>

# Planning Stage
<br>

## Identifying a Target Audience
<br>

* People who enjoy cooking.

* People who are interested in posting up their recipes, engaging with other users and those who are interested in imparting their own food wisdom on the website.

* People who have a keen interest in the culinary process and finding out a little bit more about how other food enthusiasts put their recipes together.

<br><br>

# User Stories
<br>

## First-time Visitors

* Users should want to have immediate information on the subject matter of the website.

* The site should have the ability to be easily navigable for visitors to get started in viewing and posting up recipes.

* The site should provide inspiration for a visitor who is interested in all things related to food.


<br>

## Returning Visitors

* For returning visitors it would be good to have more recipes available for those users to try out.

<br>

## Admin

* As a site administrator it is possible to create, edit, and delete recipes and comments on the blog.
* As a site administrator it is possible to moderate what comments are allowed on the website.


<br>

## User

* As a user it is possible to create an account, log in and out of that account.
* As a user it is possible to post up recipes after registering an account.
* As a user it is possible to comment on posted recipes.
* As a user it is possible to like or unlike recipes.

<br>

# Design

<br>

## Colour Schemes

<br>

* For the colour schema of the website I wanted to introduce a rich and rustic surround to the site. The landing page image was indicative of how I perceived the whole project concept, warm and inviting, to tie in accurately with the recipes offered in the site. 

* As the website landing page image is a notable feature on first viewing it didn't need too much of a remove when deciding appropriate colours to coincide with the visual aspects of the website. Button colours and the Brand lettering worked well with rgb(255, 165, 0). For the card recipes this was offset subtly with rgb(251, 241, 222), only a slight but noticeable remove on subsequent pages.

* Hover options on buttons employed short contrasts to original button colours.

<br>

## Font Families

<br>

* Font Families included Lato, Roboto and Sans Serif. It added a clarity and refinedness that the pages deserved. 

<br><br>

# Features

<br>

## The Home and Registration Page

<br>

  * The Home Page consists of the Clean and Lean brand name logo. 

  * Links to the Home Page and Login are present when the landing page is rendered. A Healthy Option link redirects to the home page. A centered button to register for the site is also present.

  * The Home Page consists of the primary details and information on how to register to post up receipes.

  <br>

  ![Home Page](static/images/homepage.png) 

  <br>

  ## The Login Page

  <br>

  * The Login Page presents two extra navbar links, Recipes and Add Recipes.

  * Post registration this gives the user the option to view recipes already posted.

  * Post registration this gives the user the option to make comments on recipes posted.

  * Post registration this gives the user the option to like or unlike recipes.

  <br>

  ![Login Page](static/images/loginpage.png)

  <br>

  ## The Recipe Pages

  <br>

  * The Recipes Page is where the most recent recipes have been posted up by registered users.

  * Recipes appear as cards, which can be clicked on to render more information about each recipe posted up.

  * The cards indicate what type of recipe it is and which user posted it.

  <br>

  ![Recipes Page](static/images/recentrecipes.png)
  ![Recipes Page](static/images/recipemobile.png)

  <br><br>

  # Testing

  * As a site administrator site content can be managed easily, with the ability to create, edit and delete user posts and comments.

  * This was tested by accessing the Django Admin Panel where all CRUD functionalities can be performed.

  * Likes and Comments features all worked as expected.

  * As a user it is possible to register, log-in and be interative with the site.

  * As a user it is possible to sign out after using the site.


  <br>

  ![Image of Django Admin](static/images/djangoadmin.png)
  <br>
  ![Image of Likes and Comments](static/images/likeandcommen.png)
  <br>
  ![Image of Comments](static/images/comments.png)
  <br>
  ![Image of Signing Out](static/images/signingout.png)
  <br>
  ![Image of Registration](static/images/signingup.png)
  <br>
  ![Image of Login/Out Status](static/images/loginlogout.png)


  <br>

  # Responsiveness

  <br>

  * The responsiveness of the site was ran through [Responsive Design Checker](https://responsivedesignchecker.com/) and rendered well on all mobile devices during testing.

  <br>

  # Validation

  * No errors were recorded when entered into the official W3C Validator for CSS.

  <br>

  ![Image of CSS Validator](static/images/cssvalid.png)

  <br>


  <br>

  

  # Future Features

  * Create the option where users receive notifications when comments are posted on their recipes.

  * Include a feature that categorises the types of cuisines posted up on the website.

  <br><br>

  # Bugs

  <br>

  * I encountered a few issues where the site didn't meet my intended expectations. This primarily resided in the arena of responsiveness when viewing the screen at mobile level. The Summernote default widget form was difficult to  didn't render seamlessly in a landscape view. A fix for this was to dispense with static height and width properties that were yielding limitations when added to the body.

  * Deployment to Heroku proved to be erratic, as a lot of the data didn't render as expected when deployed on various different occasions. This may have been issues relating to the migration process, whether is was something overlooked at the time of deployment or some issues with the server.

  <br><br>

  # Unfixed Bugs

  <br>

  * There were no unfixed bugs.

  <br><br>

  # Technologies and Languages Used

  * HTML
  * CSS
  * JavaScript
  * Python

  * [GitHub](https://github.com/)
  * [Heroku](https://id.heroku.com)
  * [Django](https://www.djangoproject.com/)
  * [Bootstrap](https://getbootstrap.com/)
  * [Summernote](https://summernote.org/)
  * [Cloudinary](https://cloudinary.com/)

  <br>

  The content and media used during the project was sourced and referenced as follows:

  * Responsive Aid [AmIResponsive](http://ami.responsivedesign.is/)
  * Social Media Icons [Font Awesome](https://fontawesome.com/)
  * Fonts [Google Fonts](https://fonts.google.com/)

  <br><br>

  # Deployment

  <br>

  * The website was deployed to GitHub Pages in the following manner:

    * From the project's [Repository](https://github.com/Th3ThirdMan/CleanProject) go to Settings:
    * Scroll down to GitHub Pages
    * Select Branch, Main & Save.
    * A message will indicate that the project has been successfully deployed here and a live link is available.

    <br>

    You can find the live site here: [CleanandLean2022](https://cleanproject2022.herokuapp.com/)

    <br><br>


