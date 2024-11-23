import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Coffliza's CV", page_icon="☕", layout="centered")

# Header
st.title("☕ Coffliza's CV")
st.subheader("Professional Barista & Coffee Consultant")

# Contact Information
st.write("---")
st.write("📍 **Location:** Verona, Italy")
st.write("✉️ **Email:** coffliza.barista@example.com")
st.write("📞 **Phone:** +39 345 678 9012")
st.write("---")

# Professional Summary
st.header("Professional Summary")
st.write(
    """
    Experienced barista with 15+ years in Italian coffee culture. Expert in espresso, modern brewing methods, 
    and crafting personalized coffee experiences. Passionate about storytelling and sharing coffee knowledge 
    with enthusiasts of all levels.
    """
)

# Key Skills
st.header("Key Skills")
st.markdown(
    """
    - Mastery of espresso and diverse brewing techniques.
    - Coffee bean sourcing and recipe creation.
    - Training and mentoring baristas.
    - Engaging workshops and event management.
    """
)

# Experience
st.header("Professional Experience")

st.subheader("Freelance Coffee Consultant")
st.caption("2015 – Present")
st.write(
    """
    - Advises cafés and conducts coffee workshops.
    - Creates personalized coffee recipes and experiences.
    """
)

st.subheader("Lead Barista")
st.caption("Caffè Dolce Vita | 2008 – 2015")
st.write(
    """
    - Designed coffee menus and trained baristas.
    - Led a team to deliver premium coffee services.
    """
)

st.subheader("Barista")
st.caption("Espresso Italiano | 2003 – 2008")
st.write(
    """
    - Perfected brewing techniques and customer service.
    """
)

# Education & Certifications
st.header("Education & Certifications")
st.write(
    """
    - **Certified Coffee Specialist** | Specialty Coffee Association (2012)
    - **Advanced Barista Training** | Barista Academy of Verona (2005)
    """
)

# Achievements
st.header("Achievements")
st.markdown(
    """
    - European Barista Championships Finalist (2014, 2016)
    - Judge at Italian Coffee Awards (2018 – 2022)
    """
)

# Languages
st.header("Languages")
st.markdown("**Italian** (Native), **English** (Fluent)")


