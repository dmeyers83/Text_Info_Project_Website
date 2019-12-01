#Dependencies 
- Flask

#run
- python main.py

#Files
- main.py: Main python code that initializes flask, runs the scrapper/LDA (not complete) and creates URL routes to the 2 HTML pages (results.html, landingpage.html)
- landingpage.html: landing page where a user will input a job search query
- results.html: page which receives the user search query in the URL, and the data objects to render in charts.

#Notes
- CSS/HTML: https://materializecss.com/
- landingpage uses jquery to bind an onclick event to the search box, creates an URL with a search query and redirects to the results.html page
- results page renders the LDA results passed from the main.py into chartjs interactive charts
- in main.py the object 'sampleLDAObject' is just a sample object which will be replaced by the return value of the LDA/Scrapper class.

#To do
- Move jupyter notebook into a python class and integrate with the python main.js
- Update charts to reflect Brian's latest analysis.

