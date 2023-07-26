---
title: Setting this site up
excerpt_separator: <!--more-->
---
When you have things to say, you need a blog. Now more than ever.

<!--more-->
### Why GitHub Pages?

Many developers already have a GitHub account, and GitHub Pages has been around for ages. Many sites use it and it seems like a good and simple option.

Whenever you start with something new, you need to start by following the documentation. In this case, the documentation was the GitHub guide to create the site. Turns out that the documentation is clear and creating the basic site was straightforward. It took a couple of minutes.

![Homepage](/assets/homepage.png)

The next step was understanding how pushing a new post works. That was the first blocker.

### How to push a new post

Following the pattern of the `index.md` that GitHub Pages explains in their documentation, the next step was to create a new file `my-new-post.md`. After pushing it, the post wasn't visible in the home page, but it existed in `/my-new-post`. Although it was a step in the right direction, the goal was to display the list of posts in the home page so visitors could find them.

### How to list the posts: The wrong way

Clearly, it was a mistake to start assuming things without reading the documentation. This time, it was the Jekyll documentation. It says that depending on how you name your files, Jekyll can infer the publication date and create a URL for that item that contains the date. For example, in the previous step, the name of the post file was `my-new-post.md` and that created the URL `/my-new-post`. What the documentation said is that if you name your file `2023-07-26-my-new-post`, it generates the following URL `/2023/07/26/my-new-post`. It's always useful to have the date of publication of an article, mostly because technical articles are likely to become obsolete in a year or two.

After pushing those changes… nothing. No posts in the home page. At least the post URL now had the date in it though.

### How to list the posts: Wrong again

Checking the documentation again, it says how to list the posts in a page. You just need to add a bit of code to the page:

{% raw %}
```
{% for post in site.posts %}
  <article>
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  </article>
{% endfor %}
```
{% endraw %}

This looks good, it makes sense. After pushing again… Nothing showed up :(

### How to list the posts: The correct way

Back to the Jekyll documentation. It turns out that the `site.posts` code infers the posts from the files in the `_posts` directory. This works by default in Jekyll but, in GitHub Pages, it also works because of the theme it uses. The theme is important for later, but for now, just note that the them it uses is [Primer](https://github.com/pages-themes/primer).

After moving the post file to the correct directory, and after another push, this time the post showed up in the homepage.

![Homepage with posts](/assets/homepage-with-posts.png)

### Customizing the theme

[Primer](https://github.com/pages-themes/primer/tree/master#project-philosophy) is a theme that aims for simplicity. It looks good, but your personal blog needs a bit of customization. Anything you need to know on how to customize it's explained in the [Primer GitHub ReadMe](https://github.com/pages-themes/primer/tree/master#customizing) page.

### Reflecting on "the process"

From this experience, it looks like GitHub Pages and Jekyll follow the [principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment). Most of the blocks in the article are easy to fix and the solution makes sense.

The problem I had is that starting with a new technology/framework/language/whatever is never straightforward, but [it looks like it after the fact](https://en.wikipedia.org/wiki/Hindsight_bias#:~:text=Hindsight%20bias%2C%20also%20known%20as,more%20predictable%20than%20they%20were.).

This problem takes many forms in software development. From seniors that can't communicate effectively with juniors, to engineers that can't explain technical things to non-technical stakeholders, and even you beating up yourself for the latest bug in production when it was so obvious that the code was wrong. It shows a lack of empathy that's, unfortunately, common in software development. There isn't any obvious solution to this problem, but the more aware we're about it, the better.
