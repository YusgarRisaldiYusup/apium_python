# mini_project_mobile_automation_with_python

# Proyek Pengujian mobile Automation ini menggunakan Phyton, Pytest, selenium dengan konsep Page Objek Model
-mobile automation ini dibuat berdasarkan apk dari api_demo debug.apk :  https://drive.google.com/file/d/1vU_n4B8n0Kvhdr3JSjD-rQM_VIwFzG1K/view

Proyek ini mengimplementasikan pengujian otomatis untuk mobile menggunakan selenium, appium dan Pytest sebagai library pengujian dan assertpy sebagai library assertion, proyek ini berbasis page Object Model (POM), Phyton untuk bahasa pemrograman.

## instal library
-pip install -r requirements.txt 

## Tujuan Proyek
- Mengelola dan menjalankan pengujian otomatis untuk fitur mobile
- Memastikan bahwa fitur berperilaku sesuai dengan spesifikasi dalam berbagai skenario.

## Cara Menjalankan Pengujian
pytest Test/ -s     = run with debug
pytest Test/ -v     = run all test with desc
pytest  Test/       = run all test

## Struktur Proyek
- .test/conftest.py            = folder/file to set up driver and send report
- .helper/action.py             = folder/file to setting our reusable action
- .helper/config.py         = folder/file to put reusable variabels
- .test_appium                           = folder/file to make our test (exp: unit/e2e/integration/etc)
    
  ## video Report
  - [Hasil Running Video](https://github.com/YusgarRisaldiYusup/apium_python/studio64_QUdPtd2dpu.mp4)


---
