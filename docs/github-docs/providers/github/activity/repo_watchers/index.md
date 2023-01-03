---
title: repo_watchers
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
<tr><td><b>Name</b></td><td><code>repo_watchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.repo_watchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `gists_url` | `string` |
| `url` | `string` |
| `html_url` | `string` |
| `type` | `string` |
| `organizations_url` | `string` |
| `login` | `string` |
| `site_admin` | `boolean` |
| `events_url` | `string` |
| `followers_url` | `string` |
| `received_events_url` | `string` |
| `following_url` | `string` |
| `starred_at` | `string` |
| `avatar_url` | `string` |
| `node_id` | `string` |
| `gravatar_id` | `string` |
| `subscriptions_url` | `string` |
| `starred_url` | `string` |
| `email` | `string` |
| `repos_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_watchers_for_repo` | `SELECT` | `owner, repo` |
