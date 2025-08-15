# generate_content.py

import os
import re

# Helper function to create a URL-friendly "slug" from a title
def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

# =============================================================================
# DATA SECTION
# =============================================================================
# Add your new publications, talks, and teaching experiences to these lists.
# The script will automatically generate the markdown files.
# =============================================================================

publications_data = [
    {
        "title": "Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires",
        "venue": "Information Geography",
        "date": "2025-01-01",
        "paperurl": "https://doi.org/10.1016/j.infgeo.2025.100003",
        "citation": "<strong>Dahal, K.</strong>*, Talchabhadel, R., Pradhan, P., et al. (2025). &quot;Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires.&quot; <i>Information Geography</i>."
    },
    {
        "title": "Urban agriculture matters for sustainable development",
        "venue": "Cell Reports Sustainability",
        "date": "2024-01-01",
        "paperurl": "https://doi.org/10.1016/j.crsus.2024.100217",
        "citation": "Pradhan, P., Subedi, D. R., <strong>Dahal, K.</strong>, et al. (2024). &quot;Urban agriculture matters for sustainable development.&quot; <i>Cell Reports Sustainability</i>."
    },
    {
        "title": "Identification of groundwater potential zones in data-scarce mountainous region using explainable machine learning",
        "venue": "Journal of Hydrology",
        "date": "2023-01-01",
        "paperurl": "https://doi.org/10.1016/j.jhydrol.2023.130417",
        "citation": "<strong>Dahal, K.</strong>*, Sharma, S., Shakya, A., et al. (2023). &quot;Identification of groundwater potential zones in data-scarce mountainous region using explainable machine learning.&quot; <i>Journal of Hydrology</i>."
    },
    # --- Add new publications here ---
]

talks_data = [
    {
        "title": "A Framework to Improve Hydrological Forecasting with Deep Learning",
        "type": "Conference Poster",
        "venue": "ASU Flow 2024",
        "date": "2024-10-21",
        "location": "Arizona State University, USA",
        "description": "This poster, which received the Outstanding Poster Award, presents a novel framework for enhancing hydrological forecasting using deep learning techniques."
    },
    {
        "title": "Explainable Machine Learning in Groundwater Potential Mapping",
        "type": "Invited Webinar",
        "venue": "UNESCO GWYN",
        "date": "2024-03-13",
        "location": "Online",
        "url": "https://rb.gy/ue0vik",
        "description": "An invited webinar on the application of explainable AI (XAI) for mapping groundwater potential."
    },
    {
        "title": "Advances in Hyperspectral Remote Sensing for Water Resources",
        "type": "Conference Presentation",
        "venue": "AGU Fall Meeting 2023",
        "date": "2023-12-11",
        "location": "San Francisco, USA",
        "description": ""
    },
    # --- Add new talks here ---
]

teaching_data = [
    {
        "title": "Num. Methods for Engrs (CEE 384)",
        "venue": "Arizona State University",
        "date": "2024-01-15", # Use start of semester
        "description": "Served as a Teaching Assistant for the Spring 2024 semester."
    },
    {
        "title": "Fluid Mechanics for Civil Engrs (CEE 341)",
        "venue": "Arizona State University",
        "date": "2023-08-20", # Use start of semester
        "description": "Served as a Teaching Assistant for the Fall 2023 semester."
    },
    # --- Add new teaching experiences here ---
]


# =============================================================================
# SCRIPT LOGIC
# =============================================================================
# You don't need to modify anything below this line.
# =============================================================================

def generate_markdown_files(data, folder, collection_name, permalink_prefix, type_key=None):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for item in data:
        slug = slugify(item['title'])[:50]
        filename = f"{item['date']}-{slug}.md"
        filepath = os.path.join(folder, filename)
        
        # --- Create YAML Front Matter ---
        content = "---\n"
        content += f"title: \"{item['title']}\"\n"
        content += f"collection: {collection_name}\n"
        content += f"permalink: /{permalink_prefix}/{item['date']}-{slug}\n"
        
        if type_key and item.get(type_key):
             content += f"type: \"{item[type_key]}\"\n"

        for key, value in item.items():
            if key not in ['title', 'type'] and value:
                content += f"{key}: '{value}'\n" if key != "citation" else f"{key}: '{value.replace('"', '&quot;')}'\n"

        content += "---\n"
        
        # --- Create Main Content ---
        if item.get('description'):
            content += f"\n{item['description']}\n"
        
        if collection_name == "publications" and item.get('citation'):
            content += f"\nRecommended citation: {item['citation']}\n"
        
        if item.get('url'):
            content += f"\n[More information here]({item['url']})\n"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created {filepath}")

# Run the generation process
print("--- Generating Content ---")
generate_markdown_files(publications_data, "_publications", "publications", "publication")
generate_markdown_files(talks_data, "_talks", "talks", "talks", type_key="type")
generate_markdown_files(teaching_data, "_teaching", "teaching", "teaching", type_key="type")
print("\nGeneration complete!")
