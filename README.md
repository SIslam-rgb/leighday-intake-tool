## Leigh Day Intake Tool

## Introduction
At Leigh Day we sepcialise in human rights, personal injury, and group litigation. I work as a Data Analyst within the firm, supporting the international human rights department. A significant part of this work involves large-scale group litigation cases where legal teams travel to regions across Africa, Asia, and South America to conduct field interviews with potential claimants.

Currently, lawyers conducting these eligibility interviews record claimant responses using Excel spreadsheets. While functional, this approach has several limitations. Excel is not optimised for structured data entry in field conditions, there is no built-in input validation, and the resulting files vary in format between interviewers, which creates significant cleaning work before the data can be uploaded into our database and or used analytically. Inconsistent formatting across submissions has caused delays in case preparation and increases the risk of data entry errors on sensitive legal records.

The Minimum Viable Product I have developed is a desktop application built using [Python](https://docs.python.org/3/) using [Streamlit](https://docs.streamlit.io/), designed to standardise and streamline the claimant intake process. The application guides a lawyer through a structured questionnaire for each claimant, combining open text, numeric, date, and yes/no question types. Validation is applied at the point of entry, where a response does not meet the expected format, an error message is displayed and progression to the next question is blocked. This ensures stored records are clean, consistent, and suitable for analytical review. This is particularly important in a legal context where inaccurate claimant data could affect case preparation and claimant eligibility assessments. A dedicated review screen acts as an additional safeguard, allowing the lawyer to check all responses before final submission.

Responses are saved to a [CSV file](https://docs.python.org/3/library/csv.html) that can be exported at the end of each session. CSV was chosen because it is lightweight, requires no database setup, and can be opened directly in [MS Excel](https://www.microsoft.com/en-gb/microsoft-365/excel) by legal staff who are already familiar with that format. Each session captures consistent column headers and data types regardless of which lawyer conducts the interview, meaning CSV files from multiple field trips can be merged and analysed without manual cleaning.

## Design

### GUI Design

**Figure 1:** Show the high-fidelity mockup that was produced in Figma prior to development. It reflect Leigh Day's black, white, and grey brand identity and was designed to show the intended user journey from entry of case details upon start of interview through to data export. The hi-fi mockup was used to plan the screen layout, validation points and navigate flow before implementation. It both represnets the final visual appearance of the application as well as structure, sequence and user interaction.

![Figure 1: Hi-Fi Mockup illustraing the user journey and screen flow of the Leigh Day Intake Tool](assets/design_overview.png)

**Figure 1:** Hi-Fi mockup

### Functional Requirements

| # | Requirement |
|---|-------------|
| FR1 | The application must present a structured claimant intake questionnaire consisting of open text, numeric, date, and yes/no question types |
| FR2 | Each question must validate input against its expected format and display an inline error message if the entry does not meet the required rules |
| FR3 | Session metadata including case reference number, interviewing lawyer name, and interview date must be captured before the questionnaire begins |
| FR4 | Completed claimant responses must be appended to a persistent CSV file stored locally on the device |
| FR5 | The lawyer must be able to review all claimant responses on a summary screen before final submission |
| FR6 | On completion, the application must allow the lawyer to export the responses CSV file for use in case preparation |
| FR7 | The application must support starting a new claimant intake session without closing or restarting the application |

### Non-Functional Requirements

| # | Requirement |
|---|-------------|
| NFR1 | The application must run locally without an internet connection to support field use |
| NFR2 | The interface must be intuitive enough for non-technical legal staff to use without training |
| NFR3 | Input validation errors must be clearly communicated to the user at the point of entry |
| NFR4 | The CSV output must be consistently formatted across sessions regardless of interviewer |
| NFR5 | The application must be portable and runnable on Windows |

### Tech Stack Outline
- [Python 3](https://docs.python.org/3/) - core programming language
- [csv](https://docs.python.org/3/library/csv.html) - local data storage in CSV format
- [datetime](https://docs.python.org/3/library/datetime.html) - timestamp generation
- [Streamlit](https://docs.streamlit.io/) -To build interactive web app

### Code Design

![class diagram](assets/class_diagram.png)

## Development
## Development

The application is structured across multiple files, each with a single responsibility. Screen navigation is handled through Streamlit's session state, which persists data between reruns. The data model is built using object-oriented programming principles, with validation logic separated into pure functions to support independent testing.

### Project Structure

```
leigh-day-intake-tool/
├── app.py                  ← main entry point and screen routing
├── welcome_screen.py       ← screen 1
├── intake_screen.py        ← screen 2
├── review_screen.py        ← screen 3
├── complete_screen.py      ← screen 4
├── question.py             ← Question base class and subclasses
├── questionnaire.py        ← Questionnaire class
├── response.py             ← Response class
├── datastore.py            ← DataStore class
├── validation.py           ← pure validation functions
├── test_validation.py      ← pytest unit tests
└── assets/                 ← Figma design screenshots
```

### App Routing — app.py

`app.py` is the main entry point. It initialises session state and routes the user to the correct screen based on the value of `st.session_state.screen`. Each screen is imported as a function from its own file, keeping the routing logic clean and separate from the UI logic.

```python
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
```

### OOP Design — models.py

The application uses inheritance and polymorphism to model different question types. A base Question class defines shared attributes — label, field type, and whether the question is required. Four subclasses inherit from it and each define their own validate() method with type-specific logic. This means the intake screen can call question.validate(value) on any question regardless of its type, and the correct validation logic runs automatically.

```python
class NumericQuestion(Question):
    """A question that expects a positive number response."""

    def __init__(self, label: str, required: bool = True) -> None:
        super().__init__(label, "numeric", required)

    def validate(self, value: str) -> bool:
        return validate_numeric(value)
```

### Pure Validation Functions — validation.py

Validation logic is separated into pure functions in `validation.py`. Each function takes a string and returns a boolean - they can be tested independently with pytest without needing to run the full application.

```python
def validate_numeric(value: str) -> bool:
    try:
        return float(value.strip()) > 0
    except ValueError:
        return False
```

### Persistent Storage — datastore.py

The `DataStore` class handles reading from and writing to `responses.csv`. On first submission it creates the file with headers. Subsequent submissions append new rows without repeating the headers. On the completion screen the file is read back and passed to Streamlit's download button for export.

```python
def save(self, response: Response) -> None:
    try:
        row = response.to_dict()
        df_new = pd.DataFrame([row])
        if os.path.exists(self._filepath):
            df_new.to_csv(self._filepath, mode='a', header=False, index=False)
        else:
            df_new.to_csv(self._filepath, mode='w', header=True, index=False)
    except Exception as e:
        raise IOError(f"Failed to save response: {e}")
```




