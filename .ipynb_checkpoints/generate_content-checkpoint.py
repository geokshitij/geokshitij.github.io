# /geokshitij.github.io/generate_content.py
import os
import re

# =============================================================================
# DATA SECTION
# This is the single source of truth for your website's content,
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
    {"authors": "Cho, H., Ashraf, F., Dahal, K.", "year": "2024", "title": "Flood Inundation Mapping Using Machine Learning for Sustainable vs. Resilient Design", "venue": "CIROH", "url": "https://edx.hydrolearn.org/courses/course-v1:NMSU+CE483+Fall2024/about"}
]
reports_data = [
    {"authors": "UNDRR", "year": "2022", "title": "Scoping Study On Compound, Cascading And Systemic Risks In The Asia Pacific", "venue": "United Nations Office for Disaster Risk Reduction (UNDRR)", "url": "https://www.undrr.org/quick/71248"}
]

blog_data = [
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
        # Use a regex to extract the date from the 'date' field
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', item['date'])
        if not date_match:
            # Fallback for dates that might not be in YYYY-MM-DD format
            date_match = re.search(r'(\d{4})', item['date'])
            if not date_match:
                print(f"  ✗ Warning: Could not parse date for '{item['title']}'. Skipping file generation.")
                continue
            item_date = f"{date_match.group(1)}-01-01" # Default to Jan 1st if only year is found
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
    nav_content = """main:\n  - title: "Publications"\n    url: /publications/\n  - title: "Talks"\n    url: /talks/\n  - title: "Teaching"\n    url: /teaching/\n  - title: "Media"\n    url: /media/\n  - title: "Blog"\n    url: /blog/\n  - title: "Resources"\n    url: /resources/\n  - title: "CV"\n    url: /cv/"""
    generate_page("_data/navigation.yml", nav_content)

    about_content = f"""---
permalink: /
title: "About Me"
author_profile: true
---
Welcome! I am a PhD Candidate at Arizona State University, working at the intersection of data-driven hydrology, earth observation, and machine learning.

My journey into geoscience began during my undergraduate studies in Civil Engineering in Nepal, where I came face-to-face with the profound impact of natural hazards on communities. The world is experiencing unprecedented environmental stress—from devastating floods and droughts to catastrophic landslides. These events are not just statistics; they are reminders that our ability to anticipate and adapt is still limited. This realization ignited my passion: I don't want to just build tools that watch our planet struggle; I want to engineer solutions that help us build a more sustainable and resilient future.

My work is driven by the need to bridge the gap between scientific knowledge and actionable, accessible solutions. To tackle this complex challenge, my research is built on three interconnected pillars:

### 1. Hydrometeorology and Hazard Science
<!-- Suggested Image: A compelling photograph of a landslide path on a green mountainside or an aerial view of a flooded river valley. -->
At its core, my work is grounded in understanding the physical processes that drive environmental hazards. I focus on hydrometeorology—the intricate dance between water and the atmosphere that leads to events like rainfall-triggered landslides, floods, and droughts. I am particularly interested in the growing threat of compound and cascading disasters, where a chain of seemingly simple events combines to create a catastrophe. By modeling these complex interactions, we can move from reactive responses to proactive preparedness. A key part of this work involves creating frameworks that help identify and protect [critical infrastructure before disaster strikes](https://www.tandfonline.com/doi/full/10.1080/23789689.2023.2181552).

### 2. Harnessing Earth Observation
<!-- Suggested Image: A striking satellite image, perhaps a false-color composite showing vegetation health, water bodies, or the extent of a wildfire. -->
We live in an era of data abundance. Space agencies like NASA and ECMWF collectively archive hundreds of petabytes of Earth Observation (EO) data—an unbelievable treasure trove of information about our planet's health. However, this raw data is not the same as knowledge. My research focuses on transforming this deluge of satellite imagery and sensor readings into actionable intelligence. The goal is to develop scalable and generalizable methods that can assimilate this information to monitor land use change, assess water resources like [groundwater potential](https://doi.org/10.1016/j.jhydrol.2023.130417), and track hazard evolution in near real-time. By creating value from this data, we can provide decision-makers with a clearer, more current picture of our changing world.

### 3. Bridging the Gap with Artificial Intelligence
<!-- Suggested Image: An abstract graphic illustrating a neural network, a data flowchart, or a dashboard displaying predictive analytics. -->
Artificial Intelligence (AI) and Machine Learning (ML) are the critical bridge connecting vast EO datasets to complex real-world problems. These tools allow us to identify patterns and relationships that are too complex for traditional models to capture. My work involves engineering a suite of intelligent software and models designed for scalability and transferability. A central focus of my PhD is developing next-generation streamflow forecasting systems for arid regions like Arizona by assimilating satellite data. Instead of relying on fragmented, empirical models, I aim to build integrated systems that learn from diverse data sources to anticipate future conditions with greater accuracy.

Ultimately, my goal is to contribute to a future where scientific innovation directly supports sustainable development and community resilience. I believe in creating tools that are not only powerful but also accessible, enabling communities everywhere to better understand and navigate the environmental challenges they face. My work has been fortunate to be featured by national and international news media, and I am committed to continuing this journey of turning data into decisions and research into real-world impact.
"""    
    generate_page("_pages/about.md", about_content)


    cv_content = """---\nlayout: archive\ntitle: "CV"\npermalink: /cv/\nauthor_profile: true\n---\n{% include base_path %}\n<a href="/files/CV_Kshitij_Dahal.pdf" class="btn btn--primary" target="_blank">Download Full CV (PDF)</a>\n\n### Education\n"""
    for item in personal_info['education']:
        cv_content += f"* {item['degree']}, *{item['university']}*, {item['period']}\n"
    cv_content += "\n### Academic Employment\n"
    for item in personal_info['employment']:
        cv_content += f"* **{item['role']}**\n  * {item['institution']}\n  * {item['period']}\n"
    cv_content += "\n### Honors and Awards\n"
    for item in personal_info['awards']:
        cv_content += f"* {item}\n"
    cv_content += """\n### Publications\n<ul>{% for post in site.publications reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>\n\n### Talks & Presentations\n<ul>{% for post in site.talks reversed %}{% include archive-single-talk-cv.html %}{% endfor %}</ul>\n\n### Teaching\n<ul>{% for post in site.teaching reversed %}{% include archive-single-cv.html %}{% endfor %}</ul>"""
    cv_content += """\n\n### Leadership and Services\n* **Executive Committee (Elected)**, *Young Earth System Scientists (YESS) Community*, July 2025 – June 2026\n* **Community Science Fellow**, *American Geophysical Union*, May 2024 – Present\n* **Regional Representative (South East Asia)**, *Young Earth System Scientists (YESS) Community*, Jan 2021 – Jan 2022\n* **Coordinator, Capacity Building**, *U-Inspire Alliance*, May 2019 – Present"""
    cv_content += """\n\n### Academic Services\n#### Editorial Advisory Board\n* *Regional Environmental Change, Springer Nature*, 2024 – Present\n\n#### Reviewer\n* *Earth’s Future*, 2024 – Present\n* *International Journal of Disaster Risk Reduction, Elsevier*, 2023 – Present\n* *Humanities and Social Sciences Communications, Nature*, 2023 – Present\n* *Regional Environmental Change, Springer Nature*, 2021 – Present\n* *Anthropocene Science, Springer Nature*, 2021 – Present\n* *PLOS Sustainability and Transformation*, 2021 – Present\n* *The Geographic Base, Nepal Journals Online*, 2020 – Present\n\n#### Memberships\n* Member, American Society of Civil Engineers, USA, 2022 – Present\n* Member, American Geophysical Union, USA, 2020 – Present\n* Registered A class Civil Engineer, Nepal Engineering Council, Nepal, 2020 – Present"""
    generate_page("_pages/cv.md", cv_content)




    
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