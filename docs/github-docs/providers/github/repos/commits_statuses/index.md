---
title: commits_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - commits_statuses
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
<tr><td><b>Name</b></td><td><code>commits_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commits_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `description` | `string` |  |
| `node_id` | `string` |  |
| `avatar_url` | `string` |  |
| `state` | `string` |  |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `creator` | `object` | A GitHub user. |
| `target_url` | `string` |  |
| `context` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_commit_statuses_for_ref` | `SELECT` | `owner, ref, repo` |
