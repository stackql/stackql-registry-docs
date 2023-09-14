---
title: starred_gists
hide_title: false
hide_table_of_contents: false
keywords:
  - starred_gists
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
<tr><td><b>Name</b></td><td><code>starred_gists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.starred_gists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `forks` | `array` |  |
| `git_pull_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `user` | `object` | A GitHub user. |
| `commits_url` | `string` |  |
| `forks_url` | `string` |  |
| `comments` | `integer` |  |
| `node_id` | `string` |  |
| `truncated` | `boolean` |  |
| `history` | `array` |  |
| `comments_url` | `string` |  |
| `public` | `boolean` |  |
| `git_push_url` | `string` |  |
| `files` | `object` |  |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_starred` | `SELECT` |  |
