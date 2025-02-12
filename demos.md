---
layout: page
title: Demos
permalink: /demos/
---
{% assign sorted = site.demos | sort: 'date' | reverse  %}
{% for demo in sorted %}
  <article>
    <h2>
      <a href="{{ site.baseurl }}{{ demo.url }}">{{ demo.title }}</a>
    </h2>
    <p class="date">{{ demo.date | date: "%B %Y" }}</p>
    {{ demo.excerpt }}
  </article>
{% endfor %}

