# Flask Blog Project

A simple blog web application built with **Flask** that dynamically renders posts from an external JSON API. 

The project uses Bootstrap for styling and a clean blog template.


## **Features**
- **Home Page**: Displays a list of blog posts fetched from an external API.
- **Post Page**: View individual blog posts.
- **About Page**: Static about page.
- **Contact Page**: Static contact page.
- **Dynamic Routing**: Each post can be accessed via `/post/<id>`.
- **Bootstrap Template**: Integrated responsive template for a modern UI.

## **Tech Stack**
- **Backend**: Flask (Python)
- **Frontend**: HTML, Jinja2 Templates, Bootstrap 5
- **API**: [npoint.io](https://api.npoint.io/3d8c82acbe30617619cc) for blog posts
- **HTTP Requests**: `requests` library to fetch posts