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
| `commits_url` | `string` |  |
| `files` | `object` |  |
| `truncated` | `boolean` |  |
| `git_push_url` | `string` |  |
| `owner` | `object` | Simple User |
| `url` | `string` |  |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `forks_url` | `string` |  |
| `forks` | `array` |  |
| `comments_url` | `string` |  |
| `user` | `string` |  |
| `git_pull_url` | `string` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `history` | `array` |  |
| `public` | `boolean` |  |
| `comments` | `integer` |  |
| `fork_of` | `object` | Gist |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `gist_id` |  |
| `fork` | `EXEC` | `gist_id` | **Note**: This was previously `/gists/:gist_id/fork`. |
