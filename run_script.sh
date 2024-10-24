#!/bin/bash
echo "Cron job started at $(date)" >> /home/yoga/Documents/script_log.txt

# Mengatur direktori kerja
cd /home/yoga/Documents

# Menjalankan script Python
/home/yoga/Documents/env/bin/python /home/yoga/Documents/Otomatis_1H.py >> /home/yoga/Documents/script_log.txt 2>&1

echo "Cron job finished at $(date)" >> /home/yoga/Documents/script_log.txt
echo "----------------------------------------" >> /home/yoga/Documents/script_log.txt
