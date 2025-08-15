# generate_content.py (Final Corrected Version)
import os
import re

# =============================================================================
# DATA SECTION
# This is the single source of truth for your website's content.
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
    ]
}

publications_data = [
    {"title": "Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires", "venue": "Information Geography", "date": "2025-01-01", "paperurl": "https://doi.org/10.1016/j.infgeo.2025.100003", "citation": "<strong>Dahal, K.</strong>*, Talchabhadel, R., Pradhan, P., et al. (2025). &quot;Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires.&quot; <i>Information Geography</i>."},
    # Add all other publications here...
]

talks_data = [
    {"title": "A Framework to Improve Hydrological Forecasting with Deep Learning", "type": "Conference Poster", "venue": "ASU Flow 2024", "date": "2024-10-21", "location": "Arizona State University, USA", "description": "This poster received the Outstanding Poster Award."},
    # Add all other talks here...
]

teaching_data = [
    {"title": "Num. Methods for Engrs (CEE 384)", "venue": "Arizona State University", "date": "2024-01-15", "description": "Served as a Teaching Assistant for the Spring 2024 semester."},
    # Add all other teaching experiences here...
]

media_data = [
    {"type": "Op-Ed", "authors": "Dahal, K. & Thapa, B. R.", "year": "2025", "title": "World Water Day 2025 on Glacier Preservation: What It Means for Nepal?", "venue": "Republica", "url": "https://myrepublica.nagariknetwork.com/news/world-water-day-2025-on-glacier-preservation-what-it-means-for-nepal/"},
    # Add all other media items here...
]

blog_data = [
    {"title": "On Data-Driven Science in Hydrology", "date": "2024-08-16", "tags": ["Data Science", "Hydrology", "Machine Learning"], "excerpt": "A reflection on the shift from process-based models to data-driven approaches in hydrology...", "content": """In a traditional approach, we lean on centuries of scientific thought..."""},
    {"title": "Reflections on a 10-Day Vipassana Course", "date": "2024-08-15", "tags": ["Meditation", "Mindfulness", "Vipassana"], "excerpt": "My experience with a 10-day silent meditation retreat...", "content": """I first became curious about Vipassana after reading *The Power of Now*..."""},
    {"title": "Favorite Books & Wisdom", "date": "2024-08-14", "tags": ["Books", "Wisdom", "Reading"], "excerpt": "A curated list of books and wisdom that I find valuable.", "content": """### Wisdom I Live By\n*   Ignorance is not bliss.\n*   Plans should be measured in decades...\n\n### Foundational Books\n*   **The Power of Now** by Eckhart Tolle..."""},
    {"title": "On the Law of Averages", "date": "2024-08-13", "tags": ["Productivity", "Mindset", "Persistence"], "excerpt": "How persistence and increasing your attempts can lead to success...", "content": """Sometimes, we really want to stand out..."""},
    {"title": "On Time Management", "date": "2024-08-12", "tags": ["Productivity", "Goals", "Time Management"], "excerpt": "A simple approach to time management that starts with a clear goal...", "content": """Time management really starts with having a clear goal..."""},
]

# =============================================================================
# SCRIPT LOGIC (No need to edit below this line)
# =============================================================================

def slugify(text):
    text = text.lower(); text = re.sub(r'[^a-z0-9\s-]', '', text); text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def clear_folder(folder_path):
    if not os.path.exists(folder_path): os.makedirs(folder_path)
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"): os.remove(os.path.join(folder_path, filename))
    print(f"Cleared markdown files in {folder_path}")

def generate_page(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f: f.write(content)
    print(f"✓ Updated {filepath}")

def generate_collection_files(data, folder, collection_name, permalink_prefix, type_key=None, default_type=None):
    for item in data:
        slug = slugify(item['title'])[:50]
        filename = f"{item['date']}-{slug}.md"
        filepath = os.path.join(folder, filename)
        
        # --- Create YAML Front Matter ---
        content = "---\n"
        content += f"title: \"{item['title'].replace(':', '')}\"\n"
        
        if collection_name == "posts":
            content += f"date: {item['date']}\n"
            content += f"permalink: /posts/{item['date'][:4]}/{slug}/\n"
            content += "tags:\n"
            for tag in item.get('tags', []):
                content += f"  - {tag}\n"
            if item.get('excerpt'):
                content += f"excerpt: \"{item['excerpt'].replace('"', '&quot;')}\"\n"
        else:
            content += f"collection: {collection_name}\n"
            content += f"permalink: /{permalink_prefix}/{item['date']}-{slug}\n"
            item_type = item.get(type_key, default_type)
            if item_type: content += f"type: \"{item_type}\"\n"
            for key, value in item.items():
                if key not in ['title', 'type', 'content', 'tags', 'excerpt'] and value:
                    clean_value = str(value).replace("'", "’").replace('"', '&quot;')
                    content += f"{key}: '{clean_value}'\n"
        
        content += "---\n\n"
        
        # --- CORRECTED: Create Main Content ---
        # This now correctly adds the main 'content' for blog posts.
        if item.get('content'):
            content += item['content']
        elif item.get('description'):
            content += item['description']
        
        if item.get('url'):
            content += f"\n\n[More information here]({item['url']})"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Created {filepath}")

if __name__ == "__main__":
    # Clear old markdown files to ensure a fresh build
    for folder in ["_publications", "_talks", "_teaching", "_posts"]: clear_folder(folder)

    # Generate static pages and navigation
    print("\n--- Generating Core Pages & Navigation ---")
    nav_content = """main:\n  - title: "Publications"\n    url: /publications/\n  - title: "Talks"\n    url: /talks/\n  - title: "Teaching"\n    url: /teaching/\n  - title: "Media"\n    url: /media/\n  - title: "Blog"\n    url: /blog/\n  - title: "Resources"\n    url: /resources/\n  - title: "CV"\n    url: /cv/"""
    generate_page("_data/navigation.yml", nav_content)

    about_content = f"""---\npermalink: /\ntitle: "About Me"\nauthor_profile: true\n---\nWelcome! I am a PhD Candidate at Arizona State University. {personal_info['summary']}"""
    generate_page("_pages/about.md", about_content)
    
    cv_content = """---\nlayout: archive\ntitle: "CV"\npermalink: /cv/\nauthor_profile: true\n---\n{% include base_path %}\n<a href="/files/CV_Kshitij_Dahal.pdf" class="btn btn--primary" target="_blank">Download Full CV (PDF)</a>\n\n### Education\n"""
    for item in personal_info['education']: cv_content += f"* {item['degree']}, *{item['university']}*, {item['period']}\n"
    cv_content += "\n### Academic Employment\n"
    for item in personal_info['employment']: cv_content += f"* **{item['role']}**\n  * {item['institution']}\n  * {item['period']}\n"
    cv_content += "\n### Honors and Awards\n"
    for item in personal_info['awards']: cv_content += f"* {item}\n"
    cv_content += """\n### Publications\n<ul>{% for post in site.publications reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>\n\n### Talks & Presentations\n<ul>{% for post in site.talks reversed %}{% include archive-single-talk-cv.html %}{% endfor %}</ul>\n\n### Teaching\n<ul>{% for post in site.teaching reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>"""
    generate_page("_pages/cv.md", cv_content)

    media_content = """---\nlayout: archive\ntitle: "Media"\npermalink: /media/\nauthor_profile: true\n---\nThis page features news articles, op-eds, and media mentions related to my work.\n"""
    grouped_media = {}; [grouped_media.setdefault(item.get("type", "General"), []).append(item) for item in media_data]
    if "Op-Ed" in grouped_media:
        media_content += "\n## News Columns (Op-Ed)\n"
        for item in grouped_media["Op-Ed"]: media_content += f"* {item['authors']} ({item['year']}). **[{item['title']}]({item['url']})**. *{item['venue']}*.\n"
    if "Media Citation" in grouped_media:
        media_content += "\n## Professional Media Citations\n"
        for item in grouped_media["Media Citation"]: media_content += f"* **[{item['title']}]({item['url']})**. *{item['venue']}*, {item['year']}.\n"
    generate_page("_pages/media.md", media_content)

    # (Other pages like resources, publications list, etc.)
    resources_content = """---\nlayout: archive\ntitle: "Resources"\npermalink: /resources/\nauthor_profile: true\n---\n"""
    generate_page("_pages/resources.md", resources_content)
    publications_page_content = """---\nlayout: archive\ntitle: "Publications"\npermalink: /publications/\nauthor_profile: true\n---\n{% if site.author.googlescholar %}\n  <div class="wordwrap">You can also find my articles on my <a href="{{site.author.googlescholar}}">Google Scholar profile</a>.</div>\n{% endif %}\n{% include base_path %}\n{% for post in site.publications reversed %}\n  {% include archive-single.html %}\n{% endfor %}"""
    generate_page("_pages/publications.html", publications_page_content)
    blog_page_content = """---\nlayout: archive\ntitle: "Blog"\npermalink: /blog/\nauthor_profile: true\n---\n{% include base_path %}\n{% capture written_year %}'None'{% endcapture %}\n{% for post in site.posts reversed %}\n  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}\n  {% if year != written_year %}\n    <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>\n    {% capture written_year %}{{ year }}{% endcapture %}\n  {% endif %}\n  {% include archive-single.html %}\n{% endfor %}"""
    generate_page("_pages/blog.md", blog_page_content)

    # Generate collection files
    print("\n--- Generating Collection Files ---")
    generate_collection_files(publications_data, "_publications", "publications", "publication")
    generate_collection_files(talks_data, "_talks", "talks", "talks", type_key="type", default_type="Talk")
    generate_collection_files(teaching_data, "_teaching", "teaching", "teaching")
    generate_collection_files(blog_data, "_posts", "posts", "posts")
    
    print("\nGeneration complete!")