import streamlit as st
import csv
from datetime import datetime

st.title("🇨🇦 BridgeAI: Your Newcomer Companion")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = {}

def next_step():
    st.session_state.step += 1

# Define conversation steps
questions = [
    ("intro", "Hi! I’m BridgeAI 👋 What brings you to Canada?", 
     ["International student", "Worker", "Family / Parent", "Refugee", "Other"]),
    ("duration", "How long have you been in Canada?", 
     ["Less than 3 months", "3–12 months", "Over a year", "Not yet arrived"]),
    ("challenge", "What has been your biggest challenge so far?", None),
    ("priority", "What kind of support would help you most right now?", 
     ["Housing", "Job search", "Documentation", "Healthcare", "Language", "Mental wellbeing"]),
]

step = st.session_state.step

if step < len(questions):
    qid, qtext, options = questions[step]
    st.write(qtext)

    if options:
        choice = st.radio("Select one:", options, key=qid)
    else:
        choice = st.text_input("Your answer:", key=qid)

    if st.button("Next"):
        st.session_state.responses[qid] = choice
        next_step()
else:
    st.success("Thank you! Here's a quick summary:")
    responses = st.session_state.responses

    st.write(f"- **Status:** {responses.get('intro', '')}")
    st.write(f"- **Time in Canada:** {responses.get('duration', '')}")
    st.write(f"- **Main challenge:** {responses.get('challenge', '')}")
    st.write(f"- **Priority need:** {responses.get('priority', '')}")

    # Save to CSV
    with open("survey_responses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            responses.get("intro", ""),
            responses.get("duration", ""),
            responses.get("challenge", ""),
            responses.get("priority", "")
        ])
