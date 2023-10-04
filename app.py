import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#judul aplikasi
st.title('Streamlit Simple App')

#menambahkan navigasi sidebare
page= st.sidebar.radio("Pilih halaman", ["Dataset","Visualisasi","Student Performance"])
if page == "Dataset":
    st.header("Halaman Dataset")

    #baca file csv
    data = pd.read_csv("pddikti_example.csv")

    #tampilkan data di streamlit
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
    st.set_option('deprecation.showPyplotGlobalUse',False)

    #baca file csv
    data = pd.read_csv("pddikti_example.csv")

    #filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data= data[data['universitas'] == selected_university]

    #buat visualisasi
    plt.figure(figsize=(12,6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]


        #urutkan data berdasarkan id dengan urutan menurun
        subset = subset.sort_values(by="id", ascending=False)

        plt.plot(subset['semester'],subset['jumlah'], label=prog_studi)

    plt.title(f"visualisasi data untuk{selected_university}")
    plt.xlabel('semester')
    plt.xticks(rotation=90)
    plt.ylabel('jumlah')
    plt.legend()
    st.pyplot()

elif page == "Student Performance":
    st.header("Halaman Student Performance")
    page = st.selectbox ("Pilih halaman",["visualisasi","dataset"])
    if page == "dataset":
        #baca file csv
        data = pd.read_csv("StudentsPerformance.csv")
        st.subheader("Data")
        st.write(data)
        st.write ()
        st.write (data.head())
        st.subheader("Nilai Rata - Rata Pelajar: ")
        st.write("math score :",data['math score'].mean(),"\nreading score:", data['reading score'].mean(),"\nwriting score", data['writing score'].mean())
        st.write (data.describe())

    else:
        data = pd.read_csv("StudentsPerformance.csv")
        plt.figure(figsize=(12,6))
        data['math score'].plot.hist(bins=10, title='Nilai Ujian Matematika')
        plt.legend()
        st.pyplot()

        plt.figure(figsize=(12,6))
        data['gender'].value_counts().sort_index().plot.bar(rot=0, title='Jenis Kelamin')
        plt.legend()
        st.pyplot()

        data.boxplot(by='gender',column=['math score'])
        plt.legend()
        st.pyplot()
