# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Domain Proyek

**Jaya Jaya Institut** adalah lembaga pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Seiring dengan perkembangannya, institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat banyak juga mahasiswa yang tidak menyelesaikan pendidikannya alias **dropout**. Tingginya angka **dropout** ini tentunya menjadi masalah besar bagi institusi pendidikan seperti Jaya Jaya Institut. Oleh karena itu, **Jaya Jaya Institut** ingin mendeteksi lebih awal mahasiswa yang berpotensi **dropout**, sehingga dapat diberi perhatian dan bimbingan khusus.

### Permasalahan Bisnis

Berdasarkan latar belakang yang ada, berikut adalah permasalahan utama yang perlu dianalisis untuk membantu manajer HR dalam mengelola tingkat **dropout** yang tinggi:

1. **Apa saja faktor-faktor yang mempengaruhi tinggi rendahnya angka dropout di Jaya Jaya Institut?**
2. **Bagaimana perbedaan tingkat dropout berdasarkan jenis kelamin, usia, atau status pernikahan mahasiswa?**
3. **Model prediksi apa yang dapat digunakan untuk mengidentifikasi mahasiswa yang berisiko tinggi melakukan dropout?**
4. **Bagaimana cara menyajikan hasil analisis yang mudah dipahami oleh pihak manajemen dan pengambil keputusan di Jaya Jaya Institut?**

### Cakupan Proyek

Proyek ini akan mencakup beberapa aspek analisis dan implementasi sebagai berikut:

1. **Analisis Faktor-Faktor yang Mempengaruhi Tingginya Angka Dropout**
   - Melakukan eksplorasi terhadap data mahasiswa untuk mengidentifikasi faktor-faktor yang mempengaruhi **dropout**. Faktor-faktor yang akan dianalisis meliputi:
     - **Status Akademik (Nilai Kualifikasi Sebelumnya, Nilai Penerimaan)**
     - **Keuangan Mahasiswa (Apakah Pembayaran Tepat Waktu)**
     - **Usia dan Jenis Kelamin**
     - **Tingkat Keterlibatan dan Kehadiran dalam Perkuliahan**
2. **Analisis Perbedaan Tingkat Dropout Berdasarkan Demografi**

   - Menganalisis perbedaan tingkat **dropout** berdasarkan **jenis kelamin**, **usia**, dan **status pernikahan** mahasiswa untuk mengetahui pola-pola yang relevan.

3. **Pembangunan Model Prediksi untuk Identifikasi Mahasiswa yang Berisiko Dropout**

   - Membangun model prediksi menggunakan algoritma **Logistic Regression**, **Random Forest**, atau **Decision Trees** untuk mengidentifikasi mahasiswa yang berisiko tinggi melakukan **dropout** berdasarkan faktor-faktor yang telah dianalisis.

4. **Penyajian Hasil Analisis dalam Bentuk Dashboard yang Mudah Dipahami**
   - Menyajikan hasil analisis dalam bentuk **dashboard interaktif** yang mudah dipahami oleh pihak manajemen. Dashboard ini akan menampilkan visualisasi yang jelas mengenai:
     - Faktor-faktor penyebab **dropout**
     - Prediksi mahasiswa yang berisiko **dropout**
     - Perbandingan **dropout** berdasarkan kategori demografis

## Persiapan

**Sumber Data**: [Dataset Mahasiswa Jaya Jaya Institut](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv)

### Setup Environment:

```bash
# Install dependencies
pip install -r requirements.txt
```

### Membuka `notebook.ipynb`

1. Pastikan seluruh **dependensi** yang diperlukan telah terinstal dengan benar sesuai dengan daftar di `requirements.txt`.
2. Buka dan jalankan seluruh isi **`notebook.ipynb`** di Google Colab atau IDE Python yang mendukung notebook (misalnya Jupyter Notebook, VSCode).
3. Di dalam notebook ini, Anda akan melakukan analisis data, menemukan pola-pola yang relevan, dan mendapatkan **insight** terkait **attrition mahasiswa** berdasarkan berbagai faktor.
4. Setelah notebook berjalan, temukan visualisasi, statistik, dan insight yang diperoleh untuk memahami hubungan antara faktor-faktor penyebab tingginya **dropout** mahasiswa.

### Menjalankan Dashboard dengan Streamlit

1.  **Buka file `app.py`** yang telah disediakan untuk aplikasi Streamlit. Aplikasi ini akan memuat visualisasi dan prediksi terkait **attrition mahasiswa**.
2.  **Jalankan aplikasi Streamlit** dengan cara:

    ```bash
    streamlit run app.py
    ```

3.  **Visualisasi** yang ditampilkan di aplikasi Streamlit akan mencakup:

    - **Prediksi status dropout atau graduate** berdasarkan input data mahasiswa.
    - **Dashboard interaktif** untuk memantau faktor-faktor yang mempengaruhi tingkat **dropout** di **Jaya Jaya Institut**.
    - **Kinerja model prediksi** seperti **accuracy**, **precision**, **recall**, dan **F1-score** untuk memberikan insight yang jelas kepada pihak pengelola.

### Menjalankan Metabase untuk Dashboard

Jika Anda ingin menggunakan **Metabase** untuk visualisasi lebih lanjut dan pembuatan dashboard interaktif berbasis **SQL**, ikuti langkah-langkah berikut:

1.  **Unduh image Metabase** dari Docker Hub:

    ```bash
    docker pull metabase/metabase:latest
    ```

2.  **Jalankan container Metabase** dengan perintah:

    ```bash
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```

3.  **Login ke Metabase**:

    - Buka **[http://localhost:3000/setup](http://localhost:3000/setup)** di browser.
    - Gunakan kredensial berikut untuk login:

      - **Username**: root@mail.com
      - **Password**: root123

4.  **Set up Business Dashboard**:

    - Setelah login berhasil, buat dashboard interaktif untuk memonitor **dropout mahasiswa** serta menganalisis faktor-faktor yang menyebabkan mahasiswa **dropout**.
    - Dashboard ini dapat membantu manajer untuk melihat secara langsung **status** mahasiswa berdasarkan faktor-faktor penting seperti **jenis kelamin**, **usia**, **status pernikahan**, dan lainnya.

## Business Dashboard

### Ringkasan Dashboard

Dashboard ini memberikan gambaran visual yang jelas tentang faktor-faktor yang mempengaruhi tingkat dropout di **Jaya Jaya Institut**, dengan fokus pada analisis data mahasiswa yang ada. Dashboard ini menggabungkan beberapa grafik untuk menggambarkan tingkat dropout berdasarkan berbagai fitur, seperti **jenis kelamin**, **program studi**, **pendidikan sebelumnya**, dan **keseimbangan kehidupan kerja**.

### Faktor Utama

1. **Tingkat Dropout Berdasarkan Jenis Kelamin**:

   - Perbandingan antara **laki-laki** dan **perempuan** menunjukkan bahwa tingkat dropout di antara **laki-laki** sedikit lebih tinggi dibandingkan dengan **perempuan**.

2. **Tingkat Dropout Berdasarkan Program Studi**:

   - Mahasiswa dari program **Nursing** menunjukkan tingkat dropout yang sangat tinggi dibandingkan dengan program lainnya seperti **Veterinary Nursing** dan **Management**.

3. **Tingkat Dropout Berdasarkan Keseimbangan Kehidupan Kerja**:
   - Mahasiswa dengan keseimbangan kehidupan kerja yang buruk lebih cenderung untuk keluar dari program pendidikan mereka dibandingkan dengan mereka yang memiliki keseimbangan kerja dan kehidupan yang baik.

### Fitur yang Paling Berpengaruh Terhadap Keputusan Mahasiswa untuk Dropout

Berdasarkan hasil analisis di dashboard, berikut adalah **10 fitur yang paling berpengaruh** terhadap keputusan mahasiswa untuk keluar (dropout) dari institut:

1. **Nilai Kualifikasi Sebelumnya**:

   - Mahasiswa dengan **nilai kualifikasi yang lebih rendah** memiliki tingkat dropout yang lebih tinggi.

2. **Mata Kuliah yang Diambil dan Disetujui**:

   - Mahasiswa yang tidak lulus **mata kuliah pada semester pertama** lebih cenderung untuk keluar.

3. **Program Studi**:

   - Program studi tertentu seperti **Nursing** dan **Veterinary Nursing** memiliki tingkat dropout yang lebih tinggi dibandingkan program studi lainnya.

4. **Pendidikan Sebelumnya**:

   - Mahasiswa yang memiliki pendidikan sebelumnya di bidang lain, selain **pendidikan dasar**, lebih berisiko untuk keluar.

5. **Keseimbangan Kehidupan Kerja**:

   - Mahasiswa yang kesulitan menyeimbangkan kehidupan kerja dan akademik lebih cenderung untuk dropout.

6. **Status Beasiswa**:

   - Mahasiswa yang tidak menerima **beasiswa** menunjukkan kecenderungan yang lebih tinggi untuk dropout.

7. **Usia Mahasiswa**:

   - Mahasiswa yang lebih muda atau lebih tua dibandingkan dengan kelompok usia rata-rata menunjukkan tingkat dropout yang lebih tinggi.

8. **Jenis Kelamin**:

   - Tingkat dropout **laki-laki** lebih tinggi dibandingkan dengan **perempuan**.

9. **Kehadiran di Kelas**:

   - Mahasiswa yang sering **tidak hadir** memiliki kemungkinan lebih tinggi untuk dropout.

10. **Status Mahasiswa**:
    - Mahasiswa dengan **status enrolled** yang memiliki kecenderungan untuk tidak lulus pada ujian atau tugas lebih besar risikonya untuk dropout.

### Hasil Prediksi

Berikut adalah perbandingan hasil prediksi untuk berbagai model yang digunakan dalam analisis ini:

| Model             | Accuracy | Precision | Recall   | F1 Score |
| ----------------- | -------- | --------- | -------- | -------- |
| **Decision Tree** | 0.847107 | 0.833119  | 0.840711 | 0.836490 |
| **Random Forest** | 0.903581 | 0.899750  | 0.889915 | 0.894407 |

- **Accuracy**: Model **Random Forest** memiliki **akurasi 90.36%**, yang menunjukkan bahwa model ini sangat baik dalam memprediksi mahasiswa yang akan keluar atau bertahan.
- **Precision**: **Random Forest** memiliki **precision 89.98%**, yang berarti 89.98% dari mahasiswa yang diprediksi akan keluar benar-benar keluar dari institut, menunjukkan kinerja yang sangat baik.
- **Recall**: Model ini memiliki **recall 88.99%**, yang menunjukkan bahwa model ini dapat memprediksi hampir 89% mahasiswa yang benar-benar keluar.
- **F1 Score**: **Random Forest** memiliki **F1 score 89.44%**, menunjukkan keseimbangan yang sangat baik antara precision dan recall.
  miliki **F1 score 56.25%**, menunjukkan keseimbangan antara precision dan recall meskipun recall bisa ditingkatkan.

## Menjalankan Sistem Machine Learning

1. **Buka terminal atau command prompt**.
2. Ketik perintah `jupyter notebook` dan tekan **Enter**. Ini akan membuka antarmuka Jupyter Notebook di browser web Anda.
3. Pilih file notebook yang ingin Anda gunakan untuk melanjutkan langkah-langkah berikut.

#### **Langkah 2: Lakukan Analisis Data Eksploratif (EDA)**

1. **Baca dataset** yang Anda miliki ke dalam notebook, misalnya:
   ```python
   import pandas as pd
   data = pd.read_csv('data_siswa.csv')
   ```
2. **Eksplorasi data** untuk memahami struktur dan pola penting, seperti:
   - Menampilkan beberapa baris pertama dataset: `data.head()`
   - Menyusun statistik deskriptif: `data.describe()`
   - Memeriksa nilai yang hilang: `data.isnull().sum()`
3. **Identifikasi atribut** yang dapat mempengaruhi kemungkinan dropout, seperti data demografis dan akademik (misalnya, usia, nilai rata-rata, jenis kelamin, status beasiswa, dll.).

#### **Langkah 3: Skalasi Atribut dengan StandardScaler**

1. **Identifikasi atribut numerik** yang memiliki rentang nilai yang berbeda dan memerlukan skala.
2. Gunakan `StandardScaler` dari `scikit-learn` untuk menormalkan data numerik:
   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X))
   ```

#### **Langkah 4: Buat Model dengan Random Forest**

1. **Pisahkan data menjadi fitur dan target**. Misalnya, target adalah status siswa (graduate, dropout, enrolled):
   ```python
   X = data.drop('status', axis=1)
   y = data['status'] 
   ```
2. **Bagi data menjadi set pelatihan dan pengujian**:
   ```python
   from sklearn.model_selection import train_test_split
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
   ```
3. **Buat model Random Forest** menggunakan `RandomForestClassifier` dari `scikit-learn`:
   ```python
   param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
   }
   grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42), param_grid=param_grid, cv=3)=
   grid_search.fit(X_train_selected, y_train_resampled_series)
   best_model = grid_search.best_estimator_
   rf_predictions = best_model.predict(X_test_selected)
   ```
4. **Evaluasi model** menggunakan data pengujian:

   ```python
   def evaluate_model(model, y_test, predictions):
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average='macro')  # Changed to 'weighted' for multiclass
    recall = recall_score(y_test, predictions, average='macro')  # Changed to 'weighted' for multiclass
    f1 = f1_score(y_test, predictions, average='macro')  # Changed to 'weighted' for multiclass
    evaluation_df = pd.DataFrame({
        'Model': [model],
        'Accuracy': [accuracy],
        'Precision': [precision],
        'Recall': [recall],
        'F1 Score': [f1]
    })
    return evaluation_df
   evaluation_df = pd.concat([
    evaluate_model('Decision_tree', y_test, dt_predictions),
    evaluate_model('Random Forest', y_test, rf_predictions)
   ])
   # Displaying the evaluation results
   print(evaluation_df)
   ```

5. **Cek fitur penting** untuk memahami faktor-faktor yang paling berpengaruh pada prediksi dropout:

   ```python
   feature_importance = model.feature_importances_
   print(feature_importance)
   ```

6. **Simpan model dan encoder** untuk digunakan nantinya:
   ```python
   import joblib
   joblib.dump(pipeline, 'model_rf.pkl')
   print("Model berhasil disimpan!")
   ```

#### **Langkah 5: Buat Streamlit GUI untuk Klasifikasi Siswa**

1. **Buat file Python baru** untuk aplikasi Streamlit:
   ```python

   import streamlit as st
   import pandas as pd
   from joblib import load
   
   model = load('model/model_rf.pkl') # Load model yang sudah disimpan
   st.markdown("<h1 style='text-align: center; color: #28a745;'>📊 Mahasiswa Dropout Prediction</h1>", unsafe_allow_html=True)
   st.markdown("<p style='text-align: center;'>Prediksi status mahasiswa apakah mereka akan lulus atau dropout berdasarkan data yang dimasukkan.</p>", unsafe_allow_html=True)
   st.sidebar.markdown("<h2 style='color: #6c757d;'>🔧 Menu Utama</h2>", unsafe_allow_html=True)
   menu = st.sidebar.radio('Pilih Opsi:', ['Formulir Prediksi'])
   
    df_input = df_input[expected_features]

   
    y_pred_test = model.predict(df_input)


    st.markdown("### 📊 Hasil Prediksi Status Mahasiswa", unsafe_allow_html=True)
    status = 'Dropout' if y_pred_test[0] == 1 else 'Graduate'
    color = 'red' if status == 'Dropout' else 'green'


    if hasattr(model, 'predict_proba'):
        y_pred_proba = model.predict_proba(df_input)
        proba = round(y_pred_proba[0][y_pred_test[0]], 3)
        st.markdown(f"<h4 style='color:{color};'>📝 {status} dengan probabilitas {proba}</h4>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h4 style='color:{color};'>📝 {status} (Probabilitas tidak tersedia)</h4>", unsafe_allow_html=True)
    ```

#### **Langkah 6: Jalankan Streamlit**
1. **Jalankan perintah Streamlit** di terminal atau command prompt:
```bash
streamlit run app.py
```

#### **Deploy Aplikasi Streamlit**

Aplikasi Streamlit telah di-deploy dan dapat diakses melalui tautan berikut:
[Mahasiswa Dropout Prediction Analytics Streamlit App](https://submissionbelajarpenerapandatascience2-aldofernandos.streamlit.app/)

## **Conclusion**

### **10 Fitur yang Paling Berpengaruh Terhadap Status Mahasiswa**

Berdasarkan hasil analisis data dan model prediktif, berikut adalah 10 fitur yang paling berpengaruh terhadap keputusan mahasiswa untuk dropout dari kampus (Status):

- **Curricular_units_2nd_sem_approved**: Mahasiswa yang lebih sering mendapatkan persetujuan untuk unit kurikuler semester kedua cenderung lebih berkomitmen dan tidak mudah keluar.
- **Curricular_units_1st_sem_approved**: Sama halnya dengan unit kurikuler semester pertama, persetujuan unit ini sangat mempengaruhi keputusan mahasiswa untuk tetap bertahan.
- **Curricular_units_2nd_sem_grade**: Nilai pada semester kedua sangat berhubungan dengan keputusan mahasiswa untuk bertahan atau keluar.
- **Tuition_fees_up_to_date**: Mahasiswa yang membayar biaya kuliah tepat waktu lebih cenderung untuk tetap terdaftar dalam program.
- **Age_at_enrollment**: Usia saat masuk kuliah mempengaruhi tingkat ketahanan mahasiswa terhadap stress atau tantangan akademis.
- **Curricular_units_2nd_sem_enrolled**: Mahasiswa yang mendaftar lebih banyak unit pada semester kedua lebih berpotensi untuk tetap melanjutkan studi.
- **Admission_grade**: Nilai saat penerimaan menunjukkan kecocokan mahasiswa dengan tingkat kesulitan program studi.
- **Previous_qualification_grade**: Nilai sebelumnya memberikan gambaran tentang kesiapan akademik mahasiswa untuk menyelesaikan pendidikan mereka.
- **Scholarship_holder**: Mahasiswa yang mendapatkan beasiswa cenderung memiliki tingkat attrition yang lebih rendah, karena adanya insentif finansial untuk tetap terdaftar.
- **Curricular_units_1st_sem_enrolled**: Mahasiswa yang lebih banyak mendaftar unit kurikuler pada semester pertama lebih cenderung bertahan.

### **Model Prediktif yang Dipilih**

Setelah melakukan perbandingan antar model prediktif, **Random Forest** dipilih sebagai model terbaik berdasarkan performa yang diberikan oleh **Accuracy**, **Precision**, **Recall**, dan **F1 Score**. Berikut adalah alasan memilih model **Random Forest**:

- **Accuracy**: Model **Random Forest** memiliki akurasi tertinggi (**90.35%**), menunjukkan kemampuannya dalam memprediksi mahasiswa yang keluar dan tetap terdaftar dengan sangat baik.
- **Precision**: Dengan precision **89.97%**, model ini sangat baik dalam memprediksi mahasiswa yang keluar.
- **Recall**: Recall sebesar **88.99%** menunjukkan bahwa model ini berhasil menangkap hampir 89% mahasiswa yang benar-benar keluar dari program.
- **F1 Score**: Dengan F1 score **89.44%**, model ini menunjukkan keseimbangan yang sangat baik antara precision dan recall.
- **Kelebihan Random Forest**: Kemampuan **Random Forest** dalam menangani data besar dan kompleks, serta menghasilkan prediksi yang stabil dan akurat, menjadikannya pilihan utama dalam memprediksi mahasiswa yang berisiko keluar dari program.

## **2. Action Items**

Berdasarkan hasil analisis dan prediksi, berikut adalah beberapa rekomendasi tindakan yang dapat dilakukan oleh pihak universitas untuk mengurangi tingkat attrition mahasiswa:

### **Mengelola Pembayaran Biaya Kuliah**:

- Memastikan bahwa biaya kuliah dapat diakses dengan mudah dan memberikan fleksibilitas dalam pembayaran bagi mahasiswa yang mungkin kesulitan finansial.

### **Meningkatkan Keterlibatan Akademik**:

- Memberikan lebih banyak kesempatan bagi mahasiswa untuk terlibat dalam kegiatan kurikuler dan ekstrakurikuler untuk meningkatkan keterlibatan mereka dalam program studi.
- Menyediakan lebih banyak peluang untuk mahasiswa untuk mendapatkan **Curricular_units_2nd_sem_approved** dan **Curricular_units_1st_sem_approved**, yang dapat meningkatkan motivasi akademik mereka.

### **Meningkatkan Beasiswa dan Dukungan Finansial**:

- Menyediakan lebih banyak beasiswa dan insentif untuk mahasiswa yang berpotensi keluar, agar mereka merasa lebih terikat dengan universitas dan memiliki lebih banyak alasan untuk tetap melanjutkan studi.

### **Meningkatkan Kualitas Pengajaran dan Pembelajaran**:

- Memberikan pelatihan tambahan bagi dosen untuk meningkatkan pengalaman belajar mahasiswa.
- Meningkatkan kualitas pembelajaran di unit-unit yang memiliki nilai rendah atau tingkat kegagalan tinggi.

### **Meningkatkan Pengalaman Mahasiswa pada Semester Pertama dan Kedua**:

- Menyediakan program orientasi dan dukungan untuk mahasiswa baru agar mereka lebih siap menghadapi tantangan akademik.
- Menyediakan lebih banyak peluang untuk mahasiswa mengambil lebih banyak **Curricular_units_1st_sem_enrolled** dan **Curricular_units_2nd_sem_enrolled** agar mereka lebih terlibat sejak awal.

### **Meningkatkan Pengelolaan Waktu dan Lingkungan Kerja**:

- Mengoptimalkan waktu yang dihabiskan mahasiswa untuk belajar dengan memberikan kesempatan untuk keseimbangan kerja kehidupan pribadi.
- Menyediakan sumber daya yang cukup untuk mendukung kesejahteraan mahasiswa selama mereka berkuliah.

### **Fokus pada Pengelolaan Beasiswa dan Insentif**:

- Memperluas program beasiswa dan insentif untuk mahasiswa yang berprestasi, dengan tujuan untuk menurunkan tingkat keluar mahasiswa yang tidak mendapatkan bantuan finansial yang cukup.

### **Pemantauan dan Intervensi Dini**:

- Menggunakan model prediktif **Random Forest** untuk memantau mahasiswa yang berisiko tinggi untuk keluar dan memberikan intervensi dini yang sesuai, seperti penyesuaian beban akademik atau peningkatan dukungan keuangan dan emosional.
