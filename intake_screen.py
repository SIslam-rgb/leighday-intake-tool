import streamlit as st
from questionnaire import Questionnaire

def intake_screen() -> None:
    """
    Render the intake form screen.
    Displays each question and validates input before allowing submission.
    """
    st.title("LEIGH DAY")
    st.caption(f"Case Ref: {st.session_state['case_ref']}")
    st.divider()
    
    # load the questionnaire and get the list of questions
    questionnaire = Questionnaire()
    questions = questionnaire.questions

    st.subheader("Claimant Questionnaire")
    st.write(f"Please complete all {questionnaire.total_questions()} questions.")
    st.divider()
    
    # pull existing answers from session state so they persist on rerun
    answers = st.session_state.get("answers", {})

    for question in questions:
        answer = st.text_input(question.label, key=question.label)
        if answer:
            answers[question.label] = answer #store only if something given

    st.divider()

    if st.button("Review Responses"):
        errors = []# collect all validation failures before showing them
        for question in questions:
            value = answers.get(question.label, "")
            if question.required and not question.validate(value):
                errors.append(f"Invalid response for: {question.label}")

        if errors:
            for error in errors:
                st.error(error) #show all for user to fix
        else:
            st.session_state["answers"] = answers #all valid just save
            st.session_state["screen"] = "review"
            st.rerun()

