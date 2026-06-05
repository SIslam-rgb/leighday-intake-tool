import streamlit as st
from responses import Response
from datastore import DataStore


def review_screen() -> None:
    """
    Display all answers for review and save to CSV on submission.
    """
    st.title("LEIGH DAY")
    st.subheader("Review Your Responses")
    st.divider()

    # display answers
    answers = st.session_state.get("answers", {})
    for question, answer in answers.items():
        st.write(f"**{question}:** {answer}")

    st.divider()

    if st.button("Submit", type="primary"):
        session_meta = {
            "case_ref": st.session_state["case_ref"],
            "associate_name": st.session_state["associate_name"],
            "interview_date": st.session_state["interview_date"]
        }
        response = Response(session_meta, answers)
        datastore = DataStore()
        try:
            datastore.save(response)
            st.session_state["screen"] = "complete"
            st.rerun()
        except IOError as e:
            st.error(f"Failed to save response: {e}")