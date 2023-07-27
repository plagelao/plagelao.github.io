---
layout: page
title: Articles
permalink: /articles/
---
{% for post in site.posts %}
  <article>
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    {{ post.excerpt }}
    <p><small><strong>{{ post.date | date: "%B %e, %Y" }}</strong></small></p>
  </article>
{% endfor %}
