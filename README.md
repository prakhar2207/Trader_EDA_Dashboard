# 📊 Trader Intelligence Dashboard

### Behavior + Sentiment Driven Analysis of Trading Performance

---

## 🚀 Overview

This project analyzes how **market sentiment (Fear/Greed)** impacts **trader behavior and performance** using real trading data from Hyperliquid.

It combines:

* 📊 Data Analysis
* 🧠 Behavioral Finance
* 🤖 Machine Learning
* 📈 Interactive Dashboard (Streamlit)

The goal is to uncover **actionable trading insights** and build a system that can **analyze and predict trader performance**.

---

## 🎯 Objectives

* Understand how **Fear vs Greed** affects trader performance
* Analyze **behavioral patterns** (activity, position size, consistency)
* Segment traders into meaningful groups
* Predict **next-day profitability** using ML
* Build an **interactive dashboard** for exploration

---

## 📂 Dataset

### 1. Market Sentiment Data

* Bitcoin Fear & Greed Index
* Columns:

  * `date`
  * `classification` (Fear / Greed / Extreme levels)

---

### 2. Trader Data

* Historical trading records
* Key columns:

  * `account`
  * `size_usd`
  * `side` (BUY/SELL)
  * `closed_pnl`
  * `timestamp`

---

## ⚙️ Methodology

### 🔹 Data Preparation

* Cleaned and merged datasets on **daily level**
* Checked for missing values and duplicates
* Created key metrics:

  * Daily PnL
  * Win rate
  * Trade frequency
  * Average trade size
  * Long/Short ratio
  * Leverage proxy (derived from trade size)

---

### 🔹 Feature Engineering

#### Behavioral Features

* `num_trades` → activity
* `avg_size` → position sizing
* `trade_intensity` → aggression
* `consistency` → discipline

#### Temporal Features

* `pnl_lag1` → recent performance
* `trade_change` → activity shift

#### Market Context

* `sentiment_score` (encoded Fear → Greed)

---

### 🔹 Exploratory Analysis

* PnL distribution across sentiment regimes
* Behavioral changes (activity, size, direction)
* Long vs Short ratio
* Risk-taking patterns
* Time-series trends

---

### 🔹 Trader Segmentation (Clustering)

Using KMeans, traders were grouped into:

| Cluster                | Description                      |
| ---------------------- | -------------------------------- |
| 🟣 Elite Traders       | High consistency, strong returns |
| 🔴 Aggressive Traders  | High activity, high risk         |
| 🔵 Balanced Traders    | Moderate behavior                |
| ⚫ Inconsistent Traders | Low performance                  |

👉 Key Insight:
**Consistency > Aggression**

---

### 🔹 Predictive Modeling

Model: **Random Forest Classifier**

#### 🎯 Task:

Predict **next-day profitability**

#### 📊 Performance:

* Accuracy: **~70%**
* ROC-AUC: **~0.75**

#### 💡 Insight:

> Behavioral features are stronger predictors than sentiment alone.

---

## 📊 Key Insights

### 🔥 1. Overtrading reduces profitability

High-frequency traders generate volume but not efficiency

---

### 🔥 2. Fear markets offer better opportunities

Higher returns with better risk efficiency

---

### 🔥 3. Consistency outperforms aggression

Disciplined traders achieve the best results

---

### 🔥 4. Behavior > Sentiment

Trader behavior is more predictive than market sentiment

---

## 💡 Strategy Recommendations

### ✅ Trade Less, Trade Better

Avoid unnecessary trades

### ✅ Focus on Fear Regimes

Better opportunities exist during Fear

### ✅ Maintain Discipline

Consistency is the strongest edge

---

## 🖥️ Interactive Dashboard

Built using **Streamlit**

### Features:

* 📅 Date filtering
* 🧠 Cluster filtering
* 👥 Trader-type filtering
* 📊 Dynamic charts
* 🔄 Reset filters
* 🤖 Model performance display

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit

---

## 📁 Project Structure

```bash
📦 trader-intelligence-dashboard
 ┣ 📜 app.py
 ┣ 📜 analysis.ipynb
 ┣ 📜 merged.csv
 ┣ 📜 trader_features.csv
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd trader-intelligence-dashboard
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Dashboard

```bash
streamlit run app.py
```

---

### 5️⃣ Open in Browser

```
http://localhost:8501
```

---

## 📌 Requirements

Example `requirements.txt`:

```bash
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## 🏆 Conclusion

This project demonstrates that:

> **Trader behavior is the primary driver of performance, not just market sentiment.**

By combining:

* Behavioral analysis
* Sentiment signals
* Machine learning

we can extract meaningful insights even from noisy financial data.

---

## 🙌 Author

**Prakhar Shukla**
Data Science | Machine Learning | Quant Analysis

---
