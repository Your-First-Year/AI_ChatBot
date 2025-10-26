# --------------------------------------------------------
# 🇨🇦 BridgeAI – Your Newcomer Companion
# A friendly Streamlit chatbot for newcomers to Canada
# --------------------------------------------------------

import streamlit as st
import csv
import os
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="BridgeAI – Your Newcomer Companion 🇨🇦",
    page_icon="🇨🇦",
    layout="centered",
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Canada.svg",
        width=100,
    )
    st.markdown("## About BridgeAI")
    st.caption(
        "An AI-powered settlement companion designed to guide newcomers in housing, "
        "employment, healthcare, and wellbeing – one step at a time."
    )
    st.markdown("**Innovation Hackathon 2025 Submission**")

# ---------- INTRO ----------
st.title("👋 Welcome to BridgeAI")
st.markdown(
    """
Hi! I’m **BridgeAI**, your friendly companion for settling in Canada 🇨🇦  
Answer a few quick questions so I can understand your situation and personalize support for you.
"""
)
st.divider()

# ---------- SECTION 1 – PROFILE ----------
st.header("Step 1 · About You")

status = st.radio(
    "What best describes your current situation?",
    [
        "🎓 International student",
        "💼 Skilled worker",
        "👨‍👩‍👧 Family member",
        "🛠️ Refugee / protected person",
        "🧳 Planning to immigrate soon",
    ],
)

province = st.selectbox(
    "Which province or city are you in (or planning to move to)?",
    [
        "Ontario",
        "Quebec",
        "British Columbia",
        "Alberta",
        "Manitoba",
        "Saskatchewan",
        "Nova Scotia",
        "New Brunswick",
        "Other",
    ],
)

timeline = st.radio(
    "How long have you been in Canada (or when will you arrive)?",
    ["Less than 3 months", "3–12 months", "Over a year", "Not yet arrived"],
)

st.divider()

# ---------- SECTION 2 – BRANCHING QUESTIONS ----------
st.header("Step 2 · Your Experience")

if "student" in status.lower():
    st.subheader("🎓 For Students")
    st.write("Let's talk about your study experience.")
    study_field = st.text_input("What are you studying (or planning to study)?")
    housing_type = st.radio("Do you live on campus or off campus?", ["On-campus", "Off-campus", "Not yet decided"])
    part_time = st.radio("Are you currently working part-time in Canada?", ["Yes", "No"])
    st.caption("Many students struggle with balancing studies and living costs — you’re not alone!")

elif "worker" in status.lower():
    st.subheader("💼 For Workers")
    st.write("Tell us about your career journey.")
    profession = st.text_input("What is your professional background or field?")
    credential = st.radio("Have you had your credentials recognized in Canada?", ["Yes", "No", "Not applicable"])
    job_search = st.slider("How confident do you feel finding a job in your field?", 1, 5, 3)
    st.caption("BridgeAI will soon connect you to local employment resources and skill-matching tools.")

elif "family" in status.lower():
    st.subheader("👨‍👩‍👧 For Families")
    st.write("We’d love to know about your family’s needs.")
    children = st.radio("Do you have school-aged children?", ["Yes", "No"])
    childcare = st.radio("Do you currently have access to childcare or schooling?", ["Yes", "No", "Not needed"])
    partner = st.radio("Is your partner currently employed in Canada?", ["Yes", "No", "Not applicable"])
    st.caption("Family settlement often involves multiple systems — BridgeAI can help organize them.")

elif "refugee" in status.lower():
    st.subheader("🛠️ For Refugees / Protected Persons")
    st.write("Let’s understand your current support network.")
    housing_support = st.radio("Do you have temporary or permanent housing?", ["Temporary", "Permanent", "Not yet"])
    language_training = st.radio("Are you currently enrolled in any language or settlement programs?", ["Yes", "No"])
    st.caption("BridgeAI will connect you to verified community and government support resources.")

else:
    st.info("You’re planning ahead — let’s prepare your checklist for when you arrive!")

st.divider()

# ---------- SECTION 3 – COMMON CHALLENGES ----------
st.header("Step 3 · Your Main Challenges")
st.caption("Rate each area from 1 (easy) to 5 (very challenging):")

housing = st.slider("🏠 Finding affordable housing", 1, 5, 3)
job = st.slider("💼 Finding employment or getting credentials recognized", 1, 5, 3)
health = st.slider("🏥 Accessing healthcare", 1, 5, 3)
community = st.slider("🤝 Building social connections", 1, 5, 3)
language = st.slider("🗣️ Communicating in English or French", 1, 5, 3)
mental = st.slider("🧠 Managing stress and mental wellbeing", 1, 5, 3)

st.divider()

# ---------- SECTION 4 – REFLECTION ----------
st.header("Step 4 · Reflection 💭")
challenge_text = st.text_area("What has been your biggest challenge so far?")
help_text = st.text_area("What kind of support would make your settlement journey easier?")

# ---------- SUBMIT ----------
if st.button("Submit ✅"):
    DATA_DIR = "data"
    os.makedirs(DATA_DIR, exist_ok=True)
    csv_path = os.path.join(DATA_DIR, "survey_responses.csv")

    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                datetime.now(),
                status,
                province,
                timeline,
                housing,
                job,
                health,
                community,
                language,
                mental,
                challenge_text,
                help_text,
            ]
        )

    # ---------- SUMMARY ----------
    st.success("✅ Thank you! Here’s your summary:")
    st.markdown(f"**Status:** {status}")
    st.markdown(f"**Province:** {province}")
    st.markdown(f"**Arrival timeline:** {timeline}")

    top_score = max(
        (housing, "Housing"),
        (job, "Employment"),
        (health, "Healthcare"),
        (community, "Community"),
        (language, "Language"),
        (mental, "Wellbeing"),
    )[1]
    st.markdown(f"**Top challenge area:** {top_score}")

    st.info(
        f"BridgeAI will soon offer you curated guidance for {top_score.lower()} and {province}. "
        "Our mission is to make your first year in Canada easier 🇨🇦."
    )

    st.caption("Responses saved ✅  (download from `data/survey_responses.csv`)")
