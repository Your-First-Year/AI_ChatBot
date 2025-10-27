# --------------------------------------------------------
# 🇨🇦 BridgeAI – Your Newcomer Companion
# Adaptive chatbot for newcomers to Canada
# Personalized flow by timeline stage:
#   1. Pre-arrival
#   2. First 6 months
#   3. 6–12 months
#   4. Over 1 year
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
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Canada.svg", width=100)
    st.markdown("## About BridgeAI")
    st.caption(
        "BridgeAI is an AI-powered settlement companion guiding newcomers through "
        "housing, employment, healthcare, and wellbeing – one step at a time."
    )
    st.markdown("**Innovation Hackathon 2025 Submission**")

# ---------- INTRO ----------
st.title("👋 Welcome to BridgeAI")

st.markdown(
    """
Hi! I’m **BridgeAI**, your personalized guide to help you build life in Canada 🇨🇦.  
Answer a few short questions — I’ll adapt them to where you are in your journey.
"""
)
st.divider()

# ---------- STEP 1 – PROFILE ----------
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
    "Where are you in your Canadian journey?",
    [
        "🛫 I haven’t arrived yet (planning my move)",
        "🌅 I’ve been in Canada less than 6 months",
        "🌤 I’ve been in Canada 6–12 months",
        "🌇 I’ve been in Canada more than a year",
    ],
)

st.divider()

# ---------- STEP 2 – PROFILE QUESTIONS ADAPTED TO TIMELINE ----------
if "haven’t arrived" in timeline.lower():
    st.subheader("🛫 Preparing for Your Move")
    st.write("You're planning your new beginning — let’s get you ready for arrival.")
    visa_status = st.radio("Have you received your visa or permit yet?", ["Yes", "No", "In progress"])
    housing_plan = st.radio("Do you already have a place to stay when you arrive?", ["Yes", "No", "Still searching"])
    prep_needs = st.multiselect(
        "What information would help you most right now?",
        ["Housing options", "Banking setup", "Healthcare system", "Job market overview", "Cultural expectations"],
    )
    st.caption("BridgeAI can create a pre-arrival checklist so you land with confidence.")

elif "less than 6" in timeline.lower():
    st.subheader("🌅 Settling In – First 6 Months")
    st.write("Welcome! These first months can be busy — let's see how you're adjusting.")
    docs_done = st.multiselect(
        "Which essential tasks have you already completed?",
        ["Got SIN", "Opened bank account", "Applied for healthcare", "Found permanent housing", "None yet"],
    )
    support = st.radio("Do you currently have someone or an organization helping you settle?", ["Yes", "No"])
    adjustment = st.slider("How settled do you feel so far?", 1, 5, 3)
    st.caption("BridgeAI supports newcomers with document checklists and access to community groups.")

elif "6–12" in timeline.lower():
    st.subheader("🌤 Finding Your Footing – 6–12 Months")
    st.write("You’ve passed the initial phase — let’s focus on growth and stability.")
    work_status = st.radio(
        "Are you currently working or studying?",
        ["Full-time job", "Part-time job", "Studying", "Looking for work", "Other"],
    )
    language_conf = st.slider("How confident are you with English/French communication?", 1, 5, 3)
    goal = st.text_input("What’s your main personal or professional goal for the next 6 months?")
    st.caption("BridgeAI connects you with upskilling and networking resources.")

else:
    st.subheader("🌇 Building Your Life in Canada – Over a Year In")
    st.write("Great work building your life here! Let’s reflect and see how you can grow further.")
    satisfaction = st.slider("Overall, how satisfied are you with your life in Canada?", 1, 5, 4)
    community_role = st.radio("Are you involved in any community or volunteering activities?", ["Yes", "No", "Not yet"])
    mentoring = st.radio("Would you like to mentor new arrivals?", ["Yes", "No", "Maybe later"])
    st.caption("BridgeAI connects experienced newcomers with mentorship and civic opportunities.")

st.divider()

# ---------- STEP 3 – CHALLENGES ----------
if "haven’t arrived" in timeline.lower():
    st.header("Step 2 · What You’re Preparing For")
    st.caption("Rate how challenging you expect each area to be (1 = easy, 5 = very challenging):")
else:
    st.header("Step 3 · Your Main Challenges")
    st.caption("Rate how challenging these areas are for you right now (1 = easy, 5 = very challenging):")

housing = st.slider("🏠 Finding affordable housing", 1, 5, 3)
job = st.slider("💼 Finding employment or credential recognition", 1, 5, 3)
health = st.slider("🏥 Accessing healthcare", 1, 5, 3)
community = st.slider("🤝 Building social connections", 1, 5, 3)
language = st.slider("🗣️ Communicating in English or French", 1, 5, 3)
mental = st.slider("🧠 Managing stress and mental wellbeing", 1, 5, 3)

st.divider()

# ---------- STEP 4 – REFLECTION ----------
if "haven’t arrived" in timeline.lower():
    st.header("Step 3 · Pre-arrival Reflections")
    st.write("What questions or worries do you have before arriving?")
    challenge_text = st.text_area("Your top concern before moving:")
    help_text = st.text_area("What kind of pre-arrival support would help you the most?")
elif "less than 6" in timeline.lower():
    st.header("Step 4 · Reflection 💭")
    st.write("Looking back at your first months, what’s been hardest and what helped the most?")
    challenge_text = st.text_area("Your biggest early challenge:")
    help_text = st.text_area("What support would make the next few months smoother?")
elif "6–12" in timeline.lower():
    st.header("Step 4 · Reflection 💭")
    st.write("You’re progressing well — let’s see what would take you further.")
    challenge_text = st.text_area("Biggest challenge as you settle deeper:")
    help_text = st.text_area("What kind of help or information would accelerate your progress?")
else:
    st.header("Step 4 · Reflection 💭")
    st.write("Your experience matters — your feedback helps improve newcomer programs.")
    challenge_text = st.text_area("What challenges do you still face after your first year?")
    help_text = st.text_area("What resources or connections would make your life even better?")

st.divider()

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
    st.markdown(f"**Stage:** {timeline}")

    top_score = max(
        (housing, "Housing"),
        (job, "Employment"),
        (health, "Healthcare"),
        (community, "Community"),
        (language, "Language"),
        (mental, "Wellbeing"),
    )[1]

    st.markdown(f"**Top focus area:** {top_score}")

    # Adaptive closing messages
    if "haven’t arrived" in timeline.lower():
        message = "BridgeAI can help you organize key steps before you land — like finding housing and understanding documents."
    elif "less than 6" in timeline.lower():
        message = "BridgeAI will help you navigate essential services and reduce stress during your first months."
    elif "6–12" in timeline.lower():
        message = "BridgeAI can guide you toward career development, education, and community engagement."
    else:
        message = "BridgeAI connects you to mentorship and community initiatives to help others succeed."

    st.info(f"{message} 🇨🇦")
    st.caption("Responses saved ✅  (download from `data/survey_responses.csv`)")
