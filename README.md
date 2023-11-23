# Semantic-Search-Engine


Semantic Search API using Flask
This repository contains code for a RESTful Semantic Search API built with Flask, enabling users to perform semantic searches across a collection of Json files.

Features:
Semantic Search Functionality: Utilizes spaCy for text preprocessing, scikit-learn for TF-IDF vectorization, and cosine similarity for semantic search capabilities.
RESTful API: Provides a simple REST API endpoint /search where users can pass a query as a URL parameter to retrieve relevant text documents.
Text Preprocessing: Removes stopwords, tokenizes, converts to lowercase, and lemmatizes text for efficient search.


How to Use:
Setup:

Clone this repository to your local machine.
Ensure Python and necessary dependencies (Flask, spaCy, scikit-learn) are installed.


Data Preparation:

Replace the folder_path variable in app.py with the path to your directory containing text files.
Ensure data files are in .json format.


Run the Application:

Execute python app.py in your terminal to start the Flask server.
The API will be available at http://127.0.0.1:5000/search.


Performing a Search:

Use a web browser or any HTTP client to send a GET request to /search endpoint with the query parameter (?query=YourQuery).


http://0.0.0.0:5000/search?query=YourQuery you can replace YourQuery with Query.


Results:

Results will be in Json format with the Relivant Text, Name of file and Matching score. Result shown will be top Three results according to the match score higher to Lower score.


Example Usage:


GET /search?query=YourQuery



Contributions:
Contributions and enhancements are welcome! Fork this repository, make changes, and create a pull request with your improvements.
