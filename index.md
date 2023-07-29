{% for article in site.articles %}
  <article>
    <h3><a href="{{ site.baseurl }}{{ article.url }}">{{ article.title }}</a></h3>
    {{ article.excerpt }}
    <p><small><strong>{{ article.date | date: "%B %e, %Y" }}</strong></small></p>
  </article>
{% endfor %}
