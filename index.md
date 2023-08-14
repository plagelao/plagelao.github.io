<p>
Hello there! Welcome to my personal corner of the internet.
</p>
<p>
This site is dedicated to your growth and learning in the exciting field of software development. Get ready to master new skills and tackle real-world challenges.
Let's learn, grow and create amazing things together.
</p>

{% assign sorted = site.posts | sort: 'date' | reverse  %}

<section class="latest">
  <h2> Latest article </h2>
  {% for post in sorted limit:1 %}
    <article>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <div class="tags">
      {% for tag in post.tags %}
      <a class="tag" href="/tags/{{ tag }}">{{ tag }}</a>
      {% endfor %}
      </div>
      <p class="date"><small><strong>{{ post.date | date: "%B %Y" }}</strong></small></p>
      {{ post.excerpt }}
    </article>
  {% endfor %}
</section>

{% assign articles_count = site.posts | size %}
{% if articles_count > 1 %}
  <section class="recent">
      <h2> Recent articles </h2>
    <table>
      {% for post in sorted offset:1 limit:5 %}
        <tr>
          <td class="date">
            <p><small><strong>{{ post.date | date: "%B %Y" }}</strong></small></p>
          </td>
          <td class="title">
            <a href="{{ post.url }}">{{ post.title }}</a>
          </td>
        </tr>
      {% endfor %}
    </table>
  </section>
{% endif %}
