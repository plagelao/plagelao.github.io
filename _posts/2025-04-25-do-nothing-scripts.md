---
title: Do-nothing scripts
excerpt_separator: <!--more-->
layout: post
categories: [Articles, Software development, Automation, Explanations]
tags: [ownership, automation, communication]
tools:
  - label: Do-nothing scripts original post
    link: https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/
purpose: By the end of the article, the reader understands that, although automation is the end goal, a first good step is creating a do-nothing script.
scope: This article will focus on why breaking the problem into its minimum possible solution is still valuable, as long as the minimum solution is still meaningful
main_points:
  - Automation is the end goal
  - Think small, avoid being overwhelmed
  - This is a do-nothing script
  - This is how it evolves into a proper solution
audience: Any developer
outcome: Another example of simplifying a problem
---

Automating recurring tasks is a good way to improve the developer experience and, also, to free time for more interesting and complex work. It's not always the most important or urgent task to work in, though. The business might have different priorities, you might not have the skill in the team to automate the work, or it might be a bit boring right now to work on that. Whatever the reason, day to day stuff might make you forget your automation goals.

In order to avoid that, you can write [do-nothing scripts](https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/) and evolve them into fully automated solutions.

With that in mind, let's get on with it!

<!--more-->

## This is a do-nothing script

Do-nothing scripts are simple scripts that don't automate the task, but they serve as a starting point to make sure you get there.

For example:

```bash
#!/bin/bash

echo "Follow the steps to publish a new vesion of the site:"

echo "Bump the version number"
read -p "Press any key to continue when you're done..."
echo "Update the changelog"
read -p "Press any key to continue when you're done..."
echo "Amend the version commit to add the changelog changes"
read -p "Press any key to continue when you're done..."
echo "Push the changes to release"
read -p "Press any key to continue when you're done..."
echo "That's all!"
```

It's just a list of the steps to complete the task, and you can make it as specific as you want to. It's not going to do anything, so you can add as much documentation as you think is needed.

In this particular case, it's very high level and not super useful. It doesn't matter, it's just a starting point to get to the end goal, which is full automation.

## Think small, avoid being overwhelmed

Now that you have created a basic do-nothing script, you can focus on automating the script iteratively.

Some steps will be easy wins that you can automate in a few minutes, and some steps will be big or complex tasks. Some steps you might not even be able to automate!

Pick your next steps and start automating one by one.

## This is how it evolves into a proper solution

Step by step, you can evolve your do-nothing script to a full solution. Let's follow the process with the previous simple example:


#### Step 1: The complex thing first

Turns out that the step that says `Amend the version commit to add the changelog changes` needs to steps. First, the changes need to be added to the git staging area, and second, the previous commit needs to be amended:

```bash
echo "Add the changes to the staging area"
git add .
echo "Amend the version commit to add the changelog changes"
git commit --amend
```

#### Step 2: The simple tasks

Because the site uses GitHub pages, pushing the commits is how a new version is released:

```bash
echo "Push the changes to release"
git push origin main
```
Bumping the version number is just a `cz` command:

```bash
echo "Bumping version number"
cz bump
```

And so is the changelog update:

```bash
echo "Updating changelog"
cz changelog
```

The final script looks like this:

```bash
#!/bin/bash

echo "Bumping version number"
cz bump
echo "Updating changelog"
cz changelog
echo "Add the changes to the staging area"
git add .
echo "Amend the version commit to add the changelog changes"
git commit --amend
echo "Push the changes to release"
git push origin main
echo "That's all!"
```

## Automation is the end goal

All of this could have been information in a `Readme.md` file, but there are many benefits in adopting the approach of using do-nothing scripts that get automated iteratively:

- It's easier to keep in sync with reality than written documentation
- Users of the script can update it when it's wrong or when they know how to automate a step
- It creates a cultural change where automation is a first class citizen

That's all!
