---
title: Clean GitLab pipelines
excerpt_separator: <!--more-->
layout: post
categories: [Articles, Software development, CI/CD, Explanations]
tags: [ci cd, gitlab, clarity]
tools:
  - label: GitLab
    link: https://gitlab.com
---

Maintaining a clean and efficient CI/CD pipeline is crucial for streamlined development workflows, quicker feedback cycles, and reliable software delivery.

It serves as the backbone of a well-organized and agile development workflow, ensuring that code changes are systematically tested, integrated, and deployed. A streamlined CI/CD pipeline facilitates faster feedback cycles, allowing developers to detect and fix issues promptly.

An efficient pipeline promotes consistency and reliability in software delivery, as it automates repetitive tasks and reduces the likelihood of errors. The clarity and structure brought by a well-maintained CI/CD setup not only enhance collaboration among development teams but also contribute to the overall speed, quality, and resilience of the software delivery lifecycle.

With that in mind, let’s get on with it!

<!--more-->

### Big YAML file

Your `.gitlab-ci.yml` may begin as a modest file, but over time, it can evolve into a complex structure that's challenging to comprehend unless managed carefully. It is essential to treat your pipeline configuration with the same level of attention and diligence as you apply to your code, ensuring clarity and maintainability throughout its growth.

### Composition: anchors

Anchors are a YAML feature that help eliminate redundancy by allowing the reuse of configurations, promoting consistency and reducing the risk of errors.

A possible use case for this is for rules. Usually you want the same rules in multiple jobs. For example, let's say that you want to run your tests always, except when you push a tag or when you push to a branch. Your original YAML file looks like this:

```yml
test_unit:
  rules:
    - if: '$CI_COMMIT_TAG'
      when: never
    - if: '$CI_COMMIT_REF_NAME == "main"'
    - if: '$CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH'

test_e2e:
  rules:
    - if: '$CI_COMMIT_TAG'
      when: never
    - if: '$CI_COMMIT_REF_NAME == "main"'
    - if: '$CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH'
```

There is a lot of duplication there that you can remove with an anchor:

```yml
.always_except_tag_or_push_to_branch: &always_except_tag_or_push_to_branch
  rules:
    - if: '$CI_COMMIT_TAG'
      when: never
    - if: '$CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH'
      when never
    - when always
```

And then you can use that in your jobs:

```yml
test_unit:
  <<: *always_except_tag_or_push_to_branch

test_e2e:
  <<: *always_except_tag_or_push_to_branch
```
One additional advantage is that you can name your anchor with a meaningful name that explain what's going on.

### Separation of concerns: Stages

The `stages` and `stage` keywords allow you to group your jobs and provide order of execution. The first stage will run first, and the second stage won't run until the first one is finished. There are ways to remove that constraint, but that's not part of this article. If tyou are are interested, have a look at the `needs` keyword.

An example of how a `.gitlab-ci.yml` file looks with stages:

```yml
stages:
  - build
  - test
  - deploy

build_docker_image:
  stage: build

build_test_docker_image:
  stage: build

run_unit_tests:
  stage: test

run_e2e_tests:
  stage: test

deploy_to_dev:
  stage: deploy

deploy_to_prod:
  stage: deploy
```

### Modularisation: include

The `include` keyword is used to include external YAML files. Using includes enables modularisation, making it easier to manage and update specific parts of the pipeline independently.

You can create a file for each stage and move all the configuration for that stage into it's own file. For the previous example:

```yml
# .gitlab-ci.yml

include:
  - local: /build/ci/gitlab/build.yml
  - local: /build/ci/gitlab/test.yml
  - local: /build/ci/gitlab/deploy.yml

stages:
  - build
  - test
  - deploy
```

```yml
# /build/ci/gitlab/build.yml

build_docker_image:
  stage: build

build_test_docker_image:
  stage: build
```

```yml
# /build/ci/gitlab/test.yml

run_unit_tests:
  stage: test

run_e2e_tests:
  stage: test
```

```yml
# /build/ci/gitlab/deploy.yml

deploy_to_dev:
  stage: deploy

deploy_to_prod:
  stage: deploy
```

### Summary

This approach enhances readability, simplifies troubleshooting, and facilitates collaboration within the development team. Moreover, a well-organized CI/CD configuration contributes to faster development cycles, as it ensures that changes can be implemented swiftly and reliably across the entire pipeline without unnecessary duplication of code.

That's all!
