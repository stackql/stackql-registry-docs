---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `history` | `array` |  |
| `created_at` | `string` |  |
| `forks` | `array` |  |
| `updated_at` | `string` |  |
| `commits_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `user` | `object` | A GitHub user. |
| `comments` | `integer` |  |
| `truncated` | `boolean` |  |
| `git_pull_url` | `string` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `git_push_url` | `string` |  |
| `forks_url` | `string` |  |
| `public` | `boolean` |  |
| `comments_url` | `string` |  |
| `files` | `object` |  |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_user` | `SELECT` | `username` |
