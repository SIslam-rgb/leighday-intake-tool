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




