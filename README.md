# TSP Visualizer

TSP Visualizer is a web application that demonstrates a solution to the Traveling Salesman Problem (TSP) using a greedy algorithm. The application allows users to select a starting city and visualize the computed route and total distance on an interactive map.

## Features

- **Greedy TSP Algorithm**: Implements a simple greedy approach to solve the TSP.
- **Interactive Map**: Visualizes the route and cities using Folium.
- **FastAPI Backend**: Provides a lightweight and efficient backend for handling requests.
- **Dynamic HTML Templates**: Uses Jinja2 templates for rendering the UI.

## Tech Stack

- **Python 3.11**
- **FastAPI**: For building the backend API.
- **Folium**: For map visualization.
- **Geopy**: For calculating geographical distances.
- **Jinja2**: For HTML templating.

## How It Works

1. The user selects a starting city from the dropdown menu.
2. The backend computes the route using the greedy TSP algorithm.
3. The route and total distance are displayed, along with an interactive map showing the path.

## Project Structure

```
.
├── main.py                  # Entry point for the application
├── pyproject.toml           # Project dependencies and configuration
├── tsc_core/
│   ├── __init__.py          # Core package initialization
│   ├── src/
│   │   ├── app.py           # FastAPI app setup
│   │   ├── data/
│   │   │   ├── locations.py # City coordinates
│   │   ├── routers/
│   │   │   ├── route_visualizer.py # Route visualization logic
│   │   ├── services/
│   │   │   ├── greedy_tsp.py       # Greedy TSP algorithm
│   │   │   ├── distance_calculator.py # Distance calculation
│   ├── templates/
│       ├── map.html         # HTML template for the UI
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tsp-visualizer.git
   cd tsp-visualizer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:
   ```bash
   uvicorn main:app --reload
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License.