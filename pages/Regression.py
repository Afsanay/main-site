import streamlit as st

st.set_page_config(layout="wide")

st.title("Regression Models")
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    text-align:center !important;
}
.small-image {
    width: 25px !important;
    height:25px !important;
    border-radius: 50%;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Regression models are statistical models used to estimate the relationship between a '
            'dependent variable and one or more independent variables. The goal of regression analysis is to '
            'understand and predict the value of the dependent variable based on the values of the independent '
            'variables. The independent variables can be either continuous or categorical, and their values are used '
            'to explain or predict the values of the dependent variable.</p>', unsafe_allow_html=True)
st.divider()
st.markdown(
    """
    <h2 class = "font-size:5px">Movie-Recommendation-System</h2>
    <p class= "font-size:2px">This project uses locally trained Linear Regression on IMDB dataset to find top 5 closest movies to the selection movie for recommendation.</p>
        <a href= "https://movie-recomm-9ah318ig7j.streamlit.app/">Checkout the project</a>
        <img class="small-image" src="https://streamlit.io/images/brand/streamlit-mark-color.svg"/> 
        <br/>
        <a href= "https://github.com/Afsanay/movie-recomm">Github</a>
        <img class="small-image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"/> 
    """,
    unsafe_allow_html=True
)
st.divider()
st.markdown(
    """
    <h2 class = "font-size:5px">ML-Auto</h2>
    <p class= "font-size:2px">This project uses Lazy-Predictor library for generating full analysis of a given dataset along with losses of all the regression models after training.</p>
        <a href= "https://imagecaption-wnkc2rz0ph.streamlit.app/">Checkout the project</a>
        <img class="small-image" src="https://streamlit.io/images/brand/streamlit-mark-color.svg"/> 
        <br/>
        <a href= "https://github.com/Afsanay/image_caption">Github</a>
        <img class="small-image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"/> 
    """,
    unsafe_allow_html=True
)
st.divider()

st.info("The locally trained models have been trained for a maximum of 10-15 hrs which may or may not be sufficient for immersive results")


