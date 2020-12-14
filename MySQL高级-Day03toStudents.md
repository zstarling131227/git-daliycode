




<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-ZUjVod2EvYMDbGqRSyW0rpfgBq3i+gnR/4PfrzLsy5f20oIcRfgFQFVKgi3Ztp917bP1K/kdP5q8+nAlJ3+cFA==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-6548d5a1dd84bd83036c6a914b25b4ae.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-aX4OkLpzulpadvOncEEPpJZnQyeKNm2npzJowbL5JxptkoZXNPPy61R059xmEa3YyVF4Y4YXB6g+5o08uvdWpA==" rel="stylesheet" href="https://github.githubassets.com/assets/github-697e0e90ba73ba5a5a76f3a770410fa4.css" />
    
    
    
    


  <meta name="viewport" content="width=device-width">
  
  <title>1905/MySQL高级-Day03toStudents.md at master · zstarling131227/1905</title>
    <meta name="description" content="第一版. Contribute to zstarling131227/1905 development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars2.githubusercontent.com/u/52898621?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="zstarling131227/1905" /><meta name="twitter:description" content="第一版. Contribute to zstarling131227/1905 development by creating an account on GitHub." />
    <meta property="og:image" content="https://avatars2.githubusercontent.com/u/52898621?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="zstarling131227/1905" /><meta property="og:url" content="https://github.com/zstarling131227/1905" /><meta property="og:description" content="第一版. Contribute to zstarling131227/1905 development by creating an account on GitHub." />

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6NTAzNjQ2Mzc2OjAxZGNiMDFlMzE5NjJiYzM0YzQwMGQ2NjVlZDk5ODY2YjcyMmFiYjU2YWI0N2Q5Nzg0ZTkyOWY4OTk3Y2QyMWU=--d77552a851afd2e4c17d4ddf6e362ad62d97eca6">
  <link rel="sudo-modal" href="/sessions/sudo_modal">

  <meta name="request-id" content="A757:5FE8:33180A:46E737:5E54C9EB" data-pjax-transient="true" /><meta name="html-safe-nonce" content="d3de5074f52ac90aef2bc4e237a0e6ea21d3cca0" data-pjax-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS96c3RhcmxpbmcxMzEyMjcvMTkwNS90cmVlL21hc3Rlci9tb250aDAzL25vdGUiLCJyZXF1ZXN0X2lkIjoiQTc1Nzo1RkU4OjMzMTgwQTo0NkU3Mzc6NUU1NEM5RUIiLCJ2aXNpdG9yX2lkIjoiNTI3NTY4ODg2Mjg3NTcxNTAyIiwicmVnaW9uX2VkZ2UiOiJhcC1zb3V0aGVhc3QtMSIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-pjax-transient="true" /><meta name="visitor-hmac" content="992077f3c3ddd3a15e3ad06803e959d95af95b1e8fb324c357eb06177d0acad4" data-pjax-transient="true" />



  <meta name="github-keyboard-shortcuts" content="repository,source-code" data-pjax-transient="true" />

  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-actor-id" content="52898621" /><meta name="octolytics-actor-login" content="zstarling131227" /><meta name="octolytics-actor-hash" content="08aa8bdc02ec30d2af8040a07c57ef2935b4d68fa0733a3c8548e25ca6c3bb93" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="8f321b914cebda67554951f441d9b050">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="zstarling131227">

      <meta name="expected-hostname" content="github.com">

      <meta name="js-proxy-site-detection-payload" content="NWI4ZjBkYTkxZmI3YTRjMWVhZThjOGM5YjM3NWNlMDU3NjcyZWJmZGM2MTAxNzNjNTUzY2UyZTUzMzQzODllZXx7InJlbW90ZV9hZGRyZXNzIjoiMjE4Ljc5LjI1My4yMjkiLCJyZXF1ZXN0X2lkIjoiQTc1Nzo1RkU4OjMzMTgwQTo0NkU3Mzc6NUU1NEM5RUIiLCJ0aW1lc3RhbXAiOjE1ODI2MTUwMjIsImhvc3QiOiJnaXRodWIuY29tIn0=">

    <meta name="enabled-features" content="MARKETPLACE_FEATURED_BLOG_POSTS,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS,RELATED_ISSUES,GHE_CLOUD_TRIAL">

  <meta http-equiv="x-pjax-version" content="8310d593c1cc38b86be83242de7e6f3f">
  

      <link href="https://github.com/zstarling131227/1905/commits/master.atom?token=AMTSWPN3OHDVU7IV57HN63F4MH6G4" rel="alternate" title="Recent Commits to 1905:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/zstarling131227/1905 git https://github.com/zstarling131227/1905.git">

  <meta name="octolytics-dimension-user_id" content="52898621" /><meta name="octolytics-dimension-user_login" content="zstarling131227" /><meta name="octolytics-dimension-repository_id" content="199369016" /><meta name="octolytics-dimension-repository_nwo" content="zstarling131227/1905" /><meta name="octolytics-dimension-repository_public" content="false" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="199369016" /><meta name="octolytics-dimension-repository_network_root_nwo" content="zstarling131227/1905" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="true" />


    <link rel="canonical" href="https://github.com/zstarling131227/1905/blob/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <span class="Progress progress-pjax-loader position-fixed width-full js-pjax-loader-bar">
      <span class="progress-pjax-loader-bar top-0 left-0" style="width: 0%;"></span>
    </span>

    
    



          <header class="Header js-details-container Details flex-wrap flex-lg-nowrap p-responsive" role="banner">

    <div class="Header-item d-none d-lg-flex">
      <a class="Header-link" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

    </div>

    <div class="Header-item d-lg-none">
      <button class="Header-link btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
        <svg height="24" class="octicon octicon-three-bars" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
      </button>
    </div>

    <div class="Header-item Header-item--full flex-column flex-lg-row width-full flex-order-2 flex-lg-order-none mr-0 mr-lg-3 mt-3 mt-lg-0 Details-content--hidden">
        <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="199369016" data-scoped-search-url="/zstarling131227/1905/search" data-unscoped-search-url="/search" action="/zstarling131227/1905/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations"
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" value="+8r4/veqFerZMv20bEtRu5wz2WYumpz7XtYNk/j4UNReRqVaq0Ud4y0UojEG/slvNK75BlrOPbXtX+RvWZZSqQ==" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


      <nav class="d-flex flex-column flex-lg-row flex-self-stretch flex-lg-self-auto" aria-label="Global">
    <a class="Header-link d-block d-lg-none py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
      Dashboard
</a>

  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
    Pull requests
</a>
  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
    Issues
</a>
    <div class="mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15">
      <a class="js-selected-navigation-item Header-link" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
    Explore
</a>


    <a class="Header-link d-block d-lg-none mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" href="https://github.com/zstarling131227">
      <img class="avatar" height="20" width="20" alt="@zstarling131227" src="https://avatars0.githubusercontent.com/u/52898621?s=60&amp;v=4" />
      zstarling131227
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="RWlYKDmuw+pIAQ1KhtEenbVNt0Fw3XP9xYISC/9sePDqTyDdzX2XCFg50o4GaS+vAmQC0MNqHnVxtfLw17pOvg==" />
      <button type="submit" class="Header-link mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15 d-lg-none btn-link d-block width-full text-left" data-ga-click="Header, sign out, icon:logout" style="padding-left: 2px;">
        <svg class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9V7H8V5h4V3l4 3-4 3zm-2 3H6V3L2 1h8v3h1V1c0-.55-.45-1-1-1H1C.45 0 0 .45 0 1v11.38c0 .39.22.73.55.91L6 16.01V13h4c.55 0 1-.45 1-1V8h-1v4z"/></svg>
        Sign out
      </button>
</form></nav>

    </div>

    <div class="Header-item Header-item--full flex-justify-center d-lg-none position-relative">
      <div class="css-truncate css-truncate-target width-fit position-absolute left-0 right-0 text-center">
              <svg class="octicon octicon-lock" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 13H3v-1h1v1zm8-6v7c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h1V4c0-2.2 1.8-4 4-4s4 1.8 4 4v2h1c.55 0 1 .45 1 1zM3.8 6h4.41V4c0-1.22-.98-2.2-2.2-2.2-1.22 0-2.2.98-2.2 2.2v2H3.8zM11 7H2v7h9V7zM4 8H3v1h1V8zm0 2H3v1h1v-1z"/></svg>
    <a class="Header-link" href="/zstarling131227">zstarling131227</a>
    /
    <a class="Header-link" href="/zstarling131227/1905">1905</a>

</div>
    </div>

    <div class="Header-item mr-0 mr-lg-3 flex-order-1 flex-lg-order-none">
      

    <a aria-label="You have no unread notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-sw js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:52898621" href="/notifications/beta">
        <span class="js-indicator-modifier mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </div>


    <div class="Header-item position-relative d-none d-lg-flex">
      <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
    <svg class="octicon octicon-plus" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="zstarling131227/1905">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/zstarling131227/1905/issues/new" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

    </div>

    <div class="Header-item position-relative mr-0 d-none d-lg-flex">
      
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/zstarling131227/feature_preview/indicator_check.json">

  <summary class="Header-link"
    aria-label="View profile and more"
    data-ga-click="Header, show menu, icon:avatar">
    <img class="avatar " alt="@zstarling131227" width="20" height="20" src="https://avatars0.githubusercontent.com/u/52898621?s=60&amp;v=4">


      <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-2" style="width: 180px">
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/zstarling131227" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">zstarling131227</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container
    user-status-compact rounded-1 px-2 py-1 mt-2
    border
  " data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit "
      role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:52898621,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:52898621,&quot;originating_url&quot;:&quot;https://github.com/zstarling131227/1905/blob/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md&quot;}}" data-hydro-click-hmac="6c149fad6cff8c5ac793065bce4f1a90ba50503be01527b8c6d03287c8a0783a">
      <div class="d-flex">
        <div class="f6 lh-condensed user-status-header
          d-inline-block v-align-middle
            user-status-emoji-only-header circle
            pr-2
"
            style="max-width: 29px"
          >
          <div class="user-status-emoji-container flex-shrink-0 mr-1 mt-1 lh-condensed-ultra v-align-bottom" style="">
            <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 01-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 01-1.45-2.17A6.59 6.59 0 011.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 018 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
          </div>
        </div>
        <div class="
          d-inline-block v-align-middle
          
          
           css-truncate css-truncate-target 
           user-status-message-wrapper f6"
           style="line-height: 20px;" >
          <div class="d-inline-block text-gray-dark v-align-text-top text-left">
              <span class="text-gray ml-2">Set status</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="rLOd+TSIGYwzuhyLe8bRlG0DLJjXFE4uO/vYttaXnC+Cl843PuCUEH0E8cjxe4uLAeFGOQVtUdK+YV9qsOdQrA==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden></span>
                  <span class="js-user-status-custom-emoji"></span>
                  <span class="js-user-status-no-emoji-icon" >
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 01-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 01-1.45-2.17A6.59 6.59 0 011.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 018 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input
                  type="text"
                  autocomplete="off"
                  data-no-org-url="/autocomplete/user-suggestions"
                  data-org-url="/suggestions?mention_suggester=1"
                  data-maxlength="80"
                  class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field"
                  placeholder="What's happening?"
                  name="message"
                  value=""
                  aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
          <div class="d-inline-block f5 mr-2 pt-3 pb-2" >
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="f5 btn-link link-gray-dark border px-2 py-1 rounded-1" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2020-02-25T15:47:02+08:00">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2020-02-25T16:17:02+08:00">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2020-02-25T19:17:02+08:00">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2020-02-25T23:59:59+08:00">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2020-03-01T23:59:59+08:00">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit" disabled class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button" disabled class="width-full js-clear-user-status-button btn ml-2 ">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>


    <a role="menuitem" class="dropdown-item" href="/zstarling131227" data-ga-click="Header, go to profile, text:your profile">Your profile</a>

    <a role="menuitem" class="dropdown-item" href="/zstarling131227?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>

    <a role="menuitem" class="dropdown-item" href="/zstarling131227?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

    <a role="menuitem" class="dropdown-item" href="/zstarling131227?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists">Your gists</a>





    <div role="none" class="dropdown-divider"></div>
      
<div id="feature-enrollment-toggle" class="hide-sm hide-md feature-preview-details position-relative">
  <button
    type="button"
    class="dropdown-item btn-link"
    role="menuitem"
    data-feature-preview-trigger-url="/users/zstarling131227/feature_previews"
    data-feature-preview-close-details="{&quot;event_type&quot;:&quot;feature_preview.clicks.close_modal&quot;,&quot;payload&quot;:{&quot;originating_url&quot;:&quot;https://github.com/zstarling131227/1905/blob/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md&quot;,&quot;user_id&quot;:52898621}}"
    data-feature-preview-close-hmac="eac47a865e97360ae7bb6293c29712ca709133f494714c8bd087374c3212f012"
    data-hydro-click="{&quot;event_type&quot;:&quot;feature_preview.clicks.open_modal&quot;,&quot;payload&quot;:{&quot;link_location&quot;:&quot;user_dropdown&quot;,&quot;originating_url&quot;:&quot;https://github.com/zstarling131227/1905/blob/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md&quot;,&quot;user_id&quot;:52898621}}"
    data-hydro-click-hmac="c41578032106e9add7cd464bd0128758ee2c6821e6aa0cb7198f691a126f0a44"
  >
    Feature preview
  </button>
    <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
</div>

    <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
    <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="CH6lmCgMjXc7QmXpPqfwAzZbzrYEIMyMSypojesVG86nWN1t3N/ZlSt6ui2+H8ExgXJ7J7eXoQT/HYh2w8MtgA==" />
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
        Sign out
      </button>
      <input type="text" name="required_field_80dc" hidden="hidden" class="form-control" /><input type="hidden" name="timestamp" value="1582615022991" class="form-control" /><input type="hidden" name="timestamp_secret" value="494d76f67ca19c01671346a5ebe11a4009125e8067c96b8f56eed2125afe8899" class="form-control" />
</form>  </details-menu>
</details>

    </div>

  </header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>


    <div id="js-flash-container">

</div>


      

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>




  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      

  











  <div class="pagehead repohead hx_repohead readability-menu bg-gray-light pb-0 pt-0 pt-lg-3">

    <div class="container-lg mb-4 p-responsive d-none d-lg-flex">

      <div class="flex-auto min-width-0 width-fit mr-3">
        <h1 class="private  d-flex flex-wrap flex-items-center break-word float-none ">
    <svg class="octicon octicon-lock" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 13H3v-1h1v1zm8-6v7c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h1V4c0-2.2 1.8-4 4-4s4 1.8 4 4v2h1c.55 0 1 .45 1 1zM3.8 6h4.41V4c0-1.22-.98-2.2-2.2-2.2-1.22 0-2.2.98-2.2 2.2v2H3.8zM11 7H2v7h9V7zM4 8H3v1h1V8zm0 2H3v1h1v-1z"/></svg>
  <span class="author ml-1 flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/zstarling131227/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/zstarling131227">zstarling131227</a>
  </span>
  <span class="path-divider flex-self-stretch">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#js-repo-pjax-container" href="/zstarling131227/1905">1905</a>
  </strong>
  <span class="Label Label--outline v-align-middle ">Private</span>
</h1>


      </div>

      <ul class="pagehead-actions flex-shrink-0"  >




  <li>
    
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="clearfix js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="YBwkl0TvJALTN7CQk0IUES5ncQa5pcnARynCX9V48Ww+d9zoYz7bWHBXXje9Eg42UQBs1zZ/1ZN7MH21fv+Sww==" />      <input type="hidden" name="repository_id" value="199369016">

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="select-menu-button float-left btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:199369016,&quot;originating_url&quot;:&quot;https://github.com/zstarling131227/1905/blob/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md&quot;,&quot;user_id&quot;:52898621}}" data-hydro-click-hmac="392a330b55520505834f574a9454b646c31c3a451fd7f87aeb54b9967491f953" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
              Unwatch
          </span>
</summary>        <details-menu
          class="select-menu-modal position-absolute mt-5"
          style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count"
          href="/zstarling131227/1905/watchers"
          aria-label="1 user is watching this repository">
          1
        </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="/zstarling131227/1905/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="0bncZUwgjg3OV3ZW5+Z4KAhvDbBQEFfNNvsfW4vZQPA+koLSEnJVtvXFu7mYM/S+0R7vzEtGgnWAAVxwqDsEkQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Unstar zstarling131227/1905" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:199369016,&quot;originating_url&quot;:&quot;https://github.com/zstarling131227/1905/blob/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md&quot;,&quot;user_id&quot;:52898621}}" data-hydro-click-hmac="a3e8885b012b3afb771fa31c7d9fb16759856d86b024e46a27ca43dc99e46949" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg aria-label="star" height="16" class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" role="img"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>

        Unstar
</button>        <a class="social-count js-social-count" href="/zstarling131227/1905/stargazers"
           aria-label="0 users starred this repository">
           0
        </a>
</form>
    <form class="unstarred js-social-form" action="/zstarling131227/1905/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="1DJTsv22FF7S6e8nyRyO6uc3guMbM9pAeIW8Nk6ad/JiyNmkIPbVDJ0Wyu5Z9CH7mAqUFnP16DUyhOdvbLmQew==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Star zstarling131227/1905" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:199369016,&quot;originating_url&quot;:&quot;https://github.com/zstarling131227/1905/blob/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md&quot;,&quot;user_id&quot;:52898621}}" data-hydro-click-hmac="bedcb700addcce345d4c7d151c97500d1b2aaabd560f9475aedbd08904220fd4" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg aria-label="star" height="16" class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" role="img"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>

        Star
</button>        <a class="social-count js-social-count" href="/zstarling131227/1905/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
        <span class="btn btn-sm btn-with-count disabled tooltipped tooltipped-sw" aria-label="Cannot fork because you own this repository and are not a member of any organizations.">
          <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 00-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 002 1a1.993 1.993 0 00-1 3.72V6.5l3 3v1.78A1.993 1.993 0 005 15a1.993 1.993 0 001-3.72V9.5l3-3V4.72A1.993 1.993 0 008 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
          Fork
</span>
    <a href="/zstarling131227/1905/network/members" class="social-count"
       aria-label="0 users forked this repository">
      0
    </a>
  </li>
</ul>

    </div>
      
<nav class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax clearfix container-lg p-responsive d-none d-lg-block"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /zstarling131227/1905" href="/zstarling131227/1905">
      <div class="d-inline"><svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg></div>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /zstarling131227/1905/issues" href="/zstarling131227/1905/issues">
        <div class="d-inline"><svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 011.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg></div>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>


  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" data-skip-pjax="true" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /zstarling131227/1905/pulls" href="/zstarling131227/1905/pulls">
      <div class="d-inline"><svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0010 15a1.993 1.993 0 001-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 00-1 3.72v6.56A1.993 1.993 0 002 15a1.993 1.993 0 001-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg></div>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="4">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement" class="position-relative float-left">
      <a data-hotkey="g w" data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /zstarling131227/1905/actions" href="/zstarling131227/1905/actions">
        <div class="d-inline"><svg class="octicon octicon-play" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8A7 7 0 110 8a7 7 0 0114 0zm-8.223 3.482l4.599-3.066a.5.5 0 000-.832L5.777 4.518A.5.5 0 005 4.934v6.132a.5.5 0 00.777.416z"/></svg></div>
        Actions
</a>
    </span>

    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /zstarling131227/1905/projects" href="/zstarling131227/1905/projects">
      <div class="d-inline"><svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg></div>
      Projects
      <span class="Counter">0</span>
</a>

    <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy token_scanning code_scanning /zstarling131227/1905/network/alerts" href="/zstarling131227/1905/network/alerts">
      <div class="d-inline"><svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"/></svg></div>
      Security
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /zstarling131227/1905/network/dependencies" href="/zstarling131227/1905/network/dependencies">
      <div class="d-inline"><svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg></div>
      Insights
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations repo_keys_settings issue_template_editor secrets_settings key_links_settings repo_actions_settings notifications /zstarling131227/1905/settings" href="/zstarling131227/1905/settings">
      <div class="d-inline"><svg class="octicon octicon-gear" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88-1.84-1.13-1.13-1.81.91-1.09-.45-.69-1.92h-1.6l-.63 1.94-1.11.45-1.84-.88-1.13 1.13.91 1.81-.45 1.09L0 7.23v1.59l1.94.64.45 1.09-.88 1.84 1.13 1.13 1.81-.91 1.09.45.69 1.92h1.59l.63-1.94 1.11-.45 1.84.88 1.13-1.13-.92-1.81.47-1.09L14 8.75v.02zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"/></svg></div>
      Settings
</a>
</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /zstarling131227/1905" href="/zstarling131227/1905">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /zstarling131227/1905/issues" href="/zstarling131227/1905/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="2">
</a>      </span>


    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /zstarling131227/1905/pulls" href="/zstarling131227/1905/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="4">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /zstarling131227/1905/projects" href="/zstarling131227/1905/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="5">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /zstarling131227/1905/actions" href="/zstarling131227/1905/actions">
          <span itemprop="name">Actions</span>
          <meta itemprop="position" content="6">
</a>      </span>


      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy token_scanning code_scanning /zstarling131227/1905/network/alerts" href="/zstarling131227/1905/network/alerts">
        <span itemprop="name">Security</span>
        <meta itemprop="position" content="8">
</a>


  </nav>
</div>


  </div>

  

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>


<div class="container-lg clearfix new-discussion-timeline  p-responsive">
  <div class="repository-content ">

    
    


  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/zstarling131227/1905/blob/fa052e47b9fe2db0bd7c7cf8cebea9ff68af3088/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:c09c14cb40a9ba08ed1fa008f529b913 -->
      

    <div class="d-flex flex-items-start flex-shrink-0 flex-column flex-md-row pb-3">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay branch-select-menu " id="branch-select-menu">
  <summary class="btn btn-sm css-truncate"
           data-hotkey="w"
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target" data-menu-button>master</span>
    <span class="dropdown-caret"></span>
  </summary>

  <details-menu class="SelectMenu SelectMenu--hasFilter" src="/zstarling131227/1905/refs/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md?source_action=show&amp;source_controller=blob" preload>
    <div class="SelectMenu-modal">
      <include-fragment class="SelectMenu-loading" aria-label="Menu is loading">
        <svg class="octicon octicon-octoface anim-pulse" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
      </include-fragment>
    </div>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/zstarling131227/1905/find/master"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="month03/note/MySQL高级-Day03toStudents.md" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/zstarling131227/1905"><span>1905</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/zstarling131227/1905/tree/master/month03"><span>month03</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/zstarling131227/1905/tree/master/month03/note"><span>note</span></a></span><span class="separator">/</span><strong class="final-path">MySQL高级-Day03toStudents.md</strong>
      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/zstarling131227/1905/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="month03/note/MySQL高级-Day03toStudents.md" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>

    



    
  <div class="Box Box--condensed d-flex flex-column flex-shrink-0">
      <div class="Box-body d-flex flex-justify-between bg-blue-light flex-column flex-md-row flex-items-start flex-md-items-center">
        <span class="pr-md-4 f6">
          <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/users/zstarling131227/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/zstarling131227"><img class="avatar" src="https://avatars3.githubusercontent.com/u/52898621?s=40&amp;v=4" width="20" height="20" alt="@zstarling131227" /></a>
          <a class="text-bold link-gray-dark lh-default v-align-middle" rel="author" data-hovercard-type="user" data-hovercard-url="/users/zstarling131227/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/zstarling131227">zstarling131227</a>
            <span class="lh-default v-align-middle">
              <a data-pjax="true" title="month05_AI_day01" class="link-gray" href="/zstarling131227/1905/commit/4aa395bcb184b3a2e0ba73795dbbb889f5ec5f4a">month05_AI_day01</a>
            </span>
        </span>
        <span class="d-inline-block flex-shrink-0 v-align-bottom f6 mt-2 mt-md-0">
          <a class="pr-2 text-mono link-gray" href="/zstarling131227/1905/commit/4aa395bcb184b3a2e0ba73795dbbb889f5ec5f4a" data-pjax>4aa395b</a>
          <relative-time datetime="2019-09-18T03:17:11Z" class="no-wrap">Sep 18, 2019</relative-time>
        </span>
      </div>

    <div class="Box-body d-flex flex-items-center flex-auto f6 border-bottom-0 flex-wrap" >
      <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
        <summary class="btn-link">
          <span><strong>1</strong> contributor</span>
        </summary>
        <details-dialog
          class="Box Box--overlay d-flex flex-column anim-fade-in fast"
          aria-label="Users who have contributed to this file"
          src="/zstarling131227/1905/contributors-list/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md" preload>
          <div class="Box-header">
            <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </button>
            <h3 class="Box-title">
              Users who have contributed to this file
            </h3>
          </div>
          <include-fragment class="octocat-spinner my-3" aria-label="Loading..."></include-fragment>
        </details-dialog>
      </details>
    </div>
  </div>






    <div class="Box mt-3 position-relative">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">
  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">

      <span class="file-mode" title="File mode">executable file</span>
      <span class="file-info-divider"></span>
      988 lines (793 sloc)
      <span class="file-info-divider"></span>
    28.2 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/zstarling131227/1905/raw/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/zstarling131227/1905/blame/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/zstarling131227/1905/commits/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md">History</a>
    </div>


    <div>
          <a class="btn-octicon tooltipped tooltipped-nw js-remove-unless-platform"
             data-platforms="windows,mac"
             href="https://desktop.github.com"
             aria-label="Open this file in GitHub Desktop"
             data-ga-click="Repository, open with desktop">
              <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
          </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/zstarling131227/1905/edit/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="ucWtYiTw/4QfvYxuIBfNVV2av0Cb1jGm6y+kMl11J7sMChHzrZhTf73MMIsPN6xumhWLtN4bEPFxzwGq5qSdCw==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Edit this file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 011.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/zstarling131227/1905/delete/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="WWHzWr0iyeN5DPNigtBBb1HTkKUKRbINlXOFL9ZFV+u6fTKUUhCKGH5PE5WB02tVYcLHKa5kT0lU4/ojJCmG8A==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Delete this file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
            </button>
</form>    </div>
  </div>
</div>




      
  <div id="readme" class="Box-body readme blob js-code-block-container">
    <article class="markdown-body entry-content p-3 p-md-6" itemprop="text"><h1><a id="user-content-mysql-day02必须掌握" class="anchor" aria-hidden="true" href="#mysql-day02必须掌握"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>MySQL-Day02必须掌握</strong></h1>
<h2><a id="user-content-外键" class="anchor" aria-hidden="true" href="#外键"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>外键</strong></h2>
<p><strong>原理</strong></p>
<pre><code>让当前表字段的值在另一张表的范围内去选择
</code></pre>
<p><strong>使用规则</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、数据类型要一致
<span class="pl-c1">2</span>、主表被参考字段必须为KEY的一种 : PRI</pre></div>
<p><strong>级联动作</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、cascade : 删除 更新同步(被参考字段)
<span class="pl-c1">2</span>、restrict(默认) : 不让主表删除 更新
<span class="pl-c1">3</span>、<span class="pl-k">set</span> <span class="pl-k">null</span> : 删除 更新,从表该字段值设置为<span class="pl-k">NULL</span></pre></div>
<h2><a id="user-content-嵌套查询子查询" class="anchor" aria-hidden="true" href="#嵌套查询子查询"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>嵌套查询（子查询）</strong></h2>
<p><strong>定义</strong></p>
<pre><code>把内层的查询结果作为外层查询的条件
</code></pre>
<h2><a id="user-content-多表查询" class="anchor" aria-hidden="true" href="#多表查询"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>多表查询</strong></h2>
<p><strong>笛卡尔积</strong></p>
<pre><code>多表查询不加where条件,一张表的每条记录分别和另一张表的所有记录分别匹配一遍
</code></pre>
<h2><a id="user-content-连接查询" class="anchor" aria-hidden="true" href="#连接查询"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>连接查询</strong></h2>
<p><strong>分类</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、内连接（表<span class="pl-c1">1</span> <span class="pl-k">inner join</span> 表<span class="pl-c1">2</span> <span class="pl-k">on</span> 条件）
<span class="pl-c1">2</span>、外连接（表<span class="pl-c1">1</span> left|<span class="pl-k">right join</span> 表<span class="pl-c1">2</span> <span class="pl-k">on</span> 条件）
	<span class="pl-c1">1</span>、左连接 ：以左表为主显示查询结果
	<span class="pl-c1">2</span>、右连接 ：以右表为主显示查询结果</pre></div>
<p><strong>语法</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-k">select</span> 表名.字段名 <span class="pl-k">from</span> 表<span class="pl-c1">1</span> <span class="pl-k">inner join</span> 表<span class="pl-c1">2</span> <span class="pl-k">on</span> 条件；</pre></div>
<h2><a id="user-content-锁" class="anchor" aria-hidden="true" href="#锁"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>锁</strong></h2>
<p><strong>1、目的</strong> ：解决客户端并发访问的冲突问题</p>
<p><strong>2、锁分类</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、锁类型 : 
      读锁：读的时候别人不能碰
      写锁：更新的时候别人不能更新，只能一个人更新
<span class="pl-c1">2</span>、锁粒度 : 
      行级锁(InnoDB) ：锁粒度小。行之间的
      表级锁(MyISAM)：锁粒度大。表之间的。表级锁会造成程序阻塞。</pre></div>
<h2><a id="user-content-数据导入" class="anchor" aria-hidden="true" href="#数据导入"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>数据导入</strong></h2>
<p><strong>方式一（使用source命令）</strong>
不需要自己创建表，结构式文件</p>
<div class="highlight highlight-source-sql"><pre>mysql<span class="pl-k">&gt;</span> source <span class="pl-k">/</span>home<span class="pl-k">/</span>tarena<span class="pl-k">/</span><span class="pl-c1">xxx</span>.<span class="pl-c1">sql</span></pre></div>
<p><strong>方式二（使用load命令）</strong>
需要自己创建表</p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、将导入文件拷贝到数据库搜索路径中
   show variables <span class="pl-k">like</span> <span class="pl-s"><span class="pl-pds">'</span>secure%<span class="pl-pds">'</span></span>;
<span class="pl-c1">2</span>、在数据库中创建对应的表
<span class="pl-c1">3</span>、执行数据导入语句</pre></div>
<p>乱码</p>
<pre lang="text"><code>哪个场景的乱码？
1、表乱码（修改表的编码方式）
2、使用load导入或导出的时候容易乱码（打开文件的时候修改编码方式）
</code></pre>
<h2><a id="user-content-索引" class="anchor" aria-hidden="true" href="#索引"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>索引</strong></h2>
<p><strong>定义</strong></p>
<pre><code>对数据库表中一列或多列的值进行排序的一种结构(BTree)
</code></pre>
<p><strong>优点</strong></p>
<div class="highlight highlight-source-sql"><pre>加快数据的检索速度</pre></div>
<p><strong>缺点</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、占用实际物理存储空间
<span class="pl-c1">2</span>、索引需动态维护，消耗资源，降低数据的维护速度</pre></div>
<p><strong>分类及约束</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、普通索引（MUL）: 无约束
<span class="pl-c1">2</span>、唯一索引（UNI）：字段值不允许重复，但可为<span class="pl-k">NULL</span>
<span class="pl-c1">3</span>、主键（PRI）	：字段值不允许重复，不可为<span class="pl-k">NULL</span>
<span class="pl-c1">4</span>、外键		 ：让当前表字段的值在另一张表的范围内选择</pre></div>
<h1><a id="user-content-mysql-day03笔记" class="anchor" aria-hidden="true" href="#mysql-day03笔记"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>MySQL-Day03笔记</strong></h1>
<h2><a id="user-content-存储引擎" class="anchor" aria-hidden="true" href="#存储引擎"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>存储引擎</strong></h2>
<p><em><strong>不要轻易切换存储引擎</strong></em></p>
<h3><a id="user-content-定义" class="anchor" aria-hidden="true" href="#定义"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>定义</strong></h3>
<div class="highlight highlight-source-sql"><pre>处理表的处理器（使数据落地就是存入磁盘的引擎）</pre></div>
<h3><a id="user-content-基本操作" class="anchor" aria-hidden="true" href="#基本操作"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>基本操作</strong></h3>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、查看所有存储引擎
   mysql<span class="pl-k">&gt;</span> show engines;
<span class="pl-c1">2</span>、查看已有表的存储引擎
   mysql<span class="pl-k">&gt;</span> show create table 表名;
<span class="pl-c1">3</span>、创建表指定
   create table 表名(...)engine<span class="pl-k">=</span>MyISAM,charset<span class="pl-k">=</span>utf8,auto_increment<span class="pl-k">=</span><span class="pl-c1">10000</span>;

   mysql<span class="pl-k">&gt;</span> create table test_myisam(id <span class="pl-k">int</span>)engine<span class="pl-k">=</span>MyISAM,charset<span class="pl-k">=</span>utf8;
   mysql<span class="pl-k">&gt;</span> show create table test_myisam;

<span class="pl-c1">4</span>、已有表指定
   <span class="pl-k">alter</span> <span class="pl-k">table</span> 表名 engine<span class="pl-k">=</span>InnoDB;</pre></div>
<h3><a id="user-content-常用存储引擎及特点" class="anchor" aria-hidden="true" href="#常用存储引擎及特点"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>==常用存储引擎及特点==</strong></h3>
<ul>
<li>InnoDB	(默认的存储引擎)</li>
</ul>
<ol>
<li>支持行级锁　　＃＃行之间的影响小</li>
<li>支持外键、事务（跟钱相关的一般都使用事务）、事务回滚</li>
<li>表字段和索引同存储在一个文件中
<ol>
<li>表名.frm ：表结构</li>
<li>表名.ibd : 表记录及索引文件 （聚集：存储数据+索引）（数据结构是B树）</li>
</ol>
</li>
</ol>
<p>创建innodb_test表检测数据存储结构</p>
<div class="highlight highlight-source-sql"><pre>mysql<span class="pl-k">&gt;</span> use db3;
mysql<span class="pl-k">&gt;</span> create table innodb_test(id <span class="pl-k">int</span>);
mysql<span class="pl-k">&gt;</span> SHOw create table innodb_test;
mysql<span class="pl-k">&gt;</span> <span class="pl-k">insert into</span> innodb_test <span class="pl-k">values</span>(<span class="pl-c1">1</span>),(<span class="pl-c1">2</span>);
mysql<span class="pl-k">&gt;</span> <span class="pl-k">select</span> <span class="pl-k">*</span> <span class="pl-k">from</span> innodb_test;</pre></div>
<ul>
<li>MyISAM</li>
</ul>
<ol>
<li>支持表级锁</li>
<li>表字段和索引分开存储
<ol>
<li>表名.frm ：表结构</li>
<li>表名.MYI : 索引文件(my index)##叶子节点，不存储数据，存储指向磁盘的物理指针，也就是查询地址。</li>
<li>表名.MYD : 表记录(my data)</li>
</ol>
</li>
</ol>
<p>创建myisam_test表检测数据存储结构</p>
<div class="highlight highlight-source-sql"><pre>mysql<span class="pl-k">&gt;</span> use db3;
mysql<span class="pl-k">&gt;</span> create table myisam_test(id <span class="pl-k">int</span>) engine<span class="pl-k">=</span>MyISAM;
mysql<span class="pl-k">&gt;</span> SHOw create table myisam_test;
mysql<span class="pl-k">&gt;</span> <span class="pl-k">insert into</span> myisam_test <span class="pl-k">values</span>(<span class="pl-c1">1</span>),(<span class="pl-c1">2</span>);
mysql<span class="pl-k">&gt;</span> <span class="pl-k">select</span> <span class="pl-k">*</span> <span class="pl-k">from</span> myisam_test;</pre></div>
<ul>
<li>MEMORY</li>
</ul>
<ol>
<li>表记录存储在内存中，效率高（hash哈希算法）
<em>跟B+ ，Ｂ树不在一个量级上,memory查找速度超级快</em></li>
<li>服务或主机重启，表记录清除</li>
</ol>
<p><em>可删除的，可有可无的数据可以用内存存储。eg:游戏皮肤，称号。</em></p>
<p>创建memory_test1表检测数据存储结构</p>
<div class="highlight highlight-source-sql"><pre>mysql<span class="pl-k">&gt;</span> use db3;
mysql<span class="pl-k">&gt;</span> create table memory_test1(id <span class="pl-k">int</span>) engine<span class="pl-k">=</span>MEMORY;
mysql<span class="pl-k">&gt;</span> SHOw create table memory_test1;
mysql<span class="pl-k">&gt;</span> <span class="pl-k">insert into</span> memory_test1 <span class="pl-k">values</span>(<span class="pl-c1">1</span>),(<span class="pl-c1">2</span>);
mysql<span class="pl-k">&gt;</span> <span class="pl-k">select</span> <span class="pl-k">*</span> <span class="pl-k">from</span> memory_test1;</pre></div>
<p>结果展示
<em>只限于查看文档类型，不能查看内容，也不要轻易修改。</em></p>
<pre><code>tarena@tarena:~$ sudo su
[sudo] tarena 的密码： 
root@tarena:/home/tarena# cd /var/lib/mysql
root@tarena:/var/lib/mysql# ls
auto.cnf  db22             ib_buffer_pool  ib_logfile1  mysql_upgrade_info  stu
country   debian-5.7.flag  ibdata1         ibtmp1       performance_schema  sys
db2       dict             ib_logfile0     mysql        spider
root@tarena:/var/lib/mysql# cd db3
root@tarena:/var/lib/mysql/db3# ls
bank.frm    db.opt            memory_test.frm  myisam_test.MYD
bank.ibd    innodb_test.frm   middle.frm       myisam_test.MYI
course.frm  innodb_test.ibd   middle.ibd       teacher.frm
course.ibd  memory_test1.frm  myisam_test.frm  teacher.ibd
</code></pre>
<p>创建memory_test表检测重启是否会失去数据</p>
<pre><code>mysql&gt; use db3;
mysql&gt; create table memory_test(id int) engine=MEMORY;
mysql&gt; SHOw create table memory_test;
mysql&gt; insert into memory_test values(1),(2);
mysql&gt; select * from memory_test;

tarena@tarena:~$ service mysql restart

mysql&gt; select * from memory_test;
Empty set (0.00 sec)
</code></pre>
<p><strong>如何选择存储引擎</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、执行查操作多的表用 MyISAM(使用InnoDB浪费资源)

<span class="pl-c"><span class="pl-c">#</span>##建议：具体问题具体分析 --&gt;不知道用什么的时候，选择Innodb.</span>
mysql中有key_buffer<span class="pl-c"><span class="pl-c">--</span>&gt;内存中缓存索引，大小为64M-12BM的内存</span>
 M:存索引    <span class="pl-k">In</span>:存索引<span class="pl-k">+</span>数据    两者相比，M的索引数量很大；Innodb也会产生大量的内存交换
 M：A  <span class="pl-k">In</span>：A<span class="pl-k">+</span>数据  <span class="pl-k">IN</span>快
 M：A   AAAAAA  <span class="pl-k">In</span>：A<span class="pl-k">+</span>数据  AAAAAA  M快
 具体情况根据压测结果对待。

<span class="pl-c1">2</span>、执行写操作多的表用 InnoDB
<span class="pl-c1">3</span>、临时表 ： MEMORY    redis简单，速度快</pre></div>
<h2><a id="user-content-mysql的用户账户管理" class="anchor" aria-hidden="true" href="#mysql的用户账户管理"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>MySQL的用户账户管理</strong></h2>
<h3><a id="user-content-开启mysql远程连接" class="anchor" aria-hidden="true" href="#开启mysql远程连接"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>开启MySQL远程连接</strong></h3>
<p><strong>更改配置文件，重启服务！</strong></p>
<h4><a id="user-content-1sudo-su" class="anchor" aria-hidden="true" href="#1sudo-su"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>1、sudo su</h4>
<div class="highlight highlight-source-sql"><pre>tarena@tarena:~$ sudo su
[sudo] tarena 的密码： 
root@tarena:<span class="pl-k">/</span>home<span class="pl-k">/</span>tarena<span class="pl-c"><span class="pl-c">#</span> cd</span></pre></div>
<h4><a id="user-content-2cd-etcmysqlmysqlconfd" class="anchor" aria-hidden="true" href="#2cd-etcmysqlmysqlconfd"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>2、cd /etc/mysql/mysql.conf.d</h4>
<p>etc：该目录一般会存当前系统（ubantu)的所有安装的软件的配置文件，前提是有超级用户root权限才能打开</p>
<pre><code>root@tarena:~# cd /etc/mysql/mysql.conf.d
root@tarena:/etc/mysql/mysql.conf.d# ls
mysqld.cnf  mysqld_safe_syslog.cnf
</code></pre>
<h4><a id="user-content-3cp-mysqldcnf-mysqldcnfbak" class="anchor" aria-hidden="true" href="#3cp-mysqldcnf-mysqldcnfbak"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>3、cp mysqld.cnf mysqld.cnf.bak</h4>
<pre><code>root@tarena:/etc/mysql/mysql.conf.d# cp mysqld.cnf mysqld.cnf.bak
root@tarena:/etc/mysql/mysql.conf.d# ls
mysqld.cnf  mysqld.cnf.bak  mysqld_safe_syslog.cnf
root@tarena:/etc/mysql/mysql.conf.d# ll
总用量 32
drwxr-xr-x 2 root root  4096 8月   9 11:31 ./
drwxr-xr-x 4 root root  4096 7月  25 08:26 ../
-rw-r--r-- 1 root root  3052 1月  12  2018 mysqld.cnf
-rw-r--r-- 1 root root  3052 8月   9 11:31 mysqld.cnf.bak
-rw-r--r-- 1 root root 12288 8月   9 11:16 .mysqld.cnf.swp
-rw-r--r-- 1 root root    21 1月  12  2018 mysqld_safe_syslog.cnf
</code></pre>
<h4><a id="user-content-4修改配置文件vi-mysqldcnf" class="anchor" aria-hidden="true" href="#4修改配置文件vi-mysqldcnf"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>4、修改配置文件vi mysqld.cnf</h4>
<p>（1） 修改监听地址</p>
<pre><code>#找到44行左右, bind-address = 127.0.0.1加 # 注释，变成#bind-address = 127.0.0.1
</code></pre>
<p>（2）修改编码方式</p>
<p>修改之前先进行模糊查询：show variables like '%chara%'</p>
<pre><code>   找到配置文件，打开，寻找[mysqld]，然后另起一行添加character_set_server = utf8
</code></pre>
<h4><a id="user-content-5保存退出" class="anchor" aria-hidden="true" href="#5保存退出"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>5、保存退出</h4>
<pre><code>vi使用 : 按a -&gt;编辑文件 -&gt;ESC -&gt;shift+: -&gt;wq
</code></pre>
<h4><a id="user-content-6service-mysql-restart" class="anchor" aria-hidden="true" href="#6service-mysql-restart"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>6、service mysql restart</h4>
<pre><code>tarena@tarena:~$ service mysql restart
tarena@tarena:~$ ps aux|grep 'mysql'
</code></pre>
<h3><a id="user-content-添加授权用户" class="anchor" aria-hidden="true" href="#添加授权用户"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>添加授权用户</strong></h3>
<ol>
<li>用root用户登录mysql</li>
</ol>
<div class="highlight highlight-source-sql"><pre>   mysql <span class="pl-k">-</span>uroot <span class="pl-k">-</span>p123456
   mysql <span class="pl-k">-</span>uroot <span class="pl-k">-</span><span class="pl-c1">h176</span>.<span class="pl-c1">23</span>.<span class="pl-c1">4</span>.<span class="pl-c1">102</span> <span class="pl-k">-</span>p
   mysql<span class="pl-k">&gt;</span> <span class="pl-k">select</span> <span class="pl-k">*</span> <span class="pl-k">from</span> <span class="pl-c1">mysql</span>.<span class="pl-c1">user</span>\G;

<span class="pl-k">***************************</span> <span class="pl-c1">1</span>. row <span class="pl-k">***************************</span>
                  Host: localhost
                  User: root

监听本地地址
  终端输入mysql <span class="pl-k">-</span>uroot <span class="pl-k">-</span>p123456
  查看用户<span class="pl-k">select</span> <span class="pl-k">*</span> <span class="pl-k">from</span> <span class="pl-c1">mysql</span>.<span class="pl-c1">user</span>\G;  host显示localhost；</pre></div>
<ol start="2">
<li>授权</li>
</ol>
<pre><code>   grant 权限列表 on 库.表 to "用户名"@"localhost" identified by "密码" with grant option;
</code></pre>
<p><strong>登录地址localhost</strong></p>
<pre><code>localhost表示登录地址。默认是127.0.0.1
当localhost是%时，表示所有的IP都可以登录服务
当localhost是特定IP地址（xixi，但是xixi是不存在的网址）时，不能可以进入服务
当localhost是特定IP地址（内网地址176.23.4.102）时，只有用户通过改地址才可以进入服务
</code></pre>
<ol start="3">
<li>刷新权限</li>
</ol>
<pre><code>   flush privileges;
</code></pre>
<p><strong>权限列表</strong></p>
<pre><code>all privileges 、select 、insert ... ... 
库.表 ： *.* 代表所有库的所有表
</code></pre>
<h3><a id="user-content-示例" class="anchor" aria-hidden="true" href="#示例"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>示例</strong></h3>
<p><strong>示例一</strong></p>
<h4><a id="user-content-1添加授权用户work密码123" class="anchor" aria-hidden="true" href="#1添加授权用户work密码123"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>1、添加授权用户work,密码123</h4>
<p>（1）对<strong>所有库</strong>的<strong>所有表</strong>有<strong>所有权限</strong></p>
<div class="highlight highlight-source-sql"><pre>  mysql<span class="pl-k">&gt;</span><span class="pl-k">grant</span> all privileges <span class="pl-k">on</span> <span class="pl-k">*</span>.<span class="pl-k">*</span> to <span class="pl-s"><span class="pl-pds">'</span>work<span class="pl-pds">'</span></span>@<span class="pl-s"><span class="pl-pds">'</span>%<span class="pl-pds">'</span></span> identified by <span class="pl-s"><span class="pl-pds">'</span>123<span class="pl-pds">'</span></span> with <span class="pl-k">grant</span> option;
  mysql<span class="pl-k">&gt;</span>flush privileges;
  mysql<span class="pl-k">&gt;</span> <span class="pl-k">select</span> <span class="pl-k">*</span> <span class="pl-k">from</span> <span class="pl-c1">mysql</span>.<span class="pl-c1">user</span>\G;

  <span class="pl-k">***************************</span> <span class="pl-c1">6</span>. row <span class="pl-k">***************************</span>
                  Host: %
                  User: work

终端输入mysql <span class="pl-k">-</span>uwork <span class="pl-k">-</span>p123
查看用户<span class="pl-k">select</span> <span class="pl-k">*</span> <span class="pl-k">from</span> <span class="pl-c1">mysql</span>.<span class="pl-c1">user</span>\G;  host显示%；
可以查看所有的库：show databases;

 <span class="pl-c"><span class="pl-c">#</span>#两种方法都可以登录</span>
mysql <span class="pl-k">-</span>uwork <span class="pl-k">-</span>p
mysql <span class="pl-k">-</span>uwork <span class="pl-k">-</span><span class="pl-c1">h176</span>.<span class="pl-c1">23</span>.<span class="pl-c1">4</span>.<span class="pl-c1">102</span> <span class="pl-k">-</span>p</pre></div>
<p>（2）对<strong>country库</strong>的<strong>sanguo数据表</strong>有<strong>所有权限</strong>：只能看当前的库</p>
<pre><code>mysql&gt;grant all privileges on country.sanguo* to 'work1'@'%' identified by '123' with grant option;
  mysql&gt;flush privileges;
  mysql&gt; select * from mysql.user\G;

*************************** 8. row ***************************
                  Host: %
                  User: work1

只能查看country库中的sanguo数据表：show databases;

mysql -uwork1 -p   ##不可以登录
</code></pre>
<h4><a id="user-content-2改变登录地址" class="anchor" aria-hidden="true" href="#2改变登录地址"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>2、改变登录地址</h4>
<p>（1）添加指定不存在网址</p>
<pre><code>  mysql&gt;grant all privileges on *.* to 'xixi'@'xixi' identified by '131227' with grant option;
  mysql&gt;flush privileges;
  mysql&gt; select * from mysql.user\G;

*************************** 7. row ***************************
                  Host: xixi
                  User: xixi

mysql -uxixi -p   ##不可以登录
mysql -uxixi -h176.23.4.102 -p   ##不可以登录
</code></pre>
<p>（2）添加特定存在网址</p>
<pre><code>  mysql&gt;grant all privileges on *.* to 'yaoyue'@'176.23.4.102' identified by '131227' with grant option;
  mysql&gt;flush privileges;
  mysql&gt; select * from mysql.user\G;

*************************** 10. row ***************************
                  Host: 176.23.4.102
                  User: yaoyue

mysql -uyaoyue -p   ##不可以登录
mysql -uyaoyue -h176.23.4.102 -p  ##可以登录
</code></pre>
<h4><a id="user-content-3添加用户duty对db2库中所有表有所有权限" class="anchor" aria-hidden="true" href="#3添加用户duty对db2库中所有表有所有权限"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>3、添加用户duty,对db2库中所有表有所有权限</h4>
<pre><code>  mysql&gt;grant all privileges on db2.* to 'duty'@'%' identified by '123' with grant option;
  mysql&gt;flush privileges;
  mysql&gt; select * from mysql.user\G;

  *************************** 5. row ***************************
                  Host: %
                  User: duty
终端输入mysql -uduty  -p123
查看用户select * from mysql.user\G;  host显示%；

可以查看db2库中的所有表：show databases;

mysql -uduty -p
</code></pre>
<p><strong>示例二</strong></p>
<p>test_utf8是在修改配置文件后，在创建表时也没有添加编码方式utf8的数据库结构</p>
<pre><code>mysql&gt; show create database test_utf8;
+-----------+--------------------------------------------------------------------+
| Database  | Create Database                                                    |
+-----------+--------------------------------------------------------------------+
| test_utf8 | CREATE DATABASE `test_utf8` /*!40100 DEFAULT CHARACTER SET utf8 */ |
+-----------+--------------------------------------------------------------------+
1 row in set (0.00 sec)
</code></pre>
<p>db2是在没有修改配置文件，在创建表时也没有添加编码方式utf8的数据库结构</p>
<pre><code>mysql&gt; show create database db2;
+----------+----------------------------------------------------------------+
| Database | Create Database                                                |
+----------+----------------------------------------------------------------+
| db2      | CREATE DATABASE `db2` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+----------+----------------------------------------------------------------+
1 row in set (0.00 sec)

</code></pre>
<h2><a id="user-content-事务和事务回滚" class="anchor" aria-hidden="true" href="#事务和事务回滚"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>==事务和事务回滚==</strong></h2>
<h3><a id="user-content-事务定义" class="anchor" aria-hidden="true" href="#事务定义"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>事务定义</strong></h3>
<div class="highlight highlight-source-sql"><pre> 一件事从开始发生到结束的过程</pre></div>
<h3><a id="user-content-作用" class="anchor" aria-hidden="true" href="#作用"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>作用</strong></h3>
<div class="highlight highlight-source-sql"><pre>确保数据的一致性、准确性、有效性</pre></div>
<h3><a id="user-content-事务操作" class="anchor" aria-hidden="true" href="#事务操作"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>事务操作</strong></h3>
<ol>
<li>开启事务
mysql&gt;begin; # 方法1
mysql&gt;start transaction; # 方法2</li>
<li>开始执行事务中的1条或者n条SQL命令</li>
<li>终止事务
mysql&gt;commit; # 事务中SQL命令都执行成功,提交到数据库,结束!
mysql&gt;rollback; # 有SQL命令执行失败,回滚到初始状态,结束!</li>
</ol>
<p><strong>模拟示例</strong></p>
<p><em>创建表</em></p>
<div class="highlight highlight-source-sql"><pre> <span class="pl-k">create</span> <span class="pl-k">table</span> <span class="pl-en">bank</span>(
   name <span class="pl-k">varchar</span>(<span class="pl-c1">20</span>),
   <span class="pl-k">money</span> <span class="pl-k">decimal</span>(<span class="pl-c1">20</span>,<span class="pl-c1">2</span>)
   )charset<span class="pl-k">=</span>utf8;

 <span class="pl-k">insert into</span> bank <span class="pl-k">values</span>
 (<span class="pl-s"><span class="pl-pds">'</span>vip1<span class="pl-pds">'</span></span>,<span class="pl-c1">20000</span>),
 (<span class="pl-s"><span class="pl-pds">'</span>vip2<span class="pl-pds">'</span></span>,<span class="pl-c1">2000</span>);</pre></div>
<p><em>rollback示例</em></p>
<pre><code>  begin;

 update bank set money=money-3000
  where name='vip1';

   select * from bank:
  +------+----------+
| name | money    |
+------+----------+
| vip1 | 17000.00 |
| vip2 |  2000.00 |
+------+----------+

work用户
因为没有提交，所以另一个用户的数据并未改变
   select * from bank:
  +------+----------+
| name | money    |
+------+----------+
| vip1 | 20000.00 |
| vip2 |  2000.00 |
+------+----------+

root用户
输入rollback后，root用户的数据恢复初始状态，数据更新失败，前提是要是‘事物’；

rollback

select * from bank:
  +------+----------+
| name | money    |
+------+----------+
| vip1 | 20000.00 |
| vip2 |  2000.00 |
+------+----------+

</code></pre>
<p><em>commit示例</em></p>
<pre><code>root 用户

  begin;

 update bank set money=money-3000
  where name='vip2';

  commit;

 select * from bank:

+------+----------+
| name | money    |
+------+----------+
| vip1 | 20000.00 |
| vip2 |  5000.00 |
+------+----------+


work用户
select * from bank;
    
+------+----------+
| name | money    |
+------+----------+
| vip1 | 20000.00 |
| vip2 |  5000.00 |
+------+----------+

</code></pre>
<p><em>在pycharm中的pymysql逻辑编写过程中大量使用</em></p>
<pre><code>try:
   转账1
   转账2
except:
   db.rollback()
db.commit()
</code></pre>
<h2><a id="user-content-事务四大特性acid" class="anchor" aria-hidden="true" href="#事务四大特性acid"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>==事务四大特性（ACID）==</strong></h2>
<ul>
<li><strong>1、原子性（atomicity）</strong>
注重结果</li>
</ul>
<pre><code>一个事务必须视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作
</code></pre>
<ul>
<li><strong>2、一致性（consistency）</strong>
每个过程的状态。开始到结束中间有很多状态。</li>
</ul>
<pre><code>数据库总是从一个一致性的状态转换到另一个一致性的状态
</code></pre>
<ul>
<li><strong>3、隔离性（isolation）</strong></li>
</ul>
<pre><code>一个事务所做的修改在最终提交以前，对其他事务是不可见的
</code></pre>
<ul>
<li><strong>4、持久性（durability）</strong></li>
</ul>
<pre><code>一旦事务提交，则其所做的修改就会永久保存到数据库中。此时即使系统崩溃，修改的数据也不会丢失
</code></pre>
<p><strong>注意</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、事务只针对于表记录操作(增删改)有效,对于库和表的操作无效
<span class="pl-c1">2</span>、事务一旦提交结束，对数据库中数据的更改是永久性的</pre></div>
<h2><a id="user-content-e-r模型entry-relationship" class="anchor" aria-hidden="true" href="#e-r模型entry-relationship"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>E-R模型(Entry-Relationship)</strong></h2>
<p><strong>定义</strong></p>
<div class="highlight highlight-source-sql"><pre>E<span class="pl-k">-</span>R模型即 实体<span class="pl-k">-</span>关系 数据模型,用于数据库设计
用简单的图(E<span class="pl-k">-</span>R图)反映了现实世界中存在的事物或数据以及他们之间的关系</pre></div>
<p><strong>实体、属性、关系</strong></p>
<ul>
<li>实体</li>
</ul>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、描述客观事物的概念
<span class="pl-c1">2</span>、表示方法 ：矩形框
<span class="pl-c1">3</span>、示例 ：一个人、一本书、一杯咖啡、一个学生</pre></div>
<ul>
<li>属性</li>
</ul>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、实体具有的某种特性
<span class="pl-c1">2</span>、表示方法 ：椭圆形
<span class="pl-c1">3</span>、示例
   学生属性 ：学号、姓名、年龄、性别、专业 ... 
   感受属性 ：悲伤、喜悦、刺激、愤怒 ...</pre></div>
<ul>
<li>==关系（重要）==</li>
</ul>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、实体之间的联系
<span class="pl-c1">2</span>、一对一关联(<span class="pl-c1">1</span>:<span class="pl-c1">1</span>) ：老公对老婆
   A中的一个实体,B中只能有一个实体与其发生关联
   B中的一个实体,A中只能有一个实体与其发生关联
<span class="pl-c1">3</span>、一对多关联(<span class="pl-c1">1</span>:n) ：父亲对孩子
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中只能有一个与其发生关联
<span class="pl-c1">4</span>、多对多关联(m:n) ：兄弟姐妹对兄弟姐妹、学生对课程
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中有多个实体与其发生关联</pre></div>
<p><strong>ER图的绘制</strong></p>
<p>矩形框代表实体,菱形框代表关系,椭圆形代表属性</p>
<ul>
<li>课堂示例（老师研究课题）</li>
</ul>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、实体 ：教师、课题
<span class="pl-c1">2</span>、属性
   教师 ：教师代码、姓名、职称
   课题 ：课题号、课题名
<span class="pl-c1">3</span>、关系
   多对多（m:n)
   <span class="pl-c"><span class="pl-c">#</span> 一个老师可以选择多个课题，一个课题也可以被多个老师选</span></pre></div>
<ul>
<li>练习</li>
</ul>
<p>设计一个学生选课系统的E-R图</p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、实体：学生、课程、老师
<span class="pl-c1">2</span>、属性
<span class="pl-c1">3</span>、关系
   学生 选择 课程 (m:n)
   课程 任课 老师 (<span class="pl-c1">1</span>:n)</pre></div>
<p>==<strong>关系映射实现（重要）</strong>==</p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>:<span class="pl-c1">1</span>实现 <span class="pl-c"><span class="pl-c">--</span>&gt; 主外键关联,外键字段添加唯一索引</span>
  表t1 : id <span class="pl-k">int</span> <span class="pl-k">primary key</span>,
          <span class="pl-c1">1</span>
  表t2 : t2_id <span class="pl-k">int</span> unique,
         <span class="pl-k">foreign key</span>(t2_id) <span class="pl-k">references</span> t1(id)
          <span class="pl-c1">1</span>
<span class="pl-c1">1</span>:n实现 <span class="pl-c"><span class="pl-c">--</span>&gt; 主外键关联</span>
  表t1 : id <span class="pl-k">int</span> <span class="pl-k">primary key</span>,
         <span class="pl-c1">1</span>
  表t2 : t2_id <span class="pl-k">int</span>,
         <span class="pl-k">foreign key</span>(t2_id) <span class="pl-k">references</span> t1(id)
         <span class="pl-c1">1</span>
         <span class="pl-c1">1</span>        
m:n实现(借助中间表):
   t1 : t1_id 
   t2 : t2_id </pre></div>
<p><strong>==多对多实现==</strong></p>
<ul>
<li>老师研究课题       <em>该表的数据都在db3库中</em></li>
</ul>
<pre><code>表1、老师表 
表2、课题表
问题？如何实现老师和课程之间的多对多映射关系？
中间表：middle
</code></pre>
<p>导入数据</p>
<pre><code>use db3;

source /home/tarena/1905/month03/code/code2/day03/mysql_day03/relation.sql

create table middle(
   id int primary key,
   tid int,cid int,
   foreign key(tid) references teacher(id),
   foreign key(cid) references course(id)
   )charset=utf8;

创建多对多的表
 insert into middle values (1,1,1),(2,1,2),(3,2,1),(4,2,3),(5,2,2);

</code></pre>
<ul>
<li>后续</li>
</ul>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、每个老师都在研究什么课题？
<span class="pl-k">select</span> <span class="pl-c1">teacher</span>.<span class="pl-c1">tname</span>,<span class="pl-c1">course</span>.<span class="pl-c1">cname</span> <span class="pl-k">from</span> teacher <span class="pl-k">inner join</span> middle <span class="pl-k">on</span> <span class="pl-c1">teacher</span>.<span class="pl-c1">id</span><span class="pl-k">=</span><span class="pl-c1">middle</span>.<span class="pl-c1">tid</span> <span class="pl-k">inner join</span> course <span class="pl-k">on</span> <span class="pl-c1">middle</span>.<span class="pl-c1">cid</span><span class="pl-k">=</span><span class="pl-c1">course</span>.<span class="pl-c1">id</span>;
<span class="pl-c1">2</span>、郭小闹在研究什么课题？
<span class="pl-k">select</span> <span class="pl-c1">teacher</span>.<span class="pl-c1">tname</span>,<span class="pl-c1">course</span>.<span class="pl-c1">cname</span> <span class="pl-k">from</span> teacher <span class="pl-k">inner join</span> middle <span class="pl-k">on</span> <span class="pl-c1">teacher</span>.<span class="pl-c1">id</span><span class="pl-k">=</span><span class="pl-c1">middle</span>.<span class="pl-c1">tid</span> <span class="pl-k">inner join</span> course <span class="pl-k">on</span> <span class="pl-c1">middle</span>.<span class="pl-c1">cid</span><span class="pl-k">=</span><span class="pl-c1">course</span>.<span class="pl-c1">id</span> <span class="pl-k">where</span> tname<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>郭小闹<span class="pl-pds">'</span></span>;</pre></div>
<h2><a id="user-content-mysql调优" class="anchor" aria-hidden="true" href="#mysql调优"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><strong>==MySQL调优==</strong></h2>
<p><strong>存储引擎优化</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、读操作多：MyISAM
<span class="pl-c1">2</span>、写操作多：InnoDB</pre></div>
<p><strong>索引优化</strong></p>
<pre><code>在 select、where、order by 常涉及到的字段建立索引
</code></pre>
<p><strong>SQL语句优化</strong></p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、单条查询最后添加 <span class="pl-k">LIMIT</span> <span class="pl-c1">1</span>，停止全表扫描
<span class="pl-c1">2</span>、<span class="pl-k">where</span>子句中不使用 <span class="pl-k">!=</span> ,否则放弃索引全表扫描
<span class="pl-c1">3</span>、尽量避免 <span class="pl-k">NULL</span> 值判断,否则放弃索引全表扫描
   优化前：<span class="pl-k">select</span> <span class="pl-k">number</span> <span class="pl-k">from</span> t1 <span class="pl-k">where</span> <span class="pl-k">number</span> is <span class="pl-k">null</span>;
   优化后：<span class="pl-k">select</span> <span class="pl-k">number</span> <span class="pl-k">from</span> t1 <span class="pl-k">where</span> <span class="pl-k">number</span><span class="pl-k">=</span><span class="pl-c1">0</span>;
   <span class="pl-c"><span class="pl-c">#</span> 在number列上设置默认值0,确保number列无NULL值</span>
<span class="pl-c1">4</span>、尽量避免 <span class="pl-k">or</span> 连接条件,否则放弃索引全表扫描
   优化前：<span class="pl-k">select</span> id <span class="pl-k">from</span> t1 <span class="pl-k">where</span> id<span class="pl-k">=</span><span class="pl-c1">10</span> <span class="pl-k">or</span> id<span class="pl-k">=</span><span class="pl-c1">20</span>;
   优化后： <span class="pl-k">select</span> id <span class="pl-k">from</span> t1 <span class="pl-k">where</span> id<span class="pl-k">=</span><span class="pl-c1">10</span> <span class="pl-k">union all</span> 
           <span class="pl-k">select</span> id <span class="pl-k">from</span> t1 <span class="pl-k">where</span> id<span class="pl-k">=</span><span class="pl-c1">20</span>;
<span class="pl-c1">5</span>、模糊查询尽量避免使用前置 % ,否则全表扫描
   <span class="pl-k">select</span> name <span class="pl-k">from</span> t1 <span class="pl-k">where</span> name <span class="pl-k">like</span> <span class="pl-s"><span class="pl-pds">"</span>c%<span class="pl-pds">"</span></span>;
<span class="pl-c1">6</span>、尽量避免使用 <span class="pl-k">in</span> 和 not <span class="pl-k">in</span>,否则全表扫描
   优化前：<span class="pl-k">select</span> id <span class="pl-k">from</span> t1 <span class="pl-k">where</span> id <span class="pl-k">in</span>(<span class="pl-c1">1</span>,<span class="pl-c1">2</span>,<span class="pl-c1">3</span>,<span class="pl-c1">4</span>);
   优化后：<span class="pl-k">select</span> id <span class="pl-k">from</span> t1 <span class="pl-k">where</span> id between <span class="pl-c1">1</span> <span class="pl-k">and</span> <span class="pl-c1">4</span>;
<span class="pl-c1">7</span>、尽量避免使用 <span class="pl-k">select</span> <span class="pl-k">*</span> ...;用具体字段代替 <span class="pl-k">*</span> ,不要返回用不到的任何字段</pre></div>
<p><strong>作业讲解</strong></p>
<p>有一张文章评论表comment如下</p>
<table>
<thead>
<tr>
<th><strong>comment_id</strong></th>
<th><strong>article_id</strong></th>
<th><strong>user_id</strong></th>
<th><strong>date</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>10000</td>
<td>10000</td>
<td>2018-01-30 09:00:00</td>
</tr>
<tr>
<td>2</td>
<td>10001</td>
<td>10001</td>
<td>... ...</td>
</tr>
<tr>
<td>3</td>
<td>10002</td>
<td>10000</td>
<td>... ...</td>
</tr>
<tr>
<td>4</td>
<td>10003</td>
<td>10015</td>
<td>... ...</td>
</tr>
<tr>
<td>5</td>
<td>10004</td>
<td>10006</td>
<td>... ...</td>
</tr>
<tr>
<td>6</td>
<td>10025</td>
<td>10006</td>
<td>... ...</td>
</tr>
<tr>
<td>7</td>
<td>10009</td>
<td>10000</td>
<td>... ...</td>
</tr>
</tbody>
</table>
<p>以上是一个应用的comment表格的一部分，请使用SQL语句找出在本站发表的所有评论数量最多的10位用户及评论数，并按评论数从高到低排序</p>
<p>备注：comment_id为评论id</p>
<p>​            article_id为被评论文章的id</p>
<p>​            user_id 指用户id</p>
<pre><code>select use_id ,count(user_id) from comment
group by user_id
order by count(user_id) desc
limit 10;
</code></pre>
<p>2、把 /etc/passwd 文件的内容导入到数据库的表中</p>
<div class="highlight highlight-source-sql"><pre>tarena:x:<span class="pl-c1">1000</span>:<span class="pl-c1">1000</span>:tarena,,,:<span class="pl-k">/</span>home<span class="pl-k">/</span>tarena:<span class="pl-k">/</span>bin<span class="pl-k">/</span>bash
<span class="pl-c1">1</span>、拷贝文件
   sudo cp <span class="pl-k">/</span>etc<span class="pl-k">/</span>passwd <span class="pl-k">/</span>var<span class="pl-k">/</span>lib<span class="pl-k">/</span>mysql<span class="pl-k">-</span>files
<span class="pl-c1">2</span>、建表
  <span class="pl-k">create</span> <span class="pl-k">table</span> <span class="pl-en">user</span>(
  username <span class="pl-k">varchar</span>(<span class="pl-c1">20</span>),
  password <span class="pl-k">char</span>(<span class="pl-c1">1</span>),
  uid <span class="pl-k">int</span>,
  gid <span class="pl-k">int</span>,
  comment <span class="pl-k">varchar</span>(<span class="pl-c1">50</span>),
  homedir <span class="pl-k">varchar</span>(<span class="pl-c1">100</span>),
  shell <span class="pl-k">varchar</span>(<span class="pl-c1">50</span>)
  )charset<span class="pl-k">=</span>utf8;
<span class="pl-c1">3</span>、导入
  load data infile <span class="pl-s"><span class="pl-pds">'</span>/var/lib/mysql-files/passwd<span class="pl-pds">'</span></span>
  into table user
  fields terminated by <span class="pl-s"><span class="pl-pds">'</span>:<span class="pl-pds">'</span></span>
  lines terminated by <span class="pl-s"><span class="pl-pds">'</span><span class="pl-cce">\n</span><span class="pl-pds">'</span></span>;</pre></div>
<p><strong>3、外键及查询题目</strong></p>
<p>综述：两张表，一张顾客信息表customers，一张订单表orders</p>
<p>表1：顾客信息表，完成后插入3条表记录</p>
<pre><code>c_id 类型为整型，设置为主键，并设置为自增长属性
c_name 字符类型，变长，宽度为20
c_age 微小整型，取值范围为0~255(无符号)
c_sex 枚举类型，要求只能在('M','F')中选择一个值
c_city 字符类型，变长，宽度为20
c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
</code></pre>
<div class="highlight highlight-source-sql"><pre><span class="pl-k">create</span> <span class="pl-k">table</span> <span class="pl-en">customers</span>(
c_id <span class="pl-k">int</span> <span class="pl-k">primary key</span> auto_increment,
c_name <span class="pl-k">varchar</span>(<span class="pl-c1">20</span>),
c_age tinyint unsigned,
c_sex enum(<span class="pl-s"><span class="pl-pds">'</span>M<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>F<span class="pl-pds">'</span></span>),
c_city <span class="pl-k">varchar</span>(<span class="pl-c1">20</span>),
c_salary <span class="pl-k">decimal</span>(<span class="pl-c1">12</span>,<span class="pl-c1">2</span>)
)charset<span class="pl-k">=</span>utf8;
<span class="pl-k">insert into</span> customers <span class="pl-k">values</span>(<span class="pl-c1">1</span>,<span class="pl-s"><span class="pl-pds">'</span>Tom<span class="pl-pds">'</span></span>,<span class="pl-c1">25</span>,<span class="pl-s"><span class="pl-pds">'</span>M<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>上海<span class="pl-pds">'</span></span>,<span class="pl-c1">10000</span>),(<span class="pl-c1">2</span>,<span class="pl-s"><span class="pl-pds">'</span>Lucy<span class="pl-pds">'</span></span>,<span class="pl-c1">23</span>,<span class="pl-s"><span class="pl-pds">'</span>F<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>广州<span class="pl-pds">'</span></span>,<span class="pl-c1">12000</span>),(<span class="pl-c1">3</span>,<span class="pl-s"><span class="pl-pds">'</span>Jim<span class="pl-pds">'</span></span>,<span class="pl-c1">22</span>,<span class="pl-s"><span class="pl-pds">'</span>M<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>北京<span class="pl-pds">'</span></span>,<span class="pl-c1">11000</span>);</pre></div>
<p>表2：顾客订单表（在表中插入5条记录）</p>
<pre><code>o_id 整型
o_name 字符类型，变长，宽度为30
o_price 浮点类型，整数最大为10位，小数部分为2位
设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(3,"mate9",3688),(2,"iwatch",2222),(2,"r11",4400);
</code></pre>
<div class="highlight highlight-source-sql"><pre><span class="pl-k">create</span> <span class="pl-k">table</span> <span class="pl-en">orders</span>(
o_id <span class="pl-k">int</span>,
o_name <span class="pl-k">varchar</span>(<span class="pl-c1">30</span>),
o_price <span class="pl-k">decimal</span>(<span class="pl-c1">12</span>,<span class="pl-c1">2</span>),
<span class="pl-k">foreign key</span>(o_id) <span class="pl-k">references</span> customers(c_id) <span class="pl-k">on delete cascade</span> <span class="pl-k">on</span> <span class="pl-k">update</span> cascade
)charset<span class="pl-k">=</span>utf8;
<span class="pl-k">insert into</span> orders <span class="pl-k">values</span>(<span class="pl-c1">1</span>,<span class="pl-s"><span class="pl-pds">"</span>iphone<span class="pl-pds">"</span></span>,<span class="pl-c1">5288</span>),(<span class="pl-c1">1</span>,<span class="pl-s"><span class="pl-pds">"</span>ipad<span class="pl-pds">"</span></span>,<span class="pl-c1">3299</span>),(<span class="pl-c1">2</span>,<span class="pl-s"><span class="pl-pds">"</span>iwatch<span class="pl-pds">"</span></span>,<span class="pl-c1">2222</span>),(<span class="pl-c1">2</span>,<span class="pl-s"><span class="pl-pds">"</span>r11<span class="pl-pds">"</span></span>,<span class="pl-c1">4400</span>);</pre></div>
<p>增删改查题</p>
<div class="highlight highlight-source-sql"><pre><span class="pl-c1">1</span>、返回customers表中，工资大于<span class="pl-c1">4000</span>元，或者年龄小于<span class="pl-c1">29</span>岁，满足这样条件的前<span class="pl-c1">2</span>条记录

<span class="pl-c1">2</span>、把customers表中，年龄大于等于<span class="pl-c1">25</span>岁，并且地址是北京或者上海，这样的人的工资上调<span class="pl-c1">15</span>%
  
<span class="pl-c1">3</span>、把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
  
<span class="pl-c1">4</span>、选择工资c_salary最少的顾客的信息
  
<span class="pl-c1">5</span>、找到工资大于<span class="pl-c1">5000</span>的顾客都买过哪些产品的记录明细	
  
<span class="pl-c1">6</span>、删除外键限制
 
<span class="pl-c1">7</span>、删除customers主键限制
 
<span class="pl-c1">8</span>、增加customers主键限制c_id
  </pre></div>
<h1><a id="user-content-补充" class="anchor" aria-hidden="true" href="#补充"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>补充</h1>
<h2><a id="user-content-1管道查询" class="anchor" aria-hidden="true" href="#1管道查询"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>1）管道查询</h2>
<pre><code>root@tarena:/var/lib/mysql/country# ls |grep 'sanguo'
tarena@tarena:~$ ps aux|grep 'mysqld' 
</code></pre>
<p>匹配字符'sanguo'查找显示</p>
<h2><a id="user-content-2查看错误日志" class="anchor" aria-hidden="true" href="#2查看错误日志"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>2）查看错误日志</h2>
<pre><code>数据库出错了，在error中查看日志
log_error = /var/log/mysql/error.log

打开方式
tarena@tarena:~$ cd /var/log/mysql
tarena@tarena:/var/log/mysql$ ls
error.log       error.log.2.gz  error.log.4.gz  error.log.6.gz
error.log.1.gz  error.log.3.gz  error.log.5.gz  error.log.7.gz
</code></pre>
<h2><a id="user-content-3-查看系统日志" class="anchor" aria-hidden="true" href="#3-查看系统日志"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>3） 查看系统日志</h2>
<pre><code>tarena@tarena:~$  cd /var/log
- 方法一：
tarena@tarena:/var/log$ vim /var/log/syslog
/log回车
 n是下一个，N 上一个
/MySQL 
- 方法二：
或者cat /var/log/syslog |grep 'MySQL '|more +
</code></pre>
<h2><a id="user-content-4vim使用" class="anchor" aria-hidden="true" href="#4vim使用"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>4）vim使用</h2>
<ol>
<li>vi打不开的时候，可以使用vim</li>
<li>vim修改时要点击i进入插入状态，</li>
<li>方向键：k是上移，j是下移,h是左移，l右移；</li>
<li>set number 添加行号</li>
<li>o从光标当前行 换行，并进入插入模式</li>
<li>插入模式后摁esc键切回阅读模式，</li>
<li>输入内件指定：w保存 q退出</li>
<li>3dd删除指定行数内容，3为指定行</li>
<li>u撤销</li>
<li>在只读状态时末尾输入'\log'搜索含有log的字段。n是下一个，N是上一个。</li>
<li>vim严格区分大小写</li>
</ol>
<h2><a id="user-content-5ifconfig查看网址ip" class="anchor" aria-hidden="true" href="#5ifconfig查看网址ip"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>5）ifconfig查看网址（IP）</h2>
<p>内网网址</p>
<pre><code>enp3s0: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt;  mtu 1500
        inet 176.23.4.102  netmask 255.255.255.0  broadcast 176.23.4.255
        inet6 fe80::be50:e020:e3d8:30a9  prefixlen 64  scopeid 0x20&lt;link&gt;
        ether fc:aa:14:eb:a5:58  txqueuelen 1000  (以太网)
        RX packets 4116  bytes 4459337 (4.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2287  bytes 256541 (256.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
</code></pre>
<p>本地网址</p>
<pre><code>lo: flags=73&lt;UP,LOOPBACK,RUNNING&gt;  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10&lt;host&gt;
        loop  txqueuelen 1000  (本地环回)
        RX packets 514  bytes 521475 (521.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 514  bytes 521475 (521.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
</code></pre>
<h2><a id="user-content-6查看进程" class="anchor" aria-hidden="true" href="#6查看进程"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>6）查看进程</h2>
<pre><code>查看当前进程
tarena@tarena:~$ ps aux
查看当前进程在哪些用户下进行
tarena@tarena:~$ ps aux|grep 'mysqld'
mysql     1081  0.0  4.7 1417112 189108 ?      Sl   08:13   0:02 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid
tarena   14473  0.0  0.0  21532  1004 pts/2    S+   09:35   0:00 grep --color=auto mysqld
tarena@tarena:~$ 
查看当前进程进行的总个数
tarena@tarena:~$ ps aux|grep 'mysqld'|wc -l
2
</code></pre>
<h2><a id="user-content-7哈希算法" class="anchor" aria-hidden="true" href="#7哈希算法"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>7）哈希算法</h2>
<pre><code>哈希算法就是散列函数，散列值（在下载环境中大量使用）

eg: '12345678'---&gt;'ABCDE'（MD5）

特点：
1. 输入为不定长的值，输出一定为定长值
2.不可逆，不可以由定长值转换为不定长值  '12345678'&lt;-!=--'ABCDE'
3.雪崩效应，修改不定长字符中的任意一个，输出的结果一定大不相同

密码（散列，散列值）
用char类型的字段，因为肯定会对密码进行哈希算法，根据散列的三大特点之一，因为输出为定长，所以char更好。varchar也可以存储密码，但是由于varchar有扩展字段，去存储一个输入字符的实际长度，由于已经定长了，就会浪费磁盘空间。
</code></pre>
<h2><a id="user-content-8配置文件etc" class="anchor" aria-hidden="true" href="#8配置文件etc"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>8）配置文件etc</h2>
<pre><code>etc：该目录一般会存当前系统（ubantu)的所有安装的软件的配置文件，前提是有超级用户root权限才能打开，在修改配置文件之前最好备份copy一份。
eg:mysql的配置文件
cd /etc/mysql/mysql.conf.d
</code></pre>
</article>
  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/zstarling131227/1905/find-symbols"
     data-tagsearch-ref="master"
     data-tagsearch-path="month03/note/MySQL高级-Day03toStudents.md"
     data-tagsearch-lang="Markdown"
     data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:199369016,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Markdown&quot;,&quot;originating_url&quot;:&quot;https://github.com/zstarling131227/1905/blob/master/month03/note/MySQL%E9%AB%98%E7%BA%A7-Day03toStudents.md&quot;,&quot;user_id&quot;:52898621}}"
     data-hydro-click-hmac="17379ee404b2ac7355445c1f24ba11a37001e7afc71ce6e6d24bb13fc94f5d86">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>



  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" async="async" integrity="sha512-VTkKwyyXYz1e8w0v/7LXDKSa7yMy1qEQofgf/5bGrUv8wpbpaZxx5S3Uc6oYrvbOe432HJdJG5qsFdM9sbP+wg==" type="application/javascript" id="js-conditional-compat" data-src="https://github.githubassets.com/assets/compat-bootstrap-55390ac3.js"></script>
    <script crossorigin="anonymous" async="async" integrity="sha512-3yNijdFdVDBZQDWrBvMeD2J9gyXwI5MKUMJSWdEGP44DgS4NEPQw2TmVlDdNAWrseJO5C/sXBSTrL24DvGMDJw==" type="application/javascript" src="https://github.githubassets.com/assets/vendor-df23628d.js"></script>
    <script crossorigin="anonymous" integrity="sha512-WZp98krTVri8yp2f8bpVGoTndKcChquCeXJdlvMy65oKppZPzZ52UwQQl0tO7kHoFC75L7MlBMxY3NhWju6CRg==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-599a7df2.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-Lap1+NRBH7wIWfmCDnMs6d5Keym1I0bJd3QDvtvFy+lfSMcvPzPioITh++pTkwx/3BvvsDvTYjSlQ6pptb8cGQ==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-2daa75f8.js"></script>
    
    
    
  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

