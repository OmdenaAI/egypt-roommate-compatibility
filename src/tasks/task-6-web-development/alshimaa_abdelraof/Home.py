import streamlit as st

st.markdown("# Home")
st.sidebar.markdown("# Home")
from PIL import Image

image = Image.open('1.jpeg')

st.image(image, caption='Shareable Life | Enhancing Roommate Compatibility Detection through Machine Learning')
st.title('The problem:')
st.markdown('The complexity of finding suitable roommates can be daunting, and traditional methods like classified ads or social media may not be effective in finding the right match. Additionally, the process of manually assessing compatibility between potential roommates can be time-consuming and subjective, leading to suboptimal matches.')

st.title('Project Goals:')
st.markdown('**:blue[The primary goal of this project is to]:**, develop a machine-learning model that can accurately match potential roommates based on their preferences, lifestyle, and psychological profiles. The model should be efficient, streamlined, and user-friendly. The project aims to: - Collect data on potential roommates, including information on their lifestyle, food preferences, and other factors that may impact their compatibility with others. - Develop a machine learning model that uses the collected data to identify potential matches. - Train and evaluate the model using a dataset of past matches. - Develop a user-friendly app that incorporates the matching algorithm and enables users to input their preferences and receive recommendations for potential roommates.')