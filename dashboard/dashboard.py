import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_total_rent_based_season(selected_year_df):
    total_based_season = selected_year_df.groupby(by=['season'])['cnt'].sum().reset_index()
    return total_based_season

def create_total_rent_based_time(selected_year_df):
    time = selected_year_df.groupby(by=['hr', 'weekday'])['cnt'].sum().reset_index()
    return time

all_df = pd.read_csv('main_data.csv')

with st.sidebar:
    st.image('https://cdn.pixabay.com/photo/2016/06/14/15/01/vector-1456759_640.png')
    selected_year = st.selectbox(
        label="Pilih Tahun",
        options=(2011, 2012)
    )

selected_year_df = all_df[all_df['yr'] == selected_year]

st.header('Dashboard Permintaan Sewa Sepeda :bike:')

st.subheader(f'Permintaan Sewa Sepeda Tahun {selected_year}')
col1, col2, col3 = st.columns(3)
with col1:
    count_sum_2011 = all_df[all_df['yr'] == 2011]['cnt'].sum()
    count_sum_2012 = all_df[all_df['yr'] == 2012]['cnt'].sum()
    count_sum = count_sum_2012 - count_sum_2011
    if selected_year == 2012:
        st.metric('Total Permintaan', value=count_sum_2012, delta=str(f'{count_sum}'))
    else:
        st.metric('Total Permintaan', value=count_sum_2011)

with col2:
    count_registered_2011 = all_df[all_df['yr'] == 2011]['registered'].sum()
    count_registered_2012 = all_df[all_df['yr'] == 2012]['registered'].sum()
    count_registered = count_registered_2012 - count_registered_2011
    if selected_year == 2012:
        st.metric('Total Tipe Terdaftar', value=count_registered_2012, delta=str(f'{count_registered}'))
    else:
        st.metric('Total Tipe Terdaftar', value=count_registered_2011)

with col3:
    count_casual_2011 = all_df[all_df['yr'] == 2011]['casual'].sum()
    count_casual_2012 = all_df[all_df['yr'] == 2012]['casual'].sum()
    count_casual = count_casual_2012 - count_casual_2011
    if selected_year == 2012:
        st.metric('Total Tipe Kasual', value=count_casual_2012, delta=str(f'{count_casual}'))
    else:
        st.metric('Total Tipe Kasual', value=count_casual_2011)

st.subheader(f'Jumlah Permintaan Berdasarkan Musim Untuk Tahun {selected_year}')
plt.figure(figsize=(12, 6))
barplot_index = sns.barplot(data=create_total_rent_based_season(selected_year_df), x='season', y='cnt')
for p in barplot_index.patches:
    height = p.get_height()
    if height > 0:
      plt.annotate(f'{int(height)}',
                 (p.get_x() + p.get_width() / 2., height),
                 ha='center',
                 va='bottom')
plt.xlabel('Musim')
plt.ylabel('Total Permintaan')
st.pyplot(plt)

st.subheader(f'Jumlah Permintaan Berdasarkan Waktu Untuk Tahun {selected_year}')
plt.figure(figsize=(12, 6))
sns.pointplot(data=create_total_rent_based_time(selected_year_df), x='hr', y='cnt', hue='weekday')
plt.xlabel('Waktu')
plt.ylabel('Total Permintaan')
plt.legend(title='Hari', loc='upper left')
st.pyplot(plt)

st.caption('Copyright © 2024 All Rights Reserved Firman Setiansyah')