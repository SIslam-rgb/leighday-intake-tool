import streamlit as st

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

    #Ensure all fields answered
    if st.button("Begin Questionnaire"):
        if not case_ref.strip():
            st.error("Please enter a case reference number.")
        elif not associate_name.strip():
            st.error("Please enter the interviewing associates name.")
        elif not interview_date.strip():
            st.error("Please enter the interview date.")
        else:
            st.session_state["case_ref"] = case_ref 
            st.session_state["associate_name"] = associate_name
            st.session_state["interview_date"] = interview_date
            st.session_state["screen"] = "intake" #move to next screen
            st.rerun()