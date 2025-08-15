# generate_content.py (Version 2)
import os
import re

# =============================================================================
# DATA SECTION
# This is the only section you need to edit.
# =============================================================================

# -- Personal Information for About and CV pages --
personal_info = {
    "summary": "I work on data-driven hydrology, decision support systems in geosciences, and the innovative use of earth observation and machine learning for achieving sustainable development.",
    "education": [
        {"degree": "PhD, Civil, Environmental and Sustainable Engineering", "university": "Arizona State University, Arizona, USA", "period": "May 2026 (Expected)"},
        {"degree": "MS (en route to PhD), Civil, Environmental and Sustainable Engineering", "university": "Arizona State University, Arizona, USA", "period": "Aug 2025"},
        {"degree": "BE, Civil Engineering", "university": "Tribhuvan University, Nepal", "period": "2015 – 2019"},
    ],
    "employment": [
        {"role": "Graduate Research Associate", "institution": "Arizona State University, Arizona, USA", "period": "Dec 2022 – Present"},
        {"role": "Graduate Teaching Assistant", "institution": "Arizona State University, Arizona, USA", "period": "Aug 2023 – May 2024"},
        {"role": "Researcher (Natural Hazards Section)", "institution": "Himalayan Risk Research Institute, Bhaktapur, Nepal", "period": "Mar 2019 – Dec 2022"},
        {"role": "Asst. Lecturer, Civil Engineering", "institution": "Khwopa College of Engineering, Tribhuvan University, Nepal", "period": "Nov 2019 – Oct 2021"},
    ],
    "awards": [
        "Travel grant, CIROH Developers Conference, The University of Vermont, USA, 2025",
        "Community Science Fellow, Thriving Earth Exchange, American Geophysical Union, 2024 – 2026",
        "Outstanding Reviewer Award, Earth’s Future, American Geophysical Union, 2025",
        # --- Add the rest of your awards here ---
    ]
}

# -- Publications --
publications_data = [
    {
        "title": "Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires",
        "venue": "Information Geography", "date": "2025-01-01", "paperurl": "https://doi.org/10.1016/j.infgeo.2025.100003",
        "citation": "<strong>Dahal, K.</strong>*, Talchabhadel, R., Pradhan, P., et al. (2025). &quot;Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires.&quot; <i>Information Geography</i>."
    },
    {
        "title": "Policy Relevance of IPCC Reports for the SDGs and Beyond",
        "venue": "Resources, Environment and Sustainability (Invited Editorial)", "date": "2025-01-01", "paperurl": "https://doi.org/10.1016/j.resenv.2025.100192",
        "citation": "Pradhan, P., Joshi, S., <strong>Dahal, K.</strong>, et al. (2025). &quot;Policy Relevance of IPCC Reports for the SDGs and Beyond.&quot; <i>Resources, Environment and Sustainability (Invited Editorial)</i>."
    },
    # --- ADD ALL YOUR OTHER PUBLISHED PAPERS HERE ---
]

# -- Talks and Presentations --
talks_data = [
    {
        "title": "A Framework to Improve Hydrological Forecasting with Deep Learning", "type": "Conference Poster",
        "venue": "ASU Flow 2024", "date": "2024-10-21", "location": "Arizona State University, USA",
        "description": "This poster, which received the Outstanding Poster Award, presents a novel framework for enhancing hydrological forecasting using deep learning techniques."
    },
    # --- ADD ALL YOUR OTHER TALKS HERE ---
]

# -- Teaching Experience --
teaching_data = [
    {
        "title": "Num. Methods for Engrs (CEE 384)", "venue": "Arizona State University",
        "date": "2024-01-15", "description": "Served as a Teaching Assistant for the Spring 2024 semester."
    },
    # --- ADD ALL YOUR OTHER TEACHING EXPERIENCES HERE ---
]


# =============================================================================
# SCRIPT LOGIC (No need to edit below this line)
# =============================================================================

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def clear_folder(folder_path):
    """Deletes all .md files in a folder to ensure a clean build."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    else:
        for filename in os.listdir(folder_path):
            if filename.endswith(".md"):
                os.remove(os.path.join(folder_path, filename))
        print(f"Cleared markdown files in {folder_path}")

def generate_markdown_files(data, folder, collection_name, permalink_prefix, type_key=None, default_type=None):
    for item in data:
        slug = slugify(item['title'])[:50]
        filename = f"{item['date']}-{slug}.md"
        filepath = os.path.join(folder, filename)
        
        content = "---\n"
        content += f"title: \"{item['title'].replace(':', '')}\"\n"
        content += f"collection: {collection_name}\n"
        content += f"permalink: /{permalink_prefix}/{item['date']}-{slug}\n"
        
        item_type = item.get(type_key, default_type)
        if item_type:
            content += f"type: \"{item_type}\"\n"

        for key, value in item.items():
            if key not in ['title', 'type'] and value:
                clean_value = str(value).replace("'", "’").replace('"', '&quot;')
                content += f"{key}: '{clean_value}'\n"

        content += "---\n"
        
        if item.get('description'): content += f"\n{item['description']}\n"
        if collection_name == "publications" and item.get('citation'): content += f"\nRecommended citation: {item['citation']}\n"
        if item.get('url'): content += f"\n[More information here]({item['url']})\n"

        with open(filepath, 'w', encoding='utf-8') as f: f.write(content)
        print(f"  ✓ Created {filepath}")

def generate_page(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Updated {filepath}")

if __name__ == "__main__":
    print("--- Clearing old content ---")
    clear_folder("_publications")
    clear_folder("_talks")
    clear_folder("_teaching")

    print("\n--- Generating Pages ---")
    about_content = f"""---
permalink: /
title: "About Me"
author_profile: true
---
Welcome! I am a PhD Candidate at Arizona State University. {personal_info['summary']}
"""
    generate_page("_pages/about.md", about_content)
    
    cv_content = """---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
---
{% include base_path %}
<a href="/files/CV_Kshitij_Dahal.pdf" class="btn btn--primary">Download Full CV (PDF)</a>

### Education
"""
    for item in personal_info['education']: cv_content += f"* {item['degree']}, *{item['university']}*, {item['period']}\n"
    cv_content += "\n### Work Experience\n"
    for item in personal_info['employment']: cv_content += f"* **{item['role']}**\n  * {item['institution']}\n  * {item['period']}\n"
    cv_content += """
### Publications
<ul>{% for post in site.publications reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>
  
### Talks
<ul>{% for post in site.talks reversed %}{% include archive-single-talk-cv.html %}{% endfor %}</ul>
  
### Teaching
<ul>{% for post in site.teaching reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>
"""
    cv_content += "\n### Honors and Awards\n"
    for item in personal_info['awards']: cv_content += f"* {item}\n"
    generate_page("_pages/cv.md", cv_content)

    print("\n--- Generating Collection Files ---")
    generate_markdown_files(publications_data, "_publications", "publications", "publication")
    generate_markdown_files(talks_data, "_talks", "talks", "talks", type_key="type", default_type="Talk")
    generate_markdown_files(teaching_data, "_teaching", "teaching", "teaching", type_key="type", default_type="Teaching Experience")
    print("\nGeneration complete!")