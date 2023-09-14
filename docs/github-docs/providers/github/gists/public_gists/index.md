---
title: public_gists
hide_title: false
hide_table_of_contents: false
keywords:
  - public_gists
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
<tr><td><b>Name</b></td><td><code>public_gists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.public_gists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `forks_url` | `string` |  |
| `files` | `object` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `truncated` | `boolean` |  |
| `commits_url` | `string` |  |
| `history` | `array` |  |
| `git_push_url` | `string` |  |
| `html_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `updated_at` | `string` |  |
| `comments` | `integer` |  |
| `public` | `boolean` |  |
| `url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `user` | `object` | A GitHub user. |
| `forks` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
