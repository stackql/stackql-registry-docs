---
title: github
hide_title: false
hide_table_of_contents: false
keywords:
  - github
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
id: github-doc
slug: /providers/github

---
Web-based version-control and collaboration.  
    
:::info Provider Summary (v23.04.00136)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>32</b></span><br />
<span>total methods:&nbsp;<b>836</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>247</b></span><br />
<span>total selectable resources:&nbsp;<b>238</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `github` provider, run the following command:  

```bash
REGISTRY PULL github;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- `STACKQL_GITHUB_USERNAME` - GitHub username (login)
- `STACKQL_GITHUB_PASSWORD` - GitHub Personal Access Token (see [Creating a personal access token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "github": { "type": "basic",  "username_var": "YOUR_GITHUB_USERNAME_VAR", "password_var": "YOUR_GITHUB_PASSWORD_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'github': { 'type': 'basic',  'username_var': 'YOUR_GITHUB_USERNAME_VAR', 'password_var': 'YOUR_GITHUB_PASSWORD_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/github/actions/">actions</a><br />
<a href="/providers/github/activity/">activity</a><br />
<a href="/providers/github/apps/">apps</a><br />
<a href="/providers/github/billing/">billing</a><br />
<a href="/providers/github/checks/">checks</a><br />
<a href="/providers/github/code_scanning/">code_scanning</a><br />
<a href="/providers/github/codes_of_conduct/">codes_of_conduct</a><br />
<a href="/providers/github/codespaces/">codespaces</a><br />
<a href="/providers/github/dependabot/">dependabot</a><br />
<a href="/providers/github/enterprise_admin/">enterprise_admin</a><br />
<a href="/providers/github/gists/">gists</a><br />
<a href="/providers/github/git/">git</a><br />
<a href="/providers/github/gitignore/">gitignore</a><br />
<a href="/providers/github/interactions/">interactions</a><br />
<a href="/providers/github/issues/">issues</a><br />
<a href="/providers/github/licenses/">licenses</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/github/markdown/">markdown</a><br />
<a href="/providers/github/meta/">meta</a><br />
<a href="/providers/github/migrations/">migrations</a><br />
<a href="/providers/github/oauth_authorizations/">oauth_authorizations</a><br />
<a href="/providers/github/orgs/">orgs</a><br />
<a href="/providers/github/packages/">packages</a><br />
<a href="/providers/github/projects/">projects</a><br />
<a href="/providers/github/pulls/">pulls</a><br />
<a href="/providers/github/rate_limit/">rate_limit</a><br />
<a href="/providers/github/reactions/">reactions</a><br />
<a href="/providers/github/repos/">repos</a><br />
<a href="/providers/github/scim/">scim</a><br />
<a href="/providers/github/search/">search</a><br />
<a href="/providers/github/secret_scanning/">secret_scanning</a><br />
<a href="/providers/github/teams/">teams</a><br />
<a href="/providers/github/users/">users</a><br />
</div>
</div>
