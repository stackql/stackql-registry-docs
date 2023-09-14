---
title: gist
hide_title: false
hide_table_of_contents: false
keywords:
  - gist
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
<tr><td><b>Name</b></td><td><code>gist</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `commits_url` | `string` |  |
| `forks` | `array` |  |
| `files` | `object` |  |
| `git_pull_url` | `string` |  |
| `history` | `array` |  |
| `fork_of` | `object` | Gist |
| `forks_url` | `string` |  |
| `git_push_url` | `string` |  |
| `user` | `string` |  |
| `updated_at` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `truncated` | `boolean` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `public` | `boolean` |  |
| `created_at` | `string` |  |
| `comments` | `integer` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `gist_id` |
