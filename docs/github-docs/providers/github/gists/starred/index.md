---
title: starred
hide_title: false
hide_table_of_contents: false
keywords:
  - starred
  - gists
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
<tr><td><b>Name</b></td><td><code>starred</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.starred</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `forks_url` | `string` |  |
| `git_push_url` | `string` |  |
| `history` | `array` |  |
| `comments` | `integer` |  |
| `comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `forks` | `array` |  |
| `user` | `object` | A GitHub user. |
| `created_at` | `string` |  |
| `files` | `object` |  |
| `truncated` | `boolean` |  |
| `updated_at` | `string` |  |
| `public` | `boolean` |  |
| `git_pull_url` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_starred` | `SELECT` |  |
