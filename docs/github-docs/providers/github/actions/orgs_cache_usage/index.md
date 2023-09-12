---
title: orgs_cache_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_cache_usage
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
<tr><td><b>Name</b></td><td><code>orgs_cache_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.orgs_cache_usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `total_active_caches_count` | `integer` | The count of active caches across all repositories of an enterprise or an organization. |
| `total_active_caches_size_in_bytes` | `integer` | The total size in bytes of all active cache items across all repositories of an enterprise or an organization. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_actions_cache_usage_for_org` | `SELECT` | `org` |
