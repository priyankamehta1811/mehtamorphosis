import streamlit as st

st.header("🎨 SciART!")

st.markdown("<div class='main-header'>Design Work</div>", unsafe_allow_html=True)
st.markdown("Explore some of my book covers and creative projects:")
    
    # Example of how you could display book covers and descriptions
st.image("https://via.placeholder.com/300x450", caption="Book Cover 1")
st.markdown("**Project Name 1**: Description of the design, inspiration, and techniques.")
    
st.image("https://via.placeholder.com/300x450", caption="Book Cover 2")
st.markdown("**Project Name 2**: Overview of the creative process and challenges faced.")

st.markdown("<div class='main-header'>Co-Curricular Activities</div>", unsafe_allow_html=True)
st.markdown("Engagement in academic and extracurricular activities has been an integral part of my growth:")
    
st.markdown("### Workshops and Seminars")
st.markdown("- **Design Thinking Workshop**: Participated in a collaborative session on design strategies.")
st.markdown("- **Science Communication Seminar**: Presented research findings and communicated complex data effectively.")
    
st.markdown("### Volunteering and Outreach")
st.markdown("- **Science Fair Mentor**: Guided students in presenting their research projects.")
st.markdown("- **Community Outreach Speaker**: Conducted talks on the importance of understanding host-pathogen interactions.")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center;'>
    © 2024 Priyanka Mehta | Ingen-hope Lab
    </p>
    """,
    unsafe_allow_html=True
)
