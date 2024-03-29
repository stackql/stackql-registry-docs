---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `node_id` | `string` |
| `tarball_url` | `string` |
| `zipball_url` | `string` |
| `commit` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_tags` | `SELECT` | `owner, repo` |
