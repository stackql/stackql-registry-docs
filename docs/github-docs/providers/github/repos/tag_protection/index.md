---
title: tag_protection
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_protection
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
<tr><td><b>Name</b></td><td><code>tag_protection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.tag_protection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `enabled` | `boolean` |
| `pattern` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_tag_protection` | `SELECT` | `owner, repo` | This returns the tag protection states of a repository.<br /><br />This information is only available to repository administrators. |
| `create_tag_protection` | `INSERT` | `owner, repo, data__pattern` | This creates a tag protection state for a repository.<br />This endpoint is only available to repository administrators. |
| `delete_tag_protection` | `DELETE` | `owner, repo, tag_protection_id` | This deletes a tag protection state for a repository.<br />This endpoint is only available to repository administrators. |
