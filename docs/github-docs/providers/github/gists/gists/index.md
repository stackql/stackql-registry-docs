---
title: gists
hide_title: false
hide_table_of_contents: false
keywords:
  - gists
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
<tr><td><b>Name</b></td><td><code>gists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `url` | `string` |  |
| `history` | `array` |  |
| `owner` | `object` | A GitHub user. |
| `public` | `boolean` |  |
| `truncated` | `boolean` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `git_push_url` | `string` |  |
| `comments` | `integer` |  |
| `forks_url` | `string` |  |
| `user` | `string` |  |
| `commits_url` | `string` |  |
| `files` | `object` |  |
| `fork_of` | `object` | Gist |
| `git_pull_url` | `string` |  |
| `forks` | `array` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gist_id` |  |
| `get_revision` | `SELECT` | `gist_id, sha` |  |
| `list` | `SELECT` |  | Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists: |
| `create` | `INSERT` | `data__files` | Allows you to add a new gist with one or more files.<br /><br />**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally. |
| `delete` | `DELETE` | `gist_id` |  |
| `update` | `EXEC` | `gist_id` | Allows you to update a gist's description and to update, delete, or rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged.<br />At least one of `description` or `files` is required. |
