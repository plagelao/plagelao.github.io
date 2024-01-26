---
layout: page
title: Search
excerpt_separator: <!--more-->
---
Demo integrating Algolia in your site. This demo is part of a [set of articles]({% post_url 2024-01-23-search-architecture %}) that shows a possible architecture for a search engine.

<!--more-->

<p>
This search uses
<a class="algolia-logo" href="https://www.algolia.com/" target="_blank">
<img src="/assets/algolia.png" alt="Powered by Algolia"/>
</a>
</p>


<div id="searchbox"><!-- SearchBox widget will appear here -->
</div>
<!-- include algolia logo -->

<div class="searchresults">
<div id="facets"><!-- RefinementList widget will appear here --></div>
<div id="hits"><!-- Hits widget will appear here --></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/algoliasearch@4.22.1/dist/algoliasearch-lite.umd.js" integrity="sha256-pxkGFjfnFWYGOtV9uhCWK/spKiGS0Z7gVDKYm39LyfM=" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.64.0/dist/instantsearch.production.min.js" integrity="sha256-OtorR+6G6evpfgqzuOJjl5iH4JW+87ETzSpLZiVPTDg=" crossorigin="anonymous"></script>

<script>
  const searchClient = algoliasearch('KOUTOKWJ7W', 'd81d7523bcd67a0c0f3630ea2454a4b2');
  const { configure } = instantsearch.widgets;

  const search = instantsearch({
    indexName: 'dev_demo',
    searchClient,
  });

  search.addWidgets([
    configure({
      attributesToSnippet: ['body:50'],
    }),

    instantsearch.widgets.searchBox({
      container: '#searchbox',
    }),

    instantsearch.widgets.hits({
      container: '#hits',
      templates: {
        item: (hit, { html, components }) => {
            let tagNodes = hit.tags.map((tag) => {
             return html`<a class="tag" href="/tags/${tag}">${tag}</a>`
            })
            let snippet = html`${components.Snippet({ attribute: 'body', hit })}`
            return html`
            <article>
              <h3>
                <a href="${hit.url}">${components.Highlight({ hit, attribute: 'title' })}</a>
              </h3>
              <div class="tags">
                ${tagNodes}
              </div>
              <p class="date"><small><strong>${components.Highlight({ hit, attribute: 'date' })}</strong></small></p>
              <p>${snippet}</p>
            </article>
          `
          },
      },
    }),

    instantsearch.widgets.refinementList({
      container: '#facets',
      attribute: 'tags',
      searchable: false
    })
  ]);

  search.start();
</script>
