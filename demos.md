---
layout: page
title: Demos
permalink: /demos/
---
{% assign sorted = site.demos | sort: 'date' | reverse  %}
{% for demo in sorted %}
  <article>
    <h3>
      <a href="{{ site.baseurl }}{{ demo.url }}">{{ demo.title }}</a>
    </h3>
    <p class="date"><small><strong>{{ post.date | date: "%B %Y" }}</strong></small></p>
    {{ demo.excerpt }}
  </article>
{% endfor %}

