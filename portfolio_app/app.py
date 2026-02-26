import streamlit as st
from pathlib import Path

# Page Config
st.set_page_config(
    page_title="Keti Pavan Kumar | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----- Global Styles -----
st.markdown(
    """
    <style>
    .main > div {
        padding-top: 4.8rem;
        padding-bottom: 3rem;
    }

    /* Hide Streamlit header/menu */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}

    /* Top Navigation */
    .top-nav {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(14, 17, 23, 0.95);
        backdrop-filter: blur(8px);
        border-bottom: 1px solid #2d2f36;
        padding: 0.85rem 1.2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .brand {
        color: #ffffff;
        font-weight: 700;
        font-size: 1rem;
        letter-spacing: 0.3px;
    }
    .nav-links {
        display: flex;
        gap: 0.9rem;
        flex-wrap: wrap;
        justify-content: flex-end;
    }
    .nav-links a, .drawer-links a {
        color: #d8deea;
        text-decoration: none;
        font-size: 0.92rem;
        padding: 0.35rem 0.55rem;
        border-radius: 6px;
    }
    .nav-links a:hover, .drawer-links a:hover {
        background: #202532;
        color: #ffffff;
    }

    /* Hamburger */
    #drawer-toggle {display: none;}
    .hamburger {
        display: none;
        cursor: pointer;
        color: white;
        font-size: 1.4rem;
        line-height: 1;
    }

    .mobile-drawer {
        display: none;
        position: fixed;
        top: 56px;
        right: 0;
        width: 72%;
        max-width: 280px;
        z-index: 999;
        background: #11141c;
        border-left: 1px solid #2d2f36;
        border-bottom: 1px solid #2d2f36;
        box-shadow: -4px 6px 20px rgba(0,0,0,0.25);
        padding: 0.8rem;
    }
    .drawer-links {
        display: flex;
        flex-direction: column;
        gap: 0.35rem;
    }

    /* Hero */
    .hero-card {
        padding: 1.4rem;
        border: 1px solid #2d2f36;
        border-radius: 14px;
        background: linear-gradient(145deg, #10131a, #151a24);
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        color: #bac4d7;
        margin-bottom: 0.4rem;
    }

    /* Persistent socials */
    .social-fixed {
        position: fixed;
        left: 14px;
        top: 42%;
        transform: translateY(-50%);
        z-index: 900;
        display: flex;
        flex-direction: column;
        gap: 0.45rem;
    }
    .social-fixed a {
        text-decoration: none;
        color: white;
        font-size: 0.85rem;
        background: #1d2330;
        border: 1px solid #333a49;
        border-radius: 999px;
        padding: 0.4rem 0.6rem;
    }

    /* Footer */
    .footer-wrap {
        margin-top: 2rem;
        padding-top: 1.2rem;
        border-top: 1px solid #2d2f36;
        color: #b4bfd3;
        font-size: 0.9rem;
    }

    /* Mobile quick actions */
    .mobile-quick-actions {
        position: fixed;
        bottom: 14px;
        right: 14px;
        z-index: 1000;
        display: none;
        flex-direction: column;
        gap: 0.5rem;
    }
    .mobile-quick-actions a {
        text-decoration: none;
        color: white;
        background: #1b2333;
        border: 1px solid #3a4a67;
        border-radius: 999px;
        padding: 0.5rem 0.8rem;
        font-size: 0.82rem;
    }

    @media (max-width: 900px) {
        .nav-links {display: none;}
        .hamburger {display: inline-block;}
        #drawer-toggle:checked ~ .mobile-drawer {display: block;}
        .social-fixed {display: none;}
        .mobile-quick-actions {display: flex;}
        .main > div {padding-top: 4.6rem;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----- Fixed Nav + Drawer -----
st.markdown(
    """
    <div class="top-nav">
      <div class="brand">Keti Pavan Kumar</div>
      <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#certificates">Certificates</a>
        <a href="#achievements">Achievements</a>
        <a href="#contact">Contact</a>
      </div>
      <label for="drawer-toggle" class="hamburger">☰</label>
    </div>
    <input id="drawer-toggle" type="checkbox" />
    <div class="mobile-drawer">
      <div class="drawer-links">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#certificates">Certificates</a>
        <a href="#achievements">Achievements</a>
        <a href="#contact">Contact</a>
      </div>
    </div>

    <div class="social-fixed">
      <a href="https://github.com" target="_blank">GitHub</a>
      <a href="https://linkedin.com" target="_blank">LinkedIn</a>
      <a href="mailto:umarpavan768@gmail.com">Email</a>
    </div>

    <div class="mobile-quick-actions">
      <a href="#contact">Contact</a>
      <a href="/resume.pdf" target="_blank">Resume</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----- Paths -----
BASE_DIR = Path(__file__).parent
PROFILE_IMAGE = BASE_DIR / "img.jpg"
RESUME_FILE = BASE_DIR / "resume.pdf"

# ----- Hero / Home -----
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-card">', unsafe_allow_html=True)

c1, c2 = st.columns([1.2, 2.2])
with c1:
    if PROFILE_IMAGE.exists():
        st.image(str(PROFILE_IMAGE), width=220)
    else:
        st.info("Profile image missing. Upload `img.jpg` to show your photo.")

with c2:
    st.title("👨‍💻 Keti Pavan Kumar")
    st.markdown("<p class='hero-subtitle'><b>Computer Science Student | Artificial Intelligence & Machine Learning Enthusiast</b></p>", unsafe_allow_html=True)
    st.write("📍 Medchal, Hyderabad 500010")
    st.write("📧 umarpavan768@gmail.com | 📞 +91 7569343025")

    b1, b2 = st.columns([1, 1])
    with b1:
        st.markdown("[🚀 View Projects](#projects)")
    with b2:
        try:
            with open(RESUME_FILE, "rb") as pdf_file:
                st.download_button(
                    label="📥 Download Resume",
                    data=pdf_file.read(),
                    file_name="Keti_Pavan_Kumar_Resume.pdf",
                    mime="application/pdf",
                )
        except FileNotFoundError:
            st.info("Resume file missing. Upload `resume.pdf` to enable download.")

st.markdown('</div>', unsafe_allow_html=True)

# ----- About -----
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.header("🌟 About")
st.write(
    """
    Passionate and driven computer science student with a focus on Artificial Intelligence and Machine Learning.
    Eager to secure an internship or entry-level role to apply analytical skills, programming proficiency,
    and a dedication to uncovering insights from data.
    """
)

# ----- Skills -----
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.header("💻 Skills")
st.write("- **Programming**: Python (NumPy, Pandas), Java, JavaScript, HTML, CSS, TypeScript")
st.write("- **Databases**: MySQL")
st.write("- **Machine Learning**: Regression, Classification, Clustering, NLP, Deep Learning (YOLOv3)")
st.write("- **Cloud & DevOps**: AWS, Terraform")
st.write("- **Tools**: Node.js, OpenCV")
st.write("- **Core Competencies**: Problem-Solving, Communication, Presentation Skills")

# ----- Projects -----
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.header("📂 Projects")
st.subheader("1. Bank Loan Eligibility Prediction")
st.write("Built ML models (Logistic Regression, Random Forest, XGBoost) to predict loan approvals.")
st.subheader("2. Da Vinci DriveAI: Autonomous Vehicle Vision")
st.write("Implemented real-time obstacle detection using YOLOv3 for autonomous vehicles.")
st.subheader("3. NLP Text Summarizer")
st.write("Created a web app for extractive & abstractive summarization using NLP libraries.")

# ----- Certificates -----
st.markdown('<div id="certificates"></div>', unsafe_allow_html=True)
st.header("🏆 Certificates")
st.write("- AWS Academy: Generative AI Foundations, Cloud Operations, Cloud Foundations")
st.write("- NPTEL: Programming in Java")
st.write("- Internship: YBI Foundation – 2 Weeks (Python Programming)")
st.write("- Hackathon: QUANTANOVA V1 2025 (Participation Certificate)")

# ----- Achievements -----
st.markdown('<div id="achievements"></div>', unsafe_allow_html=True)
st.header("🥇 Achievements")
st.write("- First Place, Intellithon 2024 (AI Project Expo)")

# ----- Contact -----
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.header("📞 Contact")
st.write("📍 Medchal, Hyderabad 500010")
st.write("📧 [umarpavan768@gmail.com](mailto:umarpavan768@gmail.com)")
st.write("📞 +91 7569343025")
st.markdown("🌐 [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")

# ----- Footer -----
st.markdown(
    """
    <div class="footer-wrap">
      <div><b>Contact:</b> umarpavan768@gmail.com | +91 7569343025</div>
      <div><b>Policies:</b> Privacy Policy (placeholder) | Terms of Service (placeholder)</div>
      <div>© 2026 Keti Pavan Kumar. All rights reserved.</div>
    </div>
    """,
    unsafe_allow_html=True,
)
