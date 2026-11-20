**AI-Driven Financial Crime Risk Intelligence & Transaction Monitoring System**

1. Project Overview

This project aims to develop an automated data profiling, cleaning, validation and anomaly detection system specialised in Financial Crime Compliance (FCC) and Anti-Money Laundering (AML).

The system uses synthetic banking transaction data for development, testing and demonstration.

The objective is to improve transaction data quality, identify potential data issues and support financial crime compliance analysis through automated data processing and reporting.

2. Project Objectives

Identify missing and invalid transaction data.

Detect duplicate transaction records.

Analyse transaction data quality.

Perform advanced data profiling and metadata analysis.

Detect mixed data types and high-cardinality columns.

Analyse transaction distributions and correlations.

Identify potential PII and suspicious column names.

Generate structured JSON profiling reports.

Develop API-based access to profiling results.

Explore automated validation and machine learning-based anomaly detection.

3. Project Modules

Module 1 – Advanced Data Profiling

Implemented features:

Synthetic banking transaction dataset.

Missing value detection.

Duplicate transaction detection.

Invalid transaction amount detection.

Column-level data profiling.

Data quality score calculation.

Cardinality analysis.

Mixed data type detection.

Distribution analysis.

Correlation analysis.

Potential PII column detection.

Suspicious column name detection.

Transaction amount histogram.

Transaction count bar chart.

JSON profiling report generation.

FastAPI application with / and /profile endpoints.

Automated API testing using pytest.

Key deliverables:

profiling_report.json

main.py

test_api.py

transaction_amount_distribution.png

transaction_count_chart.png

Module 2 – Automated Data Cleaning

Planned features:

Data standardisation.

Missing value handling.

Duplicate management.

Data transformation.

Cleaning logs.

Cleaned CSV output.

Module 3 – AI Validation and Anomaly Detection

Planned features:

Rule-based validation.

Anomaly detection.

Transaction pattern analysis.

Validation reports.

Module 4 – Integration and Production Engineering

Planned features:

End-to-end pipeline.

Testing and documentation.

Docker integration.

Final project demonstration.

4. Technology Stack

Python

Google Colab

GitHub

Pandas

Matplotlib

FastAPI

Uvicorn

Pytest

JSON

CSV

Machine Learning (planned)

5. API Endpoints

Endpoint

Description

/

API health check

/profile

Retrieve the data profiling report

The API is developed using FastAPI and tested using FastAPI TestClient.

6. Testing and Quality Assurance

Automated API tests have been implemented using pytest.

Current test results:

Home endpoint test – PASSED

Profile endpoint test – PASSED

Duplicate detection test – PASSED

Test Summary: 3 passed, 0 failed.

7. Data Visualisation

The project currently includes:

Transaction Amount Distribution Histogram.

Transaction Count by Transaction ID Bar Chart.

These visualisations support the exploration of synthetic transaction data.

8. Data Privacy and Governance

This project uses synthetic data only.

No real customer information, confidential banking information or actual financial crime investigation records are used.

The system is designed to support human review and does not independently determine criminal activity.

Potential PII and suspicious column detection currently use column-name-based screening and should not be treated as complete detection mechanisms.

9. Current Project Status

Module 1 – Advanced Data Profiling: Initial implementation and core features developed.

The current implementation includes data profiling, data quality analysis, visualisations, JSON reporting, API development and basic automated testing.

Further refinement, documentation and validation are required before Module 1 is considered fully complete.

Modules 2, 3 and 4 are planned for subsequent development.

10. Disclaimer

This is an educational prototype for data quality management and financial crime compliance technology.

It does not replace professional AML investigations, regulatory requirements or human decision-making.
