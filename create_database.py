import sqlite3

connection = sqlite3.connect("statistics_canada.db")

cursor = connection.cursor()
# ============================
# create population table
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS population (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    population INTEGER NOT NULL
)
""")

cursor.execute("""
INSERT INTO population (province, year, population)
VALUES
('Ontario', 2024, 16000000),
('Quebec', 2024, 9100000),
('British Columbia', 2024, 5800000),
('Alberta', 2024, 4900000),
('Manitoba', 2024, 1500000),
('Saskatchewan', 2024, 1250000),
('Nova Scotia', 2024, 1100000),
('New Brunswick', 2024, 860000),
('Newfoundland and Labrador', 2024, 540000),
('Prince Edward Island', 2024, 180000)
""")

# ============================
# create income table
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    median_income INTEGER NOT NULL
)
""")

cursor.execute("""
INSERT INTO income (province, year, median_income)
VALUES
('Ontario', 2024, 78000),
('Quebec', 2024, 69000),
('British Columbia', 2024, 76000),
('Alberta', 2024, 84000),
('Manitoba', 2024, 67000),
('Saskatchewan', 2024, 72000),
('Nova Scotia', 2024, 65000),
('New Brunswick', 2024, 64000),
('Newfoundland and Labrador', 2024, 70000),
('Prince Edward Island', 2024, 66000)
""")

# =========================
# CREATE HOUSING TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS housing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    average_house_price INTEGER NOT NULL
)
""")

cursor.execute("""
INSERT INTO housing (province, year, average_house_price)
VALUES
('Ontario', 2024, 870000),
('Quebec', 2024, 510000),
('British Columbia', 2024, 980000),
('Alberta', 2024, 520000),
('Manitoba', 2024, 390000),
('Saskatchewan', 2024, 360000),
('Nova Scotia', 2024, 450000),
('New Brunswick', 2024, 340000),
('Newfoundland and Labrador', 2024, 310000),
('Prince Edward Island', 2024, 430000)
""")

# =========================
# CREATE EMPLOYMENT TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS employment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    employment_rate REAL NOT NULL,
    unemployment_rate REAL NOT NULL
)
""")

cursor.execute("""
INSERT INTO employment
(province, year, employment_rate, unemployment_rate)
VALUES
('Ontario', 2024, 61.8, 6.9),
('Quebec', 2024, 62.9, 5.2),
('British Columbia', 2024, 63.4, 5.6),
('Alberta', 2024, 64.1, 7.1),
('Manitoba', 2024, 63.0, 4.8),
('Saskatchewan', 2024, 64.5, 4.9),
('Nova Scotia', 2024, 59.7, 6.5),
('New Brunswick', 2024, 58.9, 6.8),
('Newfoundland and Labrador', 2024, 56.8, 10.4),
('Prince Edward Island', 2024, 62.4, 7.0)
""")

# =========================
# CREATE HEALTHCARE TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS healthcare (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    physicians_per_1000 REAL NOT NULL,
    healthcare_spending INTEGER NOT NULL
)
""")

cursor.execute("""
INSERT INTO healthcare
(province, year, physicians_per_1000, healthcare_spending)
VALUES
('Ontario', 2024, 2.8, 8900),
('Quebec', 2024, 3.2, 9100),
('British Columbia', 2024, 2.9, 8800),
('Alberta', 2024, 2.7, 9400),
('Manitoba', 2024, 2.8, 9200),
('Saskatchewan', 2024, 2.6, 9000),
('Nova Scotia', 2024, 3.0, 9300),
('New Brunswick', 2024, 2.7, 9100),
('Newfoundland and Labrador', 2024, 2.9, 9500),
('Prince Edward Island', 2024, 2.5, 8900)
""")

# =========================
# CREATE IMMIGRATION TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS immigration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    immigrants INTEGER NOT NULL
)
""")

cursor.execute("""
INSERT INTO immigration
(province, year, immigrants)
VALUES
('Ontario', 2024, 205000),
('Quebec', 2024, 68000),
('British Columbia', 2024, 62000),
('Alberta', 2024, 58000),
('Manitoba', 2024, 18000),
('Saskatchewan', 2024, 14000),
('Nova Scotia', 2024, 12000),
('New Brunswick', 2024, 9000),
('Newfoundland and Labrador', 2024, 5000),
('Prince Edward Island', 2024, 3000)
""")

# =========================
# CREATE LIFE EXPECTANCY TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS life_expectancy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    life_expectancy REAL NOT NULL
)
""")

cursor.execute("""
INSERT INTO life_expectancy
(province, year, life_expectancy)
VALUES
('Ontario', 2024, 82.1),
('Quebec', 2024, 82.5),
('British Columbia', 2024, 82.7),
('Alberta', 2024, 81.7),
('Manitoba', 2024, 80.9),
('Saskatchewan', 2024, 80.8),
('Nova Scotia', 2024, 81.2),
('New Brunswick', 2024, 80.9),
('Newfoundland and Labrador', 2024, 79.8),
('Prince Edward Island', 2024, 81.4)
""")

# =========================
# CREATE EDUCATION TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS education (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    university_graduation_rate REAL NOT NULL
)
""")

cursor.execute("""
INSERT INTO education
(province, year, university_graduation_rate)
VALUES
('Ontario', 2024, 36.8),
('Quebec', 2024, 34.5),
('British Columbia', 2024, 38.1),
('Alberta', 2024, 35.2),
('Manitoba', 2024, 31.6),
('Saskatchewan', 2024, 30.9),
('Nova Scotia', 2024, 37.0),
('New Brunswick', 2024, 32.8),
('Newfoundland and Labrador', 2024, 29.7),
('Prince Edward Island', 2024, 33.4)
""")


# =========================
# CREATE GDP TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS gdp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    gdp_billions REAL NOT NULL
)
""")

cursor.execute("""
INSERT INTO gdp
(province, year, gdp_billions)
VALUES
('Ontario', 2024, 1100.5),
('Quebec', 2024, 520.3),
('British Columbia', 2024, 410.8),
('Alberta', 2024, 430.2),
('Manitoba', 2024, 82.5),
('Saskatchewan', 2024, 95.1),
('Nova Scotia', 2024, 58.7),
('New Brunswick', 2024, 42.9),
('Newfoundland and Labrador', 2024, 39.4),
('Prince Edward Island', 2024, 9.8)
""")

# =========================
# CREATE CRIME TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS crime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    crime_rate REAL NOT NULL
)
""")

cursor.execute("""
INSERT INTO crime
(province, year, crime_rate)
VALUES
('Ontario', 2024, 55.4),
('Quebec', 2024, 49.8),
('British Columbia', 2024, 92.1),
('Alberta', 2024, 87.5),
('Manitoba', 2024, 118.6),
('Saskatchewan', 2024, 126.3),
('Nova Scotia', 2024, 64.2),
('New Brunswick', 2024, 58.9),
('Newfoundland and Labrador', 2024, 61.4),
('Prince Edward Island', 2024, 46.7)
""")

# =========================
# CREATE WAGES TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS wages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    average_hourly_wage REAL NOT NULL
)
""")

cursor.execute("""
INSERT INTO wages
(province, year, average_hourly_wage)
VALUES
('Ontario', 2024, 36.50),
('Quebec', 2024, 33.80),
('British Columbia', 2024, 35.90),
('Alberta', 2024, 38.70),
('Manitoba', 2024, 31.90),
('Saskatchewan', 2024, 33.20),
('Nova Scotia', 2024, 30.80),
('New Brunswick', 2024, 30.50),
('Newfoundland and Labrador', 2024, 32.70),
('Prince Edward Island', 2024, 30.20)
""")

# =========================
# CREATE POVERTY TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS poverty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    poverty_rate REAL NOT NULL
)
""")

cursor.execute("""
INSERT INTO poverty
(province, year, poverty_rate)
VALUES
('Ontario', 2024, 8.2),
('Quebec', 2024, 7.6),
('British Columbia', 2024, 8.5),
('Alberta', 2024, 7.9),
('Manitoba', 2024, 10.3),
('Saskatchewan', 2024, 10.8),
('Nova Scotia', 2024, 9.7),
('New Brunswick', 2024, 9.4),
('Newfoundland and Labrador', 2024, 11.2),
('Prince Edward Island', 2024, 8.8)
""")

# =========================
# CREATE CONSUMER SPENDING TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS consumer_spending (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    average_annual_spending INTEGER NOT NULL
)
""")

cursor.execute("""
INSERT INTO consumer_spending
(province, year, average_annual_spending)
VALUES
('Ontario', 2024, 42000),
('Quebec', 2024, 38000),
('British Columbia', 2024, 41000),
('Alberta', 2024, 44000),
('Manitoba', 2024, 36000),
('Saskatchewan', 2024, 37000),
('Nova Scotia', 2024, 35000),
('New Brunswick', 2024, 34000),
('Newfoundland and Labrador', 2024, 33000),
('Prince Edward Island', 2024, 34500)
""")











connection.commit()
connection.close()