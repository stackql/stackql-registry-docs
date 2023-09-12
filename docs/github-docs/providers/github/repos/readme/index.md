---
title: readme
hide_title: false
hide_table_of_contents: false
keywords:
  - readme
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
<tr><td><b>Name</b></td><td><code>readme</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.readme</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `download_url` | `string` |
| `size` | `integer` |
| `git_url` | `string` |
| `type` | `string` |
| `content` | `string` |
| `encoding` | `string` |
| `target` | `string` |
| `submodule_git_url` | `string` |
| `path` | `string` |
| `html_url` | `string` |
| `_links` | `object` |
| `sha` | `string` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_readme` | `SELECT` | `owner, repo` | Gets the preferred README for a repository.<br /><br />READMEs support [custom media types](https://docs.github.com/rest/overview/media-types) for retrieving the raw content or rendered HTML. |
| `get_readme_in_directory` | `SELECT` | `dir, owner, repo` | Gets the README from a repository directory.<br /><br />READMEs support [custom media types](https://docs.github.com/rest/overview/media-types) for retrieving the raw content or rendered HTML. |
