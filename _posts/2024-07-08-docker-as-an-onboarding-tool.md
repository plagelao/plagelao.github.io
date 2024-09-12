---
title: Docker as an onboarding tool
excerpt_separator: <!--more-->
layout: post
categories: [Articles, Software development, Developer experience, Explanation]
tags: [developer experience, docker, docker compose]
tools:
  - label: Docker compose
    link: https://docs.docker.com/compose/
---

Having an easy onboarding experience is crucial for a team. It enables faster integration of new members, and increases productivity.

By providing and easy way to start contributing meaningfully to projects, you can ensure that new hires quickly become familiar with the team's culture, processes, and tools.

This article explores how [docker compose](https://docs.docker.com/compose/) can help achieving this.

With that in mind, let’s get on with it!
<!--more-->

### The problem

In any standard team that has existed for a while, there is a range of technologies that the team needs to maintain that. Different architectures, different languages, different databases, different everything.

It usually is overwhelming for the team members, so imagine how a new starter will feel about it. Not having a consistent way of setting up projects is a bad developer experience that can cause a high turnaround in your team.

### Guiding principles

You can tackle this problem in many ways, but the outcomes should be

1. Simplify the set up of projects
1. Define a consistent approach to every project
1. Low entry barrier to new members

### Actions

The following steps can help with achieving those outcomes:

1. Every project should run in a local machine by running a one line command
1. The configuration file should define as much of the services needed as possible
1. Name services in a meaningful way
1. Be consistent in naming as much as you can, but without loosing clarity
1. Define environments and secrets always in the same way

### Some examples

A Ruby on Rails application with [PostgreSQL](https://www.postgresql.org/) as the database service, and [Redis](https://redis.io/) as the local cache. It contains a service to migrate the database and a service to run the tests.
```yml
version: '3.2'

services:
  db:
    image: postgres:15
    volumes:
      - ./tmp/db:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: password
    profiles:
      - dev
      - data
      - testing
  redis:
    image: redis:latest
    profiles:
      - dev
      - testing
  web:
    build:
      context: .
      dockerfile: Dockerfile.development
      ssh:
        - default
    ports:
      - '3000:3000'
    env_file:
      - .env
    environment:
      RAILS_ENV: development
      RACK_ENV: development
      DATABASE_URL: postgres://postgres:password@db:5432/development
      REDIS_URL: redis://redis:6379
    volumes:
      - .:/app
    depends_on:
      - db
      - redis
    profiles:
      - dev
  db-migration:
    build:
      context: .
      dockerfile: Dockerfile.development
    entrypoint: ''
    command: bundle exec rake db:migrate
    depends_on:
      - db
    env_file:
      - .env
    environment:
      RAILS_ENV: development
      DATABASE_URL: postgres://postgres:password@db:5432/development
    profiles:
      - data
  test:
    build:
      context: .
      dockerfile: Dockerfile.development
    entrypoint: 'bin/docker-entrypoint-test.sh'
    command: 'bundle exec rake test'
    volumes:
      - .:/app
    depends_on:
      - db
      - redis
    env_file:
      - .env.test
    environment:
      RAILS_ENV: test
      DATABASE_URL: postgres://postgres:password@db:5432/test
      REDIS_URL: redis://redis:6379
    profiles:
      - testing
```

 Each behaviour or mode is defined as a different profile.

 The `dev` one is to run the app and the command is `docker compose --profile dev up`.

 The database migrations are defined with the profile `data`, and the command is `docker compose -profile data up`

 The database tests are defined with the profile `testing`, and the command is `docker compose -profile testing up`

 After this example, is simple to have another project, for example a Nuxt.js application with a Redis cache and use a similar approach:

 ```yml
services:
  redis:
    image: redis:alpine
    restart: always
    expose:
      - '6379'
    profiles:
      - dev

  web:
    build:
      context: .
      dockerfile: Dockerfile.development
      ssh:
        - default
    ports:
      - '8080:80'
    env_file:
      - .env
    environment:
      NUXT_REDIS_HOST: redis
    depends_on:
      - redis
    profiles:
      - dev

  web_zh:
    build:
      context: .
      dockerfile: Dockerfile.development
      args:
        - NUXT_PUBLIC_LOCALE=zh
      ssh:
        - default
    ports:
      - '8081:80'
    env_file:
      - .env
    environment:
      NUXT_REDIS_HOST: redis
    depends_on:
      - redis
    profiles:
      - dev

  test:
    build:
      context: .
      dockerfile: Dockerfile.development
      ssh:
        - default
    entrypoint: ''
    command: 'pnpm run tests'
    env_file:
      - .env.test
    environment:
      NUXT_REDIS_HOST: redis
    depends_on:
      - redis
    profiles:
      - testing
 ```

 In this particular case, the `dev` profile runs everything, and spins up a server for the default locale, and one for the `zh` locale. The command to run it is `docker compose --profile dev up`.

 The command to run the tests is `docker compose --profile testing up`.

 As you might have noticed, two different projects are set up in a similar way and a new member can easily switch from one to another in minutes.

### Summary

Docker compose simplifies the process of setting up and managing development environments, making it easier for teams to onboard new members and get them up to speed quickly.

It also ensures consistency for the team, making it easier for members to switch projects without having to deal with complex local configurations.

That's all!
