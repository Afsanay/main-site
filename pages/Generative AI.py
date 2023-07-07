import streamlit as st

st.set_page_config(layout="wide")

st.title("Generative Artificial Intelligence")
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

st.markdown('<p class="big-font">Generative AI is a type of artificial intelligence technology that can produce various types of content, including text, imagery, audio and synthetic data. The recent buzz around generative AI has been driven by the simplicity of new user interfaces for creating high-quality text, graphics and videos in a matter of seconds.</p>', unsafe_allow_html=True)
st.divider()
with st.expander("Generative Adversarial Networks", expanded=True):
    st.markdown(
        """
        <h2 class = "font-size:5px">ESRGAN</h2>
        <p class= "font-size:2px">This project uses locally trained ESRGAN network to enhance the pixel density of a low-resolution image and generating high-quality images</p>
            <a href= "https://esrgan-pjsbfpkid3n.streamlit.app/">Checkout the project</a>
            <img class="small-image" src="https://streamlit.io/images/brand/streamlit-mark-color.svg"/> 
            <br/>
            <a href= "https://github.com/Afsanay/ESRGAN">Github</a>
            <img class="small-image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"/> 
        """,
        unsafe_allow_html=True
    )
    st.divider()
    st.markdown(
        """
        <h2 class = "font-size:5px">Pix2Pix</h2>
        <p class= "font-size:2px">This project uses locally trained Pix2Pix network to colour the sketch-book images of anime. This also converts satellite view of maps into roadmap view</p>
            <a href= "https://pix2pixstreait-0r0lag974tq.streamlit.app/">Checkout the project</a>
            <img class="small-image" src="https://streamlit.io/images/brand/streamlit-mark-color.svg"/> 
            <br/>
            <a href= "https://github.com/Afsanay/pix2pixStreamlit">Github</a>
            <img class="small-image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"/> 
        """,
        unsafe_allow_html=True
    )
    st.divider()
    st.markdown(
        """
        <h2 class = "font-size:5px">DcGAN</h2>
        <p class= "font-size:2px">This project uses locally trained DCGAN network to generate coloured anime faces.</p>
            <a href= "https://projectgan-kmzr9m9gnsb.streamlit.app/">Checkout the project</a>
            <img class="small-image" src="https://streamlit.io/images/brand/streamlit-mark-color.svg"/> 
            <br/>
            <a href= "https://github.com/Afsanay/ProjectGAN">Github</a>
            <img class="small-image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"/> 
        """,
        unsafe_allow_html = True
    )
    st.divider()

with st.expander("Using APIs", expanded=True):
    st.markdown(
        """
        <h2 class = "font-size:5px">GPT-PPT</h2>
        <p class= "font-size:2px">This project uses OpenAI API for text completion and text-to-image generation and uses python to generate high-quality PPTs and images</p>
            <a href= "https://gptppt-hlo827ntw7.streamlit.app/">Checkout the project</a>
            <img class="small-image" src="https://streamlit.io/images/brand/streamlit-mark-color.svg"/> 
            <br/>
            <a href= "https://github.com/Afsanay/gptppt">Github</a>
            <img class="small-image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"/> 
        """,
        unsafe_allow_html=True
    )
    st.divider()

st.info("The locally trained models have been trained for a maximum of 10-15 hrs which may or may not be sufficient for immersive results")












