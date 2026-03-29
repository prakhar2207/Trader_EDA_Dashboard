import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Trader Intelligence Dashboard",
    layout="wide"
)

# -----------------------------
# CUSTOM STYLING
# -----------------------------
st.markdown("""
<style>
.big-title {
    font-size:32px;
    font-weight:700;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    merged = pd.read_csv("merged.csv")
    trader_features = pd.read_csv("trader_features.csv")
    
    # Convert date
    merged['date'] = pd.to_datetime(merged['date'])
    
    return merged, trader_features

merged, trader_features = load_data()

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="big-title">📊 Trader Intelligence Dashboard</div>', unsafe_allow_html=True)
st.caption("Behavioral + Sentiment Analysis of Traders")

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

# 📅 Date Filter
min_date = merged['date'].min()
max_date = merged['date'].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

# 🧠 Cluster Filter
cluster_options = sorted(trader_features['cluster'].dropna().unique())
selected_clusters = st.sidebar.multiselect(
    "Select Cluster",
    options=cluster_options,
    default=cluster_options
)

# 👥 Trader Type Filter
trader_types = merged['trader_type'].dropna().unique()
selected_traders = st.sidebar.multiselect(
    "Trader Type",
    options=trader_types,
    default=trader_types
)

# 📊 Sentiment Filter
sentiments = st.sidebar.multiselect(
    "Market Sentiment",
    merged['classification'].dropna().unique(),
    default=merged['classification'].dropna().unique()
)

# 🔄 Reset Button
if st.sidebar.button("Reset Filters"):
    st.experimental_rerun()

# -----------------------------
# APPLY FILTERS
# -----------------------------
filtered = merged.copy()

# Date filter
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        (filtered['date'] >= pd.to_datetime(start_date)) &
        (filtered['date'] <= pd.to_datetime(end_date))
    ]

# Trader type filter
filtered = filtered[filtered['trader_type'].isin(selected_traders)]

# Sentiment filter
filtered = filtered[filtered['classification'].isin(sentiments)]

# Merge cluster info
cluster_map = trader_features[['account', 'cluster']]
filtered = filtered.merge(cluster_map, on='account', how='left')

# Apply cluster filter
filtered = filtered[filtered['cluster'].isin(selected_clusters)]

# -----------------------------
#  FILTER SUMMARY
# -----------------------------

cluster_labels = [f"Cluster {int(c)}" for c in selected_clusters]


trader_labels = ", ".join(selected_traders)

start = date_range[0].strftime("%b %d, %Y")
end = date_range[1].strftime("%b %d, %Y")

st.markdown(f"""
### 🔍 Active Filters

🗓 **Date:** {start} → {end}  
🧠 **Clusters:** {", ".join(cluster_labels)}  
👥 **Trader Types:** {trader_labels}
""")

# -----------------------------
# KPI SECTION
# -----------------------------
st.markdown("## 📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("📊 Trades", f"{len(filtered):,}")
col2.metric("👤 Traders", filtered['account'].nunique())
col3.metric("💰 Avg PnL", round(filtered['closed_pnl'].mean(), 2))
col4.metric("📈 Avg Trade Size", round(filtered['size_usd'].mean(), 2))

# -----------------------------
# PERFORMANCE VISUALS
# -----------------------------
st.markdown("## 📊 Performance Insights")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.violinplot(data=filtered, x='classification', y='closed_pnl', ax=ax)
    plt.xticks(rotation=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered, x='classification', y='size_usd', ax=ax)
    plt.xticks(rotation=30)
    st.pyplot(fig)

# -----------------------------
# BEHAVIOR ANALYSIS
# -----------------------------
st.markdown("## 📈 Behavioral Patterns")

col1, col2 = st.columns(2)

with col1:
    ratio = pd.crosstab(
        filtered['classification'],
        filtered['side'],
        normalize='index'
    )
    st.bar_chart(ratio)

with col2:
    segment = pd.crosstab(
        filtered['classification'],
        filtered['trader_type'],
        normalize='index'
    )
    st.bar_chart(segment)

# -----------------------------
# CLUSTER VISUALIZATION
# -----------------------------
st.markdown("## 🔥 Trader Archetypes")

fig, ax = plt.subplots()

scatter = ax.scatter(
    trader_features['num_trades'],
    trader_features['daily_pnl'],
    c=trader_features['cluster'],
    cmap='viridis'
)

ax.set_xlabel("Trading Activity")
ax.set_ylabel("Profitability")

st.pyplot(fig)

# -----------------------------
# MODEL SUMMARY
# -----------------------------
st.markdown("## 🤖 Model Intelligence")

col1, col2 = st.columns(2)

col1.success("Accuracy: ~70%")
col2.success("ROC-AUC: ~0.75")

st.info("""
- Strong at predicting profitable trades  
- Behavioral features dominate predictive power  
- Loss prediction remains challenging due to market noise  
""")

