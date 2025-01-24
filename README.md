# Contextual Advertising Platform

## Overview
This project is built using Python, Django, and several other technologies. The platform extracts relevant keywords from any given blog article URL and matches them with advertisements in the database. This allows the display of ads that are highly relevant to the content of the blog.

The project works by accepting a blog URL, parsing the content using `requests` and `BeautifulSoup`, extracting relevant keywords with `RakeNLTK`, and then displaying the most suitable advertisements based on those keywords.

### Technologies Used
- **Python**: Programming language used for backend logic.
- **Django**: Web framework for building the app.
- **Requests**: Library used to make HTTP requests to blog pages and fetch content.
- **BeautifulSoup**: HTML parser used to extract and parse data from webpages.
- **RakeNLTK**: A tool for extracting the most relevant and prominent keywords from a text.
- **Tailwind CSS**: A CSS framework for styling the web app.

## Features
- Accepts a blog URL.
- Fetches the content of the blog using `requests`.
- Parses the content using `BeautifulSoup`.
- Extracts relevant keywords from the blog content using `RakeNLTK`.
- Matches the keywords with advertisements stored in the database.
- Displays relevant advertisements on the webpage.
- Admin can add new advertisements using Django’s admin interface.
  
## Setup Instructions
```bash
git clone <repository-url>
cd <project-directory>
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
## Access the App:
- To access the app, open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Admin Interface:
- To manage advertisements, log in to the Django admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) using the superuser credentials you created.
- In the admin interface, you can add new advertisement images and tags for matching with content.

## Usage:
1. **Submit a Blog URL**: Enter the URL of a blog post into the web interface.
2. **Analyze Content**: The system automatically fetches the content from the provided URL, parses the text, and extracts relevant keywords.
3. **Display Ads**: Based on the extracted keywords, the platform will display ads from the database that match the content.

## Notes:
- **Superuser Required for Adding Ads**: A superuser account is required to add new advertisements and tags for matching. You can manage ads via the Django admin interface.
- **Tailwind CSS Styling**: The app is styled using Tailwind CSS, which employs utility-first classes. You can further customize the styles by adjusting the classes in the HTML templates.



 
