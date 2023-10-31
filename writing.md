---
layout: page
title: Writing
permalink: /writing/
---
{% assign categories = 'Writing,Software development' | split: ',' %}

{% for category in categories %}
# {{ category }}
{% assign articles = site.categories[category] %}

## Tutorials
{% for post in articles %}
{% if post.categories[-1] == 'Tutorials' %}
<a href="{{ post.url }}"> {{ post.title }} </a>
{% endif %}
{% endfor %}

## How to guides
{% for post in articles %}
{% if post.categories[-1] == 'How to guides' %}
<a href="{{ post.url }}"> {{ post.title }} </a>
{% endif %}
{% endfor %}

## Explanations
{% for post in articles %}
{% if post.categories[-1] == 'Explanations' %}
<a href="{{ post.url }}"> {{ post.title }} </a>
{% endif %}
{% endfor %}

## Reference
{% for post in articles %}
{% if post.categories[-1] == 'Reference' %}
<a href="{{ post.url }}"> {{ post.title }} </a>
{% endif %}
{% endfor %}

{% endfor %}
