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
| `git_push_url` | `string` |  |
| `commits_url` | `string` |  |
| `public` | `boolean` |  |
| `comments_url` | `string` |  |
| `truncated` | `boolean` |  |
| `history` | `array` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `user` | `object` | Simple User |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `git_pull_url` | `string` |  |
| `forks_url` | `string` |  |
| `comments` | `integer` |  |
| `forks` | `array` |  |
| `owner` | `object` | Simple User |
| `files` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
