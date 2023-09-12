---
title: repos_license
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_license
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
<tr><td><b>Name</b></td><td><code>repos_license</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.licenses.repos_license</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `type` | `string` |  |
| `git_url` | `string` |  |
| `html_url` | `string` |  |
| `path` | `string` |  |
| `url` | `string` |  |
| `size` | `integer` |  |
| `sha` | `string` |  |
| `_links` | `object` |  |
| `download_url` | `string` |  |
| `content` | `string` |  |
| `encoding` | `string` |  |
| `license` | `object` | License Simple |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_for_repo` | `SELECT` | `owner, repo` |
