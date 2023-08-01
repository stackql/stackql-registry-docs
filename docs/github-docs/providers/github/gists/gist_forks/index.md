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
| `git_pull_url` | `string` |  |
| `comments_url` | `string` |  |
| `owner` | `object` | Simple User |
| `created_at` | `string` |  |
| `fork_of` | `object` | Gist |
| `commits_url` | `string` |  |
| `html_url` | `string` |  |
| `user` | `string` |  |
| `updated_at` | `string` |  |
| `comments` | `integer` |  |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `public` | `boolean` |  |
| `forks_url` | `string` |  |
| `git_push_url` | `string` |  |
| `forks` | `array` |  |
| `history` | `array` |  |
| `truncated` | `boolean` |  |
| `files` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `gist_id` |  |
| `fork` | `EXEC` | `gist_id` | **Note**: This was previously `/gists/:gist_id/fork`. |
