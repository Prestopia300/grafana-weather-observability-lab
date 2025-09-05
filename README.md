# grafana-weather-observability-lab
A hands-on observability project that demonstrates how to build a monitoring and logging stack using Grafana, Prometheus, Loki, Tempo, Alloy, and Mimir on a Linux VM.

docker-compose stop
docker-compose up -d

Test urls:

Python Weather API data: http://localhost:8000/metrics
Grafana: http://localhost:3000
Prometheus: http://localhost:9090/targets

Prometheus data source URL (set in grafana): http://yourip:9090

Importing dashboard: Go to Grafana->Dashboard, click New Dashboard, Import dashboard, select grafana-weather-observability-lab/grafana/dashboards/weather.json, click Import

also

source venv/bin/activate
python weather_exporter.py
pip install prometheus-client requests

 export OPENWEATHER_API_KEY=your_api_key_here
 export CITY="Seattle,US"

get api key from https://home.openweathermap.org/api_keys