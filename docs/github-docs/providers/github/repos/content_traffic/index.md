---
title: content_traffic
hide_title: false
hide_table_of_contents: false
keywords:
  - content_traffic
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
<tr><td><b>Name</b></td><td><code>content_traffic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.content_traffic</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `count` | `integer` |
| `path` | `string` |
| `title` | `string` |
| `uniques` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_top_paths` | `SELECT` | `owner, repo` |
