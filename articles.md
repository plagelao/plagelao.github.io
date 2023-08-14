---
layout: page
title: Articles
permalink: /articles/
---
{% assign sorted = site.posts | sort: 'date' | reverse  %}
{% for post in sorted %}
  <article>
    <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>
    <div class="tags">
    {% for tag in post.tags %}
    <a class="tag" href="/tags/{{ tag }}">{{ tag }}</a>
    {% endfor %}
    </div>
    <p class="date"><small><strong>{{ post.date | date: "%B %Y" }}</strong></small></p>
    {{ post.excerpt }}
  </article>
{% endfor %}


<!--
{% for tag in site.tags %}
  <h4>On {{ tag[0] }}</h4>
  <ul>
    {% for post in tag[1] limit:5 %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        ({{ post.date |  date: "%B %Y" }})<br>
      </li>
    {% endfor %}
  </ul>
{% endfor %}

<h3> Tools </h3>
{% assign all_tools = [] %}
{% for post in site.posts %}
  {% assign all_tools = all_tools | concat: post.tools %}
{% endfor %}
{% assign all_tools = all_tools | uniq %}

{% for tool in all_tools %}
  <h4>{{tool.label}}<a href="{{ tool.link }}"> [link]</a>
  <h5>Posts</h5>
  {% for post in site.posts %}
    {% for aux_tool in post.tools %}
      {% if tool.label == aux_tool.label %}
<a href="{{ post.url }}">{{ post.title }}</a>
      {% endif %}
    {% endfor %}
  {% endfor %}
{% endfor %}
-->
