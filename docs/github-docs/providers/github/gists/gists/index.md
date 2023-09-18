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
| `created_at` | `string` |  |
| `forks_url` | `string` |  |
| `user` | `object` | A GitHub user. |
| `forks` | `array` |  |
| `commits_url` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `truncated` | `boolean` |  |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `comments` | `integer` |  |
| `comments_url` | `string` |  |
| `history` | `array` |  |
| `files` | `object` |  |
| `git_pull_url` | `string` |  |
| `updated_at` | `string` |  |
| `public` | `boolean` |  |
| `git_push_url` | `string` |  |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` |  | Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists: |
| `list_for_user` | `SELECT` | `username` | Lists public gists for the specified user: |
| `create` | `INSERT` | `data__files` | Allows you to add a new gist with one or more files.<br /><br />**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally. |
| `delete` | `DELETE` | `gist_id` |  |
| `check_is_starred` | `EXEC` | `gist_id` |  |
| `fork` | `EXEC` | `gist_id` |  |
| `star` | `EXEC` | `gist_id` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar` | `EXEC` | `gist_id` |  |
| `update` | `EXEC` | `gist_id` | Allows you to update a gist's description and to update, delete, or rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged.<br />At least one of `description` or `files` is required. |
