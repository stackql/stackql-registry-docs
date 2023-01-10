---
title: gist_stars
hide_title: false
hide_table_of_contents: false
keywords:
  - gist_stars
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
<tr><td><b>Name</b></td><td><code>gist_stars</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.gist_stars</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `description` | `string` |  |
| `git_pull_url` | `string` |  |
| `html_url` | `string` |  |
| `forks` | `array` |  |
| `node_id` | `string` |  |
| `comments` | `integer` |  |
| `user` | `object` | Simple User |
| `url` | `string` |  |
| `updated_at` | `string` |  |
| `public` | `boolean` |  |
| `commits_url` | `string` |  |
| `truncated` | `boolean` |  |
| `comments_url` | `string` |  |
| `forks_url` | `string` |  |
| `owner` | `object` | Simple User |
| `git_push_url` | `string` |  |
| `history` | `array` |  |
| `created_at` | `string` |  |
| `files` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `check_is_starred` | `SELECT` | `gist_id` |  |
| `list_starred` | `SELECT` |  | List the authenticated user's starred gists: |
| `star` | `EXEC` | `gist_id` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar` | `EXEC` | `gist_id` |  |
