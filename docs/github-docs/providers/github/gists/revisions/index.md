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
| `comments` | `integer` |  |
| `files` | `object` |  |
| `node_id` | `string` |  |
| `forks_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `fork_of` | `object` | Gist |
| `truncated` | `boolean` |  |
| `git_push_url` | `string` |  |
| `html_url` | `string` |  |
| `commits_url` | `string` |  |
| `forks` | `array` |  |
| `history` | `array` |  |
| `updated_at` | `string` |  |
| `git_pull_url` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `user` | `string` |  |
| `comments_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_revision` | `SELECT` | `gist_id, sha` |
