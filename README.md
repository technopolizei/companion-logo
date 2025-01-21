# [ENG] IoT Monitoring and Analytics System

This project demonstrates a basic implementation of an IoT monitoring system using Siemens Logo, Raspberry Pi, and other sensors. The system collects data, stores it in a PostgreSQL database, and provides real-time monitoring through Prometheus and Grafana.

## Features
- Collects data from sensors using Modbus and TCP/UDP.
- Stores data in a PostgreSQL database with historical tracking.
- Automates ETL processes using Apache Airflow.
- Real-time monitoring and alerts via Prometheus and Grafana.

## Tools and Technologies
- **Programming:** Python
- **Database:** PostgreSQL
- **Monitoring:** Prometheus, Grafana
- **Orchestration:** Apache Airflow

## How to Run
1. Install the dependencies: `pip install -r requirements.txt`.
2. Set up the database using `src/db_setup.py`.
3. Start the data collector: `python src/data_collector.py`.
4. Run the ETL process: `scripts/start_etl.sh`.

*Note: This repository is for educational purposes only. Configuration files do not include sensitive data.*

## Сompanion-logo ADDITIONALLY
Control relays on Siemens Logo via TCP command from Streamdeck Companion. Check "companion-logo.py" file.

# [RU] Система мониторинга и аналитики данных IoT-устройств

## Описание
Этот проект демонстрирует создание системы мониторинга и аналитики данных с использованием промышленных контроллеров (Siemens Logo, Raspberry Pi) и сенсоров. Система позволяет собирать данные, хранить их в хранилище (DWH) и визуализировать в реальном времени.

## Основные функции
- Сбор данных с устройств через протоколы Modbus и TCP/UDP.
- Хранение данных в PostgreSQL с поддержкой историчности (SCD2).
- Автоматизация ETL-процессов с помощью Apache Airflow.
- Реальное время мониторинга метрик с использованием Prometheus и Grafana.
- Настройка алертов через Telegram-бота.

## Используемые технологии
- **Языки программирования:** Python
- **База данных:** PostgreSQL
- **Автоматизация:** Apache Airflow
- **Мониторинг:** Prometheus, Grafana
- **Протоколы:** Modbus, MQTT, TCP/UDP
