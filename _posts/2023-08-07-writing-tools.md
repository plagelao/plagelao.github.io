---
title: Writing in your second language is easier with help
excerpt_separator: <!--more-->
layout: post
categories: [Articles, Writing, Reference]
tags: [writing better, communication]
tools:
  - label: Alex
    link: https://github.com/get-alex/alex
  - label: Vale
    link: https://github.com/errata-ai/vale
  - label: chatGPT
    link: https://chat.openai.com/
---
Welcome to the era of hybrid working, where written communication takes center stage like never before. In this scenario, clear and effective written exchanges, including emails, chat messages and documents, are crucial for daily interactions with your team. To be successful, it's essential to be clear and precise in your writing to avoid misunderstandings or confusion. Don't think twice about getting help from available tools to enhance your writing skills and streamline your communication.

This post explores some useful tools to help you in your day-to-day writing tasks. These tools are designed to make your written communication seamless and effective.

With that in mind, let's get on with it!
<!--more-->

### Alex: Because you are a good and self-reflective person

[Alex](https://github.com/get-alex/alex) is a great opinionated tool. It helps you catch insensitive, inconsiderate writing. And believe me, you can write a lot of it without even noticing.

Here are some examples on [gender bias](https://eige.europa.eu/publications-resources/thesaurus/terms/1320?language_content_entity=en). Given the following text:

```
Your boss is around, the guy looks stressed.
He is the one that makes the big decisions.
```

Alex raises the following warnings:

```
1:26-1:29  warning  `guy` may be insensitive, use `person`, `friend`, `pal`, `folk`, `individual` instead  gal-guy  retext-equality
  2:1-2:3  warning  `He` may be insensitive, use `They`, `It` instead                                      he-she   retext-equality
```

As you can see, it highlights the problem and proposes a solution.

Alex can also do the same with the [hindsight bias](https://en.wikipedia.org/wiki/Hindsight_bias). Given the following text:

```
The solution to the problem is very simple. You just need to get the flux capacitor working.
```

Alex returns the following warnings:

```
1:37-1:43  warning  `simple` may be insensitive, try not to use it  simple  retext-equality
1:49-1:53  warning  `just` may be insensitive, try not to use it    just    retext-equality
```

Alex is a great tool from the point of view of writing better, but it's even better as a tool **to learn more about yourself**. By giving you automatic feedback about your biases, it allows you to reflect, learn and grow as a person. How cool is that?

### Vale: Linting for prose

[Vale](https://github.com/errata-ai/vale) is another great tool **for writers**. It's a command-line tool that brings code-like [linting to prose](https://vale.sh/docs/vale-cli/overview/). Vale is configurable and you can spend a lot of time [tuning it to match your style or preferences](https://vale.sh/hub/).

Given the following text:

```
I am writing about something that might interest you. This article will talk about one thing, another thing and one more thing.
Also, if you make a typo like "writting" or if you use parenthesis (sometimes you use them), Vale is going to complain about it.
Event better, it tells you to clarify acronyms the first time you use them. For example, with IPO. But if you use acronyms for well known things, like HTTP, it gives you a pass.
```

Vale, configured with the Google package, returns the following log:

```
 1:1   warning     Avoid first-person pronouns     Google.FirstPerson
                   such as 'I '.
 1:68  warning     Avoid using 'will'.             Google.Will
 2:32  error       Did you really mean             Vale.Spelling
                   'writting'?
 2:68  suggestion  Use parentheses judiciously.    Google.Parens
 3:95  suggestion  Spell out 'IPO', if it's        Google.Acronyms
                   unfamiliar to the audience.

✖ 1 error, 2 warnings and 2 suggestions in 1 file.
```

It's your choice to follow the guidelines. As Vale explains in its documentation pages, it's a tool for writers to enforce some rules. You can choose and configure those rules.

At a minimum, Vale gives you consistency in your writing style.

### ChatGPT: The obvious one

As a person with English as their second language, it's amazing how much better ChatGPT is at writing English. It's both demoralising and empowering. Demoralising because it shows you how far away your goal is. Empowering because it feels like you can express yourself in a more meaningful way with its help.

If you use it sporadically or as a way to get your ideas in a different style, it can be very powerful. To me, it still feels a bit like cheating, though.

That's all!
