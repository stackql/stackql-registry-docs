---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `key` | `string` |
| `read_only` | `boolean` |
| `title` | `string` |
| `url` | `string` |
| `verified` | `boolean` |
| `created_at` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_deploy_key` | `SELECT` | `key_id, owner, repo` |  |
| `list_deploy_keys` | `SELECT` | `owner, repo` |  |
| `create_deploy_key` | `INSERT` | `owner, repo, data__key` | You can create a read-only deploy key. |
| `delete_deploy_key` | `DELETE` | `key_id, owner, repo` | Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead. |
