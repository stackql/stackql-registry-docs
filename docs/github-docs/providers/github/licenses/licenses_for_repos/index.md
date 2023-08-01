---
title: licenses_for_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses_for_repos
  - licenses
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
<tr><td><b>Name</b></td><td><code>licenses_for_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.licenses.licenses_for_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `type` | `string` |  |
| `git_url` | `string` |  |
| `sha` | `string` |  |
| `html_url` | `string` |  |
| `_links` | `object` |  |
| `size` | `integer` |  |
| `url` | `string` |  |
| `encoding` | `string` |  |
| `path` | `string` |  |
| `license` | `object` | License Simple |
| `content` | `string` |  |
| `download_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_for_repo` | `SELECT` | `owner, repo` |
