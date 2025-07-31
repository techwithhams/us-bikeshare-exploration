# 🚲 US Bikeshare Data Exploration Project

**Python + pandas + CLI App | Udacity Nanodegree Project**

This project explores bikeshare data from three major US cities — Chicago, New York City, and Washington — through a command-line interface (CLI) application built in Python. Users can interactively filter data by city, month, and day to uncover commuting patterns, usage behavior, and demographic trends.

---

## 🎯 Project Objective

To develop a Python-based CLI app that enables users to explore real-world bikeshare data, applying data wrangling and filtering techniques to extract insights on how and when people use the service.

---

## 🧰 Tools & Skills

- **🐍 Language**: Python 3  
- **📦 Libraries**: pandas, numpy, time  
- **🧹 Techniques**: Data wrangling, datetime filtering, CLI interaction  
- **💻 Skills Applied**: Exploratory data analysis (EDA), user input validation, programmatic reporting

---

## 📂 Dataset

This project uses bikeshare usage data provided by Udacity for:

- **Chicago**: `chicago.csv`  
- **New York City**: `new_york_city.csv`  
- **Washington**: `washington.csv`

Each file contains details about individual trips made in the bikeshare system, including timestamps, trip duration, station locations, and user demographics.

> ⚠️ **Note**: The datasets are not included in this repository due to size limitations and licensing. You can obtain them from [Udacity's course materials](https://www.udacity.com/course/data-analyst-nanodegree--nd002) or request them from official sources.

---


## 📁 Project Structure

```
bikeshare-analysis/
├── bikeshare.py              # Main Python script (CLI app)
└── README.md                 # Project overview and instructions
```

---

## 🔍 Key Insights

- 🕔 Peak usage occurs around **5–6 PM**, indicating strong commuter activity.
- 📅 **Wednesdays** show high trip volumes across all cities.
- 🚉 Major hubs like **Columbus Circle** and **Union Station** are frequently used.
- 👥 Younger riders dominate in cities with available birth year data.
- 🧭 While patterns vary slightly, weekday commuting is a strong common trend.

---

## 💡 Recommendations

- 🚲 **Peak Hour Optimization**: Increase bike availability between 5–7 PM, the busiest usage window.
- 🛤️ **Station Planning**: Add stations near the most common start–end point pairs to improve access.
- 🧑‍🤝‍🧑 **Demographic Targeting**: Leverage weekday vs. weekend trends to cater to commuters vs. leisure users.

These insights can help bikeshare companies and urban planners make data-informed operational and strategic decisions.

---

## 🚀 How to Use

1. Clone this repository or download the `bikeshare.py` file and datasets.
2. Run the script in your terminal:

```bash
python bikeshare.py
```

3. Follow the prompts to explore the data interactively.

---

📬 **Author**: Hams Saeed Alhakim
📚 Udacity Data Analyst Nanodegree
🔗 **GitHub**: [github.com/techwithhams](https://github.com/techwithhams)
🗓 **Date**: 2024

