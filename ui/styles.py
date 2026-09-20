import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* ==================================================
           GLOBAL
        ================================================== */

        @import url(
            'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
        );

        html,
        body,
        [class*="css"] {
            font-family: "Inter", sans-serif;
        }

        .stApp {
            background: #ffffff;
            color: #202124;
        }

        .block-container {
            max-width: 1380px;
            padding-top: 2.5rem;
            padding-bottom: 3rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }


        /* ==================================================
           SIDEBAR
        ================================================== */

        section[data-testid="stSidebar"] {
            background: #f8f9fa;
            border-right: 1px solid #e8eaed;
        }

        section[data-testid="stSidebar"] > div {
            padding-top: 2rem;
            padding-left: 1.2rem;
            padding-right: 1.2rem;
        }

        .sidebar-label {
            margin-top: 1.8rem;
            margin-bottom: 0.7rem;

            color: #5f6368;

            font-size: 0.72rem;
            font-weight: 700;

            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        section[data-testid="stSidebar"] hr {
            border: none;
            border-top: 1px solid #dadce0;
            margin: 1.5rem 0;
        }


        /* ==================================================
           BRAND
        ================================================== */

        .brand {
            display: flex;
            align-items: center;
            gap: 0.7rem;

            margin-bottom: 1.5rem;
        }

        .brand-icon {
            width: 38px;
            height: 38px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 10px;

            background: #1a73e8;
            color: white;

            font-size: 1.2rem;
            font-weight: 800;

            box-shadow: 0 3px 10px rgba(26, 115, 232, 0.18);
        }

        .brand-name {
            color: #202124;

            font-size: 1.35rem;
            font-weight: 700;

            letter-spacing: -0.03em;
        }


        /* ==================================================
           HERO
        ================================================== */

        .hero {
            background: #f8f9fa;

            border: 1px solid #edf0f2;
            border-radius: 18px;

            padding: 2.4rem 2.5rem;

            margin-bottom: 2.2rem;

            box-shadow: 0 4px 18px rgba(60, 64, 67, 0.06);
        }

        .hero-eyebrow {
            color: #1a73e8;

            font-size: 0.75rem;
            font-weight: 700;

            letter-spacing: 0.1em;
            text-transform: uppercase;

            margin-bottom: 0.7rem;
        }

        .hero-title {
            color: #202124;

            font-size: 2.5rem;
            font-weight: 800;

            letter-spacing: -0.045em;
            line-height: 1.15;

            margin-bottom: 0.8rem;
        }

        .hero-description {
            max-width: 850px;

            color: #5f6368;

            font-size: 1rem;
            line-height: 1.7;
        }


        /* ==================================================
           SECTION HEADER
        ================================================== */

        .section-header {
            margin-top: 2rem;
            margin-bottom: 1.2rem;
        }

        .section-title {
            color: #202124;

            font-size: 1.35rem;
            font-weight: 700;

            letter-spacing: -0.02em;
        }

        .section-subtitle {
            color: #5f6368;

            font-size: 0.88rem;

            margin-top: 0.25rem;
        }


        /* ==================================================
           MARKET CARDS
        ================================================== */

        .market-card {
            background: #ffffff;

            border: 1px solid #dadce0;
            border-radius: 16px;

            padding: 1.3rem 1.4rem;

            min-height: 125px;

            box-shadow: 0 2px 8px rgba(60, 64, 67, 0.06);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;
        }

        .market-card:hover {
            transform: translateY(-2px);

            box-shadow:
                0 8px 24px rgba(60, 64, 67, 0.10);
        }

        .market-name {
            color: #5f6368;

            font-size: 0.85rem;
            font-weight: 600;

            margin-bottom: 0.55rem;
        }

        .market-price {
            color: #202124;

            font-size: 1.55rem;
            font-weight: 700;

            letter-spacing: -0.025em;
        }

        .market-change {
            margin-top: 0.45rem;

            font-size: 0.82rem;
            font-weight: 600;
        }

        .positive {
            color: #188038;
        }

        .negative {
            color: #d93025;
        }


        /* ==================================================
           KPI CARDS
        ================================================== */

        .kpi {
            background: #ffffff;

            border: 1px solid #dadce0;
            border-radius: 14px;

            padding: 1.2rem 1.3rem;

            min-height: 105px;

            box-shadow: 0 2px 8px rgba(60, 64, 67, 0.05);
        }

        .kpi-label {
            color: #5f6368;

            font-size: 0.78rem;
            font-weight: 600;

            margin-bottom: 0.45rem;
        }

        .kpi-value {
            color: #202124;

            font-size: 1.45rem;
            font-weight: 700;

            letter-spacing: -0.02em;
        }

        .kpi-description {
            color: #80868b;

            font-size: 0.75rem;

            margin-top: 0.35rem;
        }


        /* ==================================================
           CONTENT CARDS
        ================================================== */

        .content-card {
            background: #ffffff;

            border: 1px solid #dadce0;
            border-radius: 16px;

            padding: 1.5rem;

            margin-top: 1rem;

            box-shadow: 0 2px 8px rgba(60, 64, 67, 0.05);
        }


        /* ==================================================
           CONFIGURATION PANEL
        ================================================== */

        .config-panel {
            background: #f8f9fa;

            border: 1px solid #e8eaed;
            border-radius: 16px;

            padding: 1.4rem;

            margin-bottom: 1.5rem;
        }

        .config-title {
            color: #202124;

            font-size: 1rem;
            font-weight: 700;

            margin-bottom: 1rem;
        }


        /* ==================================================
           STREAMLIT INPUTS
        ================================================== */

        div[data-baseweb="select"] > div {
            background: #ffffff;

            border-color: #dadce0;

            border-radius: 10px;
        }

        div[data-baseweb="select"] > div:hover {
            border-color: #1a73e8;
        }

        input {
            border-radius: 10px !important;
        }


        /* ==================================================
           BUTTONS
        ================================================== */

        .stButton > button {
            background: #1a73e8;

            color: #ffffff;

            border: none;
            border-radius: 9px;

            padding: 0.55rem 1.15rem;

            font-weight: 600;

            transition:
                background 0.2s ease,
                box-shadow 0.2s ease;
        }

        .stButton > button:hover {
            background: #1557b0;

            color: #ffffff;

            box-shadow:
                0 4px 12px rgba(26, 115, 232, 0.22);
        }


        /* ==================================================
           TABS
        ================================================== */

        button[data-baseweb="tab"] {
            font-weight: 600;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #1a73e8;
        }


        /* ==================================================
           AI REPORT
        ================================================== */

        .ai-report {
            background: #f8f9fa;

            border-left: 4px solid #1a73e8;

            border-radius: 0 12px 12px 0;

            padding: 1.4rem 1.5rem;

            margin-top: 1rem;

            color: #3c4043;

            line-height: 1.7;
        }

        .ai-label {
            color: #1a73e8;

            font-size: 0.75rem;
            font-weight: 700;

            letter-spacing: 0.08em;
            text-transform: uppercase;

            margin-bottom: 0.6rem;
        }


        /* ==================================================
           METRIC IMPROVEMENTS
        ================================================== */

        [data-testid="stMetric"] {
            background: #ffffff;

            border: 1px solid #dadce0;

            border-radius: 14px;

            padding: 1rem 1.1rem;

            box-shadow: 0 2px 8px rgba(60, 64, 67, 0.05);
        }

        [data-testid="stMetricLabel"] {
            color: #5f6368;
        }

        [data-testid="stMetricValue"] {
            color: #202124;
        }


        /* ==================================================
           DIVIDERS
        ================================================== */

        hr {
            border: none;

            border-top: 1px solid #e8eaed;

            margin: 1.8rem 0;
        }


        /* ==================================================
           FOOTER
        ================================================== */

        .footer {
            text-align: center;

            color: #80868b;

            font-size: 0.78rem;

            line-height: 1.6;

            margin-top: 4rem;
            padding-top: 1.5rem;

            border-top: 1px solid #e8eaed;
        }


        /* ==================================================
           RESPONSIVE
        ================================================== */

        @media (max-width: 900px) {

            .block-container {
                padding-left: 1.2rem;
                padding-right: 1.2rem;
            }

            .hero {
                padding: 1.7rem;
            }

            .hero-title {
                font-size: 2rem;
            }

        }


        @media (max-width: 600px) {

            .hero-title {
                font-size: 1.7rem;
            }

            .hero-description {
                font-size: 0.9rem;
            }

            .brand-name {
                font-size: 1.15rem;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )