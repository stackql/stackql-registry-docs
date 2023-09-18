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
| `commits_url` | `string` |  |
| `url` | `string` |  |
| `git_push_url` | `string` |  |
| `created_at` | `string` |  |
| `git_pull_url` | `string` |  |
| `updated_at` | `string` |  |
| `public` | `boolean` |  |
| `truncated` | `boolean` |  |
| `history` | `array` |  |
| `comments_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `forks` | `array` |  |
| `html_url` | `string` |  |
| `files` | `object` |  |
| `forks_url` | `string` |  |
| `user` | `object` | A GitHub user. |
| `comments` | `integer` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
