import streamlit as st

# Page Config
st.set_page_config(
    page_title="Keti Pavan Kumar | Portfolio",
    page_icon="💻",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
pages = ["About Me", "Education", "Skills", "Projects", "Certifications", "Resume", "Contact"]
choice = st.sidebar.radio("Go to", pages)

# Profile Section (Common Header)
try:
    st.image("profile.jpg", width=180)
except:
    st.warning("Profile photo not found. Please upload 'profile.jpg'.")
  # <-- replace with your actual photo
st.title("👨‍💻 Keti Pavan Kumar")
st.markdown("**Computer Science Student | Artificial Intelligence & Machine Learning Enthusiast**")
st.markdown("📍 Medchal, Hyderabad 500010 | 📧 [umarpavan768@gmail.com](mailto:umarpavan768@gmail.com) | 📞 +91 7569343025")

# Light/Dark theme toggle
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("<style>body{background-color: #0E1117; color: white;}</style>", unsafe_allow_html=True)

# About Me Page
if choice == "About Me":
    st.header("🌟 About Me")
    st.write("""
    Passionate and driven computer science student with a focus on Artificial Intelligence and Machine Learning. 
    Eager to secure an internship or entry-level role to apply analytical skills, programming proficiency, 
    and a dedication to uncovering insights from data. 
    """)

# Education Page
elif choice == "Education":
    st.header("🎓 Education")
    st.write("**Malla Reddy University**, Hyderabad – B.Tech CSE (AI & ML) | CGPA: 7.64/10 | Pursuing 4th Semester")
    st.write("**Excellencia Junior College**, Hyderabad – GPA: 7.3/10 | Graduated: 2022")
    st.write("**Shantiniketan Vidyalaya**, Hyderabad – SSC: 70% | Graduated: 2020")

# Skills Page
elif choice == "Skills":
    st.header("💻 Skills")
    st.write("- **Programming**: Python (NumPy, Pandas), Java, JavaScript, HTML, CSS, TypeScript")
    st.write("- **Databases**: MySQL")
    st.write("- **Machine Learning**: Regression, Classification, Clustering, NLP, Deep Learning (YOLOv3)")
    st.write("- **Cloud & DevOps**: AWS, Terraform")
    st.write("- **Tools**: Node.js, OpenCV")
    st.write("- **Core Competencies**: Design & Analytical Abilities, Problem-Solving, Communication, Presentation Skills")

# Projects Page
elif choice == "Projects":
    st.header("📂 Projects")
    st.subheader("1. Bank Loan Eligibility Prediction")
    st.write("Built ML models (Logistic Regression, Random Forest, XGBoost) to predict loan approvals.")
    st.subheader("2. Da Vinci DriveAI: Autonomous Vehicle Vision")
    st.write("Implemented real-time obstacle detection using YOLOv3 for autonomous vehicles.")
    st.subheader("3. NLP Text Summarizer")
    st.write("Created a web app for extractive & abstractive summarization using NLP libraries.")

# Certifications Page
elif choice == "Certifications":
    st.header("🏆 Certifications & Achievements")
    st.write("- AWS Academy: Generative AI Foundations, Cloud Operations, Cloud Foundations")
    st.write("- NPTEL: Programming in Java")
    st.write("- Internship: YBI Foundation – 2 Weeks (Python Programming)")
    st.write("- Award: First Place, Intellithon 2024 (AI Project Expo)")
    st.write("- Hackathon: QUANTANOVA V1 2025 (Participation Certificate)")

# Resume Page
elif choice == "Resume":
    st.header("📄 Resume")
    try:
        with open("resume.pdf", "rb") as pdf_file:   # <-- replace with your actual resume
            PDFbyte = pdf_file.read()
        st.download_button(label="📥 Download My Resume",
                           data=PDFbyte,
                           file_name="Keti_Pavan_Kumar_Resume.pdf",
                           mime="application/pdf")
    except FileNotFoundError:
        st.error("Resume file not found. Please upload resume.pdf to the project folder.")

# Contact Page
elif choice == "Contact":
    st.header("📞 Contact")
    st.write("📍 Medchal, Hyderabad 500010")
    st.write("📧 [umarpavan768@gmail.com](mailto:umarpavan768@gmail.com)")
    st.write("📞 +91 7569343025")
    st.markdown("🌐 [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")  # <-- Add your links
