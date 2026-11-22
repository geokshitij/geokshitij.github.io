---
layout: archive
title: "Blog"
permalink: /blog/
author_profile: true
---
{% include base_path %}
{% for post in site.posts %}
<article class="blog-post">
<h2 class="blog-post-title"><a href="{{ base_path }}{{ post.url }}">{{ post.title }}</a></h2>
<p class="blog-post-date">{{ post.date | date: '%B %-d, %Y' }}</p>
{{ post.content }}
</article>
{% unless forloop.last %}<hr class="blog-post-sep">{% endunless %}
{% endfor %}