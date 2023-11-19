---
layout: page
title: Ideas
permalink: /ideas/
---
### Ideas

{% assign drafts = site.categories['Drafts'] %}
{% if drafts != nil %}
{% assign sorted = drafts | sort: 'date' | reverse  %}
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
{% endif %}

<h1> Home </h1>
<p>
Hello there! Welcome to my personal corner of the internet.
</p>
<p>
This site is dedicated to your growth and learning in the exciting field of software development. Get ready to master new skills and tackle real-world challenges.
Let's learn, grow and create amazing things together.
</p>

{% assign sorted_articles = site.categories['Articles'] | sort: 'date' | reverse  %}

<section class="latest">
  <h2> Latest article </h2>
  {% for post in sorted_articles limit:1 %}
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

{% assign articles_count = sorted_articles | size %}
<section class="recent">
    <h2> Recent articles </h2>
  <table>
    {% for post in sorted_articles offset:1 limit:10 %}
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

{% assign sorted_notes = site.categories['Notes'] | sort: 'date' | reverse  %}
<section class="recent">
    <h2> Recent notes </h2>
  <table>
    {% for post in sorted_notes limit:10 %}
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
