<p>
Hello there! Welcome to my personal corner of the internet.
</p>
<p>
This site is dedicated to your growth and learning in the exciting field of software development. Get ready to master new skills and tackle real-world challenges.
Let's learn, grow and create amazing things together.
</p>

{% assign sorted = site.articles | sort: 'date' | reverse  %}

<section class="latest">
  <h2> Latest article </h2>
  {% for article in sorted limit:1 %}
    <article>
      <h3><a href="{{ article.url }}">{{ article.title }}</a></h3>
      {{ article.excerpt }}
      <p><small><strong>{{ article.date | date: "%B %e, %Y" }}</strong></small></p>
    </article>
  {% endfor %}
</section>

{% assign articles_count = site.articles | size %}
{% if articles_count > 1 %}
  <section class="recent">
      <h2> Recent articles </h2>
    <table>
      {% for article in sorted offset:1 limit:5 %}
        <tr>
          <td class="date">
            <p><small><strong>{{ article.date | date: "%B %e, %Y" }}</strong></small></p>
          </td>
          <td class="title">
            <a href="{{ article.url }}">{{ article.title }}</a>
          </td>
        </tr>
      {% endfor %}
    </table>
  </section>
{% endif %}
