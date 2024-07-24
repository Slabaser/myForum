<h1>Technology Discussion Platform</h1>
This project is a web application that allows users to create rooms and discuss various technology topics. It is developed using the Django framework.

<h2>Table of Contents</h2>
<ul>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
</ul>
<h2 id="getting-started">Getting Started</h2>
<p>This guide provides instructions on how to set up and run the project on your local machine.</p>
<h4>Requirements</h4>
 <ul>
        <li>Python 3.10 or newer</li>
        <li>Django 4.2.13 or newer</li>
        <li>PostgreSQL or another supported database</li>
    </ul>
<h2 id="installation">Installation</h2>
<p>Follow these steps to get the project up and running:</p>
<ol>
<li><strong>Clone the Repository:</strong></li>
        <pre><code>git clone https://github.com/slabaserr/myForum.git</code></pre>
 <li><strong>Install Required Packages:</strong></li>
        <p>Navigate to the project directory and create a virtual environment:</p>
        <pre><code>cd myForum
python -m venv venv 
source venv/bin/activate  # For Windows: venv\Scripts\activate</code></pre>
<p>Then, install the required packages:</p>
<pre><code>pip install -r requirements.txt</code></pre>
<li><strong>Configure the Database:</strong></li>
<p>Configure the database settings in <strong>myForum/settings.py</strong>. By default, SQLite is used, but if you prefer PostgreSQL or another database, adjust the settings accordingly.

Create the database tables:</p>
<pre><code>python manage.py migrate</code></pre>
<li><strong>Create a Superuser:</strong></li>
<p>Create a superuser for accessing the admin panel:</p>
<pre><code>python manage.py createsuperuser</code></pre>
<li><strong>Start the Server:</strong></li>
<p>Run the web application on the local development server:</p>
<pre><code>python manage.py runserver</code></pre>
<p><i>You can view the web application at http://127.0.0.1:8000/.</i></p>
</ol>
<h2 id="usage">Usage</h2>
<p>The web application is ready for use. Users can:</p>
 <ul>
        <li><strong>Sign Up:</strong> Users who are not registered can create an account by clicking on the "Sign Up" button. Once registered, they can create new rooms and participate in discussions.</li>
        <li><strong>Create and Manage Rooms:</strong> Registered users can create new discussion rooms. They can also edit or delete rooms they have created. Each room can be customized with topics and settings.</li>
        <li><strong>Participate in Discussions:</strong> Users can join discussions in the rooms they are interested in. They can post comments and reply to other users’ comments.</li>
        <li><strong>Select Topics:</strong> On the left sidebar, users can select different topics to filter discussions according to their interests.</li>
        <li><strong>View Recent Activities:</strong> On the right sidebar, users can see recent activities of other users, including their latest comments and room creations.</li>
    </ul>
