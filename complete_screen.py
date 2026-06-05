import streamlit as st
from datastore import DataStore


def complete_screen() -> None:
    """
    Display completion confirmation and allow CSV export and new intake.
    """
    st.title("LEIGH DAY")
    st.subheader("Questionnaire Complete")
    st.write("Responses have been saved successfully.")
    st.divider()

    # display session summary
    st.write(f"**Case Reference:** {st.session_state['case_ref']}")
    st.write(f"**Associate Name:** {st.session_state['associate_name']}")
    st.write(f"**Interview Date:** {st.session_state['interview_date']}")
    st.divider()

    # load and offer CSV download
    datastore = DataStore()
    df = datastore.load()

    if not df.empty: # convert dataframe to CSV string for download
        csv = df.to_csv(index=False)
        st.download_button(
            label="Export CSV",
            data=csv,
            file_name="responses.csv",
            mime="text/csv"
        )

    st.divider()

    # start a new intake session
    if st.button("Start New Intake"):
        st.session_state["case_ref"] = ""
        st.session_state["associate_name"] = ""
        st.session_state["interview_date"] = ""
        st.session_state["answers"] = {}
        st.session_state["screen"] = "welcome"
        st.rerun()