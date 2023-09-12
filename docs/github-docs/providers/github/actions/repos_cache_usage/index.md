---
title: repos_cache_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_cache_usage
  - actions
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
<tr><td><b>Name</b></td><td><code>repos_cache_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_cache_usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `full_name` | `string` | The repository owner and name for the cache usage being shown. |
| `active_caches_count` | `integer` | The number of active caches in the repository. |
| `active_caches_size_in_bytes` | `integer` | The sum of the size in bytes of all the active cache items in the repository. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_actions_cache_usage` | `SELECT` | `owner, repo` |
