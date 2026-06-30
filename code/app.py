import streamlit as st

st.set_page_config(
    page_title="Class Connect — Registration",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
/* Hero banner */
.hero {
    background: linear-gradient(135deg, #EEEDFE 0%, #E1F5EE 100%);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    border: 1px solid #CECBF6;
}
.hero h1 { font-size: 26px; color: #26215C; margin-bottom: 4px; }
.hero p  { font-size: 15px; color: #534AB7; }

/* Section headings */
.section-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: #888780;
    margin: 1.5rem 0 .4rem;
}

/* Celebration box */
.cel-box {
    background: linear-gradient(135deg, #EEEDFE, #E1F5EE);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    border: 1px solid #AFA9EC;
    margin-bottom: 1rem;
}
.cel-box h2 { color: #26215C; font-size: 24px; margin-bottom: .4rem; }
.cel-box p  { color: #534AB7; font-size: 15px; }

/* Project cards */
.proj-card {
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: .75rem;
    border: 1px solid;
}
.proj-purple { background:#EEEDFE; border-color:#AFA9EC; }
.proj-teal   { background:#E1F5EE; border-color:#9FE1CB; }
.proj-coral  { background:#FAECE7; border-color:#F5C4B3; }
.proj-card h4 { margin:0 0 4px; font-size:15px; }
.proj-card p  { margin:0; font-size:13px; color:#5F5E5A; }
.badge {
    display:inline-block; font-size:11px; padding:3px 10px;
    border-radius:20px; margin-top:6px; font-weight:600;
}
.badge-purple { background:#EEEDFE; color:#26215C; }
.badge-teal   { background:#E1F5EE; color:#04342C; }
.badge-coral  { background:#FAECE7; color:#4A1B0C; }

/* YouTube cards */
.yt-card {
    display:flex; align-items:center; gap:12px;
    padding:10px 14px; border-radius:10px;
    background:#F1EFE8; border:1px solid #D3D1C7;
    margin-bottom:8px; text-decoration:none;
}
.yt-card:hover { background:#EEEDFE; border-color:#AFA9EC; }
.yt-icon  { font-size:24px; flex-shrink:0; }
.yt-title { font-size:13px; font-weight:600; color:#2C2C2A; margin:0; }
.yt-chan  { font-size:12px; color:#888780; margin:0; }

/* Submit button override */
div[data-testid="stButton"] > button {
    background: #7F77DD !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.6rem 2rem !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    width: 100%;
}
div[data-testid="stButton"] > button:hover {
    background: #534AB7 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "student_data" not in st.session_state:
    st.session_state.student_data = {}

# ═══════════════════════════════════════════════════════════════════════════════
#  CELEBRATION PAGE
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.submitted:
    d = st.session_state.student_data

    st.markdown(f"""
    <div class="cel-box">
        <div style="font-size:42px;margin-bottom:.5rem">🎉 🚀 ✨ 🎊 💡</div>
        <h2>You're in, {d['first_name']}!</h2>
        <p>Welcome to <strong>Class Connect</strong>. Your profile is live.<br>
           You just unlocked <strong>3 exclusive projects</strong> — explore below!</p>
        <div style="margin-top:1rem;display:inline-block;background:#EEEDFE;
                    border:1px solid #AFA9EC;border-radius:20px;padding:5px 16px;
                    font-size:13px;color:#3C3489;font-weight:600;">
            🪪 &nbsp;ID: {d['roll_no']} &nbsp;·&nbsp; {d['dept'].split('—')[0].strip()}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Student summary ────────────────────────────────────────────────────────
    with st.expander("👤 Your registration summary", expanded=False):
        c1, c2 = st.columns(2)
        c1.write(f"**Name:** {d['first_name']} {d['last_name']}")
        c1.write(f"**Email:** {d['email']}")
        c1.write(f"**Phone:** {d.get('phone') or '—'}")
        c2.write(f"**Roll No:** {d['roll_no']}")
        c2.write(f"**Year:** {d['year']}")
        c2.write(f"**Section:** {d.get('section') or '—'}")
        st.write(f"**College:** {d['college']}")
        if d.get("skills"):
            st.write(f"**Skills:** {', '.join(d['skills'])}")
        if d.get("roles"):
            st.write(f"**Roles:** {', '.join(d['roles'])}")
        if d.get("bio"):
            st.write(f"**Bio:** {d['bio']}")

    # ── Projects ──────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🔓 Projects unlocked for you</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="proj-card proj-purple">
        <h4>🏦 FinTech Payment Gateway Simulator</h4>
        <p>Build a mock NACH / mandate payment flow using Spring Boot and REST APIs</p>
        <span class="badge badge-purple">Java · Spring Boot · REST</span>
    </div>
    <div class="proj-card proj-teal">
        <h4>🧪 Automated QA Test Suite</h4>
        <p>Create end-to-end test automation with Selenium WebDriver + TestNG for a banking portal</p>
        <span class="badge badge-teal">Selenium · Java · TestNG</span>
    </div>
    <div class="proj-card proj-coral">
        <h4>☁️ Cloud Deployment Pipeline</h4>
        <p>Deploy a Java microservice to AWS EC2 with Jenkins CI/CD and Docker containerisation</p>
        <span class="badge badge-coral">DevOps · AWS · Docker</span>
    </div>
    """, unsafe_allow_html=True)

    # ── YouTube videos ────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">▶️ Recommended videos to get started</div>', unsafe_allow_html=True)

    videos = [
        {
            "title": "Spring Boot Full Course — Build REST APIs from scratch",
            "channel": "Amigoscode · 3.2M views",
            "url": "https://www.youtube.com/watch?v=9SGDpanrc8U",
            "icon": "🟥",
        },
        {
            "title": "Selenium WebDriver with Java — complete tutorial for beginners",
            "channel": "Automation Step by Step · 1.8M views",
            "url": "https://www.youtube.com/watch?v=VE_MU0xHGaI",
            "icon": "🟥",
        },
        {
            "title": "Jenkins + Docker + AWS — CI/CD pipeline in 1 hour",
            "channel": "TechWorld with Nana · 2.4M views",
            "url": "https://www.youtube.com/watch?v=pTFZFxd5uri",
            "icon": "🟥",
        },
    ]

    for v in videos:
        st.markdown(f"""
        <a class="yt-card" href="{v['url']}" target="_blank">
            <span class="yt-icon">{v['icon']}</span>
            <div>
                <p class="yt-title">{v['title']}</p>
                <p class="yt-chan">{v['channel']}</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Register another student"):
        st.session_state.submitted = False
        st.session_state.student_data = {}
        st.rerun()

    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
#  REGISTRATION FORM
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
    <div style="font-size:48px;margin-bottom:.5rem">🎓</div>
    <h1>Class Connect — Registration</h1>
    <p>Join your organisation, find teammates, and unlock exclusive projects</p>
</div>
""", unsafe_allow_html=True)

# ── Personal info ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">👤 Personal info</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
first_name = col1.text_input("First name *", placeholder="Deekshitha")
last_name  = col2.text_input("Last name *",  placeholder="K")

if first_name:
    initials = (first_name[0] + (last_name[0] if last_name else "")).upper()
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:12px;margin:.5rem 0 1rem">
        <div style="width:52px;height:52px;border-radius:50%;background:#EEEDFE;
                    border:2px solid #AFA9EC;display:flex;align-items:center;
                    justify-content:center;font-size:20px;font-weight:700;
                    color:#534AB7;">{initials}</div>
        <span style="font-size:13px;color:#534AB7;">Hi, <strong>{first_name}</strong>! 
        Looking good — keep going 🙌</span>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
email = col3.text_input("Email *", placeholder="you@university.edu")
phone = col4.text_input("Phone (optional)", placeholder="+91 98765 43210")
roll_no = st.text_input("Roll number / student ID *", placeholder="e.g. MCA2026001")

# ── Academic info ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">🏫 Academic info</div>', unsafe_allow_html=True)

dept = st.selectbox("Department / program *", [
    "", "MCA — Master of Computer Applications", "MBA — Master of Business Administration",
    "B.Tech — Computer Science", "B.Tech — Electronics",
    "BCA — Bachelor of Computer Applications", "B.Sc — Information Technology", "Other"
])

col5, col6 = st.columns(2)
year = col5.selectbox("Year / semester *", [
    "", "1st Year — Semester 1", "1st Year — Semester 2",
    "2nd Year — Semester 3", "2nd Year — Semester 4",
    "3rd Year — Semester 5", "3rd Year — Semester 6"
])
section = col6.selectbox("Section", ["", "Section A", "Section B", "Section C", "Section D"])

college = st.text_input("College / institution *", placeholder="e.g. Manipal Academy of Higher Education")

# ── Skills & interests ────────────────────────────────────────────────────────
st.markdown('<div class="section-label">💻 Skills & interests</div>', unsafe_allow_html=True)

skills = st.multiselect("Tech skills (pick all that apply)", [
    "Java", "Python", "JavaScript", "React", "SQL", "Spring Boot",
    "Machine Learning", "Cloud / AWS", "QA / Testing", "DevOps",
    "UI/UX Design", "Cybersecurity", "Docker", "Kubernetes"
])

roles = st.multiselect("Roles you're interested in", [
    "Project lead", "Developer", "Designer", "QA / tester",
    "Data analyst", "DevOps engineer", "Scrum master", "Business analyst"
])

bio = st.text_area("Short bio (optional)", placeholder="Tell your classmates a little about yourself...", height=90)

# ── GitHub / LinkedIn ─────────────────────────────────────────────────────────
st.markdown('<div class="section-label">🔗 Online profiles (optional)</div>', unsafe_allow_html=True)
col7, col8 = st.columns(2)
github   = col7.text_input("GitHub URL",   placeholder="https://github.com/username")
linkedin = col8.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/username")

# ── Progress ──────────────────────────────────────────────────────────────────
required_fields = [first_name, last_name, email, roll_no, dept, year, college]
filled = sum(1 for f in required_fields if f and str(f).strip())
pct = int((filled / len(required_fields)) * 100)

st.markdown(f"""
<div style="margin:1.5rem 0 .4rem">
    <div style="display:flex;justify-content:space-between;
                font-size:13px;color:#5F5E5A;margin-bottom:6px;">
        <span>{"✅ All set — ready to register!" if pct == 100 else f"{filled} of {len(required_fields)} required fields filled"}</span>
        <span style="font-weight:600;color:#534AB7">{pct}%</span>
    </div>
    <div style="height:8px;background:#D3D1C7;border-radius:4px;overflow:hidden">
        <div style="height:100%;width:{pct}%;background:#7F77DD;border-radius:4px;
                    transition:width .4s ease;"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Submit ────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

submitted = st.button("🎓 Complete registration & unlock projects", disabled=(pct < 100))

if submitted:
    # Basic email validation
    if "@" not in email or "." not in email:
        st.error("⚠️ Please enter a valid email address.")
    else:
        st.session_state.student_data = {
            "first_name": first_name,
            "last_name":  last_name,
            "email":      email,
            "phone":      phone,
            "roll_no":    roll_no,
            "dept":       dept,
            "year":       year,
            "section":    section,
            "college":    college,
            "skills":     skills,
            "roles":      roles,
            "bio":        bio,
            "github":     github,
            "linkedin":   linkedin,
        }
        st.session_state.submitted = True
        st.rerun()import streamlit as st

st.set_page_config(
    page_title="Class Connect — Registration",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
/* Hero banner */
.hero {
    background: linear-gradient(135deg, #EEEDFE 0%, #E1F5EE 100%);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    border: 1px solid #CECBF6;
}
.hero h1 { font-size: 26px; color: #26215C; margin-bottom: 4px; }
.hero p  { font-size: 15px; color: #534AB7; }

/* Section headings */
.section-label {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: #888780;
    margin: 1.5rem 0 .4rem;
}

/* Celebration box */
.cel-box {
    background: linear-gradient(135deg, #EEEDFE, #E1F5EE);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    border: 1px solid #AFA9EC;
    margin-bottom: 1rem;
}
.cel-box h2 { color: #26215C; font-size: 24px; margin-bottom: .4rem; }
.cel-box p  { color: #534AB7; font-size: 15px; }

/* Project cards */
.proj-card {
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: .75rem;
    border: 1px solid;
}
.proj-purple { background:#EEEDFE; border-color:#AFA9EC; }
.proj-teal   { background:#E1F5EE; border-color:#9FE1CB; }
.proj-coral  { background:#FAECE7; border-color:#F5C4B3; }
.proj-card h4 { margin:0 0 4px; font-size:15px; }
.proj-card p  { margin:0; font-size:13px; color:#5F5E5A; }
.badge {
    display:inline-block; font-size:11px; padding:3px 10px;
    border-radius:20px; margin-top:6px; font-weight:600;
}
.badge-purple { background:#EEEDFE; color:#26215C; }
.badge-teal   { background:#E1F5EE; color:#04342C; }
.badge-coral  { background:#FAECE7; color:#4A1B0C; }

/* YouTube cards */
.yt-card {
    display:flex; align-items:center; gap:12px;
    padding:10px 14px; border-radius:10px;
    background:#F1EFE8; border:1px solid #D3D1C7;
    margin-bottom:8px; text-decoration:none;
}
.yt-card:hover { background:#EEEDFE; border-color:#AFA9EC; }
.yt-icon  { font-size:24px; flex-shrink:0; }
.yt-title { font-size:13px; font-weight:600; color:#2C2C2A; margin:0; }
.yt-chan  { font-size:12px; color:#888780; margin:0; }

/* Submit button override */
div[data-testid="stButton"] > button {
    background: #7F77DD !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.6rem 2rem !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    width: 100%;
}
div[data-testid="stButton"] > button:hover {
    background: #534AB7 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "student_data" not in st.session_state:
    st.session_state.student_data = {}

# ═══════════════════════════════════════════════════════════════════════════════
#  CELEBRATION PAGE
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.submitted:
    d = st.session_state.student_data

    st.markdown(f"""
    <div class="cel-box">
        <div style="font-size:42px;margin-bottom:.5rem">🎉 🚀 ✨ 🎊 💡</div>
        <h2>You're in, {d['first_name']}!</h2>
        <p>Welcome to <strong>Class Connect</strong>. Your profile is live.<br>
           You just unlocked <strong>3 exclusive projects</strong> — explore below!</p>
        <div style="margin-top:1rem;display:inline-block;background:#EEEDFE;
                    border:1px solid #AFA9EC;border-radius:20px;padding:5px 16px;
                    font-size:13px;color:#3C3489;font-weight:600;">
            🪪 &nbsp;ID: {d['roll_no']} &nbsp;·&nbsp; {d['dept'].split('—')[0].strip()}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Student summary ────────────────────────────────────────────────────────
    with st.expander("👤 Your registration summary", expanded=False):
        c1, c2 = st.columns(2)
        c1.write(f"**Name:** {d['first_name']} {d['last_name']}")
        c1.write(f"**Email:** {d['email']}")
        c1.write(f"**Phone:** {d.get('phone') or '—'}")
        c2.write(f"**Roll No:** {d['roll_no']}")
        c2.write(f"**Year:** {d['year']}")
        c2.write(f"**Section:** {d.get('section') or '—'}")
        st.write(f"**College:** {d['college']}")
        if d.get("skills"):
            st.write(f"**Skills:** {', '.join(d['skills'])}")
        if d.get("roles"):
            st.write(f"**Roles:** {', '.join(d['roles'])}")
        if d.get("bio"):
            st.write(f"**Bio:** {d['bio']}")

    # ── Projects ──────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🔓 Projects unlocked for you</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="proj-card proj-purple">
        <h4>🏦 FinTech Payment Gateway Simulator</h4>
        <p>Build a mock NACH / mandate payment flow using Spring Boot and REST APIs</p>
        <span class="badge badge-purple">Java · Spring Boot · REST</span>
    </div>
    <div class="proj-card proj-teal">
        <h4>🧪 Automated QA Test Suite</h4>
        <p>Create end-to-end test automation with Selenium WebDriver + TestNG for a banking portal</p>
        <span class="badge badge-teal">Selenium · Java · TestNG</span>
    </div>
    <div class="proj-card proj-coral">
        <h4>☁️ Cloud Deployment Pipeline</h4>
        <p>Deploy a Java microservice to AWS EC2 with Jenkins CI/CD and Docker containerisation</p>
        <span class="badge badge-coral">DevOps · AWS · Docker</span>
    </div>
    """, unsafe_allow_html=True)

    # ── YouTube videos ────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">▶️ Recommended videos to get started</div>', unsafe_allow_html=True)

    videos = [
        {
            "title": "Spring Boot Full Course — Build REST APIs from scratch",
            "channel": "Amigoscode · 3.2M views",
            "url": "https://www.youtube.com/watch?v=9SGDpanrc8U",
            "icon": "🟥",
        },
        {
            "title": "Selenium WebDriver with Java — complete tutorial for beginners",
            "channel": "Automation Step by Step · 1.8M views",
            "url": "https://www.youtube.com/watch?v=VE_MU0xHGaI",
            "icon": "🟥",
        },
        {
            "title": "Jenkins + Docker + AWS — CI/CD pipeline in 1 hour",
            "channel": "TechWorld with Nana · 2.4M views",
            "url": "https://www.youtube.com/watch?v=pTFZFxd5uri",
            "icon": "🟥",
        },
    ]

    for v in videos:
        st.markdown(f"""
        <a class="yt-card" href="{v['url']}" target="_blank">
            <span class="yt-icon">{v['icon']}</span>
            <div>
                <p class="yt-title">{v['title']}</p>
                <p class="yt-chan">{v['channel']}</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Register another student"):
        st.session_state.submitted = False
        st.session_state.student_data = {}
        st.rerun()

    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
#  REGISTRATION FORM
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
    <div style="font-size:48px;margin-bottom:.5rem">🎓</div>
    <h1>Class Connect — Registration</h1>
    <p>Join your organisation, find teammates, and unlock exclusive projects</p>
</div>
""", unsafe_allow_html=True)

# ── Personal info ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">👤 Personal info</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
first_name = col1.text_input("First name *", placeholder="Deekshitha")
last_name  = col2.text_input("Last name *",  placeholder="K")

if first_name:
    initials = (first_name[0] + (last_name[0] if last_name else "")).upper()
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:12px;margin:.5rem 0 1rem">
        <div style="width:52px;height:52px;border-radius:50%;background:#EEEDFE;
                    border:2px solid #AFA9EC;display:flex;align-items:center;
                    justify-content:center;font-size:20px;font-weight:700;
                    color:#534AB7;">{initials}</div>
        <span style="font-size:13px;color:#534AB7;">Hi, <strong>{first_name}</strong>! 
        Looking good — keep going 🙌</span>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
email = col3.text_input("Email *", placeholder="you@university.edu")
phone = col4.text_input("Phone (optional)", placeholder="+91 98765 43210")
roll_no = st.text_input("Roll number / student ID *", placeholder="e.g. MCA2026001")

# ── Academic info ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">🏫 Academic info</div>', unsafe_allow_html=True)

dept = st.selectbox("Department / program *", [
    "", "MCA — Master of Computer Applications", "MBA — Master of Business Administration",
    "B.Tech — Computer Science", "B.Tech — Electronics",
    "BCA — Bachelor of Computer Applications", "B.Sc — Information Technology", "Other"
])

col5, col6 = st.columns(2)
year = col5.selectbox("Year / semester *", [
    "", "1st Year — Semester 1", "1st Year — Semester 2",
    "2nd Year — Semester 3", "2nd Year — Semester 4",
    "3rd Year — Semester 5", "3rd Year — Semester 6"
])
section = col6.selectbox("Section", ["", "Section A", "Section B", "Section C", "Section D"])

college = st.text_input("College / institution *", placeholder="e.g. Manipal Academy of Higher Education")

# ── Skills & interests ────────────────────────────────────────────────────────
st.markdown('<div class="section-label">💻 Skills & interests</div>', unsafe_allow_html=True)

skills = st.multiselect("Tech skills (pick all that apply)", [
    "Java", "Python", "JavaScript", "React", "SQL", "Spring Boot",
    "Machine Learning", "Cloud / AWS", "QA / Testing", "DevOps",
    "UI/UX Design", "Cybersecurity", "Docker", "Kubernetes"
])

roles = st.multiselect("Roles you're interested in", [
    "Project lead", "Developer", "Designer", "QA / tester",
    "Data analyst", "DevOps engineer", "Scrum master", "Business analyst"
])

bio = st.text_area("Short bio (optional)", placeholder="Tell your classmates a little about yourself...", height=90)

# ── GitHub / LinkedIn ─────────────────────────────────────────────────────────
st.markdown('<div class="section-label">🔗 Online profiles (optional)</div>', unsafe_allow_html=True)
col7, col8 = st.columns(2)
github   = col7.text_input("GitHub URL",   placeholder="https://github.com/username")
linkedin = col8.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/username")

# ── Progress ──────────────────────────────────────────────────────────────────
required_fields = [first_name, last_name, email, roll_no, dept, year, college]
filled = sum(1 for f in required_fields if f and str(f).strip())
pct = int((filled / len(required_fields)) * 100)

st.markdown(f"""
<div style="margin:1.5rem 0 .4rem">
    <div style="display:flex;justify-content:space-between;
                font-size:13px;color:#5F5E5A;margin-bottom:6px;">
        <span>{"✅ All set — ready to register!" if pct == 100 else f"{filled} of {len(required_fields)} required fields filled"}</span>
        <span style="font-weight:600;color:#534AB7">{pct}%</span>
    </div>
    <div style="height:8px;background:#D3D1C7;border-radius:4px;overflow:hidden">
        <div style="height:100%;width:{pct}%;background:#7F77DD;border-radius:4px;
                    transition:width .4s ease;"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Submit ────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

submitted = st.button("🎓 Complete registration & unlock projects", disabled=(pct < 100))

if submitted:
    # Basic email validation
    if "@" not in email or "." not in email:
        st.error("⚠️ Please enter a valid email address.")
    else:
        st.session_state.student_data = {
            "first_name": first_name,
            "last_name":  last_name,
            "email":      email,
            "phone":      phone,
            "roll_no":    roll_no,
            "dept":       dept,
            "year":       year,
            "section":    section,
            "college":    college,
            "skills":     skills,
            "roles":      roles,
            "bio":        bio,
            "github":     github,
            "linkedin":   linkedin,
        }
        st.session_state.submitted = True
        st.rerun()