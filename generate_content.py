# /geokshitij.github.io/generate_content.py
import os
import re
from datetime import datetime

# =============================================================================
# DATA SECTION
# This is the single source of truth for the website's content,
# =============================================================================


# This list allows you to manually add news that isn't an award or talk.
other_news_data = [
    {"date": "2025-07-29", "description": "🎓 Officially became a **PhD Candidate** after successfully passing my comprehensive exam."},
    {"date": "2024-10-21", "description": "🏆 Received the **Outstanding Poster Award** for my work on 'A Framework to Improve Hydrological Forecasting with Deep Learning' at the ASU Flow 2024 symposium."},
    {"date": "2024-05-15", "description": "✨ Selected as a **Community Science Fellow** by the American Geophysical Union's Thriving Earth Exchange."},
    {"date": "2023-06-12", "description": "🏆 Won **1st place** in the SpaceHack for Sustainability Hackathon at Arizona State University."},
    {"date": "2022-12-01", "description": "✨ Started my PhD journey at Arizona State University."},
    {"date": "2021-09-17", "description": "🏆 Won **1st place** in the Hackathon Competition at the 3rd NOAA Workshop on Leveraging AI in Environmental Sciences."},
]


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
        "Community Science Fellow, Thriving Earth Exchange, American Geophysical Union (https://thrivingearthexchange.org/project/lumberton-nc/), 2024 – 2026",
        "Outstanding Reviewer Award, Earth’s Future, American Geophysical Union, 2025",
        "Full Scholarship to the Snow Measurement Field School, CUAHSI, Mammoth Lakes, California (5 days residential school), 2025",
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
    {"title": "Developing a framework for assessment of the school’s exposure to flood-depth scenarios", "venue": "Natural Hazards", "date": "2025-12-31", "paperurl": "", "citation": "Bishui, C., … & <strong>Dahal. K.</strong> (Under Review). &quot;Developing a framework for assessment of the school’s exposure to flood-depth scenarios.&quot; <i>Natural Hazards</i>."},
    {"title": "Improving Hydrological Forecasting with Bayesian Model Averaging Over Multiple Loss Functions", "venue": "Applied Soft Computing", "date": "2025-12-30", "paperurl": "", "citation": "<strong>Dahal, K.</strong>, Gupta, A., Bokati, L. & Kumar, S.* (Under Review). &quot;Improving Hydrological Forecasting with Bayesian Model Averaging Over Multiple Loss Functions.&quot; <i>Applied Soft Computing</i>."},
    {"title": "Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires", "venue": "Information Geography", "date": "2025-01-01", "paperurl": "https://doi.org/10.1016/j.infgeo.2025.100003", "citation": "<strong>Dahal, K.</strong>*, Talchabhadel, R., Pradhan, P., Parajuli, S., Shrestha, D., Chhetri, R., Gautam, A. P., Tamrakar, R., Gurung, S., & Kumar, S. (2025). &quot;Nepal's carbon stock and biodiversity are under threat from climate exacerbated forest fires.&quot; <i>Information Geography</i>."},
    {"title": "Policy Relevance of IPCC Reports for the SDGs and Beyond", "venue": "Resources, Environment and Sustainability", "date": "2025-01-01", "paperurl": "https://doi.org/10.1016/j.resenv.2025.100192", "citation": "Pradhan, P., Joshi, S., <strong>Dahal, K.</strong>, Hu, Y., Subedi, D. R., Putra, M. P. I. F., Vaidya, S., Pant, L. P., Dhakal, S., Hubacek, K., Rupakheti, M., Roberts, D., & van den Hurk, B. (2025). &quot;Policy Relevance of IPCC Reports for the SDGs and Beyond.&quot; <i>Resources, Environment and Sustainability (Invited Editorial)</i>."},
    {"title": "Urban agriculture matters for sustainable development", "venue": "Cell Reports Sustainability", "date": "2024-01-01", "paperurl": "https://doi.org/10.1016/j.crsus.2024.100217", "citation": "Pradhan, P., Subedi, D. R., <strong>Dahal, K.</strong>, Hu, Y., Gurung, P., Pokharel, S., Kafle, S., Khatri, B., Basyal, S., Gurung, M., & Joshi, A. (2024). &quot;Urban agriculture matters for sustainable development.&quot; <i>Cell Reports Sustainability</i>."},
    {"title": "Identification of groundwater potential zones in data-scarce mountainous region using explainable machine learning", "venue": "Journal of Hydrology", "date": "2023-01-01", "paperurl": "https://doi.org/10.1016/j.jhydrol.2023.130417", "citation": "<strong>Dahal, K.</strong>*, Sharma, S., Shakya, A., Talchabhadel, R., Adhikari, S., Pokharel, A., Sheng, Z., Pradhan, A. M. S., & Kumar, S. (2023). &quot;Identification of groundwater potential zones in data-scarce mountainous region using explainable machine learning.&quot; <i>Journal of Hydrology</i>."},
    {"title": "Mapping landslide susceptibility and critical infrastructure for spatial decision-making", "venue": "Sustainable and Resilient Infrastructure", "date": "2023-01-01", "paperurl": "https://www.tandfonline.com/doi/full/10.1080/23789689.2023.2181552", "citation": "<strong>Dahal, K.</strong>*, & Gnyawali, K.R., (2023) &quot;Mapping landslide susceptibility and critical infrastructure for spatial decision-making.&quot; <i>Sustainable and Resilient Infrastructure</i>."},
    {"title": "Multimodal multiscale characterization of cascading hazard on mountain terrain", "venue": "Geomatics, Natural Hazards and Risk", "date": "2023-01-01", "paperurl": "https://doi.org/10.1080/19475705.2022.2162443", "citation": "Talchabhadel, R., Maskey, S., Gouli, M. R., <strong>Dahal, K.</strong>*, Thapa, A., Sharma, S., Dixit, A. M., & Kumar, S. (2023). &quot;Multimodal multiscale characterization of cascading hazard on mountain terrain.&quot; <i>Geomatics, Natural Hazards and Risk</i>, 14(1), 2162443."},
    {"title": "Framework for rainfall-triggered landslide-prone critical infrastructure zonation", "venue": "Science of the Total Environment", "date": "2023-01-01", "paperurl": "https://doi.org/10.1016/j.scitotenv.2023.162242", "citation": "Gnyawali, K., <strong>Dahal, K.</strong>, Talchabhadel, R., & Nirandjan, S. (2023). &quot;Framework for rainfall-triggered landslide-prone critical infrastructure zonation.&quot; <i>Science of the Total Environment</i>, 872, 162242."},
    {"title": "Land use and land cover change implications on agriculture and natural resource management of Koah Nheaek, Mondulkiri province, Cambodia", "venue": "Remote Sensing Applications: Society and Environment", "date": "2023-01-01", "paperurl": "https://doi.org/10.1016/j.rsase.2022.100895", "citation": "Teck, V., Poortinga, A., Riano, C., <strong>Dahal, K.</strong>, Legaspi, R. M. B., Ann, V., & Chea, R. (2023). &quot;Land use and land cover change implications on agriculture and natural resource management of Koah Nheaek, Mondulkiri province, Cambodia.&quot; <i>Remote Sensing Applications: Society and Environment</i>, 29, 100895."},
    {"title": "Assessment of shelter location-allocation for multi-hazard emergency evacuation", "venue": "International Journal of Disaster Risk Reduction", "date": "2023-01-01", "paperurl": "https://doi.org/10.1016/j.ijdrr.2022.103435", "citation": "Bera, S., Gnyawali, K., <strong>Dahal, K.</strong>, Melo, R., Li-Juan, M., Guru, B., & Ramana, G. V. (2023). &quot;Assessment of shelter location-allocation for multi-hazard emergency evacuation.&quot; <i>International Journal of Disaster Risk Reduction</i>, 84, 103435."},
    {"title": "A systematic review highlights that there are multiple benefits of urban agriculture besides food", "venue": "Global Food Security", "date": "2023-01-01", "paperurl": "https://doi.org/10.1016/j.gfs.2023.100700", "citation": "Pradhan, P., Callaghan, M., Hu, Y., <strong>Dahal, K.</strong>, Hunecke, C., Reusswig, F., Lotze-Campen, H., & Kropp, J. P. (2023). &quot;A systematic review highlights that there are multiple benefits of urban agriculture besides food.&quot; <i>Global Food Security</i>, 38, 100700."},
    {"title": "Vegetation loss and recovery analysis from the 2015 Gorkha earthquake (7.8 Mw) triggered landslides", "venue": "Land Use Policy", "date": "2022-01-01", "paperurl": "https://www.sciencedirect.com/science/article/pii/S0264837722002125", "citation": "Pandey, H. P., Gnyawali, K., <strong>Dahal, K.</strong>, & Pokhrel, N. P. (2022). &quot;Vegetation loss and recovery analysis from the 2015 Gorkha earthquake (7.8 Mw) triggered landslides.&quot; <i>Land Use Policy</i>."},
    {"title": "Natural Hazards Perspectives on Integrated, Coordinated, Open, Networked (ICON) Science", "venue": "Earth and Space Science", "date": "2022-01-01", "paperurl": "https://doi.org/10.1029/2021EA002114", "citation": "Sharma, S., <strong>Dahal, K.</strong>, Nava, L., Gouli, M. R., Talchabhadel, R., Panthi, J., Roy, T., & Ghimire, G. R. (2022). &quot;Natural Hazards Perspectives on Integrated, Coordinated, Open, Networked (ICON) Science.&quot; <i>Earth and Space Science</i>, 9(1), e2021EA002114."},
    {"title": "Insights on the Impacts of Hydroclimatic Extremes and Anthropogenic Activities on Sediment Yield of a River Basin", "venue": "Earth", "date": "2021-01-01", "paperurl": "https://doi.org/10.3390/earth2010003", "citation": "Talchabhadel, R., Panthi, J., Sharma, S., Ghimire, G. R., Baniya, R., Dahal, P., Baniya, M. B., K. C., S., Jha, B., Kaini, S., <strong>Dahal, K.</strong>, Gnyawali, K. R., Parajuli, B., & Kumar, S. (2021). &quot;Insights on the Impacts of Hydroclimatic Extremes and Anthropogenic Activities on Sediment Yield of a River Basin.&quot; <i>Earth</i>, 2(1), 32–50."},
]

talks_data = [
    {"title": "A Framework to Improve Hydrological Forecasting with Deep Learning", "type": "Conference Poster", "venue": "ASU Flow 2024", "date": "2024-10-21", "location": "Arizona State University, USA", "description": "This poster received the Outstanding Poster Award."},
    {"title": "Operational Streamflow Forecasting Tool for Arizona Streams", "type": "Conference Talk", "venue": "CMWR 2024", "date": "2024-10-02", "location": "University of Arizona, USA"},
    {"title": "Mapping wetland potential in arid environments: A machine learning approach with geospatial interpretability", "type": "Conference Talk", "venue": "AGU Chapman Conference on Remote Sensing of the Water Cycle", "date": "2024-02-13", "location": "Honolulu, HI, USA"},
    {"title": "Explainable Machine Learning in Groundwater Potential Mapping", "type": "Invited Webinar", "venue": "UNESCO GWYN", "date": "2024-03-13", "location": "Online", "url": "https://rb.gy/ue0vik"},
    {"title": "Advances in Hyperspectral Remote Sensing for Water Resources", "type": "Conference Poster", "venue": "AGU Fall Meeting 2023", "date": "2023-12-11", "location": "San Francisco, USA"},
    {"title": "Discussion Facilitator at Session 1 --Development of core use cases in environmental sciences", "type": "Invited Talk", "venue": "5th NOAA Workshop on Leveraging AI in Environmental Sciences", "date": "2023-09-19", "location": "Online", "url": "https://noaaai2023.sched.com/event/1Q6Qa/session-1-development-of-core-use-cases-in-environmental-sciences"},
    {"title": "Remote Sensing, Big Data Analytics, and Cloud Computing: Application to Water Quality Modeling", "type": "Workshop", "venue": "Environmental & Water Resources Institute (EWRI) Congress 2023, ASCE", "date": "2023-05-22", "location": "Henderson, NV, USA"},
    {"title": "Explainable Artificial Intelligence to visualize the unseen", "type": "Conference Talk", "venue": "EWRI Congress 2023", "date": "2023-05-21", "location": "Nevada, USA"},
    {"title": "Spatial decision making with landslide susceptibility and critical infrastructure", "type": "Conference Talk", "venue": "DRI Technical Conference 2022", "date": "2022-10-12", "location": "Delhi, India"},
    {"title": "Landslide susceptibility and monsoon preparedness in Nepal: An engineering perspective", "type": "Invited Lecture", "venue": "Khwopa College of Engineering, Tribhuvan University", "date": "2022-06-21", "location": "Nepal", "url": "https://fb.watch/kO9H0OeO2T/"},
    {"title": "Introduction to Google Earth Engine for cloud computing", "type": "Invited Discussion", "venue": "S4W Nepal", "date": "2022-04-07", "location": "Online"},
    {"title": "Google Earth Engine and cloud computing", "type": "Invited Lecture", "venue": "Central Department of Geography, Tribhuvan University", "date": "2022-04-06", "location": "Nepal"},
    {"title": "National landslides database and susceptibility assessment of Nepal", "type": "Conference Poster", "venue": "AGU Fall Meeting 2021", "date": "2021-12-13", "location": "Online", "url": "https://ui.adsabs.harvard.edu/abs/2021AGUFMNH35F..11D"},
    {"title": "Framework for multi-hazards susceptibility assessment in Google Earth Engine", "type": "Conference Poster", "venue": "AGU Fall Meeting 2021", "date": "2021-12-13", "location": "Online", "url": "https://ui.adsabs.harvard.edu/abs/2021AGUFMGC45I0916D"},
    {"title": "Spatial downscaling of coarse resolution satellite-based precipitation estimates (SPEs) to 1 km using Machine Learning", "type": "Conference Talk", "venue": "3rd NOAA Workshop on Leveraging AI in Environmental Sciences", "date": "2021-09-13", "location": "USA"},
    {"title": "Machine Learning to Estimate Precipitation with Satellite-based and Gauged Observations", "type": "Conference Talk", "venue": "3rd NOAA Workshop on Leveraging AI in Environmental Sciences", "date": "2021-09-13", "location": "USA"},
    {"title": "Chocolate Talk on DRR #3: Artificial intelligence (AI) for disaster risk reduction", "type": "Moderator", "venue": "U-INSPIRE Alliance", "date": "2021-08-28", "location": "Online", "url": "https://www.youtube.com/watch?v=mHLaFQw-C7A"},
    {"title": "DRR talk #1: The future of disaster risk governance in 2045", "type": "Invited Talk", "venue": "Disaster Risk Reduction and Tsunami Information, UNESCO Office, Jakarta", "date": "2021-07-30", "location": "Online", "url": "https://fb.watch/kO9y3nBapv/"},
    {"title": "Landslide Susceptibility Mapping in Nepal using Google Earth Engine", "type": "Conference Talk", "venue": "Geo for Good 2020", "date": "2020-10-20", "location": "USA"},
]


teaching_data = [
    {"title": "Num. Methods for Engrs (CEE 384)", "type": "Teaching Assistant", "venue": "Arizona State University", "date": "2024-01-15", "description": "Served during the Spring 2024 semester."},
    {"title": "Fluid Mechanics for Civil Engrs (CEE 341)", "type": "Teaching Assistant", "venue": "Arizona State University", "date": "2023-08-15", "description": "Served during the Fall 2023 semester."},
    {"title": "Engineering Hydrology (CE 606)", "type": "Teaching Assistant", "venue": "Tribhuvan University, Nepal", "date": "2021-01-15", "description": "Served during the Spring 2021 semester."},
    {"title": "GIS and Remote Sensing (CE 78501)", "type": "Teaching Assistant", "venue": "Tribhuvan University, Nepal", "date": "2020-08-15", "description": "Served during the Fall 2020 semester."},
    {"title": "Engineering Surveying (CE 504)", "type": "Teaching Assistant", "venue": "Tribhuvan University, Nepal", "date": "2019-01-15", "description": "Served during the Spring 2019 semester."},
    # Note: I removed one duplicate entry for Engineering Hydrology from your CV for this list.
]


media_data = [
    # Op-Eds
    {"type": "Op-Ed", "authors": "Dahal, K. & Thapa, B. R.", "year": "2025", "title": "World Water Day 2025 on Glacier Preservation: What It Means for Nepal?", "venue": "Republica", "url": "https://myrepublica.nagariknetwork.com/news/world-water-day-2025-on-glacier-preservation-what-it-means-for-nepal/"},
    {"type": "Op-Ed", "authors": "Dahal, K., Talchabhadel, R., & Thapa, B. R.", "year": "2021", "title": "Landslide susceptibility and monsoon preparedness in Nepal: An engineering perspective", "venue": "Onlinekhabar", "url": "https://english.onlinekhabar.com/landslide-susceptibility-nepal.html"},
    {"type": "Op-Ed", "authors": "Thapa, B. R., Talchabhadel, R., Dahal, K., & Pandey, V.P.", "year": "2021", "title": "मेलम्चीको बाढीबाट के सिक्ने ?", "venue": "Onlinekhabar", "url": "https://www.onlinekhabar.com/2021/06/974746"},
    
    # Media Citations
    {"type": "Media Citation", "year": "2025", "title": "Tourism and biodiversity at risk as raging wildfires devastate forests in Nepal", "venue": "China Daily", "url": "https://www.chinadaily.com.cn/a/202503/27/WS67e4bd4da3101d4e4dc2b29b.html"},
    {"type": "Media Citation", "year": "2025", "title": "Open burning main cause of air pollution", "venue": "The Rising Nepal", "url": "https://risingnepaldaily.com/news/58977"},
    {"type": "Media Citation", "year": "2025", "title": "Wildfire Ravage Hundreds Of Acres Of Forest Land In Nepal - World News", "venue": "WION TV", "url": "https://www.youtube.com/watch?v=UFb_3MyJpew"},
    {"type": "Media Citation", "year": "2025", "title": "Ignored infernos", "venue": "The Kathmandu Post (EDITORIAL)", "url": "https://kathmandupost.com/editorial/2025/03/18/ignored-infernos"},
    {"type": "Media Citation", "year": "2025", "title": "Wildfires put 500m tonnes of carbon— and tourism—at risk", "venue": "Asia News Network", "url": "https://asianews.network/nepals-wildfires-put-500m-tonnes-of-carbon-and-tourism-at-risk"},
    {"type": "Media Citation", "year": "2025", "title": "Wildfire season has begun, but the worst is yet to come", "venue": "The Himalayan Times", "url": "https://thehimalayantimes.com/nepal/wildfire-season-has-begun-but-the-worst-is-yet-to-come"},
    {"type": "Media Citation", "year": "2025", "title": "Wildfires put 500m tonnes of carbon— and tourism—at risk", "venue": "The Kathmandu Post", "url": "https://kathmandupost.com/money/2025/03/17/wildfires-put-500m-tonnes-of-carbon-and-tourism-at-risk"},
    {"type": "Media Citation", "year": "2025", "title": "Loss of Biodiversity Due to Wildfire (डढेलोबाट जैविक विविधता गुम्ने खतरा)", "venue": "Himal Khabar", "url": "https://www.himalkhabar.com/news/144165"},
    {"type": "Media Citation", "year": "2025", "title": "Study Report: Forests at Risk of Wildfire Due to Climate Crisis (अध्ययन रिपोर्ट : वन क्षेत्र जलवायु संकट कै कारण डढेलोको जोखिममा)", "venue": "Jalbayu (Climate)", "url": "https://www.jalbayu.com/news/2025-03-15-2271"},
    {"type": "Media Citation", "year": "2025", "title": "Forest Wildfires in Nepal Threaten 500 Million Tons of Carbon and Biodiversity (नेपालमा वन डढेलोले ५०० मिलियन टन कार्बन र जैविक विविधतामा खतरा)", "venue": "Artha Pranali (Economic System)", "url": "https://arthapranali.com/2025/03/11828"},
    {"type": "Media Citation", "year": "2025", "title": "Forest Wildfires Pose a Threat to Carbon and Biodiversity (वन डढेलोले कार्बन र जैविक विविधतामा खतरा)", "venue": "Everestpedia", "url": "https://www.everestpedia.com/detail/3646"},
    {"type": "Media Citation", "year": "2025", "title": "‘Forest Wildfires Threaten Biodiversity’ (‘वन डढेलोले जैविक विविधतामा खतरा’)", "venue": "Green Economy", "url": "https://greeconomy.com/fire-impact-on-biodiversity"},
    {"type": "Media Citation", "year": "2025", "title": "Forest Wildfires in Nepal Threaten 500 Million Tons of Carbon and Biodiversity (नेपालमा वन डढेलोले ५०० मिलियन टन कार्बन र जैविक विविधतामा खतरा)", "venue": "KendraBindu (Central Point)", "url": "https://kendrabindu.com/social-affairs/404665"},
    {"type": "Media Citation", "year": "2025", "title": "Forest Fires in Nepal Threaten 500 Million Tons of Carbon and Biodiversity (नेपालमा वन डढेलोले ५० करोड टन कार्बन र जैविक विविधतामा खतरा)", "venue": "Jal Sarokar (Water Concern)", "url": "https://jalasarokar.com/news/forest-fires-in-nepal-threaten-500-million-tons-of-carbon-and-biodiversity-2260"},
    {"type": "Media Citation", "year": "2025", "title": "Forest Wildfires in Nepal Threaten 500 Million Tons of Carbon and Biodiversity (नेपालमा वन डढेलोले ५ सय मिलियन टन कार्बन र जैविक विविधतामा खतरा)", "venue": "Kavre Khabar (Kavre News)", "url": "https://www.kavrekhabar.com/main-news/2025/03/16/3717"},
    {"type": "Media Citation", "year": "2025", "title": "Wildfires in Nepal pose threat to 500 million tons of carbon and biodiversity (नेपालमा वन डढेलोले ५०० मिलियन टन कार्बन र जैविक विविधतामा खतरा)", "venue": "Arthik Digital News", "url": "https://www.eaarthik.com/2025/03/117227/"},
    {"type": "Media Citation", "year": "2024", "title": "Back to the land in the cities", "venue": "Nepali Times", "url": "https://nepalitimes.com/here-now/back-to-the-land-in-the-cities"},
    {"type": "Media Citation", "year": "2021", "title": "Landslide susceptibility and monsoon preparedness in Nepal: An engineering perspective", "venue": "PreventionWeb, UNDRR", "url": "https://www.preventionweb.net/news/landslide-susceptibility-and-monsoon-preparedness-nepal-engineering-perspective"},
]



courses_data = [
    {"authors": "Cho, H., Ashraf, F., Dahal, K.", "year": "2024", "title": "Flood Inundation Mapping Using Machine Learning for Sustainable vs. Resilient Design", "venue": "CIROH", "url": "https://edx.hydrolearn.org/courses/course-v1:NMSU+CE483+Fall2024/about"},
    {"authors": "Dahal, K.", "year": "2024", "title": "py4all: The Bare Minimum Python Guide", "venue": "GitHub Repository", "url": "https://github.com/geokshitij/py4all"}
]
reports_data = [
    {"authors": "UNDRR", "year": "2022", "title": "Scoping Study On Compound, Cascading And Systemic Risks In The Asia Pacific", "venue": "United Nations Office for Disaster Risk Reduction (UNDRR)", "url": "https://www.undrr.org/quick/71248"}
]
projects_data = [
    {"authors": "Dahal, K.", "year": "2024", "title": "Arizona's Water Story: The Lifelines of the Sonoran Desert", "venue": "Data Story", "url": "https://geokshitij.github.io/azwaters/"}
]


blog_data = [



        {
        "title": "The Triangle of Self-Obsession",
        "date": "2023-06-14",
        "tags": ["Mindset", "Wisdom", "Philosophy", "Ego", "Letting Go"],
        "excerpt": "There is a self-destructive pattern that traps us in suffering. It is a triangle with three points: resentment, anger, and fear. The only way out is to see it for what it is.",
        "content": """There is a self-destructive pattern that traps us in suffering. It is a triangle that keeps our world small and centered on ourselves. To escape it, you must first recognize its shape.\n\n### Resentment is the Past\n\nThis is the poison of reliving what has already happened. It is the obsessive focus on past hurts and injustices. It keeps you chained to a story that is over, forcing you to carry a weight that no longer needs to be held. \n\n### Anger is the Present\n\nThis is the fire of reacting to what is happening right now. It is the ego’s fierce resistance to the present moment not being what it wants. It is a defense against a feeling of powerlessness, a surge of energy that consumes you here and now.\n\n### Fear is the Future\n\nThis is the anxiety of imagining what is yet to come. It is the story of a future catastrophe, a failure, or a loss that has not happened. It keeps you trapped in a negative possibility, robbing you of peace in the only moment you truly have.\n\n### One Feeling, Three Masks\n\nLook closely at these three emotions. Resentment, anger, and fear. Though they appear to live in different times—past, present, future—they are all the same feeling. \n\nThey are the feeling of self-obsession. Each one is a story entirely about *you*. What happened to you. What is happening to you. What might happen to you. \n\nThis is the illusion that will destroy your peace.\n\nGet rid of all of it. Do not hold anything back. Let go of the story, and the suffering will follow."""
    },


        {
        "title": "On Forgiveness",
        "date": "2022-04-02",
        "tags": ["Wisdom", "Forgiveness", "Mindset", "Personal Growth"],
        "excerpt": "We misunderstand forgiveness. We think it's a gift we give to others. The truth is, it's a power we give to ourselves. And it starts in the one place we often forget to look.",
        "content": """We are told to forgive. But what does that really mean? The popular view treats forgiveness as a weakness, an act of letting someone get away with a wrongdoing. This is a profound misunderstanding. Forgiveness is not weakness. It is power.\n\nBut before you can offer it to the world, you must first give it to yourself.\n\n### The First Person to Forgive is You\n\nThis is the most crucial step, and the one most people skip. We forgive others, we forget what they did, but we carry the weight of our own mistakes forever. We become our own harshest judges. But you cannot forgive the world if you live in a state of self-resentment. How can you offer compassion to others that you deny yourself?\n\nIf you want to be free, the work starts here. You must forgive yourself for not knowing then what you know now. Forgive your past self. They were doing the best they could with the understanding they had.\n\n### Don’t Take Anything Personally\n\nWhen someone hurts you, it is almost never about you. Their actions are a reflection of their own stories, their own pain, and their own limitations. We label their actions as ‘wrong,’ but ‘right’ and ‘wrong’ are often just taglines, stories we tell ourselves. In reality, people are just people, doing the best they can.\n\nSo, do not fall into their trap. Do not let their inner world become your inner prison. Forgive them. You can be sad or angry when you confirm the truth; you don't need to be that way from the beginning based on a story in your head. Simply decide not to carry their burden for them. This decision is an act of liberation.\n\n### The Power to Choose\n\nWhen you haven't forgiven yourself, you cannot truly forgive others. You will see their faults through the lens of your own self-judgment. Every mistake they make will echo a mistake of your own that you haven’t made peace with.\n\nBut when you practice self-forgiveness, everything changes. You understand that we are all flawed, all learning, all trying.\n\nFrom this place, forgiveness is no longer a chore. It becomes a simple, powerful choice. It is the choice to release the past. It is the choice to take your power back. Forgiveness is a power, and you have to do it."""
    },

    {
        "title": "The Four Agreements",
        "date": "2022-08-23",
        "tags": ["Wisdom", "Mindset", "Personal Growth", "Philosophy", "Book Summary"],
        "excerpt": "There are four simple truths that, if practiced, can free us from the self-imposed suffering of blame, judgment, and assumption. Here is a guide to these transformative agreements.",
        "content": """So much of our suffering isn't caused by life itself, but by the stories we tell ourselves about it. We live by a set of unconscious agreements that create needless conflict, both internally and externally. The Toltec wisdom of *The Four Agreements* offers a simple, yet profound, new operating system for your mind—one based on freedom and self-love.\n\nHere are the four promises to make to yourself.\n\n### 1. Be Impeccable with Your Word\n\nYour word is the power you have to create. It is a seed. With it, you can create a beautiful dream or you can destroy everything around you. \n\nThis is especially true for the words you use on yourself. Your mind doesn’t question what you tell it; it simply believes. If you tell yourself you are not smart enough, not strong enough, not worthy, your mind will accept it as truth. To be impeccable is to use your words with love and truth, starting with the way you speak to yourself. It is the first and most fundamental step to reclaiming your power.\n\n### 2. Don't Take Anything Personally\n\nWhat others say and do is a projection of their own reality, their own dream. When someone is angry or unkind to you, they are revealing their own inner struggles. It is never about you.\n\nWhen you understand this, you gain a kind of immunity. The opinions and actions of others no longer have the power to wound you. This single agreement can save you from countless grudges, conflicts, and needless emotional pain. It allows you to interact with others from a place of compassion rather than reaction.\n\n### 3. Don't Make Assumptions\n\nWe have a tendency to invent entire stories in our minds when we don’t have all the facts. We see a friend who doesn’t say hello and assume they are angry with us. We see someone driving fast and assume they are a reckless person. We rarely consider that our friend might be lost in thought, or that the driver might be in an emergency.\n\nAssumptions create misunderstanding and drama. The solution is simple: have the courage to ask questions. Seek clarity instead of creating confusion. Give people the benefit of the doubt. Clear communication can dissolve a problem before it even begins.\n\n### 4. Always Do Your Best\n\nThis agreement is not about perfection. It’s about understanding that your “best” will change from moment to moment. Your best when you are healthy is different from your best when you are sick. Your best when you are rested is different from your best when you are tired. \n\nIt simply means that in any given situation, you give it all you have—no more, no less. As the story goes, Michelangelo carved the hidden, unseen parts of his sculptures with the same care as the parts everyone would see. When asked why, he replied, \"Because God can see it.\" He was doing his best not for others, but for himself. \n\nWhen you always do your best, you have no room for self-judgment or regret. You act with integrity, and in that, you find peace."""
    },


        {
        "title": "Your Own Best Counselor is You",
        "date": "2024-12-02",
        "tags": ["Mindset", "Wisdom", "Duality", "Self-Awareness"],
        "excerpt": "When others have a problem, we give advice. When we have a problem, we seek it. What if we could create an inner observer to counsel ourselves with the same clarity and compassion?",
        "content": """Have you ever noticed a strange thing we do? When a friend comes to us with a problem, the path forward often seems perfectly clear. We see the situation from a distance, and with calm objectivity, we offer advice.\n\nBut when the very same problem happens to us, that clarity vanishes. We're lost in a fog of emotion and uncertainty. Suddenly, we are the ones seeking advice from others.\n\nWhy is there this disconnect? When it’s someone else’s issue, we are observers. When it's our own, we are participants. But what if you could be both at the same time? What if you could create a duality within yourself?\n\n### Creating Your Inner Observer\n\nThe practice is simple, but not easy. It involves creating a "second self"—a detached, wise observer who can watch you navigate life without getting swept up in the immediate emotion.\n\nI learned something like this during Vipassana meditation. You learn to observe your own thoughts and feelings as they arise and pass away, without becoming them. You realize you are not your anger, you are the one watching the anger. You are not your sadness, you are the one aware of the sadness.\n\nThis observer is your inner counselor. It's the part of you that has all the wisdom you so freely give to others.\n\n### How to Be Your Own Advisor\n\nWhen you feel overwhelmed or lost, instead of immediately seeking external advice, try this:\n\n1.  **Step Back:** Create a little space between you and the problem. Take a few breaths.\n\n2.  **Frame it as a Friend’s Problem:** Ask yourself, "If my closest friend came to me with this exact situation, what would I tell them?"\n\nInstantly, the wise, compassionate, and objective part of you will surface. The advice that emerges is often calm, clear, and exactly what you need to hear. You can be sad when you know the truth; you don't need to be sad at the beginning based on a story you tell yourself. You can be angry when you confirm the facts; you don’t need to be angry based on an assumption.\n\nWhen you counsel yourself, you give yourself the gift of your own wisdom, free from the distortions of panic and ego.\n\nThis practice also changes how you interact with others. Once you recognize that everyone has their own inner counselor, the impulse to immediately give advice fades. You realize it is often better to simply listen and trust that they, too, can find their own way. You can't live their life for them, just as they can't live yours. We must each walk our own path, but with this duality, we never have to walk it alone."""
    },

        {
        "title": "Three Roads to Peace",
        "date": "2025-04-18",
        "tags": ["Philosophy", "Wisdom", "Mindfulness", "Happiness"],
        "excerpt": "Ancient wisdom suggests that peace isn't a one-size-fits-all state. Instead, there are three distinct paths one can walk: the way of knowledge, the way of action, and the way of devotion.",
        "content": """We all seek peace, but what is it? Is it the absence of noise, the resolution of conflict, or something deeper? \n\nAncient traditions teach that peace isn't a single destination reached by one road. Instead, there are at least three distinct paths suited for different types of people: the path of the thinker, the path of the doer, and the path of the lover. They are known as the way of knowledge (Gyan), the way of action (Karma), and the way of devotion (Bhakti).\n\nYou don’t have to choose just one, but understanding them can reveal where you naturally find your moments of stillness.\n\n### 1. The Path of Knowledge (Gyan): Peace Through Understanding\n\n> *For the one who asks, \"Why?\"*\n\nThis is the path of the seeker, the philosopher, the meditator. It is the peace that comes not from changing the world, but from understanding it exactly as it is. It operates on a simple but radical premise: suffering comes from our interpretation of reality, not reality itself.\n\nOn this path, you learn to observe your thoughts and sensations without judgment. You see that an event is just an event. The story you attach to it—the one that labels it “good” or “bad”—is a separate creation of the mind. My experience with Vipassana meditation touched on this directly: pain is a sensation, but the story of “I can’t bear this pain” is suffering.\n\nThis way leads to peace by developing an inner witness, an observer self that watches the mind’s chatter without getting swept away by it. By understanding the nature of your own mind, you find a stillness that no external event can truly shake.\n\n### 2. The Path of Action (Karma): Peace Through Detachment\n\n> *For the one who asks, \"How?\"*\n\nThis is the path for the doer, the builder, the person engaged with the world. It doesn’t ask you to renounce action, but to renounce your attachment to the *fruits* of that action. It's a difficult but powerful concept: do your work for the sake of the work itself, not for praise, reward, or a specific outcome.\n\nWhen you apply for a hundred jobs, the work is in the application, not in the agony of waiting for a reply. When you write, the work is in the writing, not in the reviews. The Path of Action teaches that your duty is to your effort alone. The results are never fully in your control.\n\nBy letting go of the outcome, you are liberated. You are no longer on an emotional rollercoaster dictated by success and failure. You find a deep, quiet peace in simply doing what is in front of you with full attention and integrity. The action itself becomes a form of meditation.\n\n### 3. The Path of Devotion (Bhakti): Peace Through Surrender\n\n> *For the one who feels deeply.*\n\nThis is the path of the heart. Where the first path uses the mind and the second uses the hands, this path uses emotion and love. It is about dissolving the ego by surrendering to something larger than yourself.\n\nFor many, this is God. For others, it might be a teacher, the beauty of nature, a community, or a profound ideal like Truth or Love. The object of devotion is less important than the act of surrendering itself.\n\nThis path brings peace by replacing the ego's constant struggle for control with a feeling of profound trust and connection. Instead of trying to figure everything out or control every outcome, you learn to let go. You offer up your actions, your worries, and your hopes, and in that act of giving, you find a sense of belonging and an unshakable peace that comes from the heart."""
    },




        {
        "title": "How to Find Your Purpose",
        "date": "2023-04-02",
        "tags": ["Purpose", "Wisdom", "Self-Discovery", "Ikigai", "Work"],
        "excerpt": "The search for 'passion' can be abstract. This framework offers a practical compass with four key questions: What do you love, what are you good at, what does the world need, and what can you be paid for?",
        "content": """The advice to \"find your passion\" often feels vague and overwhelming, as if you're searching for a hidden treasure with no map. But what if you had a compass instead? A framework with four cardinal directions that, when aligned, point toward a fulfilling and sustainable purpose.\n\nThis compass is built on four simple but profound questions.\n\n### 1. What do you love?\n\n> *What activities bring you genuine joy?*\n\nThis is the starting point, the fuel for your journey. What are the things you would do even if no one was paying you or watching? What activities make you lose track of time? This is where your intrinsic motivation lies.\n\nIt could be solving complex puzzles, organizing systems, creating art, or connecting with people. Don't judge it or worry if it's practical yet. Just identify the activities that feel less like work and more like play. This is your 'passion' in its purest form.\n\n### 2. What are you good at?\n\n> *Where do your skills and talents lie?*\n\nPassion alone isn't enough; it thrives when paired with competence. This question isn't just about what you love, but what you excel at. This can be a natural talent or a skill you’ve honed through years of practice.\n\nWhere do you find that your effort produces unusually good results? Maybe you're a natural teacher, a gifted coder, or you have a knack for simplifying complex ideas. While you can love something without being a master, the feeling of competence is a crucial ingredient for long-term fulfillment. This is your 'profession' in the making.\n\n### 3. What does the world need?\n\n> *What problem do you want to solve?*\n\nThis is the question that transforms passion into purpose. An activity done only for yourself can feel isolating, but an activity that serves others creates a profound sense of meaning. \n\nThe 'world' doesn't have to be the entire globe. It can be your community, your family, a specific industry, or a small group of people who need what you have to offer. What problems do you see that you feel compelled to help solve? This could be anything from building sustainable water systems to creating software that makes someone's day a little easier. This is your 'mission'.\n\n### 4. What can you be paid for?\n\n> *How can your value sustain you?*\n\nThis is the practical question that grounds your purpose in reality. It asks: Is there a market for the intersection of what you love, what you're good at, and what the world needs?\n\nThis isn't about selling out; it's about creating a sustainable loop where you can continue doing meaningful work without burning out. The world signals what it values through exchange. Finding what people are willing to pay for—whether through a salary, a business, or freelance work—is what turns your passion and mission into a viable 'vocation'.\n\nThe goal is not to find an answer to just one of these questions, but to find the place where all four overlap. That intersection is where passion, profession, mission, and vocation meet. It's more than a job; it's a reason for being."""
    }, 

        {
        "title": "The Seasons of Life",
        "date": "2023-08-20",
        "tags": ["Wisdom", "Jim Rohn", "Personal Growth", "Resilience"],
        "excerpt": "Life moves in cycles. As Jim Rohn taught, understanding how to act in each season is the secret to a well-lived life. The rules are simple, but not easy.",
        "content": """The great philosopher Jim Rohn taught a simple but profound metaphor: life unfolds in seasons, just like a year. There are winters of hardship, springs of opportunity, summers of effort, and autumns of harvest.\n\nThe seasons don't ask for permission; they simply arrive. You cannot change them. You can, however, change what you do. Learning to act with wisdom in each season is the key to navigating everything life throws at you.\n\nHere are four essential rules for the seasons of your life.\n\n### 1. You Reap What You Sow (The Law of Spring)\n\nSpring is the season of opportunity. The ground is ready, but it won’t plant itself. This is the fundamental law of reality: you cannot have a harvest in the fall if you do not plant a seed in the spring.\n\nDon’t be fooled by the ease of the season. Spring demands action. This is the time to start the business, learn the skill, make the call. If you spend this window waiting for perfect conditions, you guarantee an empty basket later. The work must be done.\n\n### 2. Think of Summer All Winter (The Law of Winter)\n\nWinter is the season of hardship. The ground is frozen, progress seems impossible, and the warmth of success can feel like a distant memory. The winds of loss, disappointment, and delay will blow. They always do.\n\nThis is the time to build your character. While the world outside is cold, you can get stronger inside. This is when you read the books, study, reflect, and build the internal strength needed for the next opportunity. You must hold the vision of a future harvest in your mind to keep you warm through the cold. Remember the promise of summer while you endure the winter.\n\n### 3. Think of Winter All Summer (The Law of Summer)\n\nSummer is the season of abundance and growth. The sun is shining, your efforts are paying off, and everything feels easy. This is the most dangerous season, because it's when we become complacent. It's easy to forget that another winter is always coming.\n\nThe wise person uses the sunny days to prepare. While enjoying your success, you must be disciplined enough to mend the roof, save a portion of your profits, and strengthen the foundations of your life. Don't be so intoxicated by the sunshine that you forget to prepare for the inevitable storms.\n\n### 4. Understand That Sometimes, It Hails\n\nThere is a final, humbling truth. You can do everything right—you can plant in the spring, protect your crop all summer, and be fully prepared for winter—and then, just before the harvest, a hailstorm can come and wipe it all out.\n\nThis isn't fair. It isn't right. But, as Jim Rohn said, it’s just that kind of planet. Some things are out of your control. The hailstorms are part of the deal. The measure of your character is not whether you can prevent the storm—you can't—but whether you have the resilience to get up and plant again when the next spring arrives."""
    },

    {
        "title": "How Tall Should a Tree Grow?",
        "date": "2025-08-16",
        "tags": ["Potential", "Jim Rohn", "Personal Growth", "Wisdom"],
        "excerpt": "A simple lesson from nature, inspired by Jim Rohn, on why we should never place artificial limits on our own potential.",
        "content": """Have you ever asked a simple but profound question: How tall should a tree grow? The answer is beautifully simple. A tree should grow as tall as it possibly can.\n\nThis observation from nature holds one of the most powerful lessons about human potential. A tree never grows halfway and decides that’s far enough. It never stops reaching for more sun and driving its roots deeper for more nourishment. The tree isn't greedy. It is simply fulfilling its nature to become all it can be.\n\nWhy should we treat ourselves any differently? \n\nWe often put limits on our own growth. We ask questions that build fences around our possibilities. But if we apply the wisdom of the tree, the answers become clear.\n\n- How many books should you read? As many as you can.\n- How much money should you make? As much as you can.\n- How much should you share? As much as you possibly can.\n- How hard should you try? As hard as you possibly can.\n\nThe point isn't to hoard money or knowledge. The goal is to see what you are capable of becoming. The act of reaching for your full potential transforms you. When you develop the capacity to earn more, you gain the capacity to give more. When you learn more, you have more wisdom to offer the world.\n\nLife is not about being "good enough." It is about being all you can be. And just like a tree, we must accept that challenges will come. The storms will rage and the seasons will turn. Some years, the conditions will be perfect. In other years, hail might strike just before the harvest. That is the nature of this planet.\n\nBut the tree's job remains the same. And so does yours.\n\nSo the next time you wonder how far you should go, look at a tree. Stop building your own ceilings. Start reaching."""
    },

    {
        "title": "On Data-Driven Science in Hydrology",
        "date": "2024-08-16",
        "tags": ["Data Science", "Hydrology", "Machine Learning"],
        "excerpt": "A reflection on the shift from process-based models to data-driven approaches in hydrology...",
        "content": """In a traditional approach, we lean on centuries of scientific thought, painstakingly piecing together processes—like runoff, infiltration, groundwater flow, and sediment transport—into large, complex models. Now, with an explosion of data and machine learning methods, there’s a push to let the data itself guide our understanding. Instead of relying solely on a stack of equations, we stitch together relationships through patterns found in the data. It feels like a new kind of science, one where we feed in enough observations and let flexible algorithms fill in the gaps.

But as exciting as this is, I also worry about what happens when we step into completely uncharted territory. Data-driven models might predict well within the range of what we’ve seen before enough, but how do they hold up in never-before-seen conditions? That’s where these methods might struggle. We might need more than just neural networks connecting the dots, we might need models that learn underlying mechanisms, not just correlations. The dream is some hybrid approach that understands processes at a very fundamental level while still leveraging the power of massive datasets?

At the same time, there’s never been a better moment to dig deeper into data. With decades’ worth of satellite imagery, sensor networks, and massive archives of measurements, we’re definitely equipped to get creative. We need to look beyond just predicting tomorrow’s river flow and start asking bigger questions about our water resources—how they change, what they carry, and where they’re heading. If we can figure out how to generalize these methods, to make them robust against uncertainty and new scenarios, the payoff could be huge. It might take quantum computing or entirely new algorithms to get there, but the vision is clear: blending data-driven insights with fundamental processes could open up horizons in hydrology we’re only just starting to imagine."""
    },


    {
        "title": "Four Simple Laws for Navigating Life",
        "date": "2025-08-15",
        "tags": ["Mindset", "Wisdom", "Productivity", "Philosophy"],
        "excerpt": "Life doesn't come with an instruction manual, but a few fundamental principles can help make sense of it all. These mental models can help you navigate the world with more wisdom and less stress.",
        "content": """Life doesn't come with an instruction manual, but there are a few fundamental principles that can help make sense of it all. Think of these not as strict rules, but as mental models—simple ways to understand why things happen the way they do.\n\nHere are four simple “laws” that can help you navigate the world with a little more wisdom and a lot less stress.\n\n#### 1. Murphy's Law: Plan for What Can Go Wrong\n\n> *\"Anything that can go wrong will go wrong.\"*\n\nSound pessimistic? It’s actually a superpower for practical planning. Murphy’s Law reminds us that life is unpredictable. Flights get delayed, traffic appears out of nowhere, and files get corrupted right before a deadline.\n\nInstead of hoping for the best, this law encourages you to plan for it. By anticipating potential problems and giving yourself a buffer, you aren’t being negative—you’re being prepared.\n\n#### 2. The Pareto Principle: A New Look at 80/20\n\n> *80% of results come from 20% of efforts.*\n\nMost people know this rule as a way to identify what's most important. But consider it from another angle, especially when you're deep in a project.\n\nHave you ever felt like you've put in 80% of the work, but only have 20% of the final result to show for it? It can be incredibly discouraging. This is where the principle offers relief. That first 80% of your effort is for building the foundation—the research, the structure, the messy first draft. It’s essential, but not always visible.\n\nThe final 20% of your effort is where you refine, connect the dots, and polish everything. This is the phase that delivers 80% of the finished project's value. So don't worry if your progress feels slow. You will get the remaining 80% of your results when you do that final 20% of the work. It’s a reminder that progress isn’t always linear, and the biggest leaps often happen right at the end.\n\n#### 3. Hick's Law: The Paradox of Choice\n\n> *The more choices you have, the longer it takes to make a decision.*\n\nHave you ever stared at a restaurant menu the size of a novel, only to feel completely paralyzed? That’s Hick's Law. When faced with too many options, our brains can freeze, leading to indecision and anxiety.\n\nThe solution is to become a gatekeeper for your own attention. Limit your options where you can. Automate small decisions so you have more mental energy for the big ones. Simplicity is a strategy.\n\n#### 4. The Benefit of the Doubt: Don't Rush to Be Upset\n\n> *When in doubt, assume the most generous reason.*\n\nWhen a coworker sends a blunt, one-line email, it’s easy to assume they’re being dismissive. When a friend cancels plans, it’s tempting to feel slighted. Our minds are quick to create a negative story.\n\nBut why rush into feeling bad?\n\nThere will be plenty of time to be sad or angry *if* you confirm the worst is true. You can be upset when you know the facts; you don't need to be upset based on a guess. This isn't about being naive. It's about being strategic with your emotional energy. By offering the benefit of the doubt, you reserve your feelings for reality, not for the fiction you create in your own head."""
    },
    
    {
        "title": "Reflections on a 10-Day Vipassana Course",
        "date": "2024-08-15",
        "tags": ["Meditation", "Mindfulness", "Vipassana"],
        "excerpt": "My experience with a 10-day silent meditation retreat and the lessons it taught me about the mind.",
        "content": """I first became curious about Vipassana after reading The Power of Now by Eckhart Tolle. Although I don’t remember every detail of that book, it really made me think about the mind’s constant chatter and how we might quiet it. Nepal is a place proud to be the birthplace of Gautam Buddha, and while I can’t say I understand his teachings, I knew he was closely associated with Vipassana. I learned that S.N. Goenka, an Indian teacher, helped bring this ancient meditation technique to modern students worldwide. People spoke of it as an authentic teaching of Buddha passed down through generations, preserved in places like Myanmar, and then reintroduced to India and beyond.

When I signed up for a 10-day Vipassana course, I had no idea what to expect. The rules were strict: no phones, no books, and no talking. The schedule felt intense—waking up at 4:30 AM to meditate all day until about 9:30 PM. Surprisingly, I didn’t find it too difficult to adapt. Sure, I overslept few times and got a gentle reminder from the course helpers, but overall, I managed. The first three days focused entirely on Anapana, the observation of the breath. It seemed simple at first—just watch your breath, right? But quickly I realized how many random thoughts flood into my mind at every moment. The whole exercise became a lesson in noticing the non-stop mental chatter and learning not to engage with it. Over time, I realized that the mind, left unchecked, can run wild, and that learning to switch it off (or at least down) was possible, if challenging. One of the way I learned from Eckhart Tolle was to ask your mind: whats your next thought? This actually helped my brain slow down.

After three days, we moved on to Vipassana itself: scanning the body and observing sensations without judgment. The idea wasn’t just to see what’s there, but to understand that everything arises and passes away. Pain, itchiness, discomfort—these felt so immediate and personal at first, yet with practice, I saw them come and go. Nothing belonged to me permanently. This had echoes of Tolle’s ideas about staying in the present moment. When you pay close attention, the mind’s constant story-making halts. You become aware that your brain is just another organ, not the sum of who you are. By the end of the retreat, I understood that what I considered “me” was really just a shifting collection of sensations and thoughts that never stayed the same for long.

I’ve heard people say that if you meditate deeply for long stretches, you’ll need less sleep because your mind isn’t working overtime all day. I have heard people not sleeping and still ok for 2 months. While that might be an extreme claim, I did notice a certain mental lightness, as if I had more control over my thoughts instead of them controlling me. The course didn’t answer all my big questions about life, the brain, or the universe, but it gave me a new perspective on how I relate to my own mind and body. I realized that if I could step back from my thoughts and sensations, I could also step back from my cravings, fears, and distractions. Suddenly, it felt possible to break bad habits or addictions just by not feeding them with constant mental energy.

It’s been a few years since I took that course, and I don’t practice Vipassana regularly now. But the lessons stuck with me. I no longer feel so powerless against my wandering mind. I know that I can watch it, notice it drifting, and gently bring it back. I learned something interesting: I could create a sort of duality within myself, almost like splitting into two versions of me. One part would experience my thoughts, sensations, and reactions, while the other would watch this unfolding as if from the outside. It was like observing myself as I might observe another person, seeing my habits, judgments, and struggles with a kinder, more detached perspective. This small mental trick turned out to be a powerful way to approach difficult emotions and challenges.

I recommend Vipassana to anyone curious about quieting the noise inside their head, even if it’s just once. My experience in Nepal showed me that true stillness might be closer than we think—waiting behind each breath."""
    },
    {
        "title": "Favorite Books & Wisdom",
        "date": "2024-08-14",
        "tags": ["Books", "Wisdom", "Reading"],
        "excerpt": "A curated list of books and wisdom that I find valuable and live by.",
        "content": """### Wisdom I Live By
*   Ignorance is not bliss.
*   Plans should be measured in decades, execution should be measured in weeks.
*   Working with great people is the greatest experience of life.
*   If you study the subject you like for 1 hour/day, you will become a national expert within 5 years.
*   10x goals are easier than 2x goals.
*   You learn more by teaching something than by studying it as a student.
*   If you can imagine it, you can already do it.
*   Hate the crime, but love the criminal.
*   The concepts of good and bad are not inherent in reality; they are human constructs shaped by perspectives, experiences, and cultural contexts.
*   Most people are helpful if you simply ask.

### Foundational Books
*   **The Power of Now** by Eckhart Tolle
*   **How to Win Friends and Influence People** by Dale Carnegie
*   **Atomic Habits** by James Clear
*   **Seasons of Life** by Jim Rohn
*   **The Five Major Pieces to the Life Puzzle** by Jim Rohn
*   **The Richest Man in Babylon** by George Samuel Clason"""
    },
    {
        "title": "On the Law of Averages",
        "date": "2024-08-13",
        "tags": ["Productivity", "Mindset", "Persistence"],
        "excerpt": "How persistence and increasing your attempts can lead to success, even when you feel you're not an outlier.",
        "content": """Sometimes, we really want to stand out—become extraordinary or an outlier in whatever we do. But then reality hits, and we can’t even achieve what’s considered “average.” It can feel pretty brutal when you don’t get admitted to the school you wanted, or you apply to a hundred jobs and nobody ever replies. You email tons of professors and still end up with no response. It’s frustrating, I know.

This is where the Law of Averages can help us out. The idea is simple: if you keep trying enough times, something will eventually work out. It’s like if you send out a hundred job applications, there’s a higher chance that at least one will give you a shot. If you submit your paper to multiple journals, one of them might accept it. No matter how “bad” you think you are, if you keep pushing, your odds improve. You basically increase the probability of success by sheer persistence.

This reminds me of that saying: if you want something bad enough, the world somehow aligns to help you get it. It’s also kind of what the Bhagavad Gita teaches us: don’t worry so much about the end result, just focus on doing your work. Keep trying, keep pushing, and don’t overthink it. Eventually, something’s got to give. It’s a pretty good reminder!!"""
    },
    {
        "title": "On Time Management",
        "date": "2024-08-12",
        "tags": ["Productivity", "Goals", "Time Management"],
        "excerpt": "A simple approach to time management that starts with a clear goal and prioritizing tasks by their consequences.",
        "content": """Time management really starts with having a clear goal. If you don’t even know what you want, there’s no point in managing your time—just wing it, right? But once you’ve got a goal, that’s when it makes sense to organize yourself.

A good approach is to list out everything you need to do. Just write it all down, no matter how big or small. Then, rank these tasks based on the consequences of doing or not doing them. For example, if not doing something will lead to terrible outcomes, that’s clearly high priority. If doing something leads to really good results, that’s also super important. But if a task doesn’t move the needle in any direction, it’s probably not that important. Once you’ve sorted them, start doing the tasks from the top of the list. Even if you miss out on lower-ranked tasks, who cares? The big stuff will still get done.

Jim Rohn suggests planning your day before it begins, your week before it starts, and so on. Setting goals for the month before it begins, or just sitting down in the morning to decide what needs doing. You can do this on a Google Doc or any note-taking app. Keep a running list, mark things off as you finish them, and that’s it. It’s not about forcing yourself into a rigid schedule; it’s just about knowing what matters and making sure you do that first. That’s probably good enough to stay on track."""
    },
]

# =============================================================================
# SCRIPT LOGIC (No need to edit below this line unless you want to customize)
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

def generate_page(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Updated {filepath}")



def generate_collection_files(data, folder, collection_name, permalink_prefix, type_key=None, default_type=None):
    for item in data:
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', item['date'])
        if not date_match:
            date_match = re.search(r'(\d{4})', item['date'])
            if not date_match:
                print(f"  ✗ Warning: Could not parse date for '{item['title']}'. Skipping file generation.")
                continue
            item_date = f"{date_match.group(1)}-01-01"
        else:
            item_date = date_match.group(1)

        slug = slugify(item['title'])[:50]
        filename = f"{item_date}-{slug}.md"
        filepath = os.path.join(folder, filename)
        
        content = "---\n"
        content += f"title: \"{item['title'].replace(':', '')}\"\n"
        
        if collection_name == "posts":
            content += f"date: {item['date']}\n"
            content += f"permalink: /posts/{item['date'][:4]}/{slug}/\n"
            content += "tags:\n"
            for tag in item.get('tags', []):
                content += f"  - {tag}\n"
            if item.get('excerpt'):
                content += f"excerpt: \"{item['excerpt'].replace('\"', '&quot;')}\"\n"
        else:
            content += f"collection: {collection_name}\n"
            content += f"permalink: /{permalink_prefix}/{item_date}-{slug}\n"
            item_type = item.get(type_key, default_type)
            if item_type:
                content += f"type: \"{item_type}\"\n"
            
            # --- NEW LOGIC ADDED HERE ---
            # Add a status flag for publications to distinguish them in the template
            if collection_name == "publications":
                if "Under Review" in item.get('citation', ''):
                    content += "publication_status: 'Under Review'\n"
                else:
                    content += "publication_status: 'Published'\n"
            # --- END OF NEW LOGIC ---

            for key, value in item.items():
                if key not in ['title', 'type', 'content', 'tags', 'excerpt'] and value:
                    clean_value = str(value).replace("'", "’").replace('"', '&quot;')
                    content += f"{key}: '{clean_value}'\n"
        
        content += "---\n\n"
        
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
    for folder in ["_publications", "_talks", "_teaching", "_posts"]:
        clear_folder(folder)

    print("\n--- Generating Core Pages & Navigation ---")
    
        # Find this variable and update it
    # nav_content = """main:\n  - title: "Publications"\n    url: /publications/\n  - title: "Talks"\n    url: /talks/\n  - title: "Teaching"\n    url: /teaching/\n  - title: "Media"\n    url: /media/\n  - title: "Blog"\n    url: /blog/\n  - title: "Resources"\n    url: /resources/\n  - title: "CV"\n    url: /cv/"""
    # generate_page("_data/navigation.yml", nav_content)
    nav_content = """main:\n  - title: "Publications"\n    url: /publications/\n  - title: "Talks"\n    url: /talks/\n  - title: "Teaching"\n    url: /teaching/\n  - title: "Group"\n    url: /group/\n  - title: "Media"\n    url: /media/\n  - title: "Blog"\n    url: /blog/\n  - title: "Resources"\n    url: /resources/\n  - title: "CV"\n    url: /cv/"""
    generate_page("_data/navigation.yml", nav_content)





# Find the block that generates the main page and REPLACE it with this one.

    # --- Generate Main Page (About + News) ---
    print("\n--- Generating Main Page ---")
    
    # Start with the "About Me" content
    main_page_content = f"""---
permalink: /
title: "About Me"
author_profile: true
---
Welcome! I am a PhD Candidate at Arizona State University, working at the intersection of data-driven hydrology, earth observation, and machine learning.

My work is deeply rooted in my experiences growing up in Nepal. During my undergraduate studies in Civil Engineering, I came face-to-face with the real-world impact of natural hazards. I saw how floods, droughts, and landslides could disrupt lives and entire communities. These events are not just statistics. They are powerful reminders that our ability to anticipate and adapt to our changing planet is still very limited.

This realization became my driving force. I knew I didn't want to just build tools that watch our planet struggle. I wanted to engineer solutions that could actively help us build a more sustainable and resilient future. My research is my attempt to do just that. I focus on bridging the gap between complex scientific knowledge and the actionable, accessible tools that people need. To do this, I've built my work on three core pillars.

### 1. Hydrometeorology and Hazard Science
<!-- Suggested Image: A compelling photograph of a landslide path on a green mountainside or an aerial view of a flooded river valley. -->
My first focus is on understanding the fundamental science. This means digging into hydrometeorology. It's the intricate dance between water and the atmosphere that creates everything from life-giving rain to destructive floods. I am especially focused on what we call compound and cascading disasters. This is where a chain of simple events can combine to create a catastrophe. A single heavy rainfall might not be a disaster on its own. But when it triggers a landslide that blocks a river, which then causes a flood upstream, the impact multiplies.

We need to understand these complex interactions to get ahead of them. A lot of my work involves building frameworks to model and predict these events. We can build better models to understand these [cascading hazards](https://doi.org/10.1080/19475705.2022.2162443) on mountain terrain. We can also map out which areas are most susceptible to [rainfall-triggered landslides](https://doi.org/10.1016/j.scitotenv.2023.162242) and identify the critical infrastructure at risk. This allows for smarter spatial decision-making before a disaster happens. This kind of proactive work is essential. It is part of a larger vision for a more [Integrated, Coordinated, Open, and Networked (ICON) approach to science](https://doi.org/10.1029/2021EA002114) that can truly serve society.

### 2. Harnessing Earth Observation
<!-- Suggested Image: A striking satellite image, perhaps a false-color composite showing vegetation health, water bodies, or the extent of a wildfire. -->
We live in an era of an unbelievable amount of data. Space agencies like NASA and ECMWF hold hundreds of petabytes of information about our planet. This is a treasure trove. Satellites are constantly watching our forests, rivers, and cities. But raw data is not the same as knowledge. What are we actually doing with all of it?

My second pillar is about transforming this flood of data into actionable intelligence. The goal is to develop scalable and generalizable methods that make sense of it all. We can use this information to create immense value. For example, we can use it to map things like [groundwater potential in data-scarce regions](https://doi.org/10.1016/j.jhydrol.2023.130417). We can also monitor and understand the long-term impacts of [land use and land cover change](https://doi.org/10.1016/j.rsase.2022.100895) on agriculture and natural resources. This is not just about making maps. It is about providing decision-makers with a clear, current picture of our changing world so they can act on it.

### 3. Bridging the Gap with Artificial Intelligence
<!-- Suggested Image: An abstract graphic illustrating a neural network, a data flowchart, or a dashboard displaying predictive analytics. -->
If Earth Observation data is the fuel, then Artificial Intelligence is the engine that puts it to work. AI and Machine Learning are the critical bridge. They connect the vast datasets we have to the complex, real-world problems we need to solve. These tools can see patterns and relationships that are simply too complex for traditional models to capture.

My work involves engineering a suite of intelligent software and models. These tools are designed for scalability and transferability. A major part of my PhD is dedicated to this. I am building next-generation streamflow forecasting systems, particularly for arid regions like Arizona. Many current systems are based on older, empirical knowledge. They struggle to adapt when the environment changes, like when a city expands and creates more concrete surfaces. My approach is different. I am developing methods that can assimilate satellite information directly into hydrological models, aiming for more robust and accurate forecasts. This includes exploring techniques like [Bayesian model averaging](https://geokshitij.github.io/publication/2025-12-30-improving-hydrological-forecasting-with-bayesian-model-averaging-over-multiple-loss-functions) to improve reliability. The key is to create systems that learn and adapt, because our world is constantly changing.

To summarize, I want to contribute to a future where scientific innovation directly supports sustainable development and community resilience. I believe in creating tools that are not just scientifically novel, but genuinely useful. I am committed to this journey of turning data into decisions and research into real-world impact.

I am currently seeking a faculty position where I can start my own research group and continue advancing this vision. If you wish to connect or collaborate, please reach out at kdahal3@asu.edu.

"""

    # --- Now, build the News timeline ---
    news_items = []

    # Process talks with smarter grammar
    for talk in talks_data:
        date_obj = datetime.strptime(talk['date'], '%Y-%m-%d')
        
        # Smarter description based on talk type
        if talk['type'].lower() == 'moderator':
            description = f"🎤 Moderated the session, **'{talk['title']}'**, at {talk['venue']}."
        else:
            description = f"🎤 Presented a {talk['type'].lower()}, **'{talk['title']}'**, at {talk['venue']}."
        
        news_items.append({"date": date_obj, "description": description})
        
    # Process other custom news from the new list
    for item in other_news_data:
        date_obj = datetime.strptime(item['date'], '%Y-%m-%d')
        # The description is already formatted, so we just add it
        news_items.append({"date": date_obj, "description": item['description']})

    # Sort all news items in reverse chronological order
    news_items.sort(key=lambda x: x['date'], reverse=True)

    # Append the formatted news timeline to the main page content
    main_page_content += "\n\n---\n\n## News & Updates\n"
    current_year = None
    for item in news_items:
        year = item['date'].year
        if year != current_year:
            main_page_content += f"\n### {year}\n"
            current_year = year
        
        date_str = item['date'].strftime('%B %d')
        main_page_content += f"* **{date_str}**: {item['description']}\n"

    # Generate the final combined page
    generate_page("_pages/about.md", main_page_content)


    
    # --- Generate Teaching Page ---
    teaching_page_content = """---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

I plan to teach a variety of courses at the intersection of water resources, data science, and environmental engineering. My goal is to equip the next generation of engineers and scientists with the skills to tackle complex environmental challenges.

### Future Courses
- **AI in Water Resources:** Exploring the application of machine learning and artificial intelligence for hydrological modeling, forecasting, and water management.
- **Remote Sensing for Earth Observation:** Focusing on the use of satellite data and geospatial analysis for monitoring environmental systems.
- **Engineering Hydrology:** Covering the fundamentals of the hydrologic cycle, water balance, and hydrological processes.
- **Fluid Mechanics:** Introducing the principles of fluid statics and dynamics with applications in civil and environmental engineering.

---

### Past Experience (Teaching Assistant)
{% include base_path %}
{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}
"""
    generate_page("_pages/teaching.md", teaching_page_content)
    



    # --- Generate Group Page ---
    group_page_content = """---
layout: archive
title: "Research Group"
permalink: /group/
author_profile: true
---
We are in the process of building a research group.

Our group will focus on addressing critical challenges at the intersection of water, climate, and society. We will leverage cutting-edge tools in **hydrological forecasting, natural hazards assessment, sustainable development, and artificial intelligence** to create actionable solutions for a resilient future.

Stay tuned for updates.
"""
    generate_page("_pages/group.md", group_page_content)






    # --- Generate Media Page ---
    media_content = """---
layout: archive
title: "Media"
permalink: /media/
author_profile: true
---
This page features news articles, op-eds, and media mentions related to my work.
"""
    # Group the data by type
    grouped_media = {}
    for item in media_data:
        grouped_media.setdefault(item.get("type", "General"), []).append(item)
    
    # Build the content line by line to avoid indentation issues
    content_lines = []
    
    if "Op-Ed" in grouped_media:
        content_lines.append("\n## News Columns (Op-Ed)")
        for item in grouped_media["Op-Ed"]:
            line = f"* {item['authors']} ({item['year']}). **[{item['title']}]({item['url']})**. *{item['venue']}*."
            content_lines.append(line)
            
    if "Media Citation" in grouped_media:
        content_lines.append("\n## Professional Media Citations")
        for item in grouped_media["Media Citation"]:
            line = f"* **[{item['title']}]({item['url']})**. *{item['venue']}*, {item['year']}."
            content_lines.append(line)
    
    # Join the lines and generate the page
    media_content += "\n" + "\n".join(content_lines)
    generate_page("_pages/media.md", media_content)

    
    
    resources_content = """---\nlayout: archive\ntitle: "Resources"\npermalink: /resources/\nauthor_profile: true\n---\n"""
    resources_content += "\n## Courses Developed\n"
    for item in courses_data:
        resources_content += f"* {item['authors']} ({item['year']}). **[{item['title']}]({item['url']})**. *{item['venue']}*.\n"
    resources_content += "\n## Technical Reports\n"
    for item in reports_data:
        resources_content += f"* {item['authors']} ({item['year']}). **[{item['title']}]({item['url']})**. *{item['venue']}*.\n"
    generate_page("_pages/resources.md", resources_content)
    
    publications_page_content = """---\nlayout: archive\ntitle: "Publications"\npermalink: /publications/\nauthor_profile: true\n---\n{% if site.author.googlescholar %}\n  <div class="wordwrap">You can also find my articles on my <a href="{{site.author.googlescholar}}">Google Scholar profile</a>.</div>\n{% endif %}\n{% include base_path %}\n{% for post in site.publications reversed %}\n  {% include archive-single.html %}\n{% endfor %}"""
    generate_page("_pages/publications.html", publications_page_content)
    
    blog_page_content = """---
layout: archive
title: "Blog"
permalink: /blog/
author_profile: true
---
{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts reversed %}
{% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
{% if year != written_year %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture written_year %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single.html %}
{% endfor %}"""
    generate_page("_pages/blog.md", blog_page_content)
    
    print("\n--- Generating Collection Files ---")
    generate_collection_files(publications_data, "_publications", "publications", "publication")
    generate_collection_files(talks_data, "_talks", "talks", "talks", type_key="type", default_type="Talk")
    generate_collection_files(teaching_data, "_teaching", "teaching", "teaching")
    generate_collection_files(blog_data, "_posts", "posts", "posts")
    
    print("\nGeneration complete!")