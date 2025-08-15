# generate_content.py
import os
import re

# =============================================================================
# DATA SECTION
# This is the single source of truth for your website's content.
# Edit this section to add or update your information in the future.
# =============================================================================

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
        "Full Scholarship to the Snow Measurement Field School, CUAHSI, Mammoth Lakes, California, 2025",
        "HydroLearn Fellowship, Cooperative Institute for Research to Operations in Hydrology, 2024",
        "Outstanding Poster Award for “A Framework to Improve Hydrological Forecasting with Deep Learning”, ASU Flow 2024, Arizona State University, AZ, USA, 2024",
        "Travel grant, CIROH Developers Conference, The University of Alabama, USA, 2024",
        "Travel Grant, Remote Sensing of the Water Cycle Chapman, HI, USA, 2024",
        "Water Quality Tiny Grant (HaikuYourResearch), American Geophysical Union, AGU Fall Meeting 2023, 2023",
        "Recipient of the Graphical Abstract Competition Prize, American Geophysical Union, 2023",
        "Full Funding Award for Summer Graduate Writing Camp (June 12-16, 2023) at Arizona State University, 2023",
        "Hackathon Competition Winner (1st place), SpaceHack for Sustainability, Arizona State University, 2023",
        "Travel Grant, DRI Technical Conference 2022, India, 2022",
        "Coalition for Disaster Resilient Infrastructure (CDRI) fellow, 2021",
        "Hackathon Competition Winner (1st place), 3rd NOAA Workshop on Leveraging AI in Environmental Sciences, USA, 2021",
        "Travel Grant, 36th International Geological Congress, India (The event was canceled due to COVID-19), 2020",
    ]
}

publications_data = [
    {"title": "Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires", "venue": "Information Geography", "date": "2025-01-01", "paperurl": "https://doi.org/10.1016/j.infgeo.2025.100003", "citation": "<strong>Dahal, K.</strong>*, Talchabhadel, R., Pradhan, P., et al. (2025). &quot;Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires.&quot; <i>Information Geography</i>."},
    {"title": "Policy Relevance of IPCC Reports for the SDGs and Beyond", "venue": "Resources, Environment and Sustainability", "date": "2025-01-01", "paperurl": "https://doi.org/10.1016/j.resenv.2025.100192", "citation": "Pradhan, P., Joshi, S., <strong>Dahal, K.</strong>, et al. (2025). &quot;Policy Relevance of IPCC Reports for the SDGs and Beyond.&quot; <i>Resources, Environment and Sustainability</i>."},
    {"title": "Urban agriculture matters for sustainable development", "venue": "Cell Reports Sustainability", "date": "2024-01-01", "paperurl": "https://doi.org/10.1016/j.crsus.2024.100217", "citation": "Pradhan, P., Subedi, D. R., <strong>Dahal, K.</strong>, et al. (2024). &quot;Urban agriculture matters for sustainable development.&quot; <i>Cell Reports Sustainability</i>."},
    {"title": "Identification of groundwater potential zones in data-scarce mountainous region using explainable machine learning", "venue": "Journal of Hydrology", "date": "2023-01-01", "paperurl": "https://doi.org/10.1016/j.jhydrol.2023.130417", "citation": "<strong>Dahal, K.</strong>*, Sharma, S., Shakya, A., et al. (2023). &quot;Identification of groundwater potential zones in data-scarce mountainous region using explainable machine learning.&quot; <i>Journal of Hydrology</i>."},
    {"title": "Mapping landslide susceptibility and critical infrastructure for spatial decision-making", "venue": "Sustainable and Resilient Infrastructure", "date": "2023-01-01", "paperurl": "https://www.tandfonline.com/doi/full/10.1080/23789689.2023.2181552", "citation": "<strong>Dahal, K.</strong>*, & Gnyawali, K.R., (2023). &quot;Mapping landslide susceptibility and critical infrastructure for spatial decision-making.&quot; <i>Sustainable and Resilient Infrastructure</i>."},
    {"title": "Multimodal multiscale characterization of cascading hazard on mountain terrain", "venue": "Geomatics, Natural Hazards and Risk", "date": "2023-01-01", "paperurl": "https://doi.org/10.1080/19475705.2022.2162443", "citation": "Talchabhadel, R., Maskey, S., Gouli, M. R., <strong>Dahal, K.</strong>*, et al. (2023). &quot;Multimodal multiscale characterization of cascading hazard on mountain terrain.&quot; <i>Geomatics, Natural Hazards and Risk</i>."},
    {"title": "Framework for rainfall-triggered landslide-prone critical infrastructure zonation", "venue": "Science of the Total Environment", "date": "2023-01-01", "paperurl": "https://doi.org/10.1016/j.scitotenv.2023.162242", "citation": "Gnyawali, K., <strong>Dahal, K.</strong>, Talchabhadel, R., & Nirandjan, S. (2023). &quot;Framework for rainfall-triggered landslide-prone critical infrastructure zonation.&quot; <i>Science of the Total Environment</i>."},
    {"title": "Vegetation loss and recovery analysis from the 2015 Gorkha earthquake (7.8 Mw) triggered landslides", "venue": "Land Use Policy", "date": "2022-01-01", "paperurl": "https://www.sciencedirect.com/science/article/pii/S0264837722002125", "citation": "Pandey, H. P., Gnyawali, K., <strong>Dahal, K.</strong>, & Pokhrel, N. P. (2022). &quot;Vegetation loss and recovery analysis from the 2015 Gorkha earthquake (7.8 Mw) triggered landslides.&quot; <i>Land Use Policy</i>."},
    {"title": "Natural Hazards Perspectives on Integrated, Coordinated, Open, Networked (ICON) Science", "venue": "Earth and Space Science", "date": "2022-01-01", "paperurl": "https://doi.org/10.1029/2021EA002114", "citation": "Sharma, S., <strong>Dahal, K.</strong>, Nava, L., et al. (2022). &quot;Natural Hazards Perspectives on Integrated, Coordinated, Open, Networked (ICON) Science.&quot; <i>Earth and Space Science</i>."},
    {"title": "Insights on the Impacts of Hydroclimatic Extremes and Anthropogenic Activities on Sediment Yield of a River Basin", "venue": "Earth", "date": "2021-01-01", "paperurl": "https://doi.org/10.3390/earth2010003", "citation": "Talchabhadel, R., Panthi, J., Sharma, S., <strong>Dahal, K.</strong>, et al. (2021). &quot;Insights on the Impacts of Hydroclimatic Extremes and Anthropogenic Activities on Sediment Yield of a River Basin.&quot; <i>Earth</i>."},
]

talks_data = [
    {"title": "A Framework to Improve Hydrological Forecasting with Deep Learning", "type": "Conference Poster", "venue": "ASU Flow 2024", "date": "2024-10-21", "location": "Arizona State University, USA", "description": "This poster received the Outstanding Poster Award."},
    {"title": "Operational Streamflow Forecasting Tool for Arizona Streams", "type": "Conference Presentation", "venue": "CMWR 2024", "date": "2024-10-02", "location": "University of Arizona, USA"},
    {"title": "Mapping wetland potential in arid environments: A machine learning approach with geospatial interpretability", "type": "Conference Presentation", "venue": "AGU Chapman Conference", "date": "2024-02-13", "location": "Honolulu, USA"},
    {"title": "Advances in Hyperspectral Remote Sensing for Water Resources", "type": "Conference Presentation", "venue": "AGU Fall Meeting 2023", "date": "2023-12-11", "location": "San Francisco, USA"},
    {"title": "Explainable Artificial Intelligence to visualize the unseen", "type": "Conference Presentation", "venue": "EWRI Congress 2023", "date": "2023-05-21", "location": "Nevada, USA"},
    {"title": "Spatial decision making with landslide susceptibility and critical infrastructure", "type": "Conference Presentation", "venue": "DRI Technical Conference 2022", "date": "2022-10-12", "location": "Delhi, India"},
    {"title": "National landslides database and susceptibility assessment of Nepal", "type": "Conference Presentation", "venue": "AGU Fall Meeting 2021", "date": "2021-12-13", "location": "Online"},
    {"title": "Explainable Machine Learning in Groundwater Potential Mapping", "type": "Invited Webinar", "venue": "UNESCO GWYN", "date": "2024-03-13", "location": "Online", "url": "https://rb.gy/ue0vik"},
]

teaching_data = [
    {"title": "Num. Methods for Engrs (CEE 384)", "venue": "Arizona State University", "date": "2024-01-15", "description": "Served as a Teaching Assistant for the Spring 2024 semester."},
    {"title": "Fluid Mechanics for Civil Engrs (CEE 341)", "venue": "Arizona State University", "date": "2023-08-20", "description": "Served as a Teaching Assistant for the Fall 2023 semester."},
    {"title": "Engineering Hydrology (CE 606)", "venue": "Tribhuvan University, Nepal", "date": "2021-01-15", "description": "Served as a Teaching Assistant for the Spring 2021 semester."},
    {"title": "GIS and Remote Sensing (CE 78501)", "venue": "Tribhuvan University, Nepal", "date": "2020-08-20", "description": "Served as a Teaching Assistant for the Fall 2020 semester."},
    {"title": "Engineering Surveying (CE 504)", "venue": "Tribhuvan University, Nepal", "date": "2019-01-15", "description": "Served as a Teaching Assistant for the Spring 2019 semester."},
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
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
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
        if item_type: content += f"type: \"{item_type}\"\n"
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
    with open(filepath, 'w', encoding='utf-8') as f: f.write(content)
    print(f"✓ Updated {filepath}")

def generate_navigation():
    nav_content = """main:
  - title: "Publications"
    url: /publications/
  - title: "Talks"
    url: /talks/    
  - title: "Teaching"
    url: /teaching/    
  - title: "Media"
    url: /media/
  - title: "Resources"
    url: /resources/
  - title: "CV"
    url: /cv/
"""
    generate_page("_data/navigation.yml", nav_content)

if __name__ == "__main__":
    print("--- Clearing old content ---")
    clear_folder("_publications"); clear_folder("_talks"); clear_folder("_teaching")

    print("\n--- Generating Core Pages & Navigation ---")
    generate_navigation()
    
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
<a href="/files/CV_Kshitij_Dahal.pdf" class="btn btn--primary" target="_blank">Download Full CV (PDF)</a>

### Education
"""
    for item in personal_info['education']: cv_content += f"* {item['degree']}, *{item['university']}*, {item['period']}\n"
    cv_content += "\n### Academic Employment\n"
    for item in personal_info['employment']: cv_content += f"* **{item['role']}**\n  * {item['institution']}\n  * {item['period']}\n"
    cv_content += """
### Publications
<ul>{% for post in site.publications reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>
  
### Talks & Presentations
<ul>{% for post in site.talks reversed %}{% include archive-single-talk-cv.html %}{% endfor %}</ul>
  
### Teaching
<ul>{% for post in site.teaching reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>
"""
    cv_content += "\n### Honors and Awards\n"
    for item in personal_info['awards']: cv_content += f"* {item}\n"
    generate_page("_pages/cv.md", cv_content)
    
    media_content = """---
layout: archive
title: "Media"
permalink: /media/
author_profile: true
---
This page features news articles, op-eds, and other media mentions related to my work.
"""
    generate_page("_pages/media.md", media_content)
    
    resources_content = """---
layout: archive
title: "Resources"
permalink: /resources/
author_profile: true
---
This page provides links to useful resources, tools, and courses I have developed or recommend.
"""
    generate_page("_pages/resources.md", resources_content)
    
    publications_page_content = """---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on my <a href="{{site.author.googlescholar}}">Google Scholar profile</a>.</div>
{% endif %}
{% include base_path %}
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
"""
    generate_page("_pages/publications.html", publications_page_content)


    print("\n--- Generating Collection Files ---")
    generate_markdown_files(publications_data, "_publications", "publications", "publication")
    generate_markdown_files(talks_data, "_talks", "talks", "talks", type_key="type", default_type="Talk")
    generate_markdown_files(teaching_data, "_teaching", "teaching", "teaching")
    
    print("\nGeneration complete! All files created locally.")
    print("Next step: Run 'git push' to upload them to GitHub.")