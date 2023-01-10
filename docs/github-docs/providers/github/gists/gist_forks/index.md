---
title: gist_forks
hide_title: false
hide_table_of_contents: false
keywords:
  - gist_forks
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
<tr><td><b>Name</b></td><td><code>gist_forks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_forks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `git_push_url` | `string` |  |
| `forks` | `array` |  |
| `truncated` | `boolean` |  |
| `fork_of` | `object` | Gist |
| `forks_url` | `string` |  |
| `owner` | `object` | Simple User |
| `created_at` | `string` |  |
| `comments_url` | `string` |  |
| `user` | `string` |  |
| `files` | `object` |  |
| `git_pull_url` | `string` |  |
| `node_id` | `string` |  |
| `comments` | `integer` |  |
| `public` | `boolean` |  |
| `history` | `array` |  |
| `updated_at` | `string` |  |
| `commits_url` | `string` |  |
| `url` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `gist_id` |  |
| `fork` | `EXEC` | `gist_id` | **Note**: This was previously `/gists/:gist_id/fork`. |
