import os
import uuid
from datetime import date
from io import BytesIO

import streamlit as st

# Page Config
st.set_page_config(
    page_title="Keti Pavan Kumar | Portfolio",
    page_icon="💻",
    layout="wide",
)

MAX_UPLOAD_SIZE_MB = 10
CERTIFICATE_BUCKET = "certificates"


def init_supabase():
    """Create a Supabase client from Streamlit secrets or environment variables."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not (url and key):
        try:
            url = st.secrets["SUPABASE_URL"]
            key = st.secrets["SUPABASE_KEY"]
        except Exception:  # noqa: BLE001
            return None

    try:
        import importlib

        supabase_module = importlib.import_module("supabase")
        return supabase_module.create_client(url, key)
    except Exception:  # noqa: BLE001
        st.warning("Supabase package is not installed. Run `pip install -r requirements.txt`.")
        return None


def get_certificates(client):
    response = (
        client.table("certificates")
        .select("title, issuer, category, issue_date, file_path, verification_url, display_order")
        .order("display_order", desc=False)
        .execute()
    )
    return response.data or []


def get_categories(certs: list[dict]) -> list[str]:
    categories = sorted({c["category"] for c in certs if c.get("category")})
    return ["All"] + categories


def matches_search(certificate: dict, search_term: str) -> bool:
    searchable_fields = [
        certificate.get("title", ""),
        certificate.get("issuer", ""),
        certificate.get("category", ""),
    ]
    haystack = " ".join(searchable_fields).lower()
    return search_term.lower() in haystack


def get_file_public_url(client, path: str) -> str:
    data = client.storage.from_(CERTIFICATE_BUCKET).get_public_url(path)
    return data


def build_pdf_viewer(pdf_url: str) -> str:
    encoded_url = pdf_url.replace("&", "%26")
    return f"https://mozilla.github.io/pdf.js/web/viewer.html?file={encoded_url}"


def ensure_storage_bucket(client) -> tuple[bool, str]:
    try:
        buckets = client.storage.list_buckets()
        if any(bucket.get("name") == CERTIFICATE_BUCKET for bucket in buckets):
            return True, "Storage bucket already exists."
        client.storage.create_bucket(CERTIFICATE_BUCKET, {"public": True})
        return True, "Storage bucket created successfully."
    except Exception as exc:  # noqa: BLE001
        return False, f"Could not create bucket: {exc}"


def validate_uploaded_file(uploaded_file) -> tuple[bool, str]:
    if uploaded_file is None:
        return False, "Please select a PDF file."

    if uploaded_file.type != "application/pdf":
        return False, "Only PDF files are supported."

    file_size_mb = uploaded_file.size / (1024 * 1024)
    if file_size_mb > MAX_UPLOAD_SIZE_MB:
        return False, f"File exceeds {MAX_UPLOAD_SIZE_MB} MB limit."

    return True, "Valid file."


def upload_certificate_file(client, uploaded_file, category: str) -> str:
    unique_name = f"{uuid.uuid4()}_{uploaded_file.name}"
    path = f"{category.lower().replace(' ', '-')}/{unique_name}"

    client.storage.from_(CERTIFICATE_BUCKET).upload(
        path=path,
        file=BytesIO(uploaded_file.getvalue()),
        file_options={"content-type": "application/pdf"},
    )
    return path


def save_certificate_metadata(
    client,
    title: str,
    issuer: str,
    category: str,
    issue_date_value,
    file_path: str,
    verification_url: str,
    display_order: int,
):
    payload = {
        "title": title,
        "issuer": issuer,
        "category": category,
        "issue_date": str(issue_date_value),
        "file_path": file_path,
        "verification_url": verification_url or None,
        "display_order": display_order,
    }
    client.table("certificates").insert(payload).execute()


@st.dialog("📄 Certificate PDF Viewer")
def show_pdf_modal(title: str, pdf_url: str):
    st.write(f"Now viewing **{title}**")
    st.markdown(
        f"<iframe src='{build_pdf_viewer(pdf_url)}' width='100%' height='700'></iframe>",
        unsafe_allow_html=True,
    )


# Sidebar Navigation
st.sidebar.title("📌 Navigation")
pages = [
    "About Me",
    "Education",
    "Skills",
    "Projects",
    "Certifications",
    "Resume",
    "Contact",
    "Admin",
]
choice = st.sidebar.radio("Go to", pages)

# Profile Section (Common Header)
try:
    st.image("profile.jpg", width=180)
except Exception:  # noqa: BLE001
    st.warning("Profile photo not found. Please upload 'profile.jpg'.")
st.title("👨‍💻 Keti Pavan Kumar")
st.markdown(
    "**Computer Science Student | Artificial Intelligence & Machine Learning Enthusiast**"
)
st.markdown(
    "📍 Medchal, Hyderabad 500010 | 📧 [umarpavan768@gmail.com](mailto:umarpavan768@gmail.com) | 📞 +91 7569343025"
)

# Light/Dark theme toggle
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown(
        "<style>body{background-color: #0E1117; color: white;}</style>",
        unsafe_allow_html=True,
    )

supabase_client = init_supabase()

# About Me Page
if choice == "About Me":
    st.header("🌟 About Me")
    st.write(
        """
    Passionate and driven computer science student with a focus on Artificial Intelligence and Machine Learning.
    Eager to secure an internship or entry-level role to apply analytical skills, programming proficiency,
    and a dedication to uncovering insights from data.
    """
    )

# Education Page
elif choice == "Education":
    st.header("🎓 Education")
    st.write(
        "**Malla Reddy University**, Hyderabad – B.Tech CSE (AI & ML) | CGPA: 7.64/10 | Pursuing 4th Semester"
    )
    st.write("**Excellencia Junior College**, Hyderabad – GPA: 7.3/10 | Graduated: 2022")
    st.write("**Shantiniketan Vidyalaya**, Hyderabad – SSC: 70% | Graduated: 2020")

# Skills Page
elif choice == "Skills":
    st.header("💻 Skills")
    st.write("- **Programming**: Python (NumPy, Pandas), Java, JavaScript, HTML, CSS, TypeScript")
    st.write("- **Databases**: MySQL")
    st.write(
        "- **Machine Learning**: Regression, Classification, Clustering, NLP, Deep Learning (YOLOv3)"
    )
    st.write("- **Cloud & DevOps**: AWS, Terraform")
    st.write("- **Tools**: Node.js, OpenCV")
    st.write(
        "- **Core Competencies**: Design & Analytical Abilities, Problem-Solving, Communication, Presentation Skills"
    )

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
    st.header("🏆 Certifications")

    if not supabase_client:
        st.info(
            "Configure SUPABASE_URL and SUPABASE_KEY in Streamlit secrets or environment variables to enable certificate workflow."
        )
    else:
        try:
            certificates = get_certificates(supabase_client)
        except Exception as exc:  # noqa: BLE001
            st.error(f"Could not load certificates: {exc}")
            certificates = []

        if not certificates:
            st.warning("No certificates found yet.")
        else:
            filter_col, search_col = st.columns([1, 2])
            with filter_col:
                selected_category = st.selectbox("Category", get_categories(certificates))
            with search_col:
                search_value = st.text_input("Search certificates", placeholder="Search title, issuer, category")

            filtered = []
            for cert in certificates:
                category_match = selected_category == "All" or cert.get("category") == selected_category
                search_match = matches_search(cert, search_value.strip()) if search_value else True
                if category_match and search_match:
                    filtered.append(cert)

            st.caption(f"Showing {len(filtered)} of {len(certificates)} certificate(s)")

            if not filtered:
                st.info("No certificates match your filters.")
            else:
                columns = st.columns(3)
                for index, cert in enumerate(filtered):
                    col = columns[index % 3]
                    with col:
                        st.markdown("### " + cert.get("title", "Untitled"))
                        st.write(f"**Issuer:** {cert.get('issuer', 'N/A')}")
                        st.write(f"**Category:** {cert.get('category', 'N/A')}")
                        st.write(f"**Issue Date:** {cert.get('issue_date', 'N/A')}")

                        file_path = cert.get("file_path", "")
                        pdf_url = get_file_public_url(supabase_client, file_path)

                        btn_col1, btn_col2 = st.columns(2)
                        with btn_col1:
                            if st.button("View PDF", key=f"view_{index}"):
                                show_pdf_modal(cert.get("title", "Certificate"), pdf_url)
                        with btn_col2:
                            st.link_button("Download PDF", pdf_url)

                        if cert.get("verification_url"):
                            st.link_button("Verify", cert["verification_url"])
                        st.markdown("---")

# Resume Page
elif choice == "Resume":
    st.header("📄 Resume")
    try:
        with open("resume.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.download_button(
            label="📥 Download My Resume",
            data=pdf_bytes,
            file_name="Keti_Pavan_Kumar_Resume.pdf",
            mime="application/pdf",
        )
    except FileNotFoundError:
        st.error("Resume file not found. Please upload resume.pdf to the project folder.")

# Contact Page
elif choice == "Contact":
    st.header("📞 Contact")
    st.write("📍 Medchal, Hyderabad 500010")
    st.write("📧 [umarpavan768@gmail.com](mailto:umarpavan768@gmail.com)")
    st.write("📞 +91 7569343025")
    st.markdown("🌐 [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")

# Admin Page
elif choice == "Admin":
    st.header("🛠️ Certificate Admin")

    if not supabase_client:
        st.error("Admin tools need SUPABASE_URL and SUPABASE_KEY configuration.")
    else:
        st.subheader("1) Setup Storage + Table")
        if st.button("Create / validate certificate storage bucket"):
            ok, message = ensure_storage_bucket(supabase_client)
            if ok:
                st.success(message)
            else:
                st.error(message)

        st.code(
            """
create table if not exists public.certificates (
  id bigint generated by default as identity primary key,
  title text not null,
  issuer text not null,
  category text not null,
  issue_date date not null,
  file_path text not null,
  verification_url text,
  display_order int not null default 0,
  created_at timestamptz not null default now()
);

alter table public.certificates enable row level security;

create policy "Public can read certificates"
on public.certificates
for select
using (true);
            """.strip(),
            language="sql",
        )

        st.subheader("2) Upload certificate")
        with st.form("certificate_upload"):
            title = st.text_input("Title")
            issuer = st.text_input("Issuer")
            category = st.text_input("Category", value="General")
            issue_date_value = st.date_input("Issue Date", value=date.today())
            verification_url = st.text_input("Verification URL (optional)")
            display_order = st.number_input("Display Order", min_value=0, value=0, step=1)
            uploaded_file = st.file_uploader("Certificate PDF", type=["pdf"])
            submit = st.form_submit_button("Upload and Save")

        if submit:
            valid, message = validate_uploaded_file(uploaded_file)
            if not valid:
                st.error(message)
            elif not title or not issuer or not category:
                st.error("Title, issuer, and category are required.")
            else:
                try:
                    file_path = upload_certificate_file(supabase_client, uploaded_file, category)
                    save_certificate_metadata(
                        supabase_client,
                        title,
                        issuer,
                        category,
                        issue_date_value,
                        file_path,
                        verification_url,
                        int(display_order),
                    )
                    st.success("Certificate uploaded and metadata saved.")
                except Exception as exc:  # noqa: BLE001
                    st.error(f"Upload failed: {exc}")
