---
layout: page
title: Articles
permalink: /articles/
---
{% assign sorted = site.articles | sort: 'date' | reverse  %}
{% for article in sorted %}
  <article>
    <h3><a href="{{ site.baseurl }}{{ article.url }}">{{ article.title }}</a></h3>
    {{ article.excerpt }}
    <p><small><strong>{{ article.date | date: "%B %e, %Y" }}</strong></small></p>
  </article>
{% endfor %}
