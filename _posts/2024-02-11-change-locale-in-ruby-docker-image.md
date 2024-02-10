---
title: How to change the language encoding in a Ruby docker image
excerpt_separator: <!--more-->
layout: note
categories: [Notes, Software development, Ruby on Rails, Tutorials]
tags: [Ruby on Rails, Docker]
tools:
  - label: Ruby on Rails
    link: https://rubyonrails.org/
  - label: Docker
    link: https://www.docker.com/
---
The encoding section in the [docker ruby image documentation](https://hub.docker.com/_/ruby) explains how to change the locale and encoding for the image. By default, it uses `C` as locale so, to change the encoding, you can add this to your dockerfile:

```sh
ENV LANG C.UTF-8
```
