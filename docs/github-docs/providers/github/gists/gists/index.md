---
title: gists
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
<tr><td><b>Name</b></td><td><code>gists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `updated_at` | `string` |  |
| `owner` | `object` | Simple User |
| `files` | `object` |  |
| `user` | `string` |  |
| `git_push_url` | `string` |  |
| `node_id` | `string` |  |
| `history` | `array` |  |
| `public` | `boolean` |  |
| `comments` | `integer` |  |
| `git_pull_url` | `string` |  |
| `url` | `string` |  |
| `fork_of` | `object` | Gist |
| `truncated` | `boolean` |  |
| `html_url` | `string` |  |
| `forks_url` | `string` |  |
| `commits_url` | `string` |  |
| `created_at` | `string` |  |
| `comments_url` | `string` |  |
| `forks` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gist_id` |  |
| `get_revision` | `SELECT` | `gist_id, sha` |  |
| `list` | `SELECT` |  | Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists: |
| `list_for_user` | `SELECT` | `username` | Lists public gists for the specified user: |
| `create` | `INSERT` | `data__files` | Allows you to add a new gist with one or more files.<br /><br />**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally. |
| `delete` | `DELETE` | `gist_id` |  |
| `update` | `EXEC` | `gist_id` | Allows you to update or delete a gist file and rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged. |
