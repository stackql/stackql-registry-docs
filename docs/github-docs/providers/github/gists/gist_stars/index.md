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
| `files` | `object` |  |
| `git_push_url` | `string` |  |
| `comments` | `integer` |  |
| `forks_url` | `string` |  |
| `history` | `array` |  |
| `commits_url` | `string` |  |
| `user` | `object` | Simple User |
| `html_url` | `string` |  |
| `owner` | `object` | Simple User |
| `updated_at` | `string` |  |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `truncated` | `boolean` |  |
| `created_at` | `string` |  |
| `git_pull_url` | `string` |  |
| `forks` | `array` |  |
| `public` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `check_is_starred` | `SELECT` | `gist_id` |  |
| `list_starred` | `SELECT` |  | List the authenticated user's starred gists: |
| `star` | `EXEC` | `gist_id` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unstar` | `EXEC` | `gist_id` |  |
