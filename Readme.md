# Knowledge Graph Generator

## Overview
The Knowledge Graph Generator is a Python-based interactive application that visualizes structured relationships for a given company. It combines the power of OpenAI's GPT, Wikipedia API, and NetworkX to create visually appealing knowledge graphs. The app is built using Streamlit, making it user-friendly and interactive.

---

## Features
- **Wikipedia Integration**: Fetches summarized company data directly from Wikipedia.
- **OpenAI GPT Integration**: Extracts structured relationships from textual data.
- **Interactive Graph Layouts**: Choose from circular, spring, shell, or random layouts for graph visualization.
- **Custom Graph Visualization**: Nodes, edges, and labels are styled for better readability and aesthetics.

---

## Installation

### Prerequisites
- Python 3.7 or higher
- OpenAI API Key (replace the placeholder in the code)

### Setup
1. Clone the repository or download the code.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace the placeholder `openai.api_key` with your actual OpenAI API key in the code.
4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. Open the Streamlit application in your browser.
2. Enter the name of the company you want to analyze in the input field.
3. Choose a layout for the graph from the dropdown menu.
4. Click the **Generate Knowledge Graph** button.
5. View the generated graph and explore the relationships.

---

## File Structure
- `app.py`: Main script for the Streamlit application.
- `requirements.txt`: List of Python dependencies.

---

## Dependencies
- `streamlit`: For building the web app.
- `openai`: For GPT-powered relationship extraction.
- `requests`: For fetching data from the Wikipedia API.
- `networkx`: For creating and managing the graph.
- `matplotlib`: For visualizing the graph.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Key Functions
- `fetch_company_data(company_name)`: Fetches company information from Wikipedia.
- `gpt_extract_relationships(company_name, data)`: Extracts structured relationships using GPT.
- `generate_graph(company_name, relationships, layout_type)`: Generates and visualizes the knowledge graph.

---

## Customization
- **Graph Layouts**: Add or modify layouts in the `generate_graph` function.
- **Styling**: Update node and edge styles in the `generate_graph` function to match your preferences.

---

## Limitations
- Relies on the availability of company data on Wikipedia.
- GPT relationship extraction may vary based on the quality of the input data.

---

## Future Enhancements
- Add support for multiple data sources (e.g., news articles, official websites).
- Include more layout options for graph visualization.
- Enable saving graphs as images or files.

---

## License
This project is open-source and available for personal and educational use. Contributions and feedback are welcome!

