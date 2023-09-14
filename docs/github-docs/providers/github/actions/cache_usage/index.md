---
title: cache_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_usage
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
<tr><td><b>Name</b></td><td><code>cache_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.cache_usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `full_name` | `string` | The repository owner and name for the cache usage being shown. |
| `active_caches_count` | `integer` | The number of active caches in the repository. |
| `active_caches_size_in_bytes` | `integer` | The sum of the size in bytes of all the active cache items in the repository. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_actions_cache_usage` | `SELECT` | `owner, repo` | Gets GitHub Actions cache usage for a repository.<br />The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.<br />Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `get_actions_cache_usage_for_org` | `SELECT` | `org` | Gets the total GitHub Actions cache usage for an organization.<br />The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.<br />You must authenticate using an access token with the `read:org` scope to use this endpoint. GitHub Apps must have the `organization_admistration:read` permission to use this endpoint. |
