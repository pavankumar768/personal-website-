import base64
from datetime import date

import streamlit as st

st.set_page_config(
    page_title="KPavanKumar Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PRIMARY = "#1E3A8A"
SECONDARY = "#F8FAFC"
ACCENT = "#3B82F6"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}

    .stApp {{
        background:
          radial-gradient(1000px 500px at 90% -10%, rgba(59,130,246,0.18), transparent 60%),
          radial-gradient(900px 480px at -10% 5%, rgba(30,58,138,0.20), transparent 55%),
          linear-gradient(180deg, #ffffff 0%, {SECONDARY} 100%);
    }}

    .hero {{
      background: linear-gradient(120deg, {PRIMARY} 0%, #1D4ED8 55%, {ACCENT} 100%);
      border-radius: 24px;
      color: white;
      padding: 1.8rem;
      box-shadow: 0 20px 40px rgba(30,58,138,.24);
      margin-bottom: 1.2rem;
    }}

    .glass {{
      background: rgba(255,255,255,0.75);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255,255,255,0.6);
      border-radius: 18px;
      padding: 1rem;
      box-shadow: 0 8px 24px rgba(15,23,42,.08);
      height: 100%;
    }}

    .kp-chip {{
      display:inline-block;
      background:#E0E7FF;
      color:{PRIMARY};
      border-radius:999px;
      padding:0.3rem 0.75rem;
      margin:0.2rem 0.25rem 0.2rem 0;
      font-size:0.8rem;
      font-weight:600;
    }}

    .metric {{
      background: white;
      border: 1px solid #dbeafe;
      border-left: 4px solid {ACCENT};
      border-radius: 14px;
      padding: 0.8rem 1rem;
      box-shadow: 0 6px 18px rgba(2,6,23,.04);
    }}
    .section-title {{ color:{PRIMARY}; font-weight:800; letter-spacing:-0.02em; }}
    a {{ color:{ACCENT} !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

projects_seed = [
    {
        "name": "Bank Loan Eligibility Prediction",
        "category": "Machine Learning",
        "tech": ["Python", "Scikit-learn", "Pandas", "XGBoost"],
        "summary": "Predicted loan approvals using Logistic Regression, Random Forest, and XGBoost.",
        "outcome": "Improved decision support with comparative ML metrics and feature importance insights.",
        "github": "https://github.com/",
        "demo": "",
    },
    {
        "name": "Da Vinci DriveAI",
        "category": "Computer Vision",
        "tech": ["Python", "OpenCV", "YOLOv3"],
        "summary": "Real-time obstacle detection pipeline for autonomous driving scenarios.",
        "outcome": "Built a robust CV workflow with high recall in controlled test footage.",
        "github": "https://github.com/",
        "demo": "",
    },
    {
        "name": "NLP Text Summarizer",
        "category": "NLP",
        "tech": ["Python", "Transformers", "Flask"],
        "summary": "Web app for extractive and abstractive summarization.",
        "outcome": "Reduced long-read processing time with concise and context-aware summaries.",
        "github": "https://github.com/",
        "demo": "",
    },
]

cert_seed = [
    {"title": "AWS Academy - Generative AI Foundations", "org": "AWS Academy", "type": "Cloud", "date": "2024"},
    {"title": "NPTEL - Programming in Java", "org": "NPTEL", "type": "Programming", "date": "2024"},
    {"title": "Intellithon 2024 - First Place", "org": "Intellithon", "type": "Achievement", "date": "2024"},
]

if "projects" not in st.session_state:
    st.session_state.projects = projects_seed.copy()
if "certs" not in st.session_state:
    st.session_state.certs = cert_seed.copy()

st.sidebar.title("Navigation")
st.sidebar.markdown(
    "- [Home](#home)\n"
    "- [About](#about)\n"
    "- [Skills](#skills)\n"
    "- [Projects](#projects)\n"
    "- [Certificates](#certificates)\n"
    "- [Achievements](#achievements)\n"
    "- [Contact](#contact)\n"
    "- [Admin](#admin-dashboard)"
)

# Hero
st.markdown("<a id='home'></a>", unsafe_allow_html=True)
left, right = st.columns([1.2, 2.8], gap="large")
with left:
    try:
        st.image("img.jpg", width="stretch")
    except Exception:
        st.info("Add `img.jpg` in `portfolio_app/` for your headshot.")

with right:
    st.markdown(
        """
        <div class='hero'>
            <h1 style='margin:0;'>Keti Pavan Kumar</h1>
            <p style='font-size:1.05rem;opacity:.95;margin:.6rem 0;'>
                Computer Science Engineering Student • AI & ML Specialization<br/>
                Building practical intelligent systems in ML, CV, and NLP.
            </p>
            <p style='margin:0;'>📍 Hyderabad, India • ✉️ umarpavan768@gmail.com • 📞 +91 7569343025</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

resume_present = False
cta1, cta2, cta3 = st.columns(3)
with cta1:
    st.link_button("Explore Projects", "#projects", width="stretch")
with cta2:
    st.link_button("Contact Me", "#contact", width="stretch")
with cta3:
    try:
        with open("resume.pdf", "rb") as pdf:
            st.download_button(
                "Download Resume",
                data=pdf.read(),
                file_name="Keti_Pavan_Kumar_Resume.pdf",
                mime="application/pdf",
                width="stretch",
            )
        resume_present = True
    except FileNotFoundError:
        st.button("Resume Missing", disabled=True, width="stretch")

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown("<div class='metric'><b>3+</b><br/>Featured Projects</div>", unsafe_allow_html=True)
with m2:
    st.markdown("<div class='metric'><b>5+</b><br/>Certifications</div>", unsafe_allow_html=True)
with m3:
    st.markdown("<div class='metric'><b>AI/ML</b><br/>Core Specialization</div>", unsafe_allow_html=True)
with m4:
    st.markdown("<div class='metric'><b>Open</b><br/>Internship Opportunities</div>", unsafe_allow_html=True)

st.divider()

# About
st.markdown("<a id='about'></a>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>About Me</h2>", unsafe_allow_html=True)
a1, a2 = st.columns(2, gap="large")
with a1:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.write(
        "I am a passionate engineering student focused on AI and Machine Learning, seeking internship and "
        "entry-level opportunities to apply strong problem-solving, coding, and collaboration skills."
    )
    st.markdown("</div>", unsafe_allow_html=True)
with a2:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown(
        "**Education**\n"
        "- Malla Reddy University — B.Tech CSE (AI & ML), CGPA: 7.64/10\n"
        "- Excellencia Junior College — GPA: 7.3/10\n"
        "- Shantiniketan Vidyalaya — SSC: 70%"
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# Skills
st.markdown("<a id='skills'></a>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)
tech_skills = {
    "Programming": ["Python", "Java", "JavaScript", "TypeScript", "HTML", "CSS"],
    "AI/ML": ["Regression", "Classification", "Clustering", "NLP", "Deep Learning", "YOLOv3"],
    "Databases & Cloud": ["MySQL", "AWS", "Terraform"],
    "Tools": ["Node.js", "OpenCV", "Git", "Streamlit"],
    "Soft Skills": ["Communication", "Problem Solving", "Presentation", "Teamwork"],
}
cols = st.columns(2)
for idx, (group, items) in enumerate(tech_skills.items()):
    with cols[idx % 2]:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.markdown(f"**{group}**")
        st.markdown("".join([f"<span class='kp-chip'>{i}</span>" for i in items]), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# Projects
st.markdown("<a id='projects'></a>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Projects</h2>", unsafe_allow_html=True)
filter1, filter2 = st.columns([1, 2])
with filter1:
    project_categories = sorted({p["category"] for p in st.session_state.projects})
    selected_category = st.selectbox("Category", ["All"] + project_categories)
with filter2:
    project_search = st.text_input("Search", placeholder="NLP, YOLO, loan...")

filtered_projects = [
    p
    for p in st.session_state.projects
    if (selected_category == "All" or p["category"] == selected_category)
    and (
        not project_search
        or project_search.lower() in p["name"].lower()
        or project_search.lower() in p["summary"].lower()
        or any(project_search.lower() in t.lower() for t in p["tech"])
    )
]

for p in filtered_projects:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader(p["name"])
    st.caption(f"{p['category']}")
    st.write(p["summary"])
    st.write(f"**Outcome:** {p['outcome']}")
    st.markdown("".join([f"<span class='kp-chip'>{i}</span>" for i in p["tech"]]), unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("GitHub", p["github"], width="stretch")
    with c2:
        if p["demo"]:
            st.link_button("Live Demo", p["demo"], width="stretch")
        else:
            st.button("Demo Unavailable", disabled=True, key=f"{p['name']}_demo")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# Certificates
st.markdown("<a id='certificates'></a>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Certificates</h2>", unsafe_allow_html=True)
cert_types = sorted({c["type"] for c in st.session_state.certs})
selected_type = st.multiselect("Type", cert_types, default=cert_types)
cert_query = st.text_input("Search certificates", placeholder="AWS, NPTEL, achievement")

for cert in st.session_state.certs:
    matches_type = cert["type"] in selected_type if selected_type else True
    matches_query = not cert_query or any(
        cert_query.lower() in str(cert[k]).lower() for k in ["title", "org", "type", "date"]
    )
    if not (matches_type and matches_query):
        continue

    with st.expander(f"{cert['title']} • {cert['org']} ({cert['date']})"):
        st.write(f"Type: **{cert['type']}**")
        try:
            with open("resume.pdf", "rb") as f:
                pdf_data = f.read()
            b64_pdf = base64.b64encode(pdf_data).decode("utf-8")
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="420"></iframe>',
                unsafe_allow_html=True,
            )
            st.download_button(
                "Download PDF",
                data=pdf_data,
                file_name=f"{cert['title'].replace(' ', '_')}.pdf",
                mime="application/pdf",
                key=f"{cert['title']}_download",
            )
        except FileNotFoundError:
            st.warning("Add certificate PDFs via Supabase Storage/local folder.")

st.divider()

# Achievements
st.markdown("<a id='achievements'></a>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Achievements</h2>", unsafe_allow_html=True)
achievements = [
    (date(2025, 1, 20), "QUANTANOVA V1 Hackathon", "Participation Certificate"),
    (date(2024, 7, 4), "Intellithon AI Project Expo", "Secured First Place"),
    (date(2024, 3, 15), "YBI Foundation Internship", "Completed Python internship (2 weeks)"),
]
for d, event, detail in sorted(achievements, reverse=True):
    st.markdown(f"- **{d.strftime('%b %Y')}** — {event}: {detail}")

st.divider()

# Contact
st.markdown("<a id='contact'></a>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Contact</h2>", unsafe_allow_html=True)
with st.form("contact_form", clear_on_submit=True):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Name*")
        email = st.text_input("Email*")
    with c2:
        subject = st.text_input("Subject*")
        phone = st.text_input("Phone")
    message = st.text_area("Message*")
    submitted = st.form_submit_button("Send Message")

if submitted:
    if not (name and email and subject and message):
        st.error("Please fill all required fields.")
    else:
        st.success("Thanks! Message captured. Connect EmailJS/Supabase edge function to send emails.")

st.markdown("GitHub: https://github.com/  ")
st.markdown("LinkedIn: https://linkedin.com/")
if resume_present:
    st.caption("Resume is available in the hero section.")

st.divider()

# Admin
st.markdown("<a id='admin-dashboard'></a>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title'>Admin Dashboard (Demo)</h2>", unsafe_allow_html=True)
admin_token = st.text_input("Admin Access Key", type="password")

if admin_token and admin_token == "admin123":
    st.success("Admin access granted")
    t1, t2 = st.tabs(["Add Project", "Add Certificate"])

    with t1:
        with st.form("add_project"):
            pname = st.text_input("Project Name")
            pcat = st.text_input("Category")
            psummary = st.text_area("Summary")
            poutcome = st.text_area("Outcome")
            ptech = st.text_input("Technologies (comma separated)")
            pgit = st.text_input("GitHub URL")
            pdemo = st.text_input("Demo URL")
            psubmit = st.form_submit_button("Add Project")
        if psubmit and pname and pcat:
            st.session_state.projects.append(
                {
                    "name": pname,
                    "category": pcat,
                    "tech": [t.strip() for t in ptech.split(",") if t.strip()],
                    "summary": psummary,
                    "outcome": poutcome,
                    "github": pgit or "https://github.com/",
                    "demo": pdemo,
                }
            )
            st.success("Project added for current session.")

    with t2:
        with st.form("add_certificate"):
            ctitle = st.text_input("Certificate Title")
            corg = st.text_input("Issuing Organization")
            ctype = st.text_input("Type")
            cdate = st.text_input("Issue Date")
            csubmit = st.form_submit_button("Add Certificate")
        if csubmit and ctitle and corg:
            st.session_state.certs.append(
                {"title": ctitle, "org": corg, "type": ctype or "General", "date": cdate or "N/A"}
            )
            st.success("Certificate added for current session.")
else:
    st.info("Enter valid admin key to manage content.")

st.caption("Built with Streamlit. Next step: connect Supabase Auth + Storage + Postgres for realtime CMS.")
