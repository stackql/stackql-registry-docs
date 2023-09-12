---
title: public
hide_title: false
hide_table_of_contents: false
keywords:
  - public
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
<tr><td><b>Name</b></td><td><code>public</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.public</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `html_url` | `string` |  |
| `git_pull_url` | `string` |  |
| `files` | `object` |  |
| `owner` | `object` | A GitHub user. |
| `comments` | `integer` |  |
| `git_push_url` | `string` |  |
| `history` | `array` |  |
| `user` | `object` | A GitHub user. |
| `created_at` | `string` |  |
| `public` | `boolean` |  |
| `commits_url` | `string` |  |
| `url` | `string` |  |
| `forks_url` | `string` |  |
| `comments_url` | `string` |  |
| `truncated` | `boolean` |  |
| `node_id` | `string` |  |
| `forks` | `array` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public` | `SELECT` |  |
