import streamlit as st


# --------------------------------------------------
# Brand
# --------------------------------------------------

def brand():

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">Q</div>
            <div class="brand-name">QuantX</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Hero
# --------------------------------------------------

def hero(
    title,
    description,
    eyebrow="QUANTITATIVE FINANCIAL INTELLIGENCE"
):

    html = f"""
<div class="hero">
    <div class="hero-eyebrow">{eyebrow}</div>
    <div class="hero-title">{title}</div>
    <div class="hero-description">{description}</div>
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Section Header
# --------------------------------------------------

def section(title, subtitle=""):

    html = f"""
<div class="section-header">
    <div>
        <div class="section-title">{title}</div>
        <div class="section-subtitle">{subtitle}</div>
    </div>
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Market Card
# --------------------------------------------------

def market_card(name, price, change=None):

    change_html = ""

    if change is not None:

        css_class = (
            "positive"
            if change >= 0
            else "negative"
        )

        symbol = "+" if change >= 0 else ""

        change_html = f"""
<div class="market-change {css_class}">
    {symbol}{change:.2f}%
</div>
"""

    html = f"""
<div class="market-card">
    <div class="market-name">{name}</div>
    <div class="market-price">{price}</div>
    {change_html}
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# KPI Card
# --------------------------------------------------

def kpi(label, value, description=""):

    html = f"""
<div class="kpi">
    <div class="kpi-label">{label}</div>
    <div class="kpi-value">{value}</div>
    <div class="kpi-description">{description}</div>
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Footer
# --------------------------------------------------

def footer():

    st.markdown(
        """
        <div class="footer">

            QuantX · Quantitative Multi-Asset Financial Intelligence

            <br><br>

            Historical analysis and backtesting only.
            Past performance does not guarantee future results.

        </div>
        """,
        unsafe_allow_html=True
    )