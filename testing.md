---
layout: page
title: Ideas
permalink: /ideas/
---
### Ideas

{% for draft in site.drafts %}
  <a href="{{ site.baseurl }}{{ draft.url }}">{{ draft.title }}</a>
{% endfor %}
