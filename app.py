"""
Leighday Intake Tool
Main entry point - This manages the memory and routing
"""
import streamlit as st


def init_state() -> None:
    """set deafult state values
    """
    #Session metadata i.e. administartive data
    st.session_state.setdefault("case_ref","")
    st.session_state.setdefault("associate_name","")
    st.session_state.setdefault("interview_date","")
    #Claimant answers
    st.session_state.setdefault("answers",{}) #reserve a container for all answers

def main() -> None:

    init_state() #call memory

    #current user screen
    screen = st.session_state.screen

    #Check what screen user is on and route them accordingly
    if screen == "welcome":
        welcome_screen()
    elif screen == "intake":
        intake_screen()
    elif screen == "review":
        review_screen()
    elif screen == "complete":
        complete_screen()
    else:
        st.error(f'Unknown Screen: {st.session_state.screen}') #flag if some screen is wrong and just redirect to welcome
        st.session_state.screen = "welcome"
        st.rerun()

if __name__ == '__main__':
    main()

    


























from welcome_screen import welcome_screen
# from intake_screen import intake_screen
# from review_screen import review_screen
# from complete_screen import complete_screen





# def main() -> None:
#     """Main function. Routes to the correct screen based on session state."""
#     st.set_page_config(
#         page_title="Leigh Day Intake Tool",
#         layout="centered"
#     )

#     init_state()

#     screen = st.session_state.screen

#     if screen == "welcome":
#         welcome_screen()
#     elif screen == "intake":
#         intake_screen()
#     elif screen == "review":
#         review_screen()
#     elif screen == "complete":
#         complete_screen()
#     else:
#         st.session_state.screen = "welcome"
#         st.rerun()


# if __name__ == "__main__":
#     main()