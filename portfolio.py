import streamlit as st
from streamlit import config as _config
from PIL import Image
from pathlib import Path
import os

current_dir = Path(__file__).parent if "__file__" in locals() else Path()


css_file = current_dir / "portfolio1"/ "styles" / "style.css"
cv_file = current_dir / "portfolio1"/ "assets" / "Aleksa Ljujić CV.pdf"
profile_image = current_dir / "portfolio1"/ "assets" / "Aleksa Ljujic.png"



# Load CSS
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(cv_file, "rb") as pdf_file:
    PDFbytes = pdf_file.read()
profile_image = Image.open(profile_image)

if os.path.exists(cv_file):
    os.chmod(cv_file, 0o777)  # Give full permissions


def download_cv(label):
    st.download_button(
        label=label,
        data=PDFbytes,
        file_name=cv_file.name,
        mime="application/octet-stream",
    )

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
with st.sidebar:
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
    
    # Profile image
    st.image(profile_image, width=200)
    
    # Navigation menu using a selectbox
    # Menu options
    menu_options = {
        "About": "About",
        "Experience": "Experience",
        "Relevant Projects": "Relevant Projects",
        "Student Organizations": "Student Organizations",
        "Skills": "Skills",
        "Contact": "Contact",
    }

    for option, section in menu_options.items():
     btn_col, _ = st.sidebar.columns([3, 1])
     if btn_col.button(option, key=section, use_container_width=True):
         st.session_state.menu = section
    
    st.markdown("<br>", unsafe_allow_html=True)

# Content for each menu section using session state
if st.session_state.menu == "About":
    st.write("\n")
    st.write("\n")
    st.title("About Me")
    st.write("---")
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

    download_cv("Download CV")

elif st.session_state.menu == "Experience":
    st.write("\n")
    st.write("\n")
    st.title("Experience")
    st.write("---")
    st.markdown("Integration Architect Internship")
    st.write("**Company**: [STADA GIS Serbia](https://www.stadagisserbia.com/sr)")
    st.write("**Duration**: February 2023 - August 2024")
    st.write(">*What I learned:*")
    st.markdown("- `Acquired foundational knowledge of SAP environments and ERP systems.`")
    st.markdown("- `Gained experience in Enterprise Architecture, design principles, and planning.`")
    st.markdown("- `Worked with LeanIX for data quality, Power BI for analytics, and SAP Integration Suite.`")
    st.markdown("- `Participated in projects like SAP Trading Partner Management and API Management.`")

elif st.session_state.menu == "Relevant Projects":
    st.write("\n")
    st.write("\n")
    st.title("Relevant Projects")
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
            "github":"[link](link.com)",
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
        st.write("---")
        st.subheader(project["name"])
        st.write(f"**Technologies**: {project['technologies']}")
        st.write(project["description"])
        st.write(f"**See more on**: {project['github']}")

# Student Organizations Section
elif st.session_state.menu == "Student Organizations":
    # Student Organizations Section
    st.write("\n")
    st.write("\n")
    st.title("Student Organizations")
    st.markdown("---") 
    st.markdown("### FONIS *(2022 - Present)*")
    import streamlit as st

    st.markdown("Projects I worked on:")
    # Section 1: Companies to Students (C2S)
    st.markdown("**Companies to Students (C2S)** - `Human Resources team member`")
    st.markdown("**Students to Students (S2S)** - `Design team member`")
    st.markdown("**Hackathon for High School Students (HZS)** - `Logistics team member`")
    st.markdown("**Students to Students (S2S)** - `Corporate Relations team member`")
    st.write("---")
    # Section Title
    st.markdown("### Student Union Faculty of Organizational Sciences (2023 – 2024)")
    st.markdown("Projects I worked on:")
    # Role and Projects
    st.markdown("**Practice Day** - `IT & Design Team Member`")
    st.markdown("**GreenWay** - `IT & Design Team Member`")
    st.markdown("**Sport Bizz** - `IT & Design Team Member`")
    st.markdown("**KSON** - `IT & Design Team Member`")


# Skills Section
elif st.session_state.menu == "Skills":
    st.write("\n")
    st.write("\n")
    st.title("Skills")
    st.write("---")
    st.write("- **Programming**: `Java, C#, Python, C, SQL`")
    st.write("- **Web Development**: `HTML, CSS, JavaScript`")
    st.write("- **Data Science & AI**: `PyTorch, Scikit-learn, Pandas, Tableau`")
    st.write("- **Database Management**: `SQL, Database Design`")
    st.write("- **Networking & Architecture**: `Computer Networking, SAP, LeanIX`")
    st.write("- **Software & Tools**: `Adobe Photoshop, Illustrator, Word, Excel, PowerPoint`")
    st.write("- **Soft Skills**: `Critical Thinking, Problem-Solving, Time Management, Communication`")

# Contact Section
elif st.session_state.menu == "Contact":
    st.write("\n")
    st.write("\n")
    st.title("Contact")
    st.write("---")
    st.write("`Feel free to reach out to me:`")
    st.write("\n")
    st.write("- **Email**: [aleksa.ljujic2@gmail.com](mailto:aleksa.ljujic2@gmail.com)")
    st.write("- **LinkedIn**: [https://www.linkedin.com/in/aleksaljujic](https://www.linkedin.com/in/aleksaljujic)")
    st.write("- **GitHub**: [https://github.com/aleksaljujic](https://github.com/aleksaljujic)")
    st.write("- **A-GPT**: [https://aleksa-gpt.streamlit.app](https://aleksa-gpt.streamlit.app)")
