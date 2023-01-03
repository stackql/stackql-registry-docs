---
title: gist_public
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
<tr><td><b>Name</b></td><td><code>gist_public</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_public</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `owner` | `object` | Simple User |
| `history` | `array` |  |
| `forks` | `array` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `files` | `object` |  |
| `comments` | `integer` |  |
| `url` | `string` |  |
| `forks_url` | `string` |  |
| `git_push_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `comments_url` | `string` |  |
| `user` | `object` | Simple User |
| `commits_url` | `string` |  |
| `public` | `boolean` |  |
| `truncated` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
