---
layout: archive
title: "Blog"
permalink: /blog/
author_profile: true
---
{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts %}
{% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
{% if year != written_year %}
{% unless forloop.first %}</div>{% endunless %}
<h2 id="{{ year | slugify }}" class="tile-year">{{ year }}</h2>
<div class="tile-grid">
{% capture written_year %}{{ year }}{% endcapture %}
{% endif %}
<a class="tile" href="{{ base_path }}{{ post.url }}"><span class="tile-label">{{ post.date | date: '%B %-d, %Y' }}</span><span class="tile-title">{{ post.title }}</span></a>
{% endfor %}
</div>