---
layout: page
title: Articles
permalink: /articles/
---
{% assign sorted = site.categories['Articles'] | sort: 'date' | reverse  %}
{% for post in sorted %}
  <article>
    <h3>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </h3>
    <div class="tags">
      {% for tag in post.tags %}
        <a class="tag" href="/tags/{{ tag }}">{{ tag }}</a>
      {% endfor %}
    </div>
    <p class="date"><small><strong>{{ post.date | date: "%B %Y" }}</strong></small></p>
    {{ post.excerpt }}
  </article>
{% endfor %}
