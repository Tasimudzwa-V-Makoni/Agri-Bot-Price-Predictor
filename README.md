--Project Overview
Agri-Bot is a full-stack agricultural solution designed to empower small-scale farmers in Zimbabwe. It combines an autonomous hardware rover for real-time soil monitoring with a Machine Learning-powered web application to predict market crop prices. By bridging the gap between IoT (Internet of Things) and Data Science, this project aims to reduce crop failure caused by unpredictable environmental factors and minimise financial loss due to market volatility.

--Key Features
Autonomous Soil Sensing: Mobile rover equipped with pH and Soil Temperature sensors for field diagnostics.

Predictive Analytics: A Decision Tree Regressor model that forecasts crop prices with 93-95% accuracy.

Farmer Dashboard: A responsive web interface built with Flask for data visualisation.

Market Intelligence: Real-time tracking of "Top Gainer" and "Top Loser" crops to guide planting decisions.

--Tech Stack
Software
  Languages: Python (Backend & ML), C++ (Hardware Logic)
  ML Libraries: Scikit-learn, Pandas, NumPy
  Web Framework: Flask, Jinja2
  Frontend: HTML5, CSS3, Chart.js

Hardware
  Microcontroller: Arduino Uno/Mega
  Communication: I2C Protocol, Serial (PySerial)
  Sensors: DS18B20 (Temperature), Analogue pH Probe

--Machine Learning Implementation
The core of the predictive engine uses a Decision Tree Regressor. The model was trained on historical agricultural datasets, focusing on:
  1. Data cleaning and preprocessing via Pandas.
  2. Feature scaling and selection.
  3. Model validation to ensure reliability in real-world Zimbabwean market conditions.

--Project Structure
Plaintext
├── app.py              # Flask Application logic
├── model.py            # Machine Learning model training
├── static/             # CSS and JavaScript (Chart.js)
├── templates/          # HTML Dashboards (Jinja2)
├── hardware/           # Arduino (.ino) sketches
└── data/               # Historical crop price datasets

--Impact & Vision
This project addresses UN Sustainable Development Goal 2: Zero Hunger. By providing precision agriculture tools to communities that lack expensive industrial equipment, Agri-Bot fosters climate resilience and economic sovereignty for smallholder farmers.
