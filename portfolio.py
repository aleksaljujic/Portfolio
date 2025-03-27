import streamlit as st

# Page configuration
st.set_page_config(page_title="Aleksa Ljujić - Portfolio", layout="wide")

# Initialize session state for menu selection
if 'menu' not in st.session_state:
    st.session_state.menu = "About"

# Sidebar menu
st.sidebar.image("C:\\Users\\aleks\\Aleksa Portfolio\\Aelksa Ljujić.png", use_column_width=True)
st.sidebar.markdown("### Navigate")

# Menu options
menu_options = {
    "About": "About",
    "Experience": "Experience",
    "Relevant Projects": "Relevant Projects",
    "Student Organizations": "Student Organizations",
    "Skills": "Skills",
    "Contact": "Contact",
}

# Create full-width buttons in sidebar
for option, section in menu_options.items():
    btn_col, _ = st.sidebar.columns([3, 1])
    if btn_col.button(option, key=section, use_container_width=True):
        st.session_state.menu = section

# Add some spacing
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Content for each menu section using session state
if st.session_state.menu == "About":
    st.title("About Me")
    st.write("""
    I am a fourth-year student at the Faculty of Organizational Sciences, majoring
    in Information Systems and Technologies. With a deep passion for artificial
    intelligence and machine learning, I am driven by their transformative
    potential to solve complex problems, uncover valuable insights, and shape the
    future of technology.My goal is to become a highly skilled professional in AI
    and ML, leveraging innovative solutions to tackle real-world challenges and
    contribute meaningfully to technological advancement. I am eager to
    collaborate, learn, and continuously push the boundaries of what these
    technologies can achieve
    """)

elif st.session_state.menu == "Experience":
    st.title("Experience")
    st.subheader("Integration Architect Internship")
    st.write("- **Company**: STADA GIS Serbia")
    st.write("- **Duration**: February 2023 - August 2024")
    st.write("""
    - Acquired foundational knowledge of SAP environments and ERP systems.
    - Gained experience in Enterprise Architecture, design principles, and planning.
    - Worked with LeanIX for data quality, Power BI for analytics, and SAP Integration Suite.
    - Participated in projects like SAP Trading Partner Management and API Management.
    """)

elif st.session_state.menu == "Relevant Projects":
    st.title("Relevant Projects")
    projects = [
        {
            "name": "Intelligent Weather Prediction using Neural Networks",
            "technologies": "PyTorch, Pandas, NumPy",
            "description": "Designed and implemented a neural network model to predict mean temperatures based on historical weather data."
        },
        {
            "name": "Student Performance Predictor",
            "technologies": "Jupyter Notebook, Pandas, NumPy, Scikit-learn",
            "description": "Developed a machine learning model to forecast student exam outcomes using predictive analytics."
        },
        {
            "name": "Pharmacy Billing System",
            "technologies": ".NET, SQL Management Studio",
            "description": "Created a local server-client application to streamline pharmacy billing."
        },
        {
            "name": "Multiplayer Air Hockey Game",
            "technologies": "Unity, C#, Photon",
            "description": "Developed a real-time multiplayer air hockey game featuring smooth networking and responsive gameplay."
        },
        {
            "name": "Aleksa GPT",
            "technologies": "Python, Streamlit, OpenAI API",
            "description": "Built a Streamlit application based on my CV to provide precise answers about my experience."
        },
    ]
    for project in projects:
        st.subheader(project["name"])
        st.write(f"**Technologies**: {project['technologies']}")
        st.write(project["description"])

# Student Organizations Section
elif st.session_state.menu == "Student Organizations":
    st.title("Student Organizations")
    st.title("**FONIS** (2022 – Present)")
    st.write(""" 
Companies to Students (C2S) (2022 – 2023) Human Resources team member
- Organization and management of selection processes for project delegates
- Conducting internal trainings and workshops for organization members
- Monitoring member development and satisfaction through feedback sessions
- Organizing team events and team-building activities
--------------------------------   
Students to Students (S2S) (2022 – 2023) Design team member
- Creation of visual identity for events and projects
- Design of promotional materials (posters, brochures, social media content)
- Work with tools like Adobe Photoshop, Illustrator and Figma
- Collaboration with PR team on visual content
--------------------------------
Hackathon for High School Students (HZS) (2022 – 2023) Logistics team member
- Event organization (venue, technical equipment, logistical support)
- Coordination with partners and sponsors regarding event needs
- Budget management and material procurement for projects
- Solving unexpected problems during events
--------------------------------
Students to Students (S2S) (2022 – 2023) Corporate Relations team member
- Communication with companies and potential sponsors
- Writing and sending partnership and sponsorship proposals
- Organization of guest lectures and workshops with companies
- Design (S2S)
- Logistics (HZS)
- Corporate relations (S2S)

2) Student organization Student Union – Faculty of Organizational Sciences (2023 – 2024)  
IT & Design Team member for Projects like Practice Day, GreenWay, Sport Bizz, KSON
What I did:
- Creation of visual identity for events and projects
- Design of promotional materials (posters, brochures, social media content)
- Work with tools like Adobe Photoshop, Illustrator and Figma
- Collaboration with PR team on visual content.
    """)
    st.title("**Student organization Student Union** – Faculty of Organizational Sciences (2023 – 2024)")
    st.write(""" 
IT & Design Team member for Projects like Practice Day, GreenWay, Sport Bizz, KSON
What I did:
- Creation of visual identity for events and projects
- Design of promotional materials (posters, brochures, social media content)
- Work with tools like Adobe Photoshop, Illustrator and Figma
- Collaboration with PR team on visual content.
    - **Student Union, Faculty of Organizational Sciences (2023-2024)**: Contributed to IT and Design for DP, GreenWay, Sport Bizz, and KSON events.
    """)

# Skills Section
elif st.session_state.menu == "Skills":
    st.title("Skills")
    st.write("- **Programming**: Java, C#, Python, C, SQL")
    st.write("- **Web Development**: HTML, CSS, JavaScript")
    st.write("- **Data Science & AI**: PyTorch, Scikit-learn, Pandas, Tableau")
    st.write("- **Database Management**: SQL, Database Design")
    st.write("- **Networking & Architecture**: Computer Networking, SAP, LeanIX")
    st.write("- **Software & Tools**: Adobe Photoshop, Illustrator, Word, Excel, PowerPoint")
    st.write("- **Soft Skills**: Critical Thinking, Problem-Solving, Time Management, Communication")

# Contact Section
elif st.session_state.menu == "Contact":
    st.title("Contact")
    st.write("Feel free to reach out to me:")
    st.write("- 📞 +381 60333 4933")
    st.write("- 📧 [aleksa.ljujic2@gmail.com](mailto:aleksa.ljujic2@gmail.com)")
    st.write("- [LinkedIn](https://www.linkedin.com/in/aleksaljujic)")
    st.write("- [GitHub](https://github.com/aleksaljujic)")
    st.write("- [A-GPT](https://aleksa-gpt.streamlit.app)")

# Footer
st.write("Thank you for visiting my portfolio!")
