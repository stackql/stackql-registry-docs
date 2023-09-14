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
| `files` | `object` |  |
| `forks` | `array` |  |
| `commits_url` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `history` | `array` |  |
| `user` | `string` |  |
| `forks_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `truncated` | `boolean` |  |
| `git_push_url` | `string` |  |
| `comments_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `url` | `string` |  |
| `comments` | `integer` |  |
| `public` | `boolean` |  |
| `html_url` | `string` |  |
| `fork_of` | `object` | Gist |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_forks` | `SELECT` | `gist_id` |
