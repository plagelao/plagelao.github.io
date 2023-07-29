---
title: Customizing the site
excerpt_separator: <!--more-->
layout: post
---
Customizing your personal site is a journey of self-expression and creativity. It lets you craft a digital space that facilitates a deeper connection with your readers. It's a never ending task, a task where the destination isn't the goal, the learning is.

With that in mind, let's get on with it!
<!--more-->

{% raw %}
<aside>
  <p>Most of the things in this article assume that your know how to set up a site with GitHub Pages. Please refer to the <a href="https://plagelao.github.io/articles/2023-07-26-setting-this-site-up.html">previous article</a> if you need a guide on how to do it.</p>
  <p>GitHub Pages uses Jekyll under the hood, and Jekyll uses Liquid as its templating language. This article isn't going to explain them, but you can find more information about them here:</p>
  <ul>
    <li><a href="https://jekyllrb.com/docs/">Jekyll documentation</a></li>
    <li><a href="https://shopify.github.io/liquid/">Liquid documentation</a></li>
  </ul>
</aside>

### Navigation: Jekyll data

When thinking about how to structure content, it's always important to have a clear idea of what content you want to share and how do you want visitors to find it. This site follows a standard navigation patter with a home page, a section with articles and an about page.

The home page is the place where you want visitors to have a clear idea about what the site offers, the articles section is just the blog and the about page is where visitors can find some more information about the site owner.

With those three sections in mind, the directory structure ends up being something like this:

```
root_directory
    |
    + - _layouts
    |      |
    |      + - default.html
    + - index.md
    + - _articles
    |      |
    |      + - 2023-07-26-setting-this-site-up.md
    |      + - ...
    + - about.md
```

You can define the navigation in the `_layouts/default.html` layout as following:

```
<ul class="nav">
  <li><a href="/">Home</a></li>
  <li><a href="/articles/">Articles</a></li>
  <li><a href="/about/">About</a></li>
</ul>
```

This works:

![Navigation without highlighting](/assets/navigation-without-highlighting.png)

but it doesn't show the visitor in what section they're. To fix that, you need a bit of liquid, the template language that Jekyll uses, to add an `active` class to the navigation item when the visited page is in that section:

```
<ul class="nav">
  {% if page.url == '/' %}
    <li class="active"><a href="/">Home</a></li>
  {% else %}
    <li><a href="/">Home</a></li>
  {% endif %}
  {% if page.url == '/articles/' or page.url contains '/articles/' %}
    <li class="active"><a href="/articles/">Articles</a></li>
  {% else %}
    <li><a href="/articles/">Articles</a></li>
  {% endif %}
  {% if page.url == '/about/' %}
    <li class="active"><a href="/about">About</a></li>
  {% else %}
    <li><a href="/about">About</a></li>
  {% endif %}
</ul>
```

This now highlights the section the visitor is in:

![Navigation](/assets/navigation.png)

but it isn't maintainable. If you have to add another section, you have to repeat the `if` clause and it's error prone because it's likely that at some point you will end up copying and pasting.

You can refactor this code by use data. Jekyll has a feature where you can define data in the `_data` directory in multiple file formats. For this example, YAML si the chosen format. The `_data/navigation.yml` file can look like:

```
- link: /
  label: Home
- link: /articles/
  label: Articles
- link: /about/
  label: About
```

With this, you can refactor the navigation bar:

```
<ul class="nav">
  {% for item in site.data.navigation %}
    {% case item.label %}
    {% when "Home" %}
      {% if page.url == item.link %}
        <li class="active"><a href="{{ item.link }}">{{ item.label }}</a></li>
      {% else %}
        <li><a href="{{ item.link }}">{{ item.label }}</a></li>
      {% endif %}
    {% else %}
      {% if page.url contains item.link %}
        <li class="active"><a href="{{ item.link }}">{{ item.label }}</a></li>
      {% else %}
        <li><a href="{{ item.link }}">{{ item.label }}</a></li>
      {% endif %}
    {% endcase %}
  {% endfor %}
</ul>
```

There is still a special case for the home section. That's because the `contains` clause is always going to be `true` for any page URL in your site when checked against `/`. Now you can add many navigation items just by changing the `_data/navigation.yml` file.

### Articles instead of posts: Jekyll collections

One of the sections is now `Articles`, but the blog doesn't have anything like that. It only has orphan post pages. In order to change this, you can use the collections feature in Jekyll. You just need to define the collection that you want in the `_config.yml` file:

```
collections:
  articles:
    relative_directory: _articles
    output: true
```

In this case, the `articles` collection is in the directory `_articles`. Jekyll won't generate files from the contents of that directory by default, so you need to set `output` to `true` explicitly.

You can add an `article.md` file in the `_articles` directory. Jekyll is going to use that file to generate the landing page for the new collection, in this case in `/articles/`.

After that, the only thing left is to move post from `_posts/2023-07-26-my-new-post` to `_articles/2023-07-26-my-new-post`.

![Articles without reverse](/assets/articles-without-reverse.png)

### Personalised home page: Liquid limit and offset

Now that you have your sections populated, the last part is to customize the landing page of your site, the `Home` section. It's the one defined by the `index.md` file.

For this example, since the idea is to explain how limit and offset work in Jekyll, the `index.md` file is going to show the latest published post at the top of the page, just after the navigation. The idea is to highlight the latest post to any visitor to the site.

Another requirement is to also show up to five more posts from latest to oldest, excluding the latest one, because the latest one has already it's own section in the page.

The `index.md` section to highlight the latest post looks like:

```
<section class="latest">
  <h2> Latest article </h2>
  {% for article in site.articles limit:1 %}
    <article>
      <h3><a href="{{ article.url }}">{{ article.title }}</a></h3>
      {{ article.excerpt }}
      <p><small><strong>{{ article.date | date: "%B %e, %Y" }}</strong></small></p>
    </article>
  {% endfor %}
</section>
```

The interesting bit is `for article in site.articles limit:1`. This is telling Jekyll that, when fetching the site articles, the page is only interested in the first result.

Next, this is how to show up to 5 posts excluding the first one:

```
<section class="recent">
    <h2> Recent articles </h2>
  <table>
    {% for article in site.articles offset:1 limit:5 %}
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
```

The interesting bit is `for article in site.articles offset:1 limit:5`. This is telling Jekyll that, when fetching the site articles, it should exclude the first one (`offset:1`) and fetch up to 5 after that (`limit:5`).

The page now shows almost the correct data:

![Home page without reverse](/assets/home-without-reverse.png)

You might have notice this before with the articles page. The order of the posts is incorrect.

### Personalised sorting: Filters

By default, Jekyll orders the posts from oldest to newest, exactly the opposite of the original idea in the article. To fix that, you need to use Jekyll filters and variables. Filters, well, filter data. Variables store intermediate data. In the `index.md`, the change looks like:

```
{% assign sorted = site.articles | sort: 'date' | reverse  %}
```

That line of code is fetching the site articles, then it's sorting them by date and, finally, it's reversing the order. It assigns the end result to the variable `sorted`.

After that, you need to change both `for` loops:

```
  {% for article in site.articles limit:1 %}
  {% for article in site.articles offset:1 limit:5 %}
```

to use the new variable `sorted`:

```
  {% for article in sorted limit:1 %}
  {% for article in sorted offset:1 limit:5 %}
```

And now the order is correct:

![Home page](/assets/home.png)

That's all!

{% endraw %}
