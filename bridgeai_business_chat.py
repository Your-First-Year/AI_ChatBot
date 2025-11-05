# --------------------------------------------------------
# 🇨🇦 Business Survey – Reaching Immigrant Customers in Canada
# Streamlit survey app for businesses
# --------------------------------------------------------

import streamlit as st
import csv
import os
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Business Survey – Reaching Immigrant Customers in Canada",
    page_icon="📊",
    layout="centered",
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## About this survey")
    st.caption(
        "Quick 5-minute survey to understand how businesses connect with newcomers to Canada. "
        "Your responses help improve services for both businesses and immigrants. "
        "All responses are anonymous and confidential."
    )
    st.markdown("**Target:** Small & medium service businesses in Canada.")

# ---------- TITLE ----------
st.title("📊 Business Survey: Reaching Immigrant Customers in Canada")
st.markdown(
    """
Please answer the questions below as accurately as you can.  
Most questions are multiple choice; a few are open-ended.
"""
)
st.divider()

# Ensure data directory exists
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
CSV_PATH = os.path.join(DATA_DIR, "business_survey_responses.csv")

# ---------- SURVEY FORM ----------
with st.form("business_survey"):
    st.header("Section 1 · About Your Business")

    # Q1
    industry = st.radio(
        "Q1. What industry are you in?",
        [
            "Banking/Financial Services",
            "Insurance (Home, Auto, Life, Health)",
            "Telecommunications (Phone/Internet)",
            "Real Estate",
            "Legal Services",
            "Employment/Recruitment",
            "Education/Training",
            "Healthcare",
            "Transportation (Driving school, Car sales, etc.)",
            "Other",
        ],
    )
    industry_other = ""
    if industry == "Other":
        industry_other = st.text_input("Please specify your industry:")

    # Q2
    cities = st.multiselect(
        "Q2. Which cities do you operate in? (Select all that apply)",
        [
            "Toronto/GTA",
            "Vancouver/Lower Mainland",
            "Calgary",
            "Edmonton",
            "Montreal",
            "Ottawa",
            "Winnipeg",
            "Halifax",
            "Other major city",
            "All of Canada",
        ],
    )

    # Q3
    immigrant_share = st.radio(
        "Q3. What percentage of your customers are immigrants (arrived within last 5 years)?",
        [
            "0-10%",
            "11-25%",
            "26-50%",
            "51-75%",
            "76-100%",
            "Don't know",
        ],
    )

    # Q4
    more_immigrants = st.radio(
        "Q4. Would you like to have MORE immigrant customers?",
        [
            "Yes, definitely - it's a priority",
            "Yes, somewhat interested",
            "Neutral - happy with current mix",
            "No, not our target market",
        ],
    )

    st.divider()
    st.header("Section 2 · Finding Immigrant Customers")

    # Q5
    difficulty = st.slider(
        "Q5. How difficult is it to reach immigrant customers?",
        min_value=1,
        max_value=5,
        value=3,
        help="1 = Very easy, 5 = Very difficult",
    )

    # Q6
    challenge = st.radio(
        "Q6. What's your BIGGEST challenge in attracting immigrant customers? (Pick ONE)",
        [
            "Don't know where to find them",
            "They don't know about my business",
            "Hard to build trust with newcomers",
            "Language barriers",
            "They don't understand Canadian systems (credit, insurance, etc.)",
            "Too expensive to reach them (advertising costs)",
            "Long sales cycle",
            "No specific challenges",
            "Other",
        ],
    )
    challenge_other = ""
    if challenge == "Other":
        challenge_other = st.text_input("Please describe your other challenge:")

    # Q7
    cac_cost = st.radio(
        "Q7. How much does it typically cost you to acquire ONE new immigrant customer?",
        [
            "$0-50",
            "$51-100",
            "$101-200",
            "$201-500",
            "$500+",
            "Don't know / Don't track this",
        ],
    )

    # Q8
    finding_methods = st.multiselect(
        "Q8. How do you currently find immigrant customers? (Select all that apply)",
        [
            "Word of mouth/referrals",
            "Google Ads / Online advertising",
            "Social media ads (Facebook, Instagram, etc.)",
            "Community events",
            "Partnerships with immigration consultants/lawyers",
            "Real estate agents",
            "Settlement agencies (YMCA, ISSofBC, etc.)",
            "Ethnic media/newspapers",
            "We don't actively target them",
            "Other",
        ],
    )
    finding_other = ""
    if "Other" in finding_methods:
        finding_other = st.text_input("Please describe other methods you use:")

    # Q9
    satisfaction = st.slider(
        "Q9. On a scale of 1-10, how satisfied are you with your current methods of reaching immigrants?",
        min_value=1,
        max_value=10,
        value=5,
        help="1 = Very unsatisfied, 10 = Very satisfied",
    )

    st.divider()
    st.header("Section 3 · Paying for Customer Referrals")

    # Q10
    paid_referrals = st.radio(
        "Q10. Have you ever PAID for customer referrals or leads?",
        [
            "Yes, currently do this",
            "Yes, did in the past",
            "No, but open to it",
            "No, not interested in paying for referrals",
        ],
    )

    # Q11
    referral_interest = st.radio(
        "Q11. If a trusted platform could send you QUALIFIED immigrant customers, would you be interested?",
        [
            "Very interested - tell me more",
            "Somewhat interested",
            "Maybe, depends on details",
            "Not really interested",
            "Not interested at all",
        ],
    )

    # Q12
    st.markdown("**Q12. What would make you trust a referral platform? (Select up to 3)**")
    trust_factors = st.multiselect(
        "Select up to 3 options:",
        [
            "Verified customer information (real immigrants with real needs)",
            "Track record / proven results from other businesses",
            "Only pay for actual customers (not just clicks or leads)",
            "Clear, transparent pricing",
            "No long-term contract or commitment",
            "Ability to track where customers came from",
            "Other reputable businesses using it",
            "Free trial period",
            "Other",
        ],
    )
    trust_other = ""
    if "Other" in trust_factors:
        trust_other = st.text_input("Please describe any other factor that builds trust:")

    # Q13
    payment_model = st.radio(
        "Q13. Which payment model would you prefer? (Pick your TOP choice)",
        [
            "Pay per LEAD: Small fee for each potential customer (e.g., $25-50 per lead)",
            "Pay per CUSTOMER: Only pay when someone becomes a paying customer (e.g., $100-200)",
            "Commission: Pay percentage of what the customer spends (e.g., 10-15%)",
            "Monthly subscription: Fixed monthly fee for unlimited referrals (e.g., $500-1000/month)",
            "None of these - not interested in paying for referrals",
        ],
    )

    # Q14 - grid as three separate questions
    st.markdown("**Q14. For QUALIFIED immigrant leads, what would you be willing to pay?**")
    st.caption("Select one option for each payment model.")

    lead_options = ["$10-25", "$26-50", "$51-100", "Nothing - wouldn't pay"]
    customer_options = ["$50-100", "$101-200", "$201-500", "Nothing - wouldn't pay"]
    commission_options = ["5-10%", "11-20%", "21%+", "Nothing - wouldn't pay"]

    q14_lead = st.selectbox("Pay-per-lead (for each contact/lead)", lead_options)
    q14_customer = st.selectbox("Pay-per-customer (for each paying customer)", customer_options)
    q14_commission = st.selectbox("Commission rate (% of sale value)", commission_options)

    # Q15
    referral_volume = st.radio(
        "Q15. How many NEW immigrant customers per month would make paying for referrals worthwhile?",
        [
            "5-10 per month",
            "11-25 per month",
            "26-50 per month",
            "50+ per month",
            "Any amount helps",
            "Wouldn't pay for referrals",
        ],
    )

    # Q16
    refusal_reasons = st.multiselect(
        "Q16. What would make you say NO to a referral service? (Select all that apply)",
        [
            "Too expensive",
            "Don't trust the quality of leads",
            "Prefer organic/natural growth",
            "Bad past experience with referral services",
            "Don't need more customers right now",
            "Complicated setup or long contracts",
            "My competitors would also be on the platform",
            "Worried about data privacy",
            "Nothing - I'd be open to trying it",
            "Other",
        ],
    )
    refusal_other = ""
    if "Other" in refusal_reasons:
        refusal_other = st.text_input("Please describe any other reason you’d say no:")

    st.divider()
    st.header("Section 4 · Value & Timing")

    # Q17
    timing_value = st.radio(
        "Q17. A service that connects you with immigrants exactly when they need you (e.g., just arrived & need a phone plan) would be:",
        [
            "Extremely valuable - would definitely pay for this",
            "Very valuable - would likely pay for this",
            "Somewhat valuable - would consider it",
            "Not very valuable",
            "Not valuable at all",
        ],
    )

    # Q18
    discount = st.radio(
        "Q18. Would you offer a special discount to attract immigrant customers?",
        [
            "Yes, 10-20% discount",
            "Yes, 5-10% discount",
            "Maybe, depends on expected volume",
            "No, standard pricing only",
            "Not sure",
        ],
    )

    # Q19
    customer_info = st.multiselect(
        "Q19. What information about referred customers would you want? (Select all that apply)",
        [
            "Name and phone number",
            "Email address",
            "When they arrived in Canada",
            "Their country of origin",
            "What they specifically need from me",
            "Their location/city",
            "Language preference",
            "Immigration category (student, worker, PR, etc.)",
            "Just basic contact info is fine",
            "Other",
        ],
    )
    customer_info_other = ""
    if "Other" in customer_info:
        customer_info_other = st.text_input("Please describe any other information you’d like:")

    # Q20
    risk_free_trial = st.radio(
        "Q20. If there was a risk-free way to test getting immigrant referrals (no long-term commitment, cancel anytime), would you try it?",
        [
            "Yes, definitely would try it",
            "Probably yes",
            "Maybe - need more details",
            "Probably not",
            "No",
        ],
    )

    st.divider()
    st.header("Section 5 · Quick Demographics")

    # Q21
    business_age = st.radio(
        "Q21. How long have you been in business?",
        [
            "Less than 1 year",
            "1-3 years",
            "3-5 years",
            "5-10 years",
            "10+ years",
        ],
    )

    # Q22
    role = st.radio(
        "Q22. What's your role?",
        [
            "Owner/Founder",
            "Manager/Director",
            "Marketing/Sales",
            "Operations",
            "Other",
        ],
    )
    role_other = ""
    if role == "Other":
        role_other = st.text_input("Please specify your role:")

    # Q23
    company_size = st.radio(
        "Q23. Company size:",
        [
            "Just me (solo entrepreneur)",
            "2-10 employees",
            "11-50 employees",
            "51-200 employees",
            "200+ employees",
        ],
    )

    st.divider()
    st.header("Final Questions")

    # Q24
    extra_thoughts = st.text_area(
        "Q24. Any other thoughts on reaching immigrant customers or paying for referrals?",
        placeholder="Share any additional insights, concerns, or ideas...",
    )

    # Q25
    stay_updated = st.radio(
        "Q25. If we build a platform to connect businesses with immigrant customers, would you like to be notified?",
        [
            "Yes, keep me updated (provide email below)",
            "No thanks",
        ],
    )

    # Q26
    email = ""
    if "Yes" in stay_updated:
        email = st.text_input("Q26. Your email (optional):", placeholder="name@example.com")

    # ---------- SUBMIT ----------
    submitted = st.form_submit_button("Submit survey ✅")

    if submitted:
        # Simple check: enforce max 3 for Q12
        if len(trust_factors) > 3:
            st.error("Please select **no more than 3 options** for Q12.")
        else:
            # Write to CSV
            file_exists = os.path.isfile(CSV_PATH)
            with open(CSV_PATH, "a", newline="") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(
                        [
                            "timestamp",
                            "industry",
                            "industry_other",
                            "cities",
                            "immigrant_share",
                            "more_immigrants",
                            "difficulty",
                            "challenge",
                            "challenge_other",
                            "cac_cost",
                            "finding_methods",
                            "finding_other",
                            "satisfaction",
                            "paid_referrals",
                            "referral_interest",
                            "trust_factors",
                            "trust_other",
                            "payment_model",
                            "q14_lead",
                            "q14_customer",
                            "q14_commission",
                            "referral_volume",
                            "refusal_reasons",
                            "refusal_other",
                            "timing_value",
                            "discount",
                            "customer_info",
                            "customer_info_other",
                            "risk_free_trial",
                            "business_age",
                            "role",
                            "role_other",
                            "company_size",
                            "extra_thoughts",
                            "stay_updated",
                            "email",
                        ]
                    )

                writer.writerow(
                    [
                        datetime.now().isoformat(),
                        industry,
                        industry_other,
                        "; ".join(cities),
                        immigrant_share,
                        more_immigrants,
                        difficulty,
                        challenge,
                        challenge_other,
                        cac_cost,
                        "; ".join(finding_methods),
                        finding_other,
                        satisfaction,
                        paid_referrals,
                        referral_interest,
                        "; ".join(trust_factors),
                        trust_other,
                        payment_model,
                        q14_lead,
                        q14_customer,
                        q14_commission,
                        referral_volume,
                        "; ".join(refusal_reasons),
                        refusal_other,
                        timing_value,
                        discount,
                        "; ".join(customer_info),
                        customer_info_other,
                        risk_free_trial,
                        business_age,
                        role,
                        role_other,
                        company_size,
                        extra_thoughts,
                        stay_updated,
                        email,
                    ]
                )

            st.success("✅ Thank you for completing the survey!")
            st.info(
                "Your insights will help shape how businesses and immigrants connect in Canada. "
                "If you requested updates, we'll contact you when we have something to share."
            )
