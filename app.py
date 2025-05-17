import streamlit as st
import pandas as pd
from joblib import load

# Memuat model dari file yang sudah disimpan
model = load('model/model_rf.pkl')  # Load model yang sudah disimpan

# Judul aplikasi dengan ikon
st.markdown("<h1 style='text-align: center; color: #28a745;'>📊 Mahasiswa Dropout Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Prediksi status mahasiswa apakah mereka akan lulus atau dropout berdasarkan data yang dimasukkan.</p>", unsafe_allow_html=True)

# Sidebar for navigation menu
st.sidebar.markdown("<h2 style='color: #6c757d;'>🔧 Menu Utama</h2>", unsafe_allow_html=True)
menu = st.sidebar.radio('Pilih Opsi:', ['Formulir Prediksi'])

# Main content
if menu == 'Formulir Prediksi':

    st.markdown("### 🎯 Silakan isi data berikut untuk memprediksi status mahasiswa", unsafe_allow_html=True)

    def get_user_input():
        """Collect user inputs for prediction"""
        
        # Create two columns for input
        col1, col2 = st.columns(2)

        with col1:
            Application_order = st.number_input('Urutan Pendaftaran', min_value=1, max_value=10, value=1)
            Previous_qualification_grade = st.number_input('Nilai Kualifikasi Sebelumnya', min_value=0.0, max_value=200.0, value=90.0)
            Admission_grade = st.number_input('Nilai Penerimaan', min_value=0.0, max_value=200.0, value=90.0)
            Curricular_units_1st_sem_enrolled = st.number_input('Mata Kuliah 1st Sem Diambil', min_value=0, max_value=30, value=0)
            Curricular_units_1st_sem_approved = st.number_input('Mata Kuliah 1st Sem Disetujui', min_value=0, max_value=30, value=0)
            Curricular_units_1st_sem_credited = st.number_input('SKS 1st Sem Diakui', min_value=0, max_value=30, value=0)
            Curricular_units_1st_sem_grade = st.number_input('Nilai 1st Sem', min_value=0.0, max_value=30.0, value=0.0)
            Curricular_units_2nd_sem_grade = st.number_input('Nilai 2nd Sem', min_value=0.0, max_value=30.0, value=0.0)
        
        with col2:
            Curricular_units_2nd_sem_enrolled = st.number_input('Mata Kuliah 2nd Sem Diambil', min_value=0, max_value=30, value=0)
            Curricular_units_2nd_sem_approved = st.number_input('Mata Kuliah 2nd Sem Disetujui', min_value=0, max_value=30, value=0)
            Daytime_evening_attendance = st.radio('Kehadiran (Siang/Malam)', ('Daytime', 'Evening'))
            Tuition_fees_up_to_date = st.radio('Pembayaran Up-to-date', ('Yes', 'No'))
            Gender = st.radio('Jenis Kelamin', ('Male', 'Female'))
            Scholarship_holder = st.radio('Penerima Beasiswa', ('Yes', 'No'))
            Displaced = st.radio('Mahasiswa Pindahan', ('Yes', 'No'))
            Debtor = st.radio('Status Debitur', ('Yes', 'No'))

        # Prepare data in a dictionary for the user input
        input_data = {
            'Application_order': Application_order,
            'Previous_qualification_grade': Previous_qualification_grade,
            'Admission_grade': Admission_grade,
            'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
            'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
            'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
            'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
            'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
            'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
            'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
            'Daytime_evening_attendance': 1 if Daytime_evening_attendance == 'Daytime' else 0,
            'Tuition_fees_up_to_date': 1 if Tuition_fees_up_to_date == 'Yes' else 0,
            'Gender': 1 if Gender == 'Male' else 0,
            'Scholarship_holder': 1 if Scholarship_holder == 'Yes' else 0,
            'Displaced': 1 if Displaced == 'Yes' else 0,
            'Debtor': 1 if Debtor == 'Yes' else 0,
        }

        return pd.DataFrame(input_data, index=[0])

    df_input = get_user_input()

    # Ensure that the features match exactly what the model was trained on
    expected_features = model.feature_names_in_

    # Check if all expected features are present in the input
    missing_features = set(expected_features) - set(df_input.columns)
    if missing_features:
        for feature in missing_features:
            df_input[feature] = 0  # Fill missing columns with 0 (or appropriate default value)
    
    # Reorder the input columns to match the model's expected order
    df_input = df_input[expected_features]

    # Make the prediction
    y_pred_test = model.predict(df_input)

    # Display results
    st.markdown("### 📊 Hasil Prediksi Status Mahasiswa", unsafe_allow_html=True)
    status = 'Dropout' if y_pred_test[0] == 1 else 'Graduate'
    color = 'red' if status == 'Dropout' else 'green'

    # Display prediction and probability
    if hasattr(model, 'predict_proba'):
        y_pred_proba = model.predict_proba(df_input)
        proba = round(y_pred_proba[0][y_pred_test[0]], 3)
        st.markdown(f"<h4 style='color:{color};'>📝 {status} dengan probabilitas {proba}</h4>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h4 style='color:{color};'>📝 {status} (Probabilitas tidak tersedia)</h4>", unsafe_allow_html=True)
