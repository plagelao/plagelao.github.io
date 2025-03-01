### Hello there!

Welcome to my personal corner on the internet.

I have this site mostly to spend some time every day understanding things by writing them down. I've found that the act of writing helps me with clarifying my thoughts, my ideas, and my experiences. It's a way for me to find the why behind the what.

The update cadence is one month, because I'm a busy person, like everyone. I do a bit everyday, since I'm a big believer in taking incremental steps, and it usually takes me about one month to get an article ready.

I get a lot of value out of this. I hope you can find something useful here too.

Thanks for reading!

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
      <p class="date">{{ post.date | date: "%B %Y" }}</p>
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
          <p>{{ post.date | date: "%B %Y" }}</p>
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
          <p>{{ post.date | date: "%B %Y" }}</p>
        </td>
        <td class="title">
          <a href="{{ post.url }}">{{ post.title }}</a>
        </td>
      </tr>
    {% endfor %}
  </table>
</section>
