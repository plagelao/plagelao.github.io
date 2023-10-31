---
layout: page
title: Ideas
permalink: /ideas/
---
### Ideas

{% assign drafts = site.posts | where: 'draft', true %}
{% for draft in drafts %}
  <a href="{{ site.baseurl }}{{ draft.url }}">{{ draft.title }}</a>
{% endfor %}
