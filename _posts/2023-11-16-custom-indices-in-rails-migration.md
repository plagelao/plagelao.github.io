---
title: Custom indices in Ruby on Rails migrations when using references
excerpt_separator: <!--more-->
layout: note
categories: [Notes, Software development, Ruby on Rails, Tutorials]
tags: [Ruby on Rails]
tools:
  - label: Ruby on Rails
    link: https://rubyonrails.org/
---
Ruby on Rails uses [`references` method](https://guides.rubyonrails.org/active_record_migrations.html#references) creates the column in the table, and it also creates an index for the column by default.

The way to customise the index name is:

```ruby
create_table :another_super_long_table_name do |t|
  t.references :super_long_table_name, index: { name: 'another_index' }
end
```

You can also explicitly tell Rails that you don't want an index:

```ruby
create_table :another_super_long_table_name do |t|
  t.references :super_long_table_name, index: false
end
```
