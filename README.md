# 🎬 Movie-Recommendation-System

## 🌟 Overview

This project is a **content-based movie recommendation system** that utilizes **cosine similarity** to recommend movies based on their textual descriptions. The system converts movie descriptions into tags, then calculates similarity scores to suggest movies that are similar to a user's preferences.

## 🔑 Key Features

- **🎥 Content-based filtering**: Recommends movies based on similarity of movie descriptions.
- **🔍 Cosine similarity**: Measures similarity between movies by comparing their tags.
- **🌐 Streamlit Interface**: An interactive web interface for users to get movie recommendations.

## 🛠️ How It Works

1. **📊 Data Preprocessing**:
   - The movie descriptions are cleaned and preprocessed.
   - Text is transformed into tags representing the key features of the movie.

2. **🏷️ Tagging**:
   - Descriptions are converted into tags, which capture the essence of the movie.

3. **📐 Cosine Similarity Calculation**:
   - The system calculates cosine similarity between movies based on the tags.

4. **🤖 Recommendations**:
   - Movies with the highest similarity scores to the user's interest are recommended.

## ⚙️ Setup

### 🧰 Prerequisites

- Python 3.x
- Libraries: `scikit-learn`, `numpy`, `pandas`, `nltk`, and `streamlit`.
