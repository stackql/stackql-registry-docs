---
title: gist_forks
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `forks` | `array` |  |
| `truncated` | `boolean` |  |
| `created_at` | `string` |  |
| `git_pull_url` | `string` |  |
| `comments` | `integer` |  |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `fork_of` | `object` | Gist |
| `forks_url` | `string` |  |
| `user` | `string` |  |
| `owner` | `object` | Simple User |
| `history` | `array` |  |
| `files` | `object` |  |
| `git_push_url` | `string` |  |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `public` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_forks` | `SELECT` | `gist_id` |  |
| `fork` | `EXEC` | `gist_id` | **Note**: This was previously `/gists/:gist_id/fork`. |
