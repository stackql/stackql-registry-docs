---
title: pages
hide_title: false
hide_table_of_contents: false
keywords:
  - pages
  - repos
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `protected_domain_state` | `string` | The state if the domain is verified |
| `https_enforced` | `boolean` | Whether https is enabled on the domain |
| `pending_domain_unverified_at` | `string` | The timestamp when a pending domain becomes unverified. |
| `html_url` | `string` | The web address the Page can be accessed from. |
| `public` | `boolean` | Whether the GitHub Pages site is publicly visible. If set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site. |
| `status` | `string` | The status of the most recent build of the Page. |
| `url` | `string` | The API address for accessing this Page resource. |
| `https_certificate` | `object` |  |
| `source` | `object` |  |
| `custom_404` | `boolean` | Whether the Page has a custom 404 page. |
| `cname` | `string` | The Pages site's custom domain |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_pages` | `SELECT` | `owner, repo` |  |
| `create_pages_site` | `INSERT` | `owner, repo, data__source` | Configures a GitHub Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages)." |
| `delete_pages_site` | `DELETE` | `owner, repo` |  |
| `update_information_about_pages_site` | `EXEC` | `owner, repo` | Updates information for a GitHub Pages site. For more information, see "[About GitHub Pages](/github/working-with-github-pages/about-github-pages). |
