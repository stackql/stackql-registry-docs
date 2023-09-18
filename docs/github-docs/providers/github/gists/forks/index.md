---
title: forks
hide_title: false
hide_table_of_contents: false
keywords:
  - forks
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
<tr><td><b>Name</b></td><td><code>forks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.forks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `comments` | `integer` |  |
| `truncated` | `boolean` |  |
| `git_push_url` | `string` |  |
| `updated_at` | `string` |  |
| `html_url` | `string` |  |
| `comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `fork_of` | `object` | Gist |
| `forks` | `array` |  |
| `url` | `string` |  |
| `git_pull_url` | `string` |  |
| `user` | `string` |  |
| `forks_url` | `string` |  |
| `files` | `object` |  |
| `public` | `boolean` |  |
| `history` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_forks` | `SELECT` | `gist_id` |
