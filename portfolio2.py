import streamlit as st
from streamlit import config as _config
from PIL import Image
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path()

css_file = current_dir / "styles" / "style2.css"
cv_file = current_dir / "assets" / "Aleksa Ljujić CV.pdf"
profile_image = current_dir / "assets" / "Aleksa Ljujic.png"



# Load CSS
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(cv_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_image = Image.open(profile_image)


def download_cv():
    st.download_button(
        label="Download CV",
        data=PDFbyte,
        file_name=cv_file.name,
        mime="application/octet-stream",
    )



col1,col2 = st.columns([4,1])

with col2:
    # Initialize session states
    if 'menu' not in st.session_state:
        st.session_state.menu = "About"
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False

    # Apply theme immediately when app starts
    _config.set_option(
        "theme.base", 
        "dark" if st.session_state.dark_mode else "light"
    )

    # Sidebar setup
        # Theme toggle - must be the first element
    new_theme = st.toggle(
        "☀️/🌑",
        value=st.session_state.dark_mode,
        key="theme_switch"
    )

    # Update theme if toggle changed
    if new_theme != st.session_state.dark_mode:
        st.session_state.dark_mode = new_theme
        _config.set_option(
            "theme.base", 
            "dark" if st.session_state.dark_mode else "light"
        )
        
        st.rerun()  # Force refresh to apply theme

col2,col3 = st.columns([1,1])

with col2:
    # Profile image
    st.image(profile_image,width=200)

with col3:
    st.title("Aleksa Ljujic")
    st.subheader("*Data Scientist*")
    st.write("- [Email](mailto:aleksa.ljujic2@gmail.com)")
    st.write("- [LinkedIn](https://www.linkedin.com/in/aleksaljujic)")
    st.write("- [GitHub](https://github.com/aleksaljujic)")


# menu_options = {
#     "About": "https://aleksaportfolioo.streamlit.app/~/+/#about-me",
#     "Experience": "https://aleksaportfolioo.streamlit.app/~/+/#experience",
#     "Projects": "https://aleksaportfolioo.streamlit.app/~/+/#relevant-projects",
#     "Organizations": "https://aleksaportfolioo.streamlit.app/~/+/#student-organizations",
#     "Skills": "https://aleksaportfolioo.streamlit.app/~/+/#skills"
# }



# cols = st.columns(len(menu_options))

# for i, (desc, link) in enumerate(menu_options.items()):
#     with cols[i]:
#         st.markdown(f"[{desc}]({link})", unsafe_allow_html=True)
# # Navigation menu using a selectbox'



st.markdown("<br>", unsafe_allow_html=True)

# Content for each menu section using session state
#st.write("---")
st.title("About Me")
st.write("\n")
st.info("""
    `I am a fourth-year student at the Faculty of Organizational Sciences, majoring
    in Information Systems and Technologies. With a deep passion for artificial
    intelligence and machine learning, I am driven by their transformative
    potential to solve complex problems, uncover valuable insights, and shape the
    future of technology.`

    `My goal is to become a highly skilled professional in AI and ML, leveraging
    innovative solutions to tackle real-world challenges and contribute meaningfully
    to technological advancement. I am eager to collaborate, learn, and continuously
    push the boundaries of what these technologies can achieve.`
""")

download_cv()

st.write("---")
st.title("Experience")
st.markdown("Integration Architect Internship")
st.write("**Company**: [STADA GIS Serbia](https://www.stadagisserbia.com/sr)")
st.write("**Duration**: February 2023 - August 2024")
st.write(">*What I learned:*")
st.markdown("- `Acquired foundational knowledge of SAP environments and ERP systems.`")
st.markdown("- `Gained experience in Enterprise Architecture, design principles, and planning.`")
st.markdown("- `Worked with LeanIX for data quality, Power BI for analytics, and SAP Integration Suite.`")
st.markdown("- `Participated in projects like SAP Trading Partner Management and API Management.`")

#Relevant Projects Section
st.write("---")
st.title("Relevant Projects")
st.write("\n")
projects = [
    {
        "name": "Intelligent Weather Prediction using Neural Networks",
        "technologies":"`PyTorch, Pandas, NumPy`",
        "github":"[link](link.com)",
        "description": "*Designed and implemented a neural network model to predict mean temperatures based on historical weather data.*"
    },
    {
        "name": "Student Performance Predictor",
        "technologies": "`Jupyter Notebook, Pandas, NumPy, Scikit-learn`",
        "github":"[link](link.com)",
        "description": "*Developed a machine learning model to forecast student exam outcomes using predictive analytics.*"
    },
    {
        "name": "Aleksa GPT",
        "technologies": "`Python, Streamlit, OpenAI API`",
        "github":"[Aleksa GPT](https://aleksa-gpt.streamlit.app)",
        "description": "*Built a Streamlit application based on my CV to provide precise answers about my experience.*"
    },
    {
        "name": "Pharmacy Billing System",
        "technologies": "`.NET, SQL Management Studio`",
        "github":"[link](link.com)",
        "description": "*Created a local server-client application to streamline pharmacy billing.*"
    },
    {
        "name": "Multiplayer Air Hockey Game",
        "technologies": "`Unity, C#, Photon`",
        "github":"[link](link.com)",
        "description": "*Developed a real-time multiplayer air hockey game featuring smooth networking and responsive gameplay.*"
    },
]
for project in projects:
    st.write("\n")
    st.subheader(project["name"])
    st.write(f"**Technologies**: {project['technologies']}")
    st.write(project["description"])
    st.write(f"**See more on**: {project['github']}")

# Student Organizations Section
st.markdown("---") 
st.title("Student Organizations")
st.write("\n")
st.markdown("### FONIS *(2022 - Present)*")
import streamlit as st

st.markdown("Projects I worked on:")
# Section 1: Companies to Students (C2S)
st.markdown("**Companies to Students (C2S)** - `Human Resources team member`")
st.markdown("**Students to Students (S2S)** - `Design team member`")
st.markdown("**Hackathon for High School Students (HZS)** - `Logistics team member`")
st.markdown("**Students to Students (S2S)** - `Corporate Relations team member`")
st.write("\n")
# Section Title
st.markdown("### Student Union Faculty of Organizational Sciences (2023 – 2024)")
st.markdown("Projects I worked on:")
# Role and Projects
st.markdown("**Practice Day** - `IT & Design Team Member`")
st.markdown("**GreenWay** - `IT & Design Team Member`")
st.markdown("**Sport Bizz** - `IT & Design Team Member`")
st.markdown("**KSON** - `IT & Design Team Member`")


# Skills Section

st.write("---")
st.title("Skills")
st.write("\n")
st.write("- **Programming**: `Java, C#, Python, C, SQL`")
st.write("- **Web Development**: `HTML, CSS, JavaScript`")
st.write("- **Data Science & AI**: `PyTorch, Scikit-learn, Pandas, Tableau`")
st.write("- **Database Management**: `SQL, Database Design`")
st.write("- **Networking & Architecture**: `Computer Networking, SAP, LeanIX`")
st.write("- **Software & Tools**: `Adobe Photoshop, Illustrator, Word, Excel, PowerPoint`")
st.write("- **Soft Skills**: `Critical Thinking, Problem-Solving, Time Management, Communication`")
