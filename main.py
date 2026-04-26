import json
import os
import ast
import operator
import streamlit as st

# ============================
#   إعدادات الصفحة
# ============================

st.set_page_config(
    page_title="المساعد الذكي",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');

* { font-family: 'Tajawal', sans-serif; direction: rtl; }

body { background-color: #0f0f1a; }

.stApp {
    background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
    min-height: 100vh;
}

h1, h2, h3 { color: #e2b96f !important; }

.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #1e1e3a !important;
    color: #f0f0f0 !important;
    border: 1px solid #3a3a6a !important;
    border-radius: 10px !important;
    font-family: 'Tajawal', sans-serif !important;
    font-size: 16px !important;
    direction: rtl !important;
}

.stButton > button {
    background: linear-gradient(135deg, #e2b96f, #c89a4f) !important;
    color: #0f0f1a !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Tajawal', sans-serif !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    padding: 0.5rem 2rem !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 20px rgba(226,185,111,0.4) !important;
}

.stSelectbox > div > div {
    background: #1e1e3a !important;
    color: #f0f0f0 !important;
    border: 1px solid #3a3a6a !important;
    border-radius: 10px !important;
    font-family: 'Tajawal', sans-serif !important;
    direction: rtl !important;
}

.result-box {
    background: #1e1e3a;
    border: 1px solid #3a3a6a;
    border-right: 4px solid #e2b96f;
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    margin-top: 1rem;
    color: #f0f0f0;
    font-size: 16px;
    line-height: 1.8;
    direction: rtl;
    text-align: right;
}

.success-box {
    background: #0d2b1e;
    border: 1px solid #1a5c38;
    border-right: 4px solid #2ecc71;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    margin-top: 1rem;
    color: #a8f0c6;
    font-size: 18px;
    font-weight: 700;
    direction: rtl;
    text-align: right;
}

.error-box {
    background: #2b0d0d;
    border: 1px solid #5c1a1a;
    border-right: 4px solid #e74c3c;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    margin-top: 1rem;
    color: #f0a8a8;
    direction: rtl;
    text-align: right;
}

.memory-item {
    background: #1e1e3a;
    border: 1px solid #3a3a6a;
    border-radius: 8px;
    padding: 0.7rem 1rem;
    margin: 0.3rem 0;
    color: #f0f0f0;
    direction: rtl;
    text-align: right;
}

.memory-key { color: #e2b96f; font-weight: 700; }
.memory-val { color: #a0c4ff; }

.sidebar-title {
    color: #e2b96f !important;
    font-size: 22px !important;
    font-weight: 900 !important;
    text-align: center;
    margin-bottom: 1rem;
}

div[data-testid="stSidebar"] {
    background: #0d0d1f !important;
    border-left: 1px solid #3a3a6a !important;
}

div[data-testid="stSidebar"] * {
    color: #f0f0f0 !important;
}

.stRadio > div {
    gap: 0.5rem !important;
}

.stRadio > div > label {
    background: #1e1e3a !important;
    border: 1px solid #3a3a6a !important;
    border-radius: 8px !important;
    padding: 0.5rem 1rem !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    direction: rtl !important;
    text-align: right !important;
}

.stRadio > div > label:hover {
    border-color: #e2b96f !important;
    background: #2a2a4a !important;
}

hr {
    border-color: #3a3a6a !important;
}

p, label, .stMarkdown {
    color: #c0c0d0 !important;
    direction: rtl !important;
    text-align: right !important;
}
</style>
""", unsafe_allow_html=True)

# ============================
#   نظام الذاكرة
# ============================

MEMORY_FILE = "memory.json"


def