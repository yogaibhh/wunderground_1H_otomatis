Untuk memastikan format bold yang konsisten di README, gunakan dua tanda bintang (`**`) di kedua sisi teks yang ingin Anda buat tebal (bold). Berikut adalah contoh yang diperbarui dengan format bold yang konsisten:

---

# **Weather Data Logger using Weather.com API**

## **Overview**

This project is a Python script designed to fetch real-time weather data from a weather station via the Weather.com API and save it into a CSV file. The data includes parameters such as temperature, humidity, wind speed, wind direction, precipitation rate, pressure, and solar radiation. 

## **Features**

- Fetches real-time weather data from Weather.com API.
- Logs temperature, humidity, pressure, precipitation rate, wind speed, wind direction, and solar radiation.
- Automatically converts wind direction from degrees to compass directions.
- Saves weather data into a CSV file with date and time stamps.
- Automatically handles file creation and appends data without overwriting.
- Provides logs for debugging and tracking the status of data requests.

## **Prerequisites**

- Python 3.x
- Pandas library: Install using `pip install pandas`
- Requests library: Install using `pip install requests`
- A weather station with API access from Weather.com
- API Key and Station ID from Weather.com

## **File Descriptions**

- **Python Script**: The main Python script that:
  - Fetches data from the Weather.com API.
  - Logs the request parameters and responses.
  - Processes the data and saves it to a CSV file in a structured format.

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/yogaibhh/wunderground_1H_otomatis.git
   cd wunderground_1H_otomatis
   ```

2. Install required Python libraries:

   ```bash
   pip install requests pandas
   ```

3. Update your API key and Station ID in the Python script:

   ```python
   API_KEY = 'YOUR_API_KEY'
   STATION_ID = 'YOUR_STATION_ID'
   ```

4. Ensure the script has the correct permissions to access and write to the CSV file:

   ```bash
   chmod +x otomatis_wunderground.py
   ```

## **Usage**

To run the Python script manually, use:

```bash
python otomatis_wunderground.py
```

This will fetch the latest weather data and append it to the CSV file located at `/home/yoga/Documents/data_cuaca.csv`.

## **CSV File Format**

The data is saved in a CSV file (`data_cuaca.csv`) with the following columns:

| **tanggal** | **jam** | **suhu (°C)** | **kelembaban (%)** | **tekanan udara (hPa)** | **curah hujan (mm)** | **arah angin** | **kecepatan angin (km/h)** | **radiasi matahari (W/m²)** |
|--------------|----------|-----------|----------------|---------------------|------------------|------------|------------------------|-------------------------|
| 2024-10-24   | 07:00:00 | 26.1      | 82             | 1009.2              | 1.2              | 90° (E)    | 15.2                   | 340                     |

## **Logging**

Logs are written to `/home/yoga/Documents/script_python_log.txt`. These logs help in troubleshooting and keeping track of script execution.

## **License**

This project is open-source and can be modified or distributed under the terms of the MIT License.

## **Contact**

For any questions or contributions, feel free to contact the project maintainer at `yogaibhh`.

---

Dengan menggunakan dua tanda bintang (`**`) di kedua sisi teks, semua bagian yang penting terlihat tebal (bold) secara konsisten.
