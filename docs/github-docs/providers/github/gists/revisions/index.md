---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
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
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `public` | `boolean` |  |
| `git_pull_url` | `string` |  |
| `truncated` | `boolean` |  |
| `comments_url` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `files` | `object` |  |
| `history` | `array` |  |
| `user` | `string` |  |
| `fork_of` | `object` | Gist |
| `node_id` | `string` |  |
| `comments` | `integer` |  |
| `forks` | `array` |  |
| `created_at` | `string` |  |
| `forks_url` | `string` |  |
| `commits_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `git_push_url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_revision` | `SELECT` | `gist_id, sha` |
