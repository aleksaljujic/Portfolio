import streamlit as st
from streamlit import config as _config
from PIL import Image
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path()

css_file = current_dir / "styles" / "style.css"
cv_file = current_dir / "assets" / "Aleksa Ljujic CV.pdf"
profile_image = current_dir / "assets" / "Aleksa Ljujic.png"



# Load CSS
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(cv_file, "rb") as pdf_file:
    PDFbytes = pdf_file.read()
profile_image = Image.open(profile_image)


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
    menu_options = [
        "About",
        "Experience",
        "Relevant Projects",
        "Student Organizations",
        "Skills",
        "Contact"
    ]
    
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
    st.write("\n")
    st.write("\n")
    st.title("Student Organizations")
    st.markdown("---") 
    st.markdown("### FONIS *(2022 - Present)*")
    import streamlit as st

    # Section 1: Companies to Students (C2S)
    st.markdown("**Companies to Students (C2S)**")
    st.markdown("*Human Resources team member*")
    st.markdown("> **What I did:**")
    st.markdown("- `Organization and management of selection processes for project delegates`")
    st.markdown("- `Conducting internal trainings and workshops for organization members`")
    st.markdown("- `Monitoring member development and satisfaction through feedback sessions`")
    st.markdown("- `Organizing team events and team-building activities`")
    st.markdown("---")  # Separator

    # Section 2: Students to Students (S2S) - Design Team
    st.markdown("**Students to Students (S2S)**")
    st.markdown("*Design team member*")
    st.markdown("> **What I did:**")
    st.markdown("- `Creation of visual identity for events and projects`")
    st.markdown("- `Design of promotional materials (posters, brochures, social media content)`")
    st.markdown("- `Work with tools like Adobe Photoshop, Illustrator and Figma`")
    st.markdown("- `Collaboration with PR team on visual content`")
    st.markdown("---")  # Separator

    # Section 3: Hackathon for High School Students (HZS) - Logistics Team
    st.markdown("**Hackathon for High School Students (HZS)**")
    st.markdown("*Logistics team member*")
    st.markdown("> **What I did:**")
    st.markdown("- `Event organization (venue, technical equipment, logistical support)`")
    st.markdown("- `Coordination with partners and sponsors regarding event needs`")
    st.markdown("- `Budget management and material procurement for projects`")
    st.markdown("- `Solving unexpected problems during events`")
    st.markdown("---")  # Separator

    # Section 4: Students to Students (S2S) - Corporate Relations Team
    st.markdown("**Students to Students (S2S)**")
    st.markdown("*Corporate Relations team member*")
    st.markdown("> **What I did:**")
    st.markdown("- `Communication with companies and potential sponsors`")
    st.markdown("- `Writing and sending partnership and sponsorship proposals`")
    st.markdown("- `Organization of guest lectures and workshops with companies`")
    st.markdown("---")  # Separator
    # Section Title
    st.markdown("### Student Organization: Student Union – Faculty of Organizational Sciences (2023 – 2024)")

    # Role and Projects
    st.markdown("> **IT & Design Team Member**")
    st.markdown("Projects worked on:")
    st.markdown("- Practice Day")
    st.markdown("- GreenWay")
    st.markdown("- Sport Bizz")
    st.markdown("- KSON")

    # What I Did
    st.markdown("> **What I did:**")
    st.markdown("- `Created visual identities for various events and projects`")
    st.markdown("- `Designed promotional materials (posters, brochures, and social media content)`")
    st.markdown("- `Utilized tools like Adobe Photoshop, Illustrator, and Figma for design work`")
    st.markdown("- `Collaborated with the PR team to develop visual content for campaigns`")


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
    st.write("- **Phone**: +381 60333 4933")
    st.write("- **Email**: [aleksa.ljujic2@gmail.com](mailto:aleksa.ljujic2@gmail.com)")
    st.write("- **LinkedIn**: [https://www.linkedin.com/in/aleksaljujic](https://www.linkedin.com/in/aleksaljujic)")
    st.write("- **GitHub**: [https://github.com/aleksaljujic](https://github.com/aleksaljujic)")
    st.write("- **A-GPT**: [https://aleksa-gpt.streamlit.app](https://aleksa-gpt.streamlit.app)")
