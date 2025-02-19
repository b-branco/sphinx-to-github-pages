This is a simple project with a working pipeline for building and distributing sphinx documentation through GitHub Pages — mostly because I can't find an immediate use for this, and will 100% have forgotten how to do it by the time I do.

The workflow has the following steps:

1. A push to the _main_ branch (containing markdown source) triggers a sphinx HTML build.
2. The HTML build is dropped to the _gh-pages_ branch.
3. The website, hosted by Pages, gets updated according to the new HTML content in _gh-pages_

The two main steps to set this up were:
1. Set up ammaraskar's [sphinx-action](https://github.com/ammaraskar/sphinx-action) GitHub action in a yml file in **.github/workflows**. For a full example, see [sphinx-action-test](https://github.com/ammaraskar/sphinx-action-test).
2. On the **Settings/Pages** tab, set GitHub Pages to follow the _gh-pages_ branch.

It's also possible to set up a [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) for the website; I haven't got round to implementing this successfully (encountered issues with HTTPS validation), but it should involve creating **A**, **AAAA** and **ALIAS** records through the domain provider, as well as tinkering with the GitHub action to ensure a **CNAME** file containing the domain gets placed in the _gh-pages_ branch.
