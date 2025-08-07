# Aquaria-Morocco Data Analysis Project

## Overview

This project analyzes the Moroccan market for Aquaria's Atmospheric Water Generator (AWG) products. Aquaria specializes in AWGs that produce clean, potable water from air, targeting residential, commercial, and community applications. The company aims to address water security challenges, particularly in regions affected by drought or limited water infrastructure, such as Morocco. This project provides a data-driven roadmap to support Aquaria's potential market entry.

## Objectives

### Primary Objective

Conduct a comprehensive market analysis to evaluate the viability and strategic approach for Aquaria's AWG entry into the Moroccan market.

### Secondary Objectives

1.  **Market Demand Assessment**
    *   Quantify water scarcity levels across different Moroccan regions
    *   Identify geographic hotspots with the highest water stress indicators
    *   Analyze seasonal water availability patterns and drought frequency
    *   Assess current water infrastructure gaps in target areas
2.  **Target Market Segmentation**
    *   Map potential customer segments:
        *   Residential households in water-stressed areas
        *   Commercial businesses (hotels, restaurants, offices)
        *   Industrial facilities requiring clean water
        *   Community centers and public institutions
    *   Evaluate purchasing power and willingness to invest in AWG technology
    *   Identify early adopter profiles and decision-making factors
3.  **Competitive Landscape Analysis**
    *   Identify existing water solution providers in Morocco
    *   Analyze alternative water sources (bottled water, water delivery services)
    *   Assess pricing structures of current water solutions
    *   Evaluate competitive advantages of AWG technology vs. alternatives
4.  **Regulatory and Infrastructure Assessment**
    *   Research water quality standards and regulations in Morocco
    *   Analyze electricity infrastructure required for AWG operation
    *   Identify potential government incentives for sustainable water solutions
    *   Assess import/distribution requirements for AWG equipment
5.  **Market Entry Strategy Recommendations**
    *   Prioritize target cities/regions based on data analysis
    *   Recommend optimal market entry approach:
        *   Direct sales vs. partnerships
        *   B2B vs. B2C focus
        *   Pilot program locations
    *   Suggest pricing strategies adapted to local market conditions
    *   Identify key success factors and potential barriers
6.  **Financial Viability Assessment**
    *   Estimate total addressable market (TAM) size in Morocco
    *   Project potential revenue from identified target segments
    *   Analyze cost structures for market entry and operations
    *   Develop ROI projections for different market scenarios

## Success Metrics

*   **Quantitative Analysis:** Water stress indices, market size estimates, demographic data
*   **Qualitative Insights:** Regulatory landscape, cultural factors, adoption barriers
*   **Strategic Clarity:** Clear go/no-go recommendation with supporting rationale
*   **Actionable Intelligence:** Specific city targets, customer segments, and entry strategies

## Expected Outcomes

1.  Data-driven market assessment with geographic prioritization
2.  Customer segmentation framework for targeted marketing
3.  Competitive positioning strategy highlighting AWG advantages
4.  Regulatory compliance roadmap for market entry
5.  Financial projections supporting investment decisions
6.  Implementation timeline with key milestones

## Alignment with Aquaria's Mission

These objectives directly support Aquaria's goal of addressing water security challenges by:

*   Identifying communities most in need of sustainable water solutions
*   Ensuring market entry strategies align with local needs and capabilities
*   Maximizing positive impact while maintaining business viability
*   Supporting sustainable development goals in water-stressed regions

## Project Structure

```
Aquaria-Morocco_Data-Analysis_Project/
├── .gitignore
├── README.md          # This file, providing an overview of the project
├── requirements.txt   # List of Python dependencies
├── dashboards/        # Directory containing dashboard files
├── data/              # Directory for storing data
│   ├── external/      # Data from external sources
│   ├── processed/     # Processed data ready for analysis
│   └── raw/           # Raw, unprocessed data
├── documentations/    # Project documentation and reports
│   └── quaria.pdf     # Project description PDF
│   └── Timeline.xlsx  # Project timeline
├── models/            # Trained machine learning models
├── notebooks/         # Jupyter notebooks for data exploration and analysis
│   ├── eda/           # Notebooks for exploratory data analysis
│   ├── financial_modeling/ # Notebooks for financial modeling
│   └── ml_models/     # Notebooks for machine learning models
├── reports/           # Generated reports and visualizations
├── scripts/           # Python scripts for data collection and processing
│   ├── data_collection.py # Script for collecting data
│   └── morocco_water_statistics.py # Script for water statistics analysis
└── visuals/           # Directory for storing visualizations
```

## Setup Environment

To set up the environment for this project, you need to install the required dependencies. You can do this using pip:

```bash
pip install -r requirements.txt
```

### Create and Access a Virtual Environment

It is recommended to create a virtual environment to isolate the project dependencies.

1.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

2.  **Activate the virtual environment:**

    *   **Linux/macOS:**

        ```bash
        source venv/bin/activate
        ```

    *   **Windows:**

        ```bash
        venv\Scripts\activate
        ```

## Morocco Water Statistics Script

This project includes a Python script, `scripts/morocco_water_statistics.py`, that provides structured data and analysis related to water resources in Morocco. The script uses the `pandas` and `numpy` libraries to create DataFrames containing national water overview data, regional dam performance data, government investment data, and time series data for trend analysis.

### Usage

To run the script, execute the following command:

```bash
python scripts/morocco_water_statistics.py
```

The script will print key metrics and example analyses to the console. It also includes a function to export the datasets to CSV files for further analysis.

### Data Sources

The data used in this script is sourced from the Ministry of Equipment and Water and other publicly available sources.

### Key Features

*   **DataFrames:** The script uses `pandas` DataFrames to store and manipulate the data.
*   **Market Opportunity Scoring:** The script calculates a market opportunity score for each region based on water stress indicators.
*   **Key Metrics:** The script calculates key metrics for AWG market analysis, such as water crisis severity, infrastructure failure rate, and government investment ready USD.
*   **Export to CSV:** The script includes a function to export the datasets to CSV files for further analysis.

### Examples

The script includes several examples of how to use the data, such as:

*   Finding the highest priority regions for AWG deployment
*   Calculating market size indicators
*   Tracking government investment opportunities
*   Identifying competitive advantages
