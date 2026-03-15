#  Crop Recommendation System

The Crop Recommendation System is an intelligent web application designed to help farmers and agricultural stakeholders make data-driven cultivation decisions. By analyzing key soil nutrients (Nitrogen, Phosphorus, Potassium) and environmental factors (Temperature, Humidity, pH, and Rainfall), the system leverages a trained Machine Learning model to predict the most optimal crop for a given environment. Built with a Flask backend and a clean user interface, this project bridges the gap between agricultural data science and accessible technology, promoting better crop yields and sustainable farming practices.

A Machine Learning-powered web application that recommends the most suitable crop to cultivate based on soil metrics and environmental conditions. 

This project integrates a predictive model with a web interface, allowing users to input agricultural parameters and receive instant, data-driven crop recommendations.

## Features

* **Machine Learning Prediction:** Utilizes a trained model (`crop_model.pkl`) to predict the optimal crop from various target classes.
* **Interactive Web Interface:** User-friendly frontend built with HTML/CSS to easily input soil and weather data.
* **Web Framework:** Backend API built using Flask to handle client requests and serve predictions.
* **Data Processing:** Handles 7 key agricultural features to make accurate predictions.

##  Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn, NumPy, Pandas
* **Frontend:** HTML, CSS (Jinja2 Templates)
* **Environment:** Jupyter Notebook (for model training/EDA)

##  Project Structure

```text
├── templates/
│   └── index.html               # Frontend web interface
├── app.py                       # Flask application and API routing
├── crop_model.pkl               # Serialized machine learning model
├── Crop_recommendation.csv      # Dataset used for training
├── IOT_Based_Crop_Prediction (1).ipynb # Jupyter Notebook with EDA and model training
├── iot_based_crop_prediction.py # Python script for model building
└── README.md                    # Project documentation
````
##  Input Parameters

The model requires the following 7 parameters to make a prediction:

* **N:** Ratio of Nitrogen content in soil
* **P:** Ratio of Phosphorous content in soil
* **K:** Ratio of Potassium content in soil
* **Temperature:** Temperature in degrees Celsius
* **Humidity:** Relative humidity in percentage
* **pH:** Soil pH value
* **Rainfall:** Rainfall in millimeters

---


##  Local Setup and Installation

**2. Install required dependencies**
Make sure you have Python installed. It is recommended to use a virtual environment.

```bash
!pip install Flask numpy scikit-learn pandas
```

**3. Run the Flask application**
```bash
python app.py
```

**4. Access the web app**
Open your web browser and navigate to:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

**5. Machine Learning Workflow**
The model was developed using the accompanying Jupyter Notebook (IOT_Based_Crop_Prediction (1).ipynb). The workflow included:

* Loading and cleaning the Crop_recommendation.csv dataset.
* Exploratory Data Analysis (EDA) to understand feature distributions.
* Training various classification algorithms to find the highest accuracy.
* Exporting the best-performing model and a label mapping dictionary into crop_model.pkl for deployment.
