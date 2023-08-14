---
title: Consistency in version control
excerpt_separator: <!--more-->
layout: post
categories: [Articles, Explanation]
tags: [clarity, Git, versioning]
tools:
  - label: conventional-changelog
    link: https://www.conventionalcommits.org/en/v1.0.0/
---

Effective communication is all about clarity. When your messages or ideas lack clarity, they can lead to confusion, misinterpretation, and a breakdown in communication.

That's all good but, what does "clarity" mean? Clarity refers to the qualities of being logical, consistent, and understandable.

One thing that sometimes is left out, from a clarity point of view, is version control. Version control is used everywhere, it's likely you are using it for all of your projects. It's less likely that you have a well defined way to achieve consistency in your version control commit messages. How many times have you seen a commit that says `fix` or `Testing` or `Enables the flux capacitor to serve the quantum space`. This lack of consistency makes reading the version control log a bit of a nightmare. Being such a central tool in the software development ecosystem, this area needs more awareness and love.

With that in mind, let's get on with it!

<!--more-->

### Clarity in commit messages

Version control systems like Git, Mercurial, or SVN, allow you to add a message every time you commit new changes. So far, only Git describes the what the commit message is for:

> the given log message describing the changes.

That's not extremely helpful, but at least it's something. Fortunately, many authors have described how to [write](https://initialcommit.com/blog/git-commit-messages-best-practices) [good](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/) [commit](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53) [messages](https://opensource.com/article/22/12/git-commit-message) already. From my point of view, the most important tip from those good practices is:

 > Describe **why** a change is being made, not what it's changing.

<aside>
  <p>This article uses Git for any examples on version control commands and practices. Given that Git is by far the most used version control system, this article assumes that you are comfortable using it.</p>
  <p>Below is a list of links if you need more information about Git:</p>
  <ul>
    <li><a href="https://git-scm.com/doc">Git documentation</a></li>
    <li><a href="https://gitimmersion.com/">Git Immersion. A guided tour that walks through the fundamentals of Git</a></li>
  </ul>
</aside>

Software developer is part doing, part self-reflection. Quick iteration on those is the essence of writing code. Write tests, write code, refactor. Do and reflect. Somehow, when writing commit messages, many times only the 'Doing' part is done, not the reflection. But commit messages are always the last part of the development cycle, since you can't commit anything before you write it. Thinking about why a change is needed helps with this reflection.

For example, your app has a bug and you are working hard on fixing it. You want to release the bug fix as fast as you can because **something is failing**! So you write the test to reproduce the bug, you write the code that makes the test pass and then, you commit your code with a message that reads "Fixes the bug." This isn't enough. Any person reading this isn't going to have a clue about what the bug was, why it happened and why it was important by looking at the message. They will have to look at the changes themselves to find the context. Not ideal.

A solution to this problem is **taking your time** to reflect on the changes. Think about your future self or another colleague and make their life easier. Instead of "Fixes the bug" something like, what about something like:

```
Books need to start at the first page by default

A previous commit introduced the concept of starting page explicitly
with a validation on book record creation.

It didn't have a default starting page value for existing books and
that made the system to behave randomly with old books.
```

This type of message serves two purposes. First, it allows other people to quickly understand the context for the changes. Secondly, it allows you to reflect on the system and the changes and clarify your thought process. This part is important to gain insights that, otherwise, you might assume as known.

### Maintain logical coherence by re-writing history

Progress isn't always that simple. Sometimes, no matter how hard you try, you can end up with things like this:

```
35b8322 (HEAD -> fix/book-start-page) Forgot to remove another TODO comment
804f3b9 Fix a brittle test
bce24fc Forgot to remove a TODO comment
e17df87 Books need to start at the first page by default
```

At this point, the thing to do is to stop and re-write history. Git `rebase` command allows to refactor the history of your branch so you can make sense of cases like this one. With the help of rebasing, you can get the previous timeline into something more clear. For this example, the original rebase screen might look like this:

```
pick e17df87 Books need to start at the first page by default
pick bce24fc Forgot to remove a TODO comment
pick 804f3b9 Fix a brittle test
pick 35b8322 Forgot to remove another TODO comment
```

You can choose to order the commits in any way you want. In the example it groups the `TODO` commits together and marks them as "squashed" into the original commit `e17df87`. It also marks the commit that fixes the brittle test as "reword needed":

```
pick e17df87 Books need to start at the first page by default
squash bce24fc Forgot to remove a TODO comment
squash 35b8322 Forgot to remove another TODO comment
reword 804f3b9 Fix a brittle test
```

After a bit, the end result can look similar to the following log:

```
5e6819b (HEAD -> fix/book-start-page) More robust tests so pipeline doesn't fail intermitently
e6819b8 Books need to start at the first page by default
```

Git rebase is another tool that allows you to reflect on your work and you should use it. The end goal is to bring clarity into your thought process, and reflecting on it can only bring you benefits.


### Consistency

<aside>
  <p>This section assumes that you have some knowledge about semantic versioning. Check the links below if you want to know more:</p>
  <ul>
    <li><a href="https://semver.org/">Semantic versioning</a></li>
    <li><a href="https://gitversion.net/docs/learn/intro-to-semver">Intro to semantic versioning</a></li>
  </ul>
</aside>

Teams can achieve consistency in many ways, the most effective one is usually automation. Coding standards, deployments, infrastructure, documentation, reporting, etc, most of the work software developers do can benefit from automation by keeping consistency between projects and the different parts in a particular projects. Automation is great in that regard because you can repeatedly get the same result over and over and, if something changes, the result changes accordingly but in a consistent way. For that reason, developers give automation a lot of love and thought.

How does this apply to version control? One way to seek consistency in version control is by enforcing a format for your commits. The benefits you get from this approach are many:

    - Easier to write or use automated tools. This article will demonstrate how to generate an automated change log.
    - Clarity about what the commit is for. Such as, is it a feature, a refactor, a bug fix, etc.
    - Simplify your versioning decisions. The commit itself defines if the change is a major, minor or patch.

You can achieve this in many ways. This article explores [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

> The Conventional Commits specification is a lightweight convention on top of commit messages. It provides an easy set of rules for creating an explicit commit history; which makes it easier to write automated tools on top of. This convention dovetails with [SemVer](http://semver.org/), by describing the features, fixes, and breaking changes made in commit messages.

The Conventional Commits documentation is clear and you should have a look at it. The most relevant part for this article is that commits have a defined structure, and that commits can be labeled to communicate the intent of the commit itself. The recommended labels are `fix`, `feat`, `BREAKING CHANGE`, `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, and `test`, but it leaves it open to the user to add more if needed. The first three labels, `fix`, `feat`, `BREAKING CHANGE`, are special in that they correlate to `PATCH`, `MINOR`, and `MAJOR` changes in your semantic versioning. A `MAJOR` change can also be defined by appending `!` to any of the other labels.

With this information, this article is going to move from a repository with unstructured commits to one with Conventional Commits. First, this is the original unstructured log:

```
4f7af22 (HEAD -> main, tag: v1.1.2, origin/main) Corrections and drafts
a10b8d7 (tag: v1.1.1) About section
2f8fccd (tag: v1.1.0) New article about Jekyll customization
b7dbbc6 (tag: v1.0.1) Sorting in reverse to get latest first
2c1cd18 Style aside tag
294ef0b Modifying home page
3900d95 Using collections
04ce7f4 Move navigation to data
b3c8bec (tag: v1.0.0) Add navigation
84e673e Add footer
e9dd393 Change name
2c16160 Initial commit
```

The thing that you might have noticed about this log is the random tags for the versions. The author is creating them without any consistency or methodology. This lack of clarity is a source of confusion.

After converting the log to Conventional Commits:

```
1b70f00 (HEAD -> feat/automatic-changelog, tag: v1.1.1) fix(content): Corrections and drafts
abb9024 (tag: v1.1.0) feat(about): About section
020a0ee (tag: v1.0.0) feat(content)!: New article about Jekyll customization
e17df87 (tag: v0.5.1) fix(landing): Sorting in reverse to get latest first
5e6819b (tag: v0.5.0) feat(articles): Style aside tag
9af77e3 (tag: v0.4.0) feat(landing): Modifying home page
720afc0 (tag: v0.3.0) feat(articles): Using collections
847d0e2 perf: Move navigation to data
c609ef8 (tag: v0.2.0) feat(style): Add navigation
5310460 (tag: v0.1.0) feat(style): Add footer
98ccaab (tag: v0.0.1) fix(brand): Change name
dcf2749 (tag: v0.0.0) feat: Initial commit
```

The tagging makes sense. It follows a defined pattern, and increases the clarity of the process. It also improves the first glance analysis about the reasons for the code to change. Also, now that the repository has a defined structure, an automation tool can use it to generate an automated change log. For this article, the [conventional-chagelog](https://github.com/conventional-changelog/conventional-changelog) package is used:

```
conventional-changelog -r 0 -p conventionalcommits
```

And it generates:

```
## [](https://github.com/plagelao/plagelao.github.io/compare/v1.1.1...v) (2023-08-06)

## [1.1.1](https://github.com/plagelao/plagelao.github.io/compare/v1.1.0...v1.1.1) (2023-08-06)


### Bug Fixes

* **content:** Corrections and drafts ([1b70f00](https://github.com/plagelao/plagelao.github.io/commit/1b70f0041fa50d348279b9e40481e5201378b765))

## [1.1.0](https://github.com/plagelao/plagelao.github.io/compare/v1.0.0...v1.1.0) (2023-08-06)


### Features

* **about:** About section ([abb9024](https://github.com/plagelao/plagelao.github.io/commit/abb902471c97bb03d6805dce2bb412517b1f61b8))

## [1.0.0](https://github.com/plagelao/plagelao.github.io/compare/v0.5.1...v1.0.0) (2023-08-06)


### ⚠ BREAKING CHANGES

* **content:** New article about Jekyll customization

### Features

* **content:** New article about Jekyll customization ([020a0ee](https://github.com/plagelao/plagelao.github.io/commit/020a0ee8f023095f25466513a8f9ff1dae79f30a))

## [0.5.1](https://github.com/plagelao/plagelao.github.io/compare/v0.5.0...v0.5.1) (2023-08-04)


### Bug Fixes

* **landing:** Sorting in reverse to get latest first ([e17df87](https://github.com/plagelao/plagelao.github.io/commit/e17df87cde4360a6e88899c139633a0019cb4035))

## [0.5.0](https://github.com/plagelao/plagelao.github.io/compare/v0.4.0...v0.5.0) (2023-08-04)


### Features

* **articles:** Style aside tag ([5e6819b](https://github.com/plagelao/plagelao.github.io/commit/5e6819b88fcd4d2482fd5ff102d959fd432473a5))

## [0.4.0](https://github.com/plagelao/plagelao.github.io/compare/v0.3.0...v0.4.0) (2023-08-04)


### Features

* **landing:** Modifying home page ([9af77e3](https://github.com/plagelao/plagelao.github.io/commit/9af77e3a638c3ea76637e43863e69ed7beb134f3))

## [0.3.0](https://github.com/plagelao/plagelao.github.io/compare/v0.2.0...v0.3.0) (2023-08-04)


### Features

* **articles:** Using collections ([720afc0](https://github.com/plagelao/plagelao.github.io/commit/720afc0b52e1b5544a183c58557f1c8e2709dc71))


### Performance Improvements

* Move navigation to data ([847d0e2](https://github.com/plagelao/plagelao.github.io/commit/847d0e21fe48103b33b9b3e893e4928c444ace13))

## [0.2.0](https://github.com/plagelao/plagelao.github.io/compare/v0.1.0...v0.2.0) (2023-08-04)


### Features

* **style:** Add navigation ([c609ef8](https://github.com/plagelao/plagelao.github.io/commit/c609ef83554c79eea514688060d80997b04e6dd3))

## [0.1.0](https://github.com/plagelao/plagelao.github.io/compare/v0.0.1...v0.1.0) (2023-08-04)


### Features

* **style:** Add footer ([5310460](https://github.com/plagelao/plagelao.github.io/commit/53104600558209451c11d977d29f7e92967e23f8))

## [0.0.1](https://github.com/plagelao/plagelao.github.io/compare/v0.0.0...v0.0.1) (2023-08-04)


### Bug Fixes

* **brand:** Change name ([98ccaab](https://github.com/plagelao/plagelao.github.io/commit/98ccaab77bb0287faf82b9cbcba06fc660c50fe0))

## [0.0.0](https://github.com/plagelao/plagelao.github.io/compare/dcf27499246acf2c57adcf02862def4509e09e6b...v0.0.0) (2023-08-04)


### Features

* Initial commit ([dcf2749](https://github.com/plagelao/plagelao.github.io/commit/dcf27499246acf2c57adcf02862def4509e09e6b))
```

It groups commits by release and by type, increasing the clarity of what's has changed when and, most importantly, it gives you a reproducible way to re-generate or add to the changelog.

### Buy in

That's all good, but how do you scale this into the team? How do you make this consistent inside the whole team? Start by discussing this with the team. It's always good to lead by example, so practice this yourself and, once you are comfortable, talk to the team about it.

That's all!
