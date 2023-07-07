import streamlit as st

st.set_page_config(layout="wide")

st.title("Long Short-Term Memory Network")
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

st.markdown('<p class="big-font">LSTM is a type of recurrent neural network (RNN) architecture designed to handle sequential data. Unlike traditional RNNs, LSTM has an internal memory mechanism that allows it to capture and store information over long periods of time. It achieves this by using specialized units called memory cells, which are equipped with gates to control the flow of information.</p>', unsafe_allow_html=True)
st.divider()
st.markdown(
    """
    <h2 class = "font-size:5px">Image-Caption</h2>
    <p class= "font-size:2px">This project uses a locally trained model, consisting of VGG-16 and LSTM, to generate a caption for a particular image.</p>
        <a href= "https://imagecaption-wnkc2rz0ph.streamlit.app/">Checkout the project</a>
        <img class="small-image" src="https://streamlit.io/images/brand/streamlit-mark-color.svg"/> 
        <br/>
        <a href= "https://github.com/Afsanay/image_caption">Github</a>
        <img class="small-image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"/> 
    """,
    unsafe_allow_html=True
)
st.divider()
st.markdown(
    """
    <h2 class = "font-size:5px">Lip-Stream</h2>
    <p class= "font-size:2px">This project uses locally trained LipNet network,which is an architecture for lip-reading and generate the sentence for a particular video.</p>
        <a href= "https://lipstream-7sdq5z5lftc.streamlit.app/">Checkout the project</a>
        <img class="small-image" src="https://streamlit.io/images/brand/streamlit-mark-color.svg"/> 
        <br/>
        <a href= "https://github.com/Afsanay/LipStream">Github</a>
        <img class="small-image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"/> 
    """,
    unsafe_allow_html=True
)
st.divider()

st.info("The locally trained models have been trained for a maximum of 10-15 hrs which may or may not be sufficient for immersive results")


