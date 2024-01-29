import streamlit as st
import requests

st.title("Disaster Tweet Prediction")

# Input text box for user to enter a tweet
tweet_input = st.text_area("Enter a tweet:", "")

if st.button("Predict"):
    # Make a request to the Flask API for prediction
    response = requests.post("http://127.0.0.1:5000/predict", json={"tweet": tweet_input})
    
    # Display the prediction result
    if response.status_code == 200:
        result = response.json()
        prediction = result['prediction']
        confidence = result.get('confidence', None)
        
        st.success(f"Prediction: {prediction} (Confidence: {confidence:.2f})")
    else:
        st.error("Error making prediction. Please try again.")
