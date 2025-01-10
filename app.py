import streamlit as st
import openai
import requests
import networkx as nx
import matplotlib.pyplot as plt

# Set up OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

# Function to fetch company data from Wikipedia
def fetch_company_data(company_name):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{company_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", f"No information found for {company_name}.")
    else:
        return f"Failed to fetch data for {company_name}."

# Function to use GPT to extract relationships
def gpt_extract_relationships(company_name, data):
    prompt = f"""
    Extract structured relationships for a knowledge graph about the company '{company_name}' from the following description:
    
    {data}
    
    Format the output as a list of relationships in this structure:
    - Entity1 → Relationship → Entity2
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant creating knowledge graphs."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error with GPT API: {e}"

# Function to generate and visualize the graph
def generate_graph(company_name, relationships, layout_type="circular"):
    G = nx.DiGraph()
    
    # Parse relationships and add them to the graph
    for line in relationships.split("\n"):
        if "→" in line:
            try:
                entity1, relationship, entity2 = map(str.strip, line.split("→"))
                G.add_edge(entity1, entity2, label=relationship)
            except ValueError:
                continue  # Skip invalid lines

    # Select layout for better visualization
    if layout_type == "circular":
        pos = nx.circular_layout(G)
    elif layout_type == "spring":
        pos = nx.spring_layout(G, seed=42)
    elif layout_type == "shell":
        pos = nx.shell_layout(G)
    else:
        pos = nx.random_layout(G)

    # Initialize figure
    plt.figure(figsize=(18, 14))
    plt.gca().set_facecolor("white")  # Set background to white for better contrast

    # Draw nodes with enhanced color and size
    nx.draw_networkx_nodes(G, pos, node_color='dodgerblue', node_size=5000, edgecolors='black', linewidths=1.5)

    # Draw edges with clean styles
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=25, arrowstyle='-|>', width=2)

    # Draw node labels with larger font size for visibility
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold', font_color='black')

    # Draw edge labels with increased font size and better color contrast
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14, font_color='darkgreen')

    # Add title with improved font size
    plt.title(f"📘 Knowledge Graph for '{company_name}'", fontsize=24, fontweight='bold', color='navy')

    # Add a legend or descriptive text
    plt.text(-1.5, -1.3, "📍 Nodes: Entities\n🔗 Edges: Relationships", fontsize=14, bbox=dict(facecolor='white', alpha=0.8))

    # Remove axes for cleaner presentation
    plt.axis('off')

    # Show the plot on Streamlit
    st.pyplot(plt)

# Streamlit App
def main():
    st.title("🌟 Interactive Knowledge Graph Generator")
    st.markdown("Generate visually appealing knowledge graphs for any company using OpenAI GPT and Wikipedia data.")

    # Input for company name
    company_name = st.text_input("🔍 Enter the name of a company:")
    
    # Layout selection
    layout_type = st.selectbox("🎨 Choose a graph layout:", ["Circular", "Spring", "Shell", "Random"])
    layout_map = {"Circular": "circular", "Spring": "spring", "Shell": "shell", "Random": "random"}

    # Generate button
    if st.button("🚀 Generate Knowledge Graph"):
        if company_name.strip() == "":
            st.error("⚠️ Please enter a company name.")
        else:
            # Fetch company data
            with st.spinner("🔄 Fetching company data..."):
                company_data = fetch_company_data(company_name)
            if "No information found" in company_data or "Failed" in company_data:
                st.error(company_data)
                return

            # Extract relationships
            with st.spinner("🤖 Extracting relationships using GPT..."):
                relationships = gpt_extract_relationships(company_name, company_data)
            if "Error" in relationships:
                st.error(relationships)
                return

            # Generate graph
            with st.spinner("✨ Generating the knowledge graph..."):
                st.subheader(f"Knowledge Graph for '{company_name}'")
                generate_graph(company_name, relationships, layout_map[layout_type])
                st.success("🎉 Knowledge graph generated successfully!")

if __name__ == "__main__":
    main()
