

import streamlit as st
from validation import validate_date
from validation import validate_text

def welcome_screen() -> None:
    """
    Render the welcome screen.
    """
    st.title("LEIGH DAY")
    st.subheader("Claimant Intake Tool")
    st.caption("International Human Rights Case Questionnaire")
    st.divider()

    case_ref = st.text_input("Case Reference Number")
    associate_name = st.text_input("Associate Name")
    interview_date = st.text_input("Interview Date (DD/MM/YYYY)")

    st.divider()

    if st.button("Begin Questionnaire"):
        if not (case_ref):
            st.error("Please enter a case reference number.")
        elif not validate_text(associate_name):
            st.error("Please enter the interviewing associate name.")
        elif not validate_date(interview_date):
            st.error("Please enter a valid date in DD/MM/YYYY format.")
        else:
            st.session_state["case_ref"] = case_ref
            st.session_state["associate_name"] = associate_name
            st.session_state["interview_date"] = interview_date
            st.session_state["screen"] = "intake"
            st.rerun()
    
    

