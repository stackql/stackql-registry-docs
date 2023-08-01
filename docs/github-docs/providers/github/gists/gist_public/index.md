---
title: gist_public
hide_title: false
hide_table_of_contents: false
keywords:
  - gist_public
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
<tr><td><b>Name</b></td><td><code>gist_public</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_public</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `files` | `object` |  |
| `commits_url` | `string` |  |
| `comments_url` | `string` |  |
| `git_push_url` | `string` |  |
| `comments` | `integer` |  |
| `created_at` | `string` |  |
| `forks` | `array` |  |
| `html_url` | `string` |  |
| `history` | `array` |  |
| `updated_at` | `string` |  |
| `git_pull_url` | `string` |  |
| `forks_url` | `string` |  |
| `url` | `string` |  |
| `owner` | `object` | Simple User |
| `user` | `object` | Simple User |
| `public` | `boolean` |  |
| `node_id` | `string` |  |
| `truncated` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
