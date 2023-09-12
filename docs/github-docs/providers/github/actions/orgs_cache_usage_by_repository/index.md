---
title: orgs_cache_usage_by_repository
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_cache_usage_by_repository
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
<tr><td><b>Name</b></td><td><code>orgs_cache_usage_by_repository</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.orgs_cache_usage_by_repository</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `total_count` | `integer` |
| `repository_cache_usages` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_actions_cache_usage_by_repo_for_org` | `SELECT` | `org` |
