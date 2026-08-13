import streamlit as st
import numpy as np
import joblib

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Cancer Prediction AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS - MODERN MEDICAL DASHBOARD
# ============================================================

st.markdown("""
<style>

/* ================================
   MAIN APPLICATION
================================ */

.stApp {
    background: #f4f7fb;
}


/* ================================
   MAIN CONTENT
================================ */

.block-container {
    padding-top: 3rem;
    padding-left: 3rem;
    padding-right: 3rem;
}


/* ================================
   TITLE
================================ */

.main-title {
    font-size: 44px;
    font-weight: 800;
    color: #102a43;
    letter-spacing: -1px;
    margin-bottom: 3px;
}


/* ================================
   SUBTITLE
================================ */

.subtitle {
    font-size: 17px;
    color: #627d98;
    margin-bottom: 25px;
}


/* ================================
   SECTION HEADINGS
================================ */

h2, h3 {
    color: #102a43 !important;
    font-weight: 750 !important;
}


/* ================================
   SIDEBAR
================================ */

[data-testid="stSidebar"] {
    background: #102a43;
    border-right: 1px solid #243b53;
}


/* Sidebar text */

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: #ffffff !important;
}


/* Sidebar divider */

[data-testid="stSidebar"] hr {
    border-color: #486581 !important;
}


/* ================================
   FORM CONTAINER
================================ */

div[data-testid="stForm"] {
    background: #ffffff;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #d9e2ec;
    box-shadow: 0px 8px 25px rgba(16, 42, 67, 0.08);
}


/* ================================
   INPUT LABELS
================================ */

label {
    font-weight: 600 !important;
    color: #334e68 !important;
}


/* ================================
   SELECT BOX
================================ */

div[data-baseweb="select"] > div {
    background-color: #ffffff;
    border: 1px solid #bcccdc;
    border-radius: 10px;
    transition: all 0.2s ease;
}


/* Select box hover */

div[data-baseweb="select"] > div:hover {
    border: 1px solid #2f80ed;
    box-shadow: 0 0 0 2px rgba(47,128,237,0.10);
}


/* ================================
   NUMBER INPUT
================================ */

div[data-testid="stNumberInput"] input {
    background: #ffffff !important;
    color: #102a43 !important;
    -webkit-text-fill-color: #102a43 !important;
    opacity: 1 !important;

    border: 1px solid #bcccdc;
    border-radius: 10px;
    font-weight: 600 !important;
}

/* Fix number values on mobile devices */
div[data-testid="stNumberInput"] input[type="number"] {
    color: #102a43 !important;
    -webkit-text-fill-color: #102a43 !important;
    opacity: 1 !important;
}


/* ================================
   BUTTON
================================ */

div.stButton > button,
button[kind="primaryFormSubmit"] {

    width: 100%;
    min-height: 52px;

    background: linear-gradient(
        135deg,
        #2f80ed,
        #56ccf2
    );

    color: white !important;

    border: none;
    border-radius: 12px;

    font-size: 18px;
    font-weight: 700;

    box-shadow:
        0 6px 15px rgba(47,128,237,0.25);

    transition: all 0.25s ease;
}


/* Button hover */

div.stButton > button:hover,
button[kind="primaryFormSubmit"]:hover {

    transform: translateY(-2px);

    box-shadow:
        0 10px 22px rgba(47,128,237,0.30);

    background: linear-gradient(
        135deg,
        #1d6fe8,
        #2db5e5
    );
}


/* ================================
   METRIC CARDS
================================ */

[data-testid="stMetric"] {

    background: #ffffff;

    padding: 20px;

    border-radius: 16px;

    border: 1px solid #d9e2ec;

    box-shadow:
        0 5px 18px rgba(16,42,67,0.07);

    transition: all 0.2s ease;
}


/* Metric hover */

[data-testid="stMetric"]:hover {

    transform: translateY(-3px);

    box-shadow:
        0 10px 25px rgba(16,42,67,0.12);
}


/* Metric label */

[data-testid="stMetricLabel"] {
    color: #627d98 !important;
    font-weight: 600;
}


/* Metric value */

[data-testid="stMetricValue"] {
    color: #102a43 !important;
    font-weight: 800;
}


/* ================================
   ALERT BOXES
================================ */

div[data-testid="stAlert"] {
    border-radius: 12px;
}


/* ================================
   PROGRESS BAR
================================ */

div[data-testid="stProgressBar"] {
    border-radius: 20px;
}


/* ================================
   EXPANDER
================================ */

[data-testid="stExpander"] {

    background: #ffffff;

    border: 1px solid #d9e2ec;

    border-radius: 14px;

    box-shadow:
        0 4px 15px rgba(16,42,67,0.06);
}


/* ================================
   DIVIDERS
================================ */

hr {
    border-color: #d9e2ec !important;
}


/* ================================
   FOOTER
================================ */

.stCaption {
    color: #829ab1 !important;
}


/* ================================
   WARNING BOX TEXT
================================ */

div[data-testid="stAlert"] {
    color: #102a43 !important;
}

div[data-testid="stAlert"] p {
    color: #102a43 !important;
    -webkit-text-fill-color: #102a43 !important;
    font-weight: 600 !important;
    opacity: 1 !important;
}

div[data-testid="stAlert"] span {
    color: #102a43 !important;
    -webkit-text-fill-color: #102a43 !important;
    opacity: 1 !important;
}

/* ================================
   SCROLLBAR
================================ */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #f4f7fb;
}

::-webkit-scrollbar-thumb {
    background: #9fb3c8;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #627d98;
}
/* =================================
   MOBILE RESPONSIVE DESIGN
   ================================= */

@media (max-width: 768px) {

    /* Use almost the full phone width */
    .block-container {
        padding-top: 1.5rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        padding-bottom: 1.5rem !important;
    }

    /* Make the form wider */
    div[data-testid="stForm"] {
        padding: 18px !important;
        border-radius: 18px !important;
    }

    /* Main title */
    .main-title {
        font-size: 36px !important;
        line-height: 1.15 !important;
    }

    /* Subtitle */
    .subtitle {
        font-size: 16px !important;
        line-height: 1.5 !important;
    }

    /* Section headings */
    h2, h3 {
        font-size: 30px !important;
        line-height: 1.2 !important;
    }

    /* Input controls */
    div[data-testid="stNumberInput"],
    div[data-baseweb="select"] {
        width: 100% !important;
    }

    /* Number input text */
    div[data-testid="stNumberInput"] input {
        font-size: 16px !important;
        color: #102a43 !important;
        -webkit-text-fill-color: #102a43 !important;
        opacity: 1 !important;
    }

    /* Buttons */
    div.stButton > button,
    button[kind="primaryFormSubmit"] {
        min-height: 50px !important;
        font-size: 17px !important;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        padding: 16px !important;
    }

    /* Make tables fit the phone */
    [data-testid="stDataFrame"] {
        width: 100% !important;
    }
}
/* =================================
   MOBILE PROGRESS TEXT
   ================================= */

@media (max-width: 768px) {

    div[data-testid="stProgress"] {
        margin-top: 8px !important;
    }

    div[data-testid="stProgress"] p {
        color: #102a43 !important;
        font-weight: 600 !important;
    }

}
</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD MODEL
# ============================================================
@st.cache_resource
def load_model():
    return joblib.load("random_forest_classifier_compressed.joblib")

try:
    model = load_model()
except Exception as e:
    st.error("❌ Model could not be loaded.")
    st.code(str(e))
    st.stop()

# ============================================================
# HEADER
# ============================================================
st.markdown('<div class="main-title">🩺 Cancer Prediction AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">'
    'A Random Forest based machine-learning application for cancer classification.'
    '</div>',
    unsafe_allow_html=True
)

st.warning(
    "🛡️ This application is an educational ML project and medical diagnosis. "
    
)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.header("📌 About the Model")
    st.write(
        "Enter the patient and tumor-related information and click "
        "**Predict Cancer** to generate a model prediction."
    )

    st.divider()

    st.subheader("📊 Model")
    st.write("Algorithm: **Random Forest Classifier**")

    st.subheader("🧩 Input Features")
    st.write("17 features are used by the trained model.")

    st.divider()

    if st.button("🔄 Reset All Inputs"):
        st.rerun()

# ============================================================
# INPUT FORM
# ============================================================
with st.form("prediction_form"):

    # --------------------------------------------------------
    # SECTION 1: PATIENT INFORMATION
    # --------------------------------------------------------
    st.subheader("👤 Patient Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            value=30,
            step=1,
            help="Patient age in years."
        )

    with col2:
        gender_label = st.selectbox(
            "Gender",
            options=["Female", "Male"],
            help="Select the patient's gender."
        )

    st.divider()

    # --------------------------------------------------------
    # SECTION 2: TUMOR INFORMATION
    # --------------------------------------------------------
    st.subheader("🔬 Tumor Information")

    col1, col2 = st.columns(2)

    with col1:
        tumor_size = st.number_input(
            "Tumor Size (cm)",
            min_value=0.0,
            value=2.5,
            step=0.1,
            format="%.2f",
            help="Approximate tumor size in centimeters."
        )

        location_map = {
            "Frontal": 0,
            "Occipital": 1,
            "Parietal": 2,
            "Temporal": 3
        }

        location_label = st.selectbox(
            "Tumor Location",
            options=list(location_map.keys()),
            help="Select the tumor location."
        )
        location = location_map[location_label]

    with col2:
        histology_map = {
            "Astrocytoma": 0,
            "Glioblastoma": 1,
            "Medulloblastoma": 2,
            "Meningioma": 3
        }

        histology_label = st.selectbox(
            "Histology Type",
            options=list(histology_map.keys()),
            help="Select the histology type."
        )
        histology = histology_map[histology_label]

        stage_map = {
            "Stage 0": 0,
            "Stage 1": 1,
            "Stage 2": 2,
            "Stage 3": 3,
            "Stage 4": 4
        }

        stage_label = st.selectbox(
            "Cancer Stage",
            options=list(stage_map.keys()),
            help="Select the cancer stage."
        )
        stage = stage_map[stage_label]

    st.divider()

    # --------------------------------------------------------
    # SECTION 3: SYMPTOMS
    # --------------------------------------------------------
    st.subheader("🩹 Symptoms")

    col1, col2, col3 = st.columns(3)

    symptom_options = {
        "None / Level 0": 0,
        "Level 1": 1,
        "Level 2": 2,
        "Level 3": 3
    }

    with col1:
        symptom_1_label = st.selectbox("Symptom 1", list(symptom_options.keys()))
        symptom_1 = symptom_options[symptom_1_label]

    with col2:
        symptom_2_label = st.selectbox("Symptom 2", list(symptom_options.keys()))
        symptom_2 = symptom_options[symptom_2_label]

    with col3:
        symptom_3_label = st.selectbox("Symptom 3", list(symptom_options.keys()))
        symptom_3 = symptom_options[symptom_3_label]

    st.divider()

    # --------------------------------------------------------
    # SECTION 4: TREATMENT
    # --------------------------------------------------------
    st.subheader("💊 Treatment Information")

    yes_no = {
        "No": 0,
        "Yes": 1
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        radiation_label = st.selectbox(
            "Radiation Treatment Received",
            list(yes_no.keys())
        )
        radiation = yes_no[radiation_label]

    with col2:
        surgery_label = st.selectbox(
            "Surgery Performed",
            list(yes_no.keys())
        )
        surgery = yes_no[surgery_label]

    with col3:
        chemo_label = st.selectbox(
            "Chemotherapy Received",
            list(yes_no.keys())
        )
        chemo = yes_no[chemo_label]

    st.divider()

    # --------------------------------------------------------
    # SECTION 5: MEDICAL HISTORY / MONITORING
    # --------------------------------------------------------
    st.subheader("📈 Medical History & Monitoring")

    col1, col2 = st.columns(2)

    with col1:
        survival_rate = st.number_input(
            "Survival Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=0.5,
            format="%.2f"
        )

        tumor_growth_rate = st.number_input(
            "Tumor Growth Rate",
            min_value=0.0,
            value=1.2,
            step=0.1,
            format="%.2f",
            help="Use the same unit/scale used during model training."
        )

    with col2:
        family_history_label = st.selectbox(
            "Family History of Cancer",
            list(yes_no.keys())
        )
        family_history = yes_no[family_history_label]

        mri_label = st.selectbox(
            "MRI Result Abnormality",
            list(yes_no.keys())
        )
        mri_result = yes_no[mri_label]

        follow_up_label = st.selectbox(
            "Follow-Up Required?",
            list(yes_no.keys())
        )
        follow_up = yes_no[follow_up_label]

    st.divider()

    # --------------------------------------------------------
    # PREDICT BUTTON
    # --------------------------------------------------------
    predict_button = st.form_submit_button(
        "🔍 Predict Cancer",
        use_container_width=True
    )

# ============================================================
# PREDICTION
# ============================================================
if predict_button:

    # IMPORTANT:
    # Keep this feature order exactly the same as the order
    # used when the Random Forest model was trained.
    input_data = np.array([[
        age,
        0 if gender_label == "Female" else 1,
        tumor_size,
        location,
        histology,
        stage,
        symptom_1,
        symptom_2,
        symptom_3,
        radiation,
        surgery,
        chemo,
        survival_rate,
        tumor_growth_rate,
        family_history,
        mri_result,
        follow_up
    ]])

    try:
        prediction = model.predict(input_data)[0]

        st.divider()
        st.subheader("📋 Prediction Result")

        # Binary classifier expected by the original application:
        # 0 = Benign, 1 = Malignant
        if int(prediction) == 1:
            st.error(
                "🔴 Model Prediction: Malignant"
            )
        else:
            st.success(
                "🟢 Model Prediction: Benign"
            )

        # ----------------------------------------------------
        # PREDICTION PROBABILITY
        # ----------------------------------------------------
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]

            classes = list(model.classes_)

            if 1 in classes:
                malignant_probability = probabilities[classes.index(1)] * 100
                benign_probability = 100 - malignant_probability

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Benign Probability",
                        f"{benign_probability:.2f}%"
                    )

                with col2:
                    st.metric(
                        "Malignant Probability",
                        f"{malignant_probability:.2f}%"
                    )

                st.progress(
                    int(round(malignant_probability)),
                    text=f"Malignant probability: {malignant_probability:.2f}%"
                )

        # ----------------------------------------------------
        # INPUT SUMMARY
        # ----------------------------------------------------
        with st.expander("📄 View Entered Patient Information"):
            summary = {
                "Age": age,
                "Gender": gender_label,
                "Tumor Size (cm)": tumor_size,
                "Tumor Location": location_label,
                "Histology": histology_label,
                "Cancer Stage": stage_label,
                "Symptom 1": symptom_1_label,
                "Symptom 2": symptom_2_label,
                "Symptom 3": symptom_3_label,
                "Radiation": radiation_label,
                "Surgery": surgery_label,
                "Chemotherapy": chemo_label,
                "Survival Rate (%)": survival_rate,
                "Tumor Growth Rate": tumor_growth_rate,
                "Family History": family_history_label,
                "MRI Abnormality": mri_label,
                "Follow-Up Required": follow_up_label
            }

            st.dataframe(summary, use_container_width=True)

    except Exception as e:
        st.error("❌ Prediction failed.")
        st.exception(e)

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.caption(
    "Educational machine-learning project • Random Forest Classifier • "
)
