# 🏏 Cricket Player Role Prediction

This project is a **web-based application** that predicts the role of a cricket player (**Batsman**, **Bowler**, or **All-rounder**) based on their career performance statistics. Users can input key stats, and the app instantly returns the most likely role.

## 📌 Project Overview

* The application uses a **Flask** backend with a rule-based classification system.
* Users enter stats such as runs, batting average, wickets, bowling average, and economy rate.
* The backend applies predefined logic to predict the player’s role.
* Results are displayed instantly on the web page.

## 📊 Roles

The application predicts one of the following:

* 🏏 **Batsman**
* 🎯 **Bowler**
* ⚡ **All-rounder**

## 📂 Dataset

The project uses a structured cricket player dataset with the following columns:

* `Player` — Name of the cricketer
* `Batting_Avg` — Career batting average
* `Runs` — Total career runs
* `Bowling_Avg` — Career bowling average
* `Wickets` — Total career wickets
* `Economy_Rate` — Bowling economy rate
* `Role` — Target label (Batsman, Bowler, All-rounder)

## 🛠️ Technologies Used

* **Python**
* **Flask** (backend)
* **HTML/CSS** (frontend)
* **Pandas** (data handling)
* **Scikit-learn** (exploratory ML model development in Jupyter Notebook)

## ⚙️ How It Works

1. **User Input:** Player stats are entered via the web form.
2. **Processing:** Data is sent to the Flask backend.
3. **Prediction Logic:** `model.py` applies role classification rules based on thresholds.
4. **Output:** The predicted role is shown on the result page.

