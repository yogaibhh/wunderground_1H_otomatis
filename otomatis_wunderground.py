#!/usr/bin/env python3
import requests
import pandas as pd
from datetime import datetime
import os
import sys

def log_message(message):
    with open('/home/yoga/Documents/script_python_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

def degrees_to_compass(degrees):
    if degrees is None:
        return None
    val = (degrees / 22.5) + 0.5
    val = int(val) % 16
    arr = ["N", "NNE", "NE", "ENE",
           "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW",
           "W", "WNW", "NW", "NNW"]
    return arr[val]

try:
    current_dir = os.getcwd()
    log_message(f"Current working directory: {current_dir}")

    # Masukkan API Key dan Station ID Anda di sini
    API_KEY = '...'  # Ganti dengan API Key Anda
    STATION_ID = '....'                        # Ganti dengan Station ID Anda

    # Endpoint API
    url = 'https://api.weather.com/v2/pws/observations/current'

    # Parameter untuk permintaan API
    params = {
        'stationId': STATION_ID,
        'format': 'json',
        'units': 'm',  # Ubah kembali menjadi 'm' untuk pengujian
        'apiKey': API_KEY
    }

    # Mengirim permintaan GET ke API
    response = requests.get(url, params=params)
    response.raise_for_status()  # Memeriksa kesalahan HTTP
    data = response.json()

    # Logging data yang diterima
    log_message(f"Data yang diterima dari API: {data}")

    # Mengambil data observasi
    obs = data['observations'][0]

    # Memeriksa ketersediaan kunci 'metric'
    if 'metric' in obs:
        unit_system = 'metric'
    elif 'metric_si' in obs:
        unit_system = 'metric_si'
    elif 'imperial' in obs:
        unit_system = 'imperial'
    else:
        log_message("Kunci 'metric', 'metric_si', atau 'imperial' tidak ditemukan dalam 'obs'.")
        log_message(f"Data observasi: {obs}")
        sys.exit(1)

    # Ekstraksi data yang diperlukan
    observation_time = obs['obsTimeLocal']                      # Waktu observasi lokal
    temperature = obs[unit_system]['temp']                      # Suhu
    humidity = obs['humidity']                                  # Kelembaban dalam %
    pressure = obs[unit_system]['pressure']                     # Tekanan udara
    precip_rate = obs[unit_system]['precipRate']                # Curah hujan
    wind_dir = obs.get('winddir')                               # Arah angin dalam derajat
    wind_speed = obs[unit_system]['windSpeed']                  # Kecepatan angin
    solar_radiation = obs.get('solarRadiation')                 # Radiasi matahari

    # Pastikan semua variabel numerik memiliki tipe float
    temperature = float(temperature)
    humidity = float(humidity)
    pressure = float(pressure)
    precip_rate = float(precip_rate)
    wind_dir = float(wind_dir) if wind_dir is not None else None
    wind_speed = float(wind_speed)
    solar_radiation = float(solar_radiation) if solar_radiation is not None else None

    # Konversi arah angin menjadi arah mata angin (kompas)
    wind_dir_compass = degrees_to_compass(wind_dir)

    # Konversi waktu observasi ke objek datetime
    obs_datetime = datetime.strptime(observation_time, '%Y-%m-%d %H:%M:%S')
    date = obs_datetime.date()
    time = obs_datetime.time()

    # Membuat baris data
    data_row = {
        'tanggal': date,
        'jam': time,
        'suhu (°C)': temperature,
        'kelembaban (%)': humidity,
        'tekanan udara (hPa)': pressure,
        'curah hujan (mm)': precip_rate,
        'arah angin': f"{wind_dir}° ({wind_dir_compass})",
        'kecepatan angin (km/h)': wind_speed,
        'radiasi matahari (W/m²)': solar_radiation
    }

    # Mengonversi ke DataFrame
    df = pd.DataFrame([data_row])

    # Nama file CSV dengan path absolut
    file_name = '/home/yoga/Documents/data_cuaca.csv'

    # Mengecek apakah file sudah ada
    if not os.path.isfile(file_name):
        # Jika tidak ada, tulis header
        df.to_csv(file_name, index=False, mode='w', encoding='utf-8-sig')
    else:
        # Jika ada, tambahkan data tanpa header
        df.to_csv(file_name, index=False, mode='a', header=False, encoding='utf-8-sig')

    log_message('Data berhasil disimpan.')

except Exception as e:
    log_message(f"Error terjadi: {e}")
    sys.exit(1)
