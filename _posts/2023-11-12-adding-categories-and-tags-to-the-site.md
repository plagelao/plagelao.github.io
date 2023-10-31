---
title: Adding categories and tags to your site
excerpt_separator: <!--more-->
layout: post
categories: [Articles, Software development, Jekyll, Tutorials]
tags: [clarity, Jekyll]
tools:
  - label: Jekyll
    link: https://jekyllrb.com/docs/
  - label: Github Pages
    link: https://pages.github.com/
---
As discussed in the [previous post]({% post_url 2023-11-03-organising-content %}), organising content is not a trivial task, and making a decision on how to tackle it is just the beginning. Once you've settled on an approach, it's time to roll up your sleeves and put that solution into action.

This article serves as a guide on creating a category and tagging system in Jekyll. While it does come with a few caveats, this tutorial should provide you with the know-how needed to implement this system effectively.

With that in mind, let's get on with it!
<!--more-->
### How to do it in Jekyll
After all the hard work thinking about your content, the implementation is straightforward.

<aside>
  <p>Most of the things in this article assume that your know how to set up a site with GitHub Pages. Please refer to the <a href="https://plagelao.github.io/articles/2023-07-26-setting-this-site-up.html">previous article</a> if you need a guide on how to do it.</p>
  <p>GitHub Pages uses Jekyll under the hood, and Jekyll uses Liquid as its templating language. This article isn't going to explain them, but you can find more information about them here:</p>
  <ul>
    <li><a href="https://jekyllrb.com/docs/">Jekyll documentation</a></li>
    <li><a href="https://shopify.github.io/liquid/">Liquid documentation</a></li>
  </ul>
</aside>

Jekyll uses the [front matter format](https://jekyllrb.com/docs/front-matter/) to add variables to your content. Out of the box, Jekyll has a way to define categories and tags with this format. The only thing you need to do is add them to your files. This post, for example, startes with the following section:

```yaml
---
title: Adding tags to your site
excerpt_separator: <!--more-->
categories: [Articles, Jekyll, Tutorials]
tags: [clarity, Jekyll]
---
```

The keyword `categories` expects a list of elements. Jekyll creates a tree of categories from the list. For this example, this post categories translate into `Articles > Writing > Tutorials`.

The keyword `tags` also expects a list of elements. Jekyll will create a list of tags, no nesting in this case. In this example, the list of tags will be `clarity, Jekyll, diátaxis`.

Having this content is all good, but you want your visitors to be able to explore your site based on your tags. For that, you need to add a couple of things.

### Adding a list of links based on the article tags

### Generating the page for each tag
Jekyll is a static site generator, so you need to create each of the tag pages. Manually creating them does not scale, and it is error prone. One solution is to create a simple rake task that loops through all your posts, gets the tags and creates a page for the new ones.

You can find the latest version of my solution [here](), in the site's repository. To end this post, I'll explain the version of the file at the moment this post was published:

```ruby
Dir["_posts/**/*.md"].each do |file|
  tag_line = File.readlines(file).detect do |line|
    line =~ /tags:/
  end
  YAML.load(tag_line)['tags'].each do |tag|
    if Dir["tags/**/*.md"].none?{|tag_file| tag_file.split('/').last.split('.').first == tag.downcase}
      content = ['---', 'layout: tag', "title: 'Tag: #{tag}'", "tag: #{tag}", '---'].join("\n")
      File.write("tags/#{tag.downcase}.md", content)
    end
  end
end
```

First, the task finds and loops over all the markdown files in the `_posts` directory:

```ruby
Dir["_posts/**/*.md"].each do |file|
```

Then, for each markdown file, it finds the line that defines the tags and assigns the line to the `tag_line` variable:

```ruby
tag_line = File.readlines(file).detect do |line|
  line =~ /tags:/
end
```

The next step is to load the line as YAML. This parses the line and converts it into a ruby `Hash`. After that, the code finds the value stored for the key `tags` and loops over each it to get each tag:

```ruby
YAML.load(tag_line)['tags'].each do |tag|
```

Once it has the tag, it checks if there is already a page created for that tag. If a file doesn't exist, it uses the tag to create a new file:

```ruby
if Dir["tags/**/*.md"].none?{|tag_file| tag_file.split('/').last.split('.').first == tag.downcase}
```

The final section creates a new markdown file in the `tags` directory with the name of the tag in lowercase. The file's content is only the front matter part that defines the title and the layout. It will use the `tag` layout.

```ruby
content = ['---', 'layout: tag', "title: 'Tag: #{tag}'", "tag: #{tag}", '---'].join("\n")
File.write("tags/#{tag.downcase}.md", content)
```

Assuming that no tag pages existed, this script creates an structure like this:

```
root_directory
    |
    + - tags
          |
          + - clarity.md
          |
          + - jekyll.md
```

That's all!
