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
| `comments` | `integer` |  |
| `public` | `boolean` |  |
| `history` | `array` |  |
| `truncated` | `boolean` |  |
| `commits_url` | `string` |  |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `git_pull_url` | `string` |  |
| `git_push_url` | `string` |  |
| `user` | `object` | Simple User |
| `html_url` | `string` |  |
| `owner` | `object` | Simple User |
| `files` | `object` |  |
| `forks` | `array` |  |
| `forks_url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
