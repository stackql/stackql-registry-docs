---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `added_by` | `string` |
| `created_at` | `string` |
| `key` | `string` |
| `verified` | `boolean` |
| `last_used` | `string` |
| `url` | `string` |
| `read_only` | `boolean` |
| `title` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_deploy_key` | `SELECT` | `key_id, owner, repo` |  |
| `list_deploy_keys` | `SELECT` | `owner, repo` |  |
| `create_deploy_key` | `INSERT` | `owner, repo, data__key` | You can create a read-only deploy key. |
| `delete_deploy_key` | `DELETE` | `key_id, owner, repo` | Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead. |
