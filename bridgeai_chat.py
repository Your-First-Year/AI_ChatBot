import streamlit as st
import csv, os
from datetime import datetime

st.set_page_config(page_title="YourFirstYear Canada 🇨🇦", page_icon="🇨🇦")
st.title("🇨🇦 YourFirstYear Canada – Immigrant Experience Survey")

st.markdown("""
Help us understand what newcomers need most during their first year in Canada.  
Your responses are anonymous and help shape future newcomer tools. 🍁
""")

# ---------- Data setup ----------
os.makedirs("data", exist_ok=True)
csv_path = "data/yourfirstyear_customer_survey.csv"

# ---------- Start the form ----------
with st.form(key="yourfirstyear_form"):

    # SECTION 1 --------------------------------------------------------
    st.header("Section 1 · Your Immigration to Canada")
    q1 = st.radio("Q1. Have you immigrated to Canada in the past 5 years?", ["Yes", "No"])
    if q1 == "No":
        st.warning("Thank you! This survey is for newcomers who moved within the past 5 years.")
        submitted = st.form_submit_button("End Survey")
        if submitted:
            st.stop()

    q2 = st.selectbox(
        "Q2. Which province/city did you settle in?",
        [
            "Ontario - Toronto", "Ontario - Ottawa", "Ontario - Mississauga", "Ontario - Hamilton",
            "British Columbia - Vancouver", "British Columbia - Surrey", "Alberta - Calgary",
            "Alberta - Edmonton", "Quebec - Montreal", "Quebec - Quebec City", "Manitoba - Winnipeg",
            "Saskatchewan - Regina", "Nova Scotia - Halifax", "New Brunswick - Moncton", "Other"
        ],
    )
    q3 = st.text_input("Q3. When did you arrive in Canada? (Example: January 2023)")
    q4 = st.radio(
        "Q4. What was your immigration category?",
        [
            "Express Entry (Skilled Worker)", "Provincial Nominee Program (PNP)",
            "Study Permit (International Student)", "Family Sponsorship",
            "Refugee/Protected Person", "Work Permit (Temporary Foreign Worker)", "Other",
        ],
    )
    q4_other = st.text_input("If other, please specify:") if q4 == "Other" else ""
    q5 = st.radio(
        "Q5. What was your PRIMARY reason for choosing Canada?",
        [
            "Career opportunities", "Better quality of life", "Education (for self or children)",
            "Safety and security", "Family reunification", "Healthcare system", "Other",
        ],
    )
    q5_other = st.text_input("If other, please specify:") if q5 == "Other" else ""

    # SECTION 2 --------------------------------------------------------
    st.divider()
    st.header("Section 2 · Before Arriving in Canada")

    q6 = st.radio(
        "Q6. How much time did you have to prepare before moving?",
        ["<1 month", "1–3 months", "3–6 months", "6–12 months", "More than 1 year"],
    )
    q7 = st.multiselect(
        "Q7. What were your top 3 concerns BEFORE arriving?",
        [
            "Finding housing", "Finding a job", "Cold weather/winter", "Making friends",
            "Language (English/French)", "Getting credentials recognized",
            "Understanding Canadian culture", "Financial stability", "Healthcare system",
            "Missing family back home", "Other",
        ],
    )
    q7_other = st.text_input("If other, please specify:") if "Other" in q7 else ""
    q8 = st.multiselect(
        "Q8. Where did you get information to prepare for Canada?",
        [
            "Government of Canada website (canada.ca)", "YouTube videos", "Facebook groups",
            "Reddit", "Friends/family already in Canada", "Immigration consultant/lawyer",
            "Google searches", "TikTok", "Settlement agencies", "Other",
        ],
    )
    q8_other = st.text_input("If other, please specify:") if "Other" in q8 else ""
    q9 = st.text_area("Q9. What information do you wish you had BEFORE arriving?")
    q10 = st.radio("Q10. Rate the quality of pre-arrival information you found:",
                   ["Very poor", "Poor", "Okay", "Good", "Excellent"])

    # SECTION 3 --------------------------------------------------------
    st.divider()
    st.header("Section 3 · First Month in Canada")

    q11 = st.multiselect(
        "Q11. What did you do in your FIRST WEEK in Canada?",
        [
            "Applied for SIN", "Opened bank account", "Got a phone plan", "Applied for health card",
            "Looked for housing", "Bought winter clothes", "Figured out transit", "Searched for jobs",
            "Explored neighborhood", "Rested and adjusted", "Registered children for school", "Other",
        ],
    )
    q12 = st.multiselect(
        "Q12. Which tasks were most DIFFICULT or CONFUSING?",
        [
            "Getting SIN", "Opening bank account", "Getting phone plan", "Understanding transit",
            "Finding affordable housing", "Applying for health card", "Filing taxes", "Driver’s license",
            "Finding family doctor", "Understanding job market", "Language barriers", "Other",
        ],
    )
    q13 = st.text_area("Q13. What was the biggest surprise or unexpected challenge in your first month?")
    q14 = st.radio(
        "Q14. How did you find housing?",
        [
            "Facebook Marketplace", "Kijiji", "Craigslist", "Realtor", "Friends/family",
            "Student housing", "Airbnb", "PadMapper/Zumper/RentBoard", "Other",
        ],
    )
    q15 = st.multiselect(
        "Q15. Did you experience any of these in your first month?",
        [
            "Loneliness/isolation", "Culture shock", "Homesickness", "Overwhelmed by tasks",
            "Difficulty communicating", "Financial stress", "Excitement and optimism",
            "Regret about moving", "Weather shock", "None of the above",
        ],
    )
    q16 = st.slider("Q16. On a scale of 1–10, how overwhelming was your first month?", 1, 10, 5)

    # SECTION 4 --------------------------------------------------------
    st.divider()
    st.header("Section 4 · Settlement Experience (3–12 months)")

    q17 = st.multiselect(
        "Q17. What were your biggest challenges AFTER the first 3 months?",
        [
            "Finding a job in my field", "Canadian experience requirement", "Making friends/social isolation",
            "Winter/cold weather", "Cost of living", "Getting credentials recognized",
            "Missing family/friends", "Language barriers", "Mental health/depression",
            "Work-life balance", "Housing affordability", "Other",
        ],
    )
    q18 = st.radio(
        "Q18. When did you start feeling 'at home' in Canada?",
        ["Within first month", "1–3 months", "3–6 months", "6–12 months",
         "1–2 years", "More than 2 years", "Still don't feel at home"],
    )
    q19 = st.multiselect(
        "Q19. What helped you adjust and feel more settled?",
        [
            "Getting a job", "Making friends", "Joining community groups",
            "Learning about Canadian culture", "Finding permanent housing", "Improving English/French",
            "Meeting people from my country", "Exploring Canadian activities", "Establishing routines",
            "Time/natural adjustment", "Other",
        ],
    )
    q20 = st.radio(
        "Q20. Did you try to find people for activities or hobbies?",
        ["Yes, actively looked", "Yes, but struggled to find people", "No, but wish I had", "No, wasn’t interested"],
    )
    q21 = st.radio(
        "Q21. If there was an app to help you find people for activities, would you have used it?",
        ["Definitely yes", "Probably yes", "Maybe", "Probably not", "Definitely not"],
    )
    q22 = st.multiselect(
        "Q22. What support would have been most helpful during your first year?",
        [
            "Step-by-step arrival checklist", "24/7 chatbot for questions", "Job search/networking help",
            "Social events to meet people", "Mental health support", "Help finding housing",
            "Understanding Canadian workplace culture", "Tax filing guidance", "Credential recognition guidance",
            "Language practice partners", "Just someone to talk to", "Other",
        ],
    )

    # SECTION 5 --------------------------------------------------------
    st.divider()
    st.header("Section 5 · Looking Back & Feedback")

    q23 = st.text_area("Q23. If you could go back, what ONE thing do you wish you had known or had help with?")
    q24 = st.slider("Q24. Rate your overall first-year experience in Canada (1=Very difficult, 10=Excellent):", 1, 10, 6)
    q25 = st.radio(
        "Q25. Would you have paid for an app that helped you with settlement?",
        ["Yes - $5-10/month", "Yes - $2-5/month", "Maybe if free trial", "No - only if free", "No - wouldn't use it"],
    )
    q26 = st.radio(
        "Q26. When would this kind of app be MOST helpful?",
        ["Before arriving", "First week", "First 3 months", "Throughout first year", "All stages equally important"],
    )

    # BONUS SECTION ---------------------------------------------------
    st.divider()
    st.header("Bonus Section (Optional)")

    q27 = st.radio(
        "Q27. Would you be interested in a 20-min interview for a $20 Tim Hortons gift card?",
        ["Yes", "No"]
    )
    q27_email = st.text_input("Email for interview (optional):") if q27 == "Yes" else ""

    q28 = st.radio("Q28. Want early access to the YourFirstYear app?", ["Yes", "No"])
    q28_email = st.text_input("Email for early access (optional):") if q28 == "Yes" else ""

    q29 = st.radio("Q29. Would you like to receive updates about newcomer tools?", ["Yes", "No"])
    q29_email = st.text_input("Email for updates (optional):") if q29 == "Yes" else ""

    q30 = st.text_area("Q30. Any other comments or suggestions?")

    # ---------- Submit ----------
    submitted = st.form_submit_button("✅ Submit Survey")

    if submitted:
        file_exists = os.path.isfile(csv_path)
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow([
                    "timestamp", "city", "arrival_date", "category", "category_other", "reason", "reason_other",
                    "prep_time", "concerns", "sources", "missing_info", "info_quality",
                    "first_week", "difficult_tasks", "biggest_surprise", "housing_method",
                    "experiences", "overwhelm_score", "challenges_after_3m", "feel_home_when",
                    "adjustment_factors", "found_hobby", "would_use_app", "needed_support",
                    "wish_known", "overall_experience", "pay_app", "best_timing",
                    "interview_interest", "interview_email", "early_access", "early_email",
                    "receive_updates", "updates_email", "other_comments"
                ])
            writer.writerow([
                datetime.now().isoformat(), q2, q3, q4, q4_other, q5, q5_other, q6,
                "; ".join(q7), "; ".join(q8), q9, q10, "; ".join(q11), "; ".join(q12),
                q13, q14, "; ".join(q15), q16, "; ".join(q17), q18, "; ".join(q19),
                q20, q21, "; ".join(q22), q23, q24, q25, q26, q27, q27_email,
                q28, q28_email, q29, q29_email, q30
            ])

        st.success("🎉 Thank you for completing the survey!")
        st.balloons()
        st.info("Your insights will help build better newcomer resources across Canada 🇨🇦.")
