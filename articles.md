---
layout: page
title: Articles
permalink: /articles/
---
{% assign sorted = site.categories['Articles'] | sort: 'date' | reverse  %}
{% for post in sorted %}
  <article>
    <h2>
      <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
    </h2>
    <div class="tags">
      {% for tag in post.tags %}
        <a class="tag" href="/tags/{{ tag }}">{{ tag }}</a>
      {% endfor %}
    </div>
    <p class="date">{{ post.date | date: "%B %Y" }}</p>
    {{ post.excerpt }}
  </article>
{% endfor %}
