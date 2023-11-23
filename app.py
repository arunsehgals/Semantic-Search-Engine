# app.py
import os
import json
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 9999999

# Load and preprocess text dataS
def load_and_preprocess_data(file_paths):
    documents = []
    document_names = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            text_content = file.read()
            # Tokenize, lowercase, remove stopwords, and lemmatize
            processed_text = " ".join(token.lemma_ for token in nlp(text_content) if not token.is_stop)
            documents.append(processed_text)
            document_names.append(os.path.basename(file_path))
    return documents, document_names

# Function for semantic search
def semantic_search(query, documents, document_names):
    # Vectorize documents using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Vectorize query
    query_vector = vectorizer.transform([query])
    
    # Calculate similarity scores
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    
    # Retrieve documents with matching scores
    matching_documents = []
    for i, score in enumerate(similarity_scores[0]):
        matching_documents.append({'document_name': document_names[i], 'score': score, 'text': documents[i]})
    
    # Sort by scores (highest to lowest)
    matching_documents = sorted(matching_documents, key=lambda x: x['score'], reverse=True)
    
    return matching_documents



@app.route('/search', methods=['GET'])
def search():
    folder_path = r'./data'  # Replace with your folder path containing text files
    query = request.args.get('query', '')
    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.json')]
    

    documents, document_names = load_and_preprocess_data(file_paths)
    results = semantic_search(query, documents, document_names)

    formatted_results = []

    # Format results into JSON-compatible structure
    for result in results:
        formatted_result = {
            "Document Name": result['document_name'],
            "Score": result['score'],
            "Relevant Text": result['text'][:500]  # Limiting text to 500 characters
        }
        formatted_results.append(formatted_result)

    # Convert the formatted results to JSON
    json_result = json.dumps(formatted_results, indent=4)

    # Print or return the JSON result
    #print(json_result)
    results = formatted_results[:3]
    return jsonify(results)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')